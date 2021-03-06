import datetime as dt
from datetime import datetime
from django.db import models
from django.db.models import signals
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify

from school_user.models import User, Tenant
from school_teacher.models import Teacher
from school_student.models import Student
from school_genadmin.models import class_group, Subject, House

class TenantManager(models.Manager):
	def for_tenant(self, tenant):
		return self.get_queryset().filter(tenant=tenant)

#This is the class model. Each student has a class.
class class_section(models.Model):
	id=models.BigAutoField(primary_key=True)
	name=models.CharField("Class Name with section", db_index=True,blank=True, max_length=15)
	room=models.CharField("Room name/no.",blank=True, max_length=10)
	classgroup=models.ForeignKey(class_group,db_index=True,related_name='classSection_eduadmin_classGroup_genadmin')
	slug=models.SlugField(max_length=40)
	tenant=models.ForeignKey(Tenant,db_index=True,related_name='classsection_eduadmin_user_tenant')
	objects=TenantManager()
	
	def get_absolute_url(self):
		return reverse('eduadmin:class_detail', kwargs={'detail':self.slug})

	def save(self, *args, **kwargs):
		if not self.id:
			item="cs"+" "+self.tenant.key+" "+self.name
			self.slug=slugify(item)
		super(class_section, self).save(*args, **kwargs)

	class Meta:
		unique_together = (("name", "tenant"))
		# ordering = ('name',)
		
	def __str__(self):
		return self.name

class classteacher(models.Model):
	id=models.BigAutoField(primary_key=True)
	class_section=models.ForeignKey(class_section,db_index=True,related_name='classteacher_classSection')
	class_teacher=models.ForeignKey(Teacher,db_index=True,related_name='classteacher_eduadmin_teacher_teacher')
	year=models.PositiveSmallIntegerField(db_index=True,default=datetime.now().year)
	tenant=models.ForeignKey(Tenant,db_index=True,related_name='classteacher_eduadmin_user_tenant')
	objects=TenantManager()
	
	# def get_absolute_url(self):
	# 	return reverse('master:detail', kwargs={'detail':self.slug})

	class Meta:
		unique_together = (("class_section", "year","tenant"))
		#ordering = ('name',)
		
	def __str__(self):
		return '%s %s %s' % (self.class_section, self.class_teacher, self.year)

#This is for subject teacher for each subject. Lets create a FK to syllabus, so as to ease in rendering views.
class subject_teacher(models.Model):
	id=models.BigAutoField(primary_key=True)
	subject=models.ForeignKey(Subject,db_index=True,related_name='subjectTeacher_eduadmin_subject_genadmin')
	class_section=models.ForeignKey(class_section,db_index=True,related_name='subjectTeacher_classSection')
	teacher=models.ForeignKey(Teacher,db_index=True,related_name='subjectTeacher_eduadmin_teacher_teacher')
	year=models.PositiveSmallIntegerField(db_index=True,default=datetime.now().year)
	tenant=models.ForeignKey(Tenant,db_index=True,related_name='subjectTeacher_eduadmin_user_tenant')
	objects=TenantManager()
	
	class Meta:
		unique_together = (("class_section","subject","teacher","year", "tenant"))

	def __str__(self):
		return '%s %s %s' % (self.class_section.name, self.subject.name, self.teacher.key)

class classstudent(models.Model):
	id=models.BigAutoField(primary_key=True)
	class_section=models.ForeignKey(class_section,db_index=True,related_name='classstudent_classSection')
	roll_no=models.PositiveSmallIntegerField()
	student=models.ForeignKey(Student,db_index=True,related_name='classstudent_eduadmin_student_student')
	year=models.PositiveSmallIntegerField(db_index=True,default=datetime.now().year)
	is_promoted=models.BooleanField(default=False)
	tenant=models.ForeignKey(Tenant,db_index=True,related_name='classstudent_eduadmin_user_tenant')
	objects=TenantManager()
	
	# def get_absolute_url(self):
	# 	return reverse('master:detail', kwargs={'detail':self.slug})

	class Meta:
		unique_together = (("class_section","student","year", "tenant"), ("class_section", "roll_no","year", "tenant"))
		ordering = ('roll_no',)
		
	def __str__(self):
		return '%s %s - %s' % (self.class_section, self.student, self.year)


exam_type=(('CBSE','CBSE'),
		('M','Marks Only'),
		('MG','Marks And Grades'))

