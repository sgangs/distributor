import json
import calendar
from datetime import date, datetime
from django.utils import timezone
from django.utils.timezone import localtime
from functools import partial, wraps
from io import BytesIO
#from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.core.serializers.json import DjangoJSONEncoder
from django.db import IntegrityError, transaction
from django.db.models import Prefetch
from django.forms.formsets import formset_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
#from django.db.models import F

from school_user.models import Tenant
#from .forms import SubjectForm, classGroupForm, HouseForm
from school_account.models import Account
from school_eduadmin.models import class_section, classstudent
from school_genadmin.models import class_group, academic_year
from school_student.models import Student
from .models import generic_fee, generic_fee_list, student_fee, group_default_fee
from .fee_utils import *
from school.school_general import *

@login_required
#This is the base page.
def base(request):
	return render (request, 'fees/fees_base.html')

@login_required
#For adding new entry for fees structure
def feestructure_new(request, input_type):
	extension="base.html"
	accountlist=Account.objects.for_tenant(request.user.tenant).filter(ledger_group__name='Fees').all()
	accounts=[]
	for account in accountlist:
		accounts.append({'data_type':'Accounts','id':encoder(account.id),'name':account.name})
	jsondata = json.dumps(accounts)
	fee_type='Yearly'
	if request.method == 'POST':
		response_data = {}
		this_tenant=request.user.tenant
		# saving the fee structure
		with transaction.atomic():
			try:
				create_fee_structure(request, fee_type)
			except:
				transaction.rollback()
		jsondata = json.dumps(response_data)
		return HttpResponse(jsondata)

	return render(request, 'fees/fee_structure.html',{'accounts':jsondata, 'fee_type':'Yearly', 'extension':extension})

@login_required
#For adding new entry for fees structure
def group_fee_linking(request):
	extension="base.html"
	this_tenant=request.user.tenant
	group=class_group.objects.for_tenant(this_tenant).all()
	generic=generic_fee.objects.for_tenant(this_tenant).filter(is_active=True).all()
	year=academic_year.objects.for_tenant(this_tenant).get(current_academic_year=True).year
	if request.method == 'POST':
		response_data = []
		classgroups=json.loads(request.POST.get('classgroups'))
		genericfee_inputs =json.loads(request.POST.get('genericfees'))
		addstudent =request.POST.get('addstudent')
		total=0
		genericfeeall=[]
		for fees in genericfee_inputs:
			genericfeeid=fees['fee_id']
			genericfee=generic_fee.objects.get(id=int(genericfeeid))
			genericfeeall.append(genericfee)
		for groups in classgroups:
			groupid=groups['classgroup_id']
			group=class_group.objects.get(id=int(groupid))
			with transaction.atomic():
				try:
					exist=group_default_fee.objects.for_tenant(this_tenant).filter(classgroup=group, year=year).exists()
					if (exist):
						transaction.rollback()			
					else:
						pass
					group_fee=group_default_fee()
					group_fee.classgroup=group
					group_fee.year=int(year)
					group_fee.tenant=this_tenant
					group_fee.save()
					for fees in genericfeeall:
						group_fee.generic_fee.add(fees)
					if (addstudent == "Yes"):
						classlist=class_section.objects.for_tenant(this_tenant).filter(classgroup=group).all()
						for classdata in classlist:
							class_students=Student.objects.filter(classstudent_eduadmin_student_student__year=year,\
											classstudent_eduadmin_student_student__class_section=classdata)
							for student in class_students:
								studentfee=student_fee()
								studentfee.student=student
								studentfee.year=year
								studentfee.tenant=this_tenant
								studentfee.save()
								for fees in genericfeeall:
									studentfee.generic_fee.add(fees)								
				except:
					transaction.rollback()
		jsondata = json.dumps(response_data)
		return HttpResponse(jsondata)
	#This has to change to geenric_fee as the term being sent to html
	return render(request, 'fees/fee_linking.html',{'groups':group,'year':year, 'yearly_fee':generic,'extension':extension})


