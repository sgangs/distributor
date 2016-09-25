from django.db import models
from django.db.models import signals
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
import datetime as dt
from datetime import datetime

from distribution_master.models import Manufacturer, Product, Zone, Customer, Vendor, Unit
from distribution_user.models import Tenant


class TenantManager(models.Manager):
	def for_tenant(self, tenant):
		return self.get_queryset().filter(tenant=tenant)


#This model is for the sales invoice
class salesInvoice(models.Model):
	#address=models.TextField
	invoice_id = models.CharField(blank=True, max_length=12)
	slug=models.SlugField(max_length=300)
	total=models.DecimalField(max_digits=12, decimal_places=2)
	grand_discount=models.DecimalField(max_digits=10, decimal_places=2)
	#amount_paid=models.DecimalField(max_digits=12, decimal_places=2)
	date=models.DateTimeField(default=datetime.now, blank=True)
	customer=models.ForeignKey(Customer, related_name='salesInvoice_sales_master_customer')
	tenant=models.ForeignKey(Tenant,related_name='sales_sales_user_tenant')
	objects = TenantManager()
		

	def get_absolute_url(self):
		return reverse('sales:invoice_detail', kwargs={'detail':self.slug})

	#the save method is overriden to give unique invoice ids, slug and customer_name
	def save(self, *args, **kwargs):
		if not self.id:
			data="si"
			tenant=self.tenant.key
			today=dt.date.today()
			today_string=today.strftime('%y%m%d')
			next_invoice_number='001'
			last_invoice=type(self).objects.filter(tenant=self.tenant).filter(invoice_id__contains=today_string).order_by('invoice_id').last()
			if last_invoice:
				last_invoice_number=int(last_invoice.invoice_id[8:])
				next_invoice_number='{0:03d}'.format(last_invoice_number + 1)
			self.invoice_id=data + today_string + next_invoice_number
			toslug=tenant+" " +self.invoice_id
			self.slug=slugify(toslug)
		super(salesInvoice, self).save(*args, **kwargs)


	class Meta:
		ordering = ('date',)


	def __str__(self):
		return  '%s %s %s' % (self.invoice_id, self.customer_name, self.date)



		
#This model is for line items of a sales invoice
class salesLineItem(models.Model):
	name=models.CharField(max_length =200)
	key=models.CharField(max_length =20)
	sub_key=models.CharField(max_length=50)
	unit=models.CharField(max_length=20)
	manufacturer=models.CharField(max_length=20)
	#batch=models.CharField(max_length=200)
	discount1=models.DecimalField(max_digits=4, decimal_places=2)
	discount2=models.DecimalField(max_digits=4, decimal_places=2)
	quantity=models.PositiveSmallIntegerField(default=0)
	free=models.PositiveSmallIntegerField(default=0)
	mrp=models.DecimalField(max_digits=10, decimal_places=2)
	selling_price=models.DecimalField(max_digits=10, decimal_places=2)
	vat_type=models.CharField(max_length =50)
	vat_percent=models.DecimalField(max_digits=4, decimal_places=2)
	invoice_no=models.ForeignKey(salesInvoice, related_name='salesLineItem_sales_sales_salesInvoice')
	item_key=models.CharField('product-id', max_length = 10)

class salesPayment(models.Model):
	invoice_no=models.ForeignKey(salesInvoice, related_name='salesPayment_sales_sales_salesInvoice')
	amount_paid=models.DecimalField(max_digits=12, decimal_places=2)
	collected_on=models.DateTimeField(null=True)