from django.db.models import Avg
from django.shortcuts import get_object_or_404
from .models import Attendance, exam_report
#from school_eduadmin.models import * #class_section
from school_student.models import Student
from school_eduadmin.models import class_section, classstudent, Exam, Syllabus
from school_genadmin.models import class_group, Subject, academic_year
from school.school_general import *

#This function is used to provide students' data for attendance/exam score entry
def get_subject_data(request, called_for, classes):
    classid=request.POST.get('classid')
    examid=int(request.POST.get('examid'))
    try:
        year=int(request.POST.get('year'))
    except:
        year=academic_year.objects.for_tenant(this_tenant).get(current_academic_year=True).year
    class_selected=classes.get(id__exact=classid)
    response_data=[]
    try:
        class_group=class_selected.classgroup
        subjects=Syllabus.objects.filter(class_group=class_group, year=year).select_related("subject")
        for subject in subjects:
            response_data.append({'data_type':'Subject','id':subject.subject.id,'name':subject.subject.name})
        return response_data
    except:
      pass

def get_student_data(request, called_for, classes ):
    classid=request.POST.get('classid')
    this_tenant=request.user.tenant
    if (called_for=='Attendance'):
    	year=academic_year.objects.for_tenant(this_tenant).get(current_academic_year=True).year
    else:
        examid=int(request.POST.get('examid'))
        exam=Exam.objects.for_tenant(request.user.tenant).get(id__exact=examid)
        year=exam.year
        subjectid=int(request.POST.get('subjectid'))
        subject=Subject.objects.for_tenant(this_tenant).get(id=subjectid)
    class_selected=classes.get(id__exact=classid)
    response_data=[]
    # try:
    if (called_for=='Attendance'):
        date=request.POST.get('date')
        excluded_student_raw=Attendance.objects.filter(tenant=request.user.tenant, class_section=class_selected,\
                date=date).all()
        excluded_student=Student.objects.filter(attendance_classadmin_student_student=excluded_student_raw).all()
        students_list=classstudent.objects.for_tenant(request.user.tenant).\
    	   filter(class_section=class_selected,year=year).exclude(student__id__in=excluded_student).select_related("student")        
    else:
        try:
            excluded_student_raw=exam_report.objects.filter(tenant=request.user.tenant, class_section=class_selected,\
                exam=exam,subject=subject).all()
            excluded_student=Student.objects.filter(examReport_classadmin_student_student__in=excluded_student_raw).all()
            students_list=classstudent.objects.for_tenant(request.user.tenant).\
                filter(class_section=class_selected,year=year).all().exclude(student__in=excluded_student).select_related("student")
        except:
            students_list=classstudent.objects.for_tenant(request.user.tenant).\
                filter(class_section=class_selected,year=year).select_related("student")

    for student in students_list:
    	response_data.append({'data_type':'Student','id':student.student.id,'key':student.student.key,\
    		  'local_id': student.student.local_id,'roll_no': student.roll_no,'first_name': student.student.first_name,\
              'last_name': student.student.last_name})
    return response_data
    # except:
   	# 	pass



def get_exam_marks(request, classes, this_tenant):
    response_data=[]
    classid=request.POST.get('classid')
    examid=request.POST.get('examid')
    subjectid=int(request.POST.get('subjectid'))
    class_selected=classes.get(id__exact=classid)
    year=academic_year.objects.for_tenant(this_tenant).get(current_academic_year=True).year
    exam=Exam.objects.for_tenant(request.user.tenant).filter(year=year).get(id__exact=examid)    
    subject=Subject.objects.for_tenant(this_tenant).get(id=subjectid)
    exam_data=exam_report.objects.for_tenant(request.user.tenant).filter(class_section=class_selected, exam=exam, year=year).\
                select_related('student')
    for data in exam_data:
        roll_no=classstudent.objects.for_tenant(this_tenant).get(student=data.student, year=year).roll_no
        response_data.append({'id':data.id,'key':data.student.key,'local_id': data.student.local_id,'roll_no': \
            roll_no,'first_name': data.student.first_name,'last_name': data.student.last_name, 'final':data.final_score,\
            'grade':data.grade, 'point':data.grade_point})
    return response_data                

#This function is used to provide data for students' attendance view
def get_attendance_data(request):
    classid=request.POST.get('classid')
    date=request.POST.get('date')
    class_selected=class_section.objects.for_tenant(request.user.tenant).get(id__exact=classid)
    attendance_list=Attendance.objects.filter(class_section=class_selected, date=date)
    response_data=[]
    try:
        for data in attendance_list:
            response_data.append({'data_type':'Attendance','id':data.student.id,'key':data.student.key,\
     				'local_id': data.student.local_id,'first_name': data.student.first_name, 'last_name': data.student.last_name,\
     				'is_present': data.ispresent, 'remarks':data.remarks})
        return response_data
    except:
        pass