class exam_creation(models.Model):
	id=models.BigAutoField(primary_key=True)
	exam_type=models.CharField(max_length=6,choices=exam_type)
	is_term=models.BooleanField(default=True) #Does the system have terms?
	year=models.PositiveSmallIntegerField(db_index=True)
	# has_coscholastic=models.BooleanField(default=True)
	opted=models.BooleanField()
	tenant=models.ForeignKey(Tenant,db_index=True,related_name='examCreation_eduadmin_user_tenant')
	objects=TenantManager()

	class Meta:
		unique_together = (("exam_type","year", "tenant"))
		# ordering = ('show_from','show_until')

	def __str__(self):
		return '%s ' % (self.exam_type)


#Define Terms, example Term 1 & Term 2
class Term(models.Model):
	id=models.BigAutoField(primary_key=True)
	name=models.CharField(max_length=15)
	number=models.PositiveSmallIntegerField("Term Number")
	year=models.PositiveSmallIntegerField("Academic Year",db_index=True)
	weightage=models.PositiveSmallIntegerField("Term Weightage",default=1)
	total=models.PositiveSmallIntegerField("Term Total",default=100)
	is_active=models.BooleanField("Is this Term active", default=True)
	tenant=models.ForeignKey(Tenant,db_index=True,related_name='term_eduadmin_user_tenant')
	objects=TenantManager()
	
	# def get_absolute_url(self):
	# 	return reverse('master:detail', kwargs={'detail':self.slug})

	class Meta:
		unique_together = (("is_active","name","year", "tenant"))
		ordering = ('name',)

	def __str__(self):
		return '%s' % (self.name)


#This is for the syllabus class group wise. 
class Syllabus(models.Model):
	id=models.BigAutoField(primary_key=True)
	class_group=models.ForeignKey(class_group,db_index=True,related_name='syllabus_eduadmin_classGroup_genadmin')
	subject=models.ForeignKey(Subject,db_index=True,related_name='syllabus_eduadmin_subject_genadmin')
	year=models.PositiveSmallIntegerField(db_index=True)
	weightage=models.PositiveSmallIntegerField("Subject Weightage",default=1)
	#Additional subjects wont have any effect on final score
	is_additional=models.BooleanField('Is This Additional (Wont effect total calculation in exam)?',default=False) 
	is_elective=models.BooleanField('Is This An Elective?',default=False) 
	tenant=models.ForeignKey(Tenant,db_index=True,related_name='syllabus_eduadmin_user_tenant')
	objects=TenantManager()
	
	# def get_absolute_url(self):
	# 	return reverse('master:detail', kwargs={'detail':self.slug})

	class Meta:
		unique_together = (("class_group", "subject", "year","tenant"))
		# unique_together = (("key", "term","tenant"))
		ordering = ('class_group','id')
		
	# def __str__(self):
	# 	return self.key

#This is for the syllabus class group wise. 
class syllabus_topic(models.Model):
	syllabus=models.ForeignKey(Syllabus,db_index=True,related_name='syllabusTopic_syllabusSubject')
	topic=models.TextField()
	month=models.TextField() #Expected month whe this will be studied
	tenant=models.ForeignKey(Tenant,db_index=True,related_name='syllabusTopic_eduadmin_user_tenant')
	objects=TenantManager()



grade_choices=(('S','Scholastic'),
		('C','Co-scholastic'))

#This is the list of subjects to be taught in school.
class grade_table(models.Model):
	id=models.BigAutoField(primary_key=True)
	grade_type=models.CharField("Type of grade?",max_length=1,choices=grade_choices)
	table_name=models.CharField("Table Name",max_length=80,choices=grade_choices)
	tenant=models.ForeignKey(Tenant,db_index=True,related_name='gradeTable_eduadmin_user_tenant')
	objects=TenantManager()
	
	# def get_absolute_url(self):
	# 	return reverse('master:detail', kwargs={'detail':self.slug})
	
	class Meta:
		unique_together = (("table_name", "tenant"))
		# ordering = ('tenant','sl_no')
		
	def __str__(self):
		return self.name

