#from functools import partial, wraps
import json
#from datetime import datetime
from django.contrib.auth.decorators import login_required
#from django.db import IntegrityError, transaction
#from django.db.models import Prefetch
#from django.forms.formsets import formset_factory
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
#from django.db.models import F


from school_user.models import Tenant
from .forms import StudentForm, StudentGuardianForm, StudentEducationForm
from .models import Student, student_guardian, student_education

@login_required
#This is students' base
def base(request):
	return render(request, 'student/student_base.html')


@login_required
#This function helps in addidng new syllabus and exams
def studentprofile_new(request, input_type):
	if (input_type=="Student"):
		importform=StudentForm
		name='student:student_list'
	elif (input_type=="Guardian"):
		importform=StudentGuardianForm
		name='stuent:student_list'
	elif (input_type=="Education"):
		importform=StudentEducationForm
		name='student:student_list'
	current_tenant=request.user.tenant
	form=importform(tenant=current_tenant)
	if (request.method == "POST"):
		current_tenant=request.user.tenant
		form = importform(request.POST, tenant=current_tenant)
		if form.is_valid():
			item=form.save(commit=False)			
			item.tenant=current_tenant
			item.save()
			return redirect(name)
	return render(request, 'genadmin/new.html',{'form': form, 'item': input_type})

def student_list(request):
	students=Student.objects.for_tenant(request.user.tenant).all()
	return render(request, 'student/list.html',{'students': students})

