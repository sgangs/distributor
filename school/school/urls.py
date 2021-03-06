from django.conf.urls import include,url
from django.conf.urls import (handler400, handler403, handler404, handler500)
from django.contrib import admin
from django.contrib.auth.views import logout, password_reset, password_reset_done, password_reset_confirm,\
        password_reset_complete, password_change, password_change_done

from school import views
from .forms import revisedPasswordResetForm

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^$', views.HomeView.as_view()),
    url(r'^$', views.home, name='home'),
    url(r'^register/$', views.RegisterView, name='register'),

    #Login and logout
    url(r'^login/', views.custom_login, name='login'),
    url(r'^logout/$', logout, name='logout'),

    #Post login landing
    url(r'^landing/$', views.landing, name='landing'),

    #change password
    url(r'^password-change/$',password_change,name='password_change'),
    url(r'^password-change/done/$',password_change_done,name='password_change_done'),

    # restore password urls
    url(r'^password-reset/$', views.custom_password_reset, {'from_email': 'support@techassisto.com', \
        'subject_template_name':"Assisto-Your Technical Assistant Reset Password",\
        'password_reset_form':revisedPasswordResetForm},name='password_reset'),
    url(r'^password-reset/done/$', password_reset_done, name='password_reset_done'),
    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', password_reset_confirm, name='password_reset_confirm'),
    url(r'^password-reset/complete/$', password_reset_complete, name='password_reset_complete'),

    #rasie error url
    url(r'^permission-denied/$', views.permission_denied, name='permission_denied'),
    #All the apps
    url(r'^genadmin/', include('school_genadmin.urls',namespace='genadmin', app_name='genadmin')),
    url(r'^eduadmin/', include('school_eduadmin.urls',namespace='eduadmin', app_name='eduadmin')),
    url(r'^classadmin/', include('school_classadmin.urls',namespace='classadmin', app_name='classadmin')),
    url(r'^accounts/', include('school_account.urls',namespace='accounts', app_name='accounts')),
    url(r'^student/', include('school_student.urls',namespace='student', app_name='student')),
    url(r'^teacher/', include('school_teacher.urls',namespace='teacher', app_name='teacher')),
    url(r'^fees/', include('school_fees.urls',namespace='fees', app_name='fees')),
    url(r'^salary/', include('school_salary.urls',namespace='salary', app_name='salary')),
    url(r'^library/', include('school_library.urls',namespace='library', app_name='library')),
    url(r'^hr/', include('school_hr.urls',namespace='hr', app_name='hr')),
    url(r'^studentview/', include('school_student_view.urls',namespace='student_view', app_name='student_view')),
]

#Error Handlers
handler400 = 'school.views.bad_request'
handler403 = 'school.views.permission_denied'
handler404 = 'school.views.page_not_found'
handler500 = 'school.views.server_error'