@login_required
def fee_view(request, input_type):
	extension="base.html"
	fee_type='Yearly'
	fees=generic_fee.objects.for_tenant(request.user.tenant).filter(is_active=True)
	if request.method == 'POST':
		response_data = []
		feeid=request.POST.get('feeid')
		fee_target=generic_fee.objects.get(id=feeid)
		fee_list=generic_fee_list.objects.filter(generic_fee=fee_target).select_related('account')
		for fee in fee_list:
			response_data.append({'data_type':'Yearly Fee','account':fee.account.name,\
				'name': fee.name,'amount': str(fee.amount),})
		jsondata = json.dumps(response_data)
		return HttpResponse(jsondata)
	return render(request, 'fees/fees_view.html',{'fees':fees, 'fee_type':fee_type, 'extension':extension})

#This view is to edit fee structure
@login_required
def student_fee_structure(request):
	extension="base.html"
	this_tenant=request.user.tenant
	# year=academic_year.objects.for_tenant(this_tenant).get(current_academic_year=True).year	
	classes=class_section.objects.for_tenant(this_tenant).all()
	generic_fees=generic_fee.objects.for_tenant(this_tenant).filter(is_active=True)
	if request.method == 'POST':
		response_data=[]	
		calltype=request.POST.get('calltype')
		if (calltype == 'student'):
			response_data=view_student(request)
		elif (calltype == 'details'):			
			response_data=view_class_fees(request)
		elif (calltype == 'fee_student'):			
			response_data=view_student_fees(request)
		elif (calltype == 'save'):
			year=int(request.POST.get('year'))
			students=json.loads(request.POST.get('items'))
			genericfee_inputs =json.loads(request.POST.get('generic_fees'))
			genericfeeall=[]
			for fees in genericfee_inputs:
				genericfeeid=fees['fee_id']
				genericfee=generic_fee.objects.get(id=int(genericfeeid))
				genericfeeall.append(genericfee)
			with transaction.atomic():
				try:
					for data in students:
							student=Student.objects.for_tenant(this_tenant).get(id=data['student_id'])
							student_fee_data=student_fee.objects.get(year=year,student=student)
							for fees in genericfeeall:
								student_fee_data.generic_fee.add(fees)
				except:
					transaction.rollback()

		jsondata = json.dumps(response_data, cls=DjangoJSONEncoder)
		return HttpResponse(jsondata)
	return render(request, 'fees/student_fee_edit.html',{'classes':classes, "extension":extension,'generic_fees':generic_fees})

@login_required
#For fees payment
def student_payment(request, input_type):
	extension="base.html"
	if request.method == 'POST':
		response_data = []
		calltype=request.POST.get('calltype')
		if (calltype == 'student'):
			response_data=view_student(request)
		elif (calltype == 'details'):
			response_data=view_fee_details(request)
			# print (response_data)
		elif (calltype == 'payment_history'):
			response_data=view_payment_details(request)
		elif (calltype == 'save'):
			response_data=save_student_payment(request)
			response_data="Saved"
		elif (calltype=='pdf'):
			with transaction.atomic():
				try:
					response_data=view_fee_details(request)
					paid_on=save_student_payment(request)
				except:
					transaction.rollback()
				response = HttpResponse(content_type='application/pdf')
				filename = 'Fee_Payment'
				response['Content-Disposition'] ='attachement; filename={0}.pdf'.format(filename)
				buffer = BytesIO()
				report = PdfPrint(buffer,'A4')
				pdf = report.report(request, paid_on, response_data, 'Fee Payment')
				response.write(pdf)					
				response_data=[]				
			return response
		jsondata = json.dumps(response_data, cls=DjangoJSONEncoder)
		return HttpResponse(jsondata)
	classsection=class_section.objects.for_tenant(request.user.tenant).all()
	return render(request, 'fees/student_fee_payment.html',{'input_type':input_type,\
					'classsection':classsection, 'extension':extension})


