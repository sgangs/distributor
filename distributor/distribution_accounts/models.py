from django.db import models
from django.db.models import signals
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
import datetime as dt
from datetime import datetime

from distribution_user.models import Tenant


class TenantManager(models.Manager):
	def for_tenant(self, tenant):
		return self.get_queryset().filter(tenant=tenant)
		

#This creates an accounting period
class accountingPeriod(models.Model):
	start=models.DateField(auto_now=False)
	end=models.DateField(auto_now=False)
	key=models.CharField(max_length=10)
	slug=models.SlugField(max_length=20)
	tenant=models.ForeignKey(Tenant,related_name='period_account_user_tenant')
	objects = TenantManager()
	
	#def get_absolute_url(self):
	#	return reverse('master_detail', kwargs={'detail':self.slug})

	def save(self, *args, **kwargs):
		if not self.key:
			item=self.tenant.key+" "+self.key
			self.slug=slugify(item)
		super(accountingPeriod, self).save(*args, **kwargs)
	
	class Meta:
		unique_together = (("key", "tenant"))
		ordering = ('start',)

	def __str__(self):
		return self.start


#This is a list of accounts
class accountChart(models.Model):
	account_type=(('Assets','Assets'),
				('Liabilities','Liabilities'),
				('Equity','Equity'),
				('Revenue','Revenue'),
				('Expense','Expense'))
	name=models.CharField(max_length =200)
	remarks=models.TextField(blank=True)
	account_type=models.CharField('Account type', max_length=12,choices=account_type)
	slug=models.SlugField(max_length=20)
	key=models.CharField(max_length=20)
	tenant=models.ForeignKey(Tenant,related_name='accountchart_account_user_tenant')
	objects = TenantManager()
	
	def get_absolute_url(self):
		return reverse('accounts:account_detail', kwargs={'detail':self.slug})

	def save(self, *args, **kwargs):
		if not self.id:
			item=self.tenant.key+" "+self.key
			self.slug=slugify(item)
		super(accountChart, self).save(*args, **kwargs)
	
	class Meta:
		unique_together = (("key", "name","tenant"))
		ordering = ['account_type','name',]

	def __str__(self):
		return self.name


#This is a list of journals
class Journal(models.Model):
	date=models.DateTimeField(default=datetime.now)
	journal_type=models.TextField(blank=True, null=True)
	group=models.CharField(max_length=15, blank=True, null=True)
	slug=models.SlugField(max_length=20)
	key=models.CharField(max_length=20)
	tenant=models.ForeignKey(Tenant,related_name='journal_account_user_tenant')
	objects = TenantManager()

	#def get_absolute_url(self):
	#	return reverse('master_detail', kwargs={'detail':self.slug})

	def save(self, *args, **kwargs):
		if not self.id and self.key == "":
			data="jr"
			tenant=self.tenant.key
			today=dt.date.today()
			today_string=today.strftime('%y%m%d')
			next_journal_number='001'
			last_journal=type(self).objects.filter(tenant=self.tenant).\
							filter(key__contains=today_string).order_by('key').last()
			if last_journal:
				last_journal_number=int(last_journal.key[8:])
				next_journal_number='{0:03d}'.format(last_journal_number + 1)
			self.key=data + today_string + next_journal_number

		if not self.id:
			item=self.tenant.key+" "+self.key
			self.slug=slugify(item)
		super(Journal, self).save(*args, **kwargs)
	
	class Meta:
		unique_together = (("key", "tenant"))
		ordering = ('date','group',)

	def __str__(self):
		return self.name

#This is to link journal entry for each journal
class journalEntry(models.Model):
	transaction_type=(('Credit','Credit'),
				('Debit','Debit'))	
	journal=models.ForeignKey(Journal,related_name='journalEntry_journal')
	account=models.ForeignKey(accountChart,related_name='journalEntry_accountChart')
	transaction_type=models.CharField('Transaction type', max_length=6,choices=transaction_type)
	value=models.DecimalField(max_digits=12, decimal_places=2)
	tenant=models.ForeignKey(Tenant,related_name='journalentry_account_user_tenant')
	objects = TenantManager()
	
	#def get_absolute_url(self):
	#	return reverse('master_detail', kwargs={'detail':self.slug})

	#def save(self, *args, **kwargs):
	#	if not self.id:
	#		item=self.tenant.key+" "+self.key
	#		self.slug=slugify(item)
	#	super(Account, self).save(*args, **kwargs)
	
	class Meta:
		unique_together = (("journal", "account"))
		ordering = ('journal','-transaction_type',)

	def __str__(self):
		return self.name


#This model is for modes of payment
class paymentMode(models.Model):
	choice=(('Yes','Yes'),
				('No','No'))
	name = models.TextField('Payment Mode Name')
	payment_account=models.ForeignKey(accountChart,related_name='paymentMode_accountChart')
	default=models.CharField('Default Payment Mode ?', max_length=3,choices=choice, default="No")
	tenant=models.ForeignKey(Tenant,related_name='paymentmode_account_user_tenant')
	objects = TenantManager()

	class Meta:
		unique_together = (("payment_account", "tenant"),("name", "tenant") )
		ordering = ('name',)

	def __str__(self):
		return self.name