class grade_item(models.Model):
	id=models.BigAutoField(primary_key=True)
	grade_table=models.ForeignKey(grade_table,db_index=True,related_name='gradeItem_gradeTable')
	sl_no=models.PositiveSmallIntegerField()
	min_mark=models.PositiveSmallIntegerField()
	max_mark=models.PositiveSmallIntegerField()
	grade=models.CharField(max_length=4)
	grade_point=models.DecimalField(max_digits=4, decimal_places=2)
	tenant=models.ForeignKey(Tenant,db_index=True,related_name='gradeItem_eduadmin_user_tenant')
	objects=TenantManager()

	class Meta:
		# unique_together = (("grade_type", "tenant"))
		ordering = ('tenant','sl_no')


class Exam(models.Model):
	id=models.BigAutoField(primary_key=True)
	name=models.CharField(db_index=True,max_length=40)
	term=models.ForeignKey(Term, related_name='exam_term')
	classgroup=models.ManyToManyField(class_group,db_index=True,related_name='exam_eduadmin_classGroup_genadmin')
	key=models.CharField("Short Form",max_length=20)
	total=models.PositiveSmallIntegerField()
	year=models.PositiveSmallIntegerField(db_index=True)
	has_subexam=models.BooleanField(default=False)
	period_from=models.DateField("Exam Class Starts", null=True, blank=True)
	period_to=models.DateField("Exam Class Ends", null=True, blank=True)
	is_published=models.BooleanField(default=False)
	# is_active=models.BooleanField(default=True)
	weightage=models.DecimalField("Exam Weightage",max_digits=4, decimal_places=2, default=1)
	serial_no=models.PositiveSmallIntegerField("Exam number")
	tenant=models.ForeignKey(Tenant,db_index=True,related_name='exam_eduadmin_user_tenant')
	objects=TenantManager()
	
	# def get_absolute_url(self):
	# 	return reverse('master:detail', kwargs={'detail':self.slug})

	class Meta:
		unique_together = (("key","year", "tenant"))
		ordering = ('year','term','serial_no')

	def __str__(self):
		return '%s %s' % (self.name, self.year)



class student_house(models.Model):
	id=models.BigAutoField(primary_key=True)
	house=models.ForeignKey(House,db_index=True,related_name='studentHouse_eduadmin_genadmin_house')
	student=models.ForeignKey(Student,db_index=True,related_name='studentHouse_eduadmin_student_student')
	year=models.PositiveSmallIntegerField(default=datetime.now().year)
	tenant=models.ForeignKey(Tenant,db_index=True,related_name='studentHouse_eduadmin_user_tenant')
	objects=TenantManager()
	
	# def get_absolute_url(self):
	# 	return reverse('master:detail', kwargs={'detail':self.slug})

	class Meta:
		unique_together = (("house","student","year", "tenant"))
		# ordering = ('name',)
		
	def __str__(self):
		return '%s %s %s' % (self.house, self.student, self.year)

class total_period(models.Model):
	id=models.BigAutoField(primary_key=True)
	number_period=models.PositiveSmallIntegerField("Number of Periods in a day",db_index=True)
	tenant=models.OneToOneField(Tenant, db_index=True,related_name='totalPeriod_eduadmin_user_tenant')
	objects=TenantManager()
	
	# def get_absolute_url(self):
	# 	return reverse('master:detail', kwargs={'detail':self.slug})

	def __str__(self):
		return self.number_periods

class period(models.Model):
	id=models.BigAutoField(primary_key=True)
	day=models.PositiveSmallIntegerField()
	period=models.PositiveSmallIntegerField()
	year=models.PositiveSmallIntegerField()
	slug=models.SlugField(max_length=42)
	class_section=models.ForeignKey(class_section,db_index=True,related_name='period_classSection')
	subject=models.ForeignKey(Subject,db_index=True, related_name='period_eduadmin_subject_genadmin')
	teacher=models.ForeignKey(Teacher,db_index=True, related_name='period_eduadmin_teacher_teacher')
	tenant=models.ForeignKey(Tenant,db_index=True,related_name='period_eduadmin_user_tenant')
	objects=TenantManager()

	def save(self, *args, **kwargs):
		if not self.id:
			item="pe"+""+self.tenant.key+" "+str(self.day)+" "+str(self.period)+" "+str(self.year)
			self.slug=slugify(item)
		super(period, self).save(*args, **kwargs)

	# class Meta:
	# 	unique_together = (("day","period","year", "tenant"))
		# ordering = ('name',)
		
	def __str__(self):
		return '%s %s' % (self.day, self.period)