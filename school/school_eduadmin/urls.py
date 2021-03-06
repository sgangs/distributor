from django.conf.urls import include,url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^base/$', views.base, name='base'),
    url(r'^newclass/$', views.class_new, name='new_class'),
    url(r'^newsyllabus/$', views.new_syllabus, name='new_syllabus'),
    # url(r'^newexam/$', views.eduadmin_new, {'input_type': 'Exam'}, name='new_exam'),
    url(r'^newexam/$', views.new_exam, name='new_exam'),
    url(r'^newclassteacher/$', views.eduadmin_new, {'input_type': 'ClassTeacher'}, name='new_classteacher'),
    url(r'^newsubjectteacher/$', views.eduadmin_new, {'input_type': 'Subject Teacher'}, name='new_subject_teacher'),
    url(r'^newclassstudentone/$', views.eduadmin_new, {'input_type': 'ClassStudent'}, name='new_class_student'),
    url(r'^newclassstudent/$', views.class_student_add, name='new_class_student'),
    url(r'^newterm/$', views.eduadmin_new, {'input_type': 'Term'}, name='new_term'),
    url(r'^newexamtype/$', views.exam_type_new,name='new_exam_type'),
    url(r'^newgradetable/$', views.new_grade_table,name='new_grade_table'),
    # url(r'^linkexamclass/$', views.link_exam_class,name='link_exam_class'),
    url(r'^viewexamlist/$', views.view_exam_list,name='view_exam_list'),    
    url(r'^publishexam/$', views.publish_exam,name='publish_exam'),
    url(r'^totalperiodentry/$', views.eduadmin_new, {'input_type': 'Total Period'}, name='total_period_entry'),
    url(r'^teacherperiod/$', views.view_teacher_period, name='teacher_period'),
    url(r'^viewgradetable/$', views.view_grade_table,name='view_grade_table'),
    url(r'^viewsyllabus/$', views.view_syllabus,name='view_syllabus'),
    url(r'^classlist/$', views.eduadmin_list, {'input_type': 'Class'}, name='class_list'),
    url(r'^subjectteacherlist/$', views.eduadmin_list, {'input_type': 'Subject Teacher'}, name='subject_teacher_list'),
    url(r'^promotestudent/$', views.promote_student, name='promote_student'),
    url(r'^classdetail/(?P<detail>[-\S]+)/addperiod/$', views.view_add_period, name='add_period'),
    url(r'^classdetail/(?P<detail>[-\S]+)/classteacher/$', views.view_add_period, name='add_period'),
    url(r'^classdetail/(?P<detail>[-\S]+)/subjectteacher/$', views.view_add_period, name='add_period'),
    url(r'^classdetail/(?P<detail>[-\S]+)/$', views.classdetail, name='class_detail'),
    #url(r'^(?P<detail>[-\S]+)/$',views.purchase_detail, {'type': 'Detail'}, name='invoice_detail'),
    #url(r'^calender/$', views.calender, name='calender'),
]