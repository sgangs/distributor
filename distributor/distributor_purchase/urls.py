from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^receipt-order/(?P<pk>[-\S]+)/$', views.receipt_order, name='receipt_order'),

    url(r'^receipt/$', views.purchase_receipt_new, name='purchase_receipt_new'),
    url(r'^receipt/save/$', views.purchase_receipt_save, name='purchase_receipt_save'),
    url(r'^receipt/detailview/(?P<pk>[-\S]+)/$', views.receipts_detail_view, name='receipts_detail_view'),
    url(r'^receipt/api/getproduct$', views.get_product, name='get_product'),
    url(r'^receipt/detail/(?P<pk>[-\S]+)/$', views.receipts_details, name='receipts_details'),
    url(r'^receipt/excel/(?P<pk>[-\S]+)/$$', views.excel_receipt, name='excel_receipt'),

    url(r'^receipt/api/getproduct/details$', views.get_product_data_id, name='get_product_data_id'),
    url(r'^receipt/api/getproduct/barcode$', views.get_product_data_barcode, name='get_product_data_barcode'),
    url(r'^productinventorydetails/$', views.product_inventory_details, name='product_inventory_details'),

    url(r'^purchase-receipt-vendor/$', views.purchase_receipt_vendor, name='purchase_receipt_vendor'),

    # url(r'^receipt/api/getproduct/warehouse/$', views.get_product_inventory, name='get_product_inventory'),

    
    url(r'^receipt/delete/$', views.delete_purchase, name='delete_purchase'),

    url(r'^receiptlist/$', views.receipt_list, name='receipt_list'),
    url(r'^receiptlist/listall/$', views.all_receipts, name='all_receipts'),
    url(r'^receiptlist/metadata/$', views.receipts_metadata, name='receipts_metadata'),
    
    url(r'^receipt/paymentsave/$', views.payment_register, name='payment_register'),
    url(r'^paymentlist/$', views.payment_list, name='payment_list'),
    url(r'^paymentlistview/$', views.payment_list_view, name='payment_list_view'),
    
    url(r'^receipt/noninventory/$', views.purchase_receipt_new_noninventory, name='purchase_receipt_new_noninventory'),
    url(r'^receipt/noninventory/save/$', views.purchase_receipt_noninventory_save, name='purchase_receipt_noninventory_save'),

    url(r'^return/inventory/$', views.return_new_inventory, name='return_new_inventory'),
    url(r'^return/inventory/save/$', views.purchase_return_inventory_save, name='purchase_return_inventory_save'),

    url(r'^return/noninventory/$', views.return_new_noninventory, name='return_new_noninventory'),
    url(r'^return/noninventory/save/$', views.purchase_return_noninventory_save, name='purchase_return_noninventory_save'),

    url(r'^return/list/$', views.all_return_view, name='all_return_view'),
    url(r'^return/list/data/$', views.all_return_data, name='all_return_data'),
    
    url(r'^return/detailview/(?P<pk>[-\S]+)/$', views.return_detail_view, name='return_detail_view'),
    url(r'^return/detail/(?P<pk>[-\S]+)/$', views.return_details, name='return_details'),
    # url(r'^purchase_graph/$', views.purchase_crossfilter, name='purchase_crossfilter'),
    # url(r'^purchase_graph/data/$', views.receipts_crossfilter, name='receipts_crossfilter'),

    url(r'^hsnreport/$', views.get_hsn_report, name='get_hsn_report'),
    # url(r'^eventdetail/(?P<detail>[-\S]+)/$', views.classdetail, name='class_detail'),

    url(r'^vendor-ledger/$', views.vendor_ledger, name='vendor_ledger'),
    url(r'^vendor-ledger/data/$', views.vendor_ledger_data, name='vendor_ledger_data'),
    
    url(r'^vendor/opening-balance/$', views.vendor_opening_balance, name='vendor_opening_balance'),
    url(r'^vendor/opening-payment-list/$', views.vendor_opening_payment_list, name='vendor_opening_payment_list'),

    url(r'^order/$', views.purchase_order_new, name='purchase_order_new'),
    url(r'^order/save/$', views.purchase_order_save, name='purchase_order_save'),
    url(r'^order/list/$', views.order_list_view, name='order_list_view'),
    url(r'^order/list/data/$', views.all_orders, name='all_orders'),
    url(r'^order/detailview/(?P<pk>[-\S]+)/$', views.order_detail_view, name='order_detail_view'),
    url(r'^order/detail/$', views.order_details, name='order_details'),
    url(r'^order/delete/$', views.order_delete, name='order_delete'),

]