# def get_exam_report(request, called_for, classes ):
#     classid=int(request.POST.get('classid'))
#     examid=int(request.POST.get('examid'))
#     subjectid=int(request.POST.get('subjectid'))
#     exam=Exam.objects.for_tenant(request.user.tenant).get(id__exact=examid)
#     class_selected=classes.get(id__exact=classid)
#     subject=Subject.objects.get(id=subjectid)
#     exam_report_details=exam_report.objects.filter(exam=exam, class_section=class_selected, subject=subject).\
#                         select_related('student').all()
#     average=exam_report_details.aggregate(Avg('final_score'))
#     average_external=exam_report_details.aggregate(Avg('external_score'))
#     try:
#         average=round(average['final_score__avg'],2)
#         response_data=[]
#         if (average_external['external_score__avg'] != None):
#             for report in exam_report_details:
#                 response_data.append({'data_type':'Report w ext','score': report.final_score,'internal': report.internal_score,\
#                 'average':average,'external':report.external_score,\
#                 'first_name': report.student.first_name, 'last_name': report.student.last_name})
#         else:
#             for report in exam_report_details:
#                 response_data.append({'data_type':'Report w.o. ext','score': report.final_score,'internal': report.internal_score,\
#                 'average':average,'first_name': report.student.first_name, 'last_name': report.student.last_name})
#         return response_data
#     except:
#         pass


def get_exam_report(request, called_for, classes ):
    # classid=int(request.POST.get('classid'))
    examid=int(request.POST.get('examid'))
    this_tenant=request.user.tenant
    exam=Exam.objects.for_tenant(this_tenant).get(id__exact=examid)
    total=exam.total
    exam_report_details=exam_report.objects.for_tenant(this_tenant).filter(exam=exam).\
                        select_related('student','subject','class_section').all()
    response_data=[]
    for report in exam_report_details:
        response_data.append({'data_type':'Report w ext','marks': float((report.final_score/total)*100),'subject':report.subject.name,\
            'student_id':str(report.student.id) + " "+report.student.first_name+ " "+report.student.last_name,\
            'class':report.class_section.name})
    return response_data
    
#This function is used to provide individual student's data for attendance
def get_studentattendance_data(request, called_for, classes):
    classid=int(request.POST.get('classid'))
    studentid=int(request.POST.get('studentid'))
    date=request.POST.get('date')
    class_selected=classes.get(id__exact=classid)
    student=Student.objects.for_tenant(request.user.tenant).get(id=studentid)
    response_data=[]
    # try:
    attendance=Attendance.objects.filter(class_section=class_selected, student=student).get(date=date)
    response_data.append({'is_present':attendance.ispresent, 'remarks':attendance.remarks,'id':attendance.id})
    return response_data
    # except:
    #   pass

def get_cce_transcript(request, year):
    this_tenant=request.user.tenant
    studentid=int(request.POST.get('student'))
    classid=int(request.POST.get('classsection'))
    response_data=[]
    class_group_selected=class_group.objects.for_tenant(this_tenant).\
                    get(classSection_classadmin_classGroup_genadmin=classid)
    subjects=Syllabus.objects.for_tenant(this_tenant).filter(class_group=class_group_selected,year=year).select_related('subject')
    for item in subjects:
        response_data.append({'data_type':'Subject','name': item.subject.name, 'id':item.subject.id})
    try:
        final_data=exam_year_final.objects.for_tenant(this_tenant).get(year=year,class_section=classid)
    except:
        pass
    student=Student.objects.for_tenant(this_tenant).get(id=studentid)
    this_tenant=request.user.tenant
    exam_report_details=exam_report.objects.for_tenant(this_tenant).filter(student=student, year=year)
    subjects=Syllabus.objects.for_tenant(this_tenant).filter(class_group=class_group_selected)
    for report in exam_report_details:
        exam=report.exam        
        if (exam.name=='SA2'):
            try:
                subject_data=Subject.objects.for_tenant.get(id=report.subject.id)
                final_subject=exam_year_final.objects.for_tenant(this_tenant).filter(final_report=final_data,subject=subject_data)
                response_data.append({'data_type':'Final','subject': report.subject.name, 'total':final_subject.final_score})
            except:
                pass        
        response_data.append({'data_type':'Exam','name':exam.key,'grade':report.grade,'subject': report.subject.name})
    return response_data