#All views hereafter are fee collection related

@login_required
def fee_collected_between(request):
	extension="base.html"
	this_tenant=request.user.tenant
	academic=academic_year.objects.for_tenant(this_tenant).get(current_academic_year=True)
	min_date=academic.start.isoformat()
	max_date=academic.end.isoformat()
	if request.method == 'POST':
		response_data=[]
		start=request.POST.get('start')
		end=request.POST.get('end')
		fees_paid=student_fee_payment.objects.for_tenant(this_tenant).filter(paid_on__range=(start,end)).\
					order_by('paid_on').select_related('student')
		total_collected=0
		for fee in fees_paid:
			total_collected+=fee.amount
			response_data.append({'data':'Student','student_name':fee.student.first_name+" "+fee.student.first_name,\
				'student_id':fee.student.key,'student_local':fee.student.local_id,'amount':str(fee.amount),\
				'date':fee.paid_on.isoformat()})
		response_data.append({'data':'Total', 'collected':str(total_collected)})
		jsondata=json.dumps(response_data)
		return HttpResponse(jsondata)
	return render(request, 'fees/fee_collection.html',{'min':min_date,'max':max_date, 'extension':extension})	


@login_required
def fee_collection_graph(request):
	extension="base.html"
	this_tenant=request.user.tenant
	academic=academic_year.objects.for_tenant(this_tenant).get(current_academic_year=True)
	min_date=academic.start.isoformat()
	max_date=academic.end.isoformat()
	fees_paid=student_fee_payment.objects.for_tenant(this_tenant).filter(paid_on__range=(min_date,max_date)).\
					order_by('paid_on').select_related('student','student_class')
	response_data=[]
	for fee in fees_paid:
		response_data.append({'student':str(fee.student.id) + " "+fee.student.first_name+ " "+fee.student.last_name,\
			'fee_month':fee.month, 'amount':float(fee.amount),'date':fee.paid_on.isoformat(), 'class':fee.student_class.name})
	# jsondata=
		# return HttpResponse(jsondata)
	return render(request, 'fees/view_feereport_crossfilter.html',{'data':json.dumps(response_data), 'min':min_date,'max':max_date, \
		'extension':extension})

#This view is used to print fee structure of astudent of particular month.
# def print_fee_structure(request):
# 	response_data=view_fee_details(request)
# 	response = HttpResponse(content_type='application/pdf')
# 	filename = 'fee_payment'
# 	response['Content-Disposition'] ='attachement; filename={0}.pdf'.format(filename)
# 	buffer = BytesIO()
# 	report = PdfPrint(buffer,
# 	 'A4')
# 	pdf = report.report(respo, 'Fee Payment')
# 	response.write(pdf)
# 	return response

#Check the requirement of this view

# @login_required
# #This view is a fee history of the student
# def fee_payment_history(request):
# 	extension="base.html"
# 	this_tenant=request.user.tenant
# 	classes=class_section.objects.for_tenant(this_tenant).all()
# 	if request.method == 'POST':		
# 		calltype=request.POST.get('calltype')
# 		if (calltype == 'student'):
# 			response_data=view_student(request)
# 		elif (calltype == 'details'):
# 			start=request.POST.get('start')
# 			end=request.POST.get('end')
# 			studentid=request.POST.get('studentid')
# 			response_data=list(student_fee_payment.objects.for_tenant(this_tenant).\
# 							filter(student=studentid).order_by('paid_on').\
# 							values('year','month','paid_on','amount'))
# 		jsondata = json.dumps(response_data, cls=DjangoJSONEncoder)
# 		return HttpResponse(jsondata)
# 	return render(request, 'fees/student_fee_history.html',{'classes':classes, "extension":extension})

