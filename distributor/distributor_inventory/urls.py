from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [

    url(r'^noinventory/$', views.not_maintained_inventory, name='not_maintained_inventory'),
    url(r'^getproduct/$', views.get_product, name='get_product'),
    url(r'^getcurrentdata$', views.inventory_data, name='inventory_data'),
    url(r'^currentinventory/$', views.inventory_template, name='inventory_template'),
    url(r'^openinginventory/$', views.opening_inventory, name='opening_inventory'),
    url(r'^openinginventory/data/$', views.opening_inventory_data, name='opening_inventory_data'),
    url(r'^uploadopeninginventory/$', views.import_opening_inventory, name='import_opening_inventory'),
    url(r'^getproduct/$', views.get_product, name='get_product'),
    url(r'^getproductinventory/$', views.get_product_inventory, name='get_product_inventory'),
    url(r'^inventorytransfer/$', views.inventory_transfer_template, name='inventory_transfer_template'),
    url(r'^inventorytransfer/data/$', views.inventory_transfer_data, name='inventory_transfer_data'),
    url(r'^inventorywastage/$', views.inventory_wastage_template, name='inventory_wastage_template'),
    url(r'^productvaluationmovement/data/$', views.product_valuation_movement_data, name='product_valuation_movement_data'),
    url(r'^productvaluationmovement/$', views.product_valuation_movement_template, name='product_valuation_movement_template'),

    url(r'^openinginventory/product/data/$', views.productwise_opening_inventory, name='productwise_opening_inventory'),
    url(r'^inventory/delete/$', views.delete_inventory_view, name='delete_inventory_view'),
    url(r'^inventory/delete/data/$', views.delete_opening_inventory, name='delete_opening_inventory'),


    url(r'^barcode/(?P<pk_detail>[-\S]+)/$', views.write_pdf_view, name='write_pdf_view'),
    # url(r'^eventdetail/(?P<detail>[-\S]+)/$', views.classdetail, name='class_detail'),    
]