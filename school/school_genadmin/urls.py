from django.conf.urls import include,url
from django.contrib import admin
from django.contrib.auth.views import login, logout
#from distributor.views import HomeView
from . import views

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    #url(r'^landing/$', views.genadmin_new, name='landing'),
    #url(r'^newbranch/$', views.genadmin_new, {'input_type': 'Branch'}, name='new_branch'),
    url(r'^base/$', views.base, name='base'),
    url(r'^newsubject/$', views.genadmin_new, {'input_type': 'Subject'}, name='new_subject'),
    url(r'^newclassgroup/$', views.genadmin_new, {'input_type': 'class_group'}, name='new_class_group'),
    url(r'^newhouse/$', views.genadmin_new, {'input_type': 'House'}, name='new_house'),
    url(r'^calender/$', views.calender, name='calender'),
    url(r'^subjectlist/$', views.master_list, {'input_type': 'Subject'}, name='subject_list'),
    url(r'^classgrouplist/$', views.master_list, {'input_type': 'Class Group'}, name='class_group_list'),
    url(r'^houselist/$', views.master_list, {'input_type': 'House'}, name='house_list'),
    #url(r'^housedetail/(?P<detail>[-\S]+)/$', views.classdetail, name='class_detail'),
]