@login_required
#Fron end is yet to be completed
def fee_payment_monthwise(request):
	extension="base.html"
	this_tenant=request.user.tenant
	classes=class_section.objects.for_tenant(this_tenant).all()
	if request.method == 'POST':
		month=request.POST.get('month')
		classid=int(request.POST.get('classid'))
		class_selected=classes.get(id=classid)
		year=academic_year.objects.for_tenant(this_tenant).get(current_academic_year=True).year
		response_data=[]
		# year=int(request.POST.get('year'))
		# num_days=calendar.monthrange(year, month)
		# start=datetime.date(year, month, 1)
		# end=datetime.date(year, month, num_days)
		payment_list=student_fee_payment.objects.for_tenant(this_tenant).filter(year=year,month=month, student_class=class_selected).\
					order_by('paid_on', 'student__first_name').select_related('student')
		for data in payment_list:
			response_data.append({'paid_on':data.paid_on,'amount':data.amount,\
				'name':data.student.first_name+" "+data.student.last_name, 'local_id':data.student.local_id, 'key':data.student.key})
		jsondata = json.dumps(response_data, cls=DjangoJSONEncoder)
		return HttpResponse(jsondata)
	return render(request, 'fees/fee_collection_month.html',{'classes':classes, "extension":extension})

@login_required
#Fron end is yet to be completed
def fee_defaulter(request):
	extension="base.html"
	this_tenant=request.user.tenant
	classes=class_section.objects.for_tenant(this_tenant).all()
	if request.method == 'POST':
		month=request.POST.get('month')
		classid=int(request.POST.get('classid'))
		class_selected=classes.get(id=classid)
		year=academic_year.objects.for_tenant(this_tenant).get(current_academic_year=True).year
		response_data=[]
		classstudents=classstudent.objects.for_tenant(this_tenant).filter(year=year, class_section=class_selected)
		payment_list=student_fee_payment.objects.for_tenant(this_tenant).filter(year=year,month=month)
		students=list(Student.objects.for_tenant(this_tenant).filter(classstudent_eduadmin_student_student__in=classstudents).\
					exclude(studentFeePayment_fees_student_student__in=payment_list).values('id','key','local_id',\
						'first_name','last_name'))
		jsondata = json.dumps(students, cls=DjangoJSONEncoder)
		return HttpResponse(jsondata)
	return render(request, 'fees/fee_collection_month.html',{'classes':classes, "extension":extension, 'calltype':'Defaulter'})

@login_required
#Fron end is yet to be completed
def fee_deactivate(request):
	extension="base.html"
	this_tenant=request.user.tenant
	fee_list=generic_fee.objects.for_tenant(this_tenant).filter(is_active=True)
	if request.method == 'POST':
		response_data=[]
		feeid=int(request.POST.get('classid'))
		fee_selected=fee_list.get(id=classid)
		fee_selected.is_active=False
		fee_selected.save()
		jsondata = json.dumps(response_data, cls=DjangoJSONEncoder)
		return HttpResponse(jsondata)
	return render(request, 'fees/fee_collection_month.html',{'fee_list':fee_list, "extension":extension})

#Create a fee view structure
# @login_required
# #For fees payment
# def student_payment(request, input_type):
# 	extension="base.html"
# 	if request.method == 'POST':
# 		response_data = []
# 		calltype=request.POST.get('calltype')
# 		if (calltype == 'student'):
# 			response_data=view_student(request)
# 		elif (calltype == 'details'):
# 			response_data=view_fee_details(request)
# 			# print (response_data)
# 		jsondata = json.dumps(response_data, cls=DjangoJSONEncoder)
# 		return HttpResponse(jsondata)
# 	classsection=class_section.objects.for_tenant(request.user.tenant).all()
# 	return render(request, 'fees/student_fee_payment.html',{'input_type':input_type,\
# 					'classsection':classsection, 'extension':extension})