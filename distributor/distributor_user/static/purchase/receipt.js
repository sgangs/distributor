$(function(){
vat_type=["No VAT", "On MRP", "On actual"];
vat_type_reverse={"No VAT":0, "On MRP":1, "On actual":2};
var vat_input, vat_percent, unit_data;

$(document).on('keydown.autocomplete', '.name', function() {
    var el=this;
    $(this).autocomplete({
        source : "api/getproduct", 
        minLength: 3,
        timeout: 200,
        select: function( event, ui ) {
            $(el).closest('tr').find('td:nth-child(1) input').val(ui['item']['id']);
            $(el).closest('tr').find('td:nth-child(6) .unit').val(ui['item']['unit']);
            $(el).closest('tr').find('td:nth-child(15) input').val(ui['item']['cgst']);
            $(el).closest('tr').find('td:nth-child(17) input').val(ui['item']['sgst']);
            $(el).closest('tr').find('td:nth-child(19) input').val(ui['item']['igst']);
            // vat_input=ui['item']['vat_type']
            // $(el).closest('tr').find('td:nth-child(17) ').html(vat_type[vat_input]);
            // vat_percent=ui['item']['tax']
            // $(el).closest('tr').find('td:nth-child(18) ').html(vat_percent);
            $('.unit').selectpicker('refresh');
        }
    });
});

load_warehouse()

function load_warehouse(){
    $.ajax({
        url : "/master/warehouse/getdata/", 
        type: "GET",
        dataType: 'json',
        // handle a successful response
        success : function(jsondata) {
            $.each(jsondata, function(){
                $('#warehouse').append($('<option>',{
                    'data-id': this.id,
                    'text': this.address_1 + " "+ this.address_2
                }));
            });
            $('#warehouse').selectpicker('refresh')
        },
        // handle a non-successful response
        error : function() {
            swal("Oops...", "No warehouse data exist.", "error");
        }
    });
}

load_units()

function load_units(){
    $.ajax({
        url : "/master/dimensionunit/unitdata/", 
        type: "GET",
        dataType: 'json',
        // handle a successful response
        success : function(jsondata) {
            unit_data=jsondata
            $.each(jsondata, function(){
                $('#unit').append($('<option>',{
                    'data-id': this.id,
                    'title':this.symbol,
                    'text': this.name,
                }));
            });
            $('#unit').selectpicker('refresh');
        },
        // handle a non-successful response
        error : function() {
            swal("Oops...", "No unit is registered.", "error");
        }
    });
}

load_vendor()

function load_vendor(){
    $.ajax({
        url : "/master/vendor/getdata/", 
        type: "GET",
        dataType: 'json',
        // handle a successful response
        success : function(jsondata) {
            $.each(jsondata, function(){
                $('#vendor').append($('<option>',{
                    'data-id': this.id,
                    'text': this.name + ": "+ this.key
                }));
            });
            $('#vendor').selectpicker('refresh')
        },
        // handle a non-successful response
        error : function() {
            swal("Oops...", "No warehouse data exist.", "error");
        }
    });
}

$('.details').on("mouseenter", ".first", function() {
    $( this ).children( ".delete" ).show();
});

$('.details').on("mouseleave", ".first", function() {
    $( this ).children( ".delete" ).hide();
});

$('.details').on("click", ".delete", function() {
    $(this).parent().parent().remove();
    get_total();
});

$(".details").on("keyup", ".qty", function(){
    get_total();
});
$(".details").on("keydown", ".qty", function(){
    get_total();
});


$(".details").on("keyup", ".pr", function(){
    get_total();
});
$(".details").on("keydown", ".pr", function(){
    get_total();
});

$(".details").on("keyup", ".dv", function(){
    get_total();
});
$(".details").on("keydown", ".dv", function(){
    get_total();
});

$(".details").on("keyup", ".dv2", function(){
    get_total();
});
$(".details").on("keydown", ".dv2", function(){
    get_total();
});

$(".details").on("keyup", ".mrp", function(){
    get_total();
});
$(".details").on("keydown", ".mrp", function(){
    get_total();
});

$(".details").on("keyup", ".freet", function(){
    get_total();
});
$(".details").on("keydown", ".freet", function(){
    get_total();
});

$(".details").on("change", ".dt", function(){
    get_total();
});

$(".details").on("change", ".dt2", function(){
    get_total();
});

$(".details").on("keyup", ".cgstp", function(){
    get_total();
});
$(".details").on("keydown", ".cgstp", function(){
    get_total();
});

$(".details").on("keyup", ".sgstp", function(){
    get_total();
});
$(".details").on("keydown", ".sgstp", function(){
    get_total();
});

$(".details").on("keyup", ".igstp", function(){
    get_total();
});
$(".details").on("keydown", ".igstp", function(){
    get_total();
});


$( ".gd" ).change(function() {
    get_total();
});

$( ".gdt" ).change(function() {
    get_total();
});

function get_total(){
    var subtotal=0, total=0, tax_total=0;
    for (var a = document.querySelectorAll('table.details tbody tr'), i = 0; a[i]; ++i) {
        // get all cells with input field
        cells = a[i].querySelectorAll('input:last-child');
        // console.log(cells);
        var quantity=parseFloat($(cells[2]).val());
        // var free_tax_qty=parseFloat($(cells[4]).val());
        var free_tax_qty=0;
        var pur_rate=$(cells[4]).val()
        var mrp=$(cells[6]).val()
        var vat_total=0
        discount_type=$(a[i]).find('td:nth-child(10) :selected').data('id');
        discount_val=$(cells[7]).val();
        discount_type_2=$(a[i]).find('td:nth-child(12) :selected').data('id');
        discount_val_2=$(cells[8]).val();
        // vat_input=parseInt(vat_type_reverse[$(a[i]).find('td:nth-child(17)').html()]);
        // vat_percent=parseFloat($(a[i]).find('td:nth-child(18)').html());
        cgst_percent=parseFloat($(cells[9]).val());
        sgst_percent=parseFloat($(cells[10]).val());
        igst_percent=parseFloat($(cells[11]).val());
        if(isNaN(pur_rate)){
            pur_rate=0;
        }
        if(isNaN(quantity)){
            quantity=0;
        }
        if(isNaN(mrp)){
            mrp=0;
        }

        if(isNaN(cgst_percent)){
            cgst_percent=0;
        }
        if(isNaN(sgst_percent)){
            sgst_percent=0;
        }
        if(isNaN(igst_percent)){
            igst_percent=0;
        }
        // if(isNaN(free_tax_qty)){
        //     free_tax_qty=0;
        // }
        
        var this_total=quantity*pur_rate
        
        pur_disc_rate=pur_rate
        if (discount_type == 1){
            pur_disc_rate=pur_disc_rate-(discount_val*this_total/100);
            this_total=(this_total)-(discount_val*this_total/100);
        }
        else if(discount_type == 2){
            pur_disc_rate=pur_disc_rate - discount_val/quantity;
            this_total=(this_total - discount_val);
        }
        if (discount_type_2 == 1){
            pur_disc_rate=pur_disc_rate-(discount_val_2*this_total/100);
            this_total=(this_total)-(discount_val_2*this_total/100);
        }
        else if(discount_type_2 == 2){
            pur_disc_rate=pur_disc_rate - discount_val_2/quantity;
            this_total=(this_total - discount_val_2);
        }
        cgst_total=(this_total*cgst_percent)/100;
        sgst_total=(this_total*sgst_percent)/100;
        igst_total=(this_total*igst_percent)/100;
        $(a[i]).find('td:nth-child(16) ').html(cgst_total.toFixed(2))
        $(a[i]).find('td:nth-child(18) ').html(sgst_total.toFixed(2))
        $(a[i]).find('td:nth-child(20) ').html(igst_total.toFixed(2))
        // if (vat_input == 1){
            // vat_total=(mrp*(quantity+free_tax_qty))-(mrp*(quantity+free_tax_qty))/(100+vat_percent)*100;
        // }
        // else if (vat_input == 2){
            // vat_total=((pur_disc_rate*(quantity+free_tax_qty))*vat_percent)/100;
        // }
        $(a[i]).find('td:nth-child(14) ').html(this_total.toFixed(2));
        this_final_total=this_total+cgst_total+sgst_total+igst_total;
        $(a[i]).find('td:nth-child(21) ').html(this_final_total.toFixed(2));
        subtotal=subtotal+this_total;
        tax_total+=cgst_total+sgst_total+igst_total;
    }
    total=subtotal+tax_total
    gd_type=$('.gdt').find(':selected').data('id')
    gd_value=parseFloat($('.gd').val())
    var gd_calculated=0;
    if(isNaN(gd_value)){
        gd_value=0;
    }
    if (gd_type == 1){
        gd_calculated=(gd_value*subtotal/100)
        total=total-gd_calculated;
    }
    else if(gd_type == 2){
        gd_calculated=gd_value
        total=(total-gd_calculated);
    }
    $('.subtotal_receipt').html(subtotal.toFixed(2))
    $('.grand_discount').html(gd_calculated.toFixed(2))
    $('.taxtotal_receipt').html(tax_total.toFixed(2))
    $('.total_receipt').html(total.toFixed(2))
};

$('.addmore').click(function(){
    count=$('.details tr').length;
    var data='<tr class="data">'+
    '<td hidden=""><input class="id"></td>'+
    '<th colspan="1" class="first"><button style="display: none;" class="delete btn btn-danger btn-xs">-</button></th>'+
    '<td colspan="3"><input class="form-control name"></td>'+
    '<td colspan="1"><input class="form-control qty"></td>'+
    // '<td colspan="1"><input class="form-control free"></td>'+
    // '<td colspan="1"><input class="form-control freet"></td>'+
    '<td colspan="1" hidden><input class="unitid"></td>'+
    '<td colspan="1"><select class="form-control selectpicker unit" id="unit"></select></td>'+
    '<td colspan="1"><input class="form-control pr"></td>'+
    '<td colspan="1"><input class="form-control tsr"></td>'+
    '<td colspan="1"><input class="form-control mrp"></td>'+
    '<td colspan="1">'+
        '<select class="form-control selectpicker dt">'+
            '<option data-id=0 title="-">No Disc.</option>'+
            '<option data-id=1 title="%">Percent(%)</option>'+
            '<option data-id=2 title="V">Value</option>'+
    '</select></td>'+
    '<td colspan="1"><input class="form-control dv"></td>'+
    '<td colspan="1">'+
        '<select class="form-control selectpicker dt2">'+
            '<option data-id=0 title="-">No Disc.</option>'+
            '<option data-id=1 title="%">Percent(%)</option>'+
            '<option data-id=2 title="V">Value</option>'+
    '</select></td>'+
    '<td colspan="1"><input class="form-control dv2"></td>'+
    '<td colspan="1" class="total">0.00</td>'+
    // '<td colspan="1" class="vt"></td>'+
    // '<td colspan="1" class="vp"></td>'+
    '<td colspan="1"><input class="form-control cgstp"></td>'+
    '<td colspan="1" class="cgstv">0.00</td>'+
    '<td colspan="1"><input class="form-control sgstp"></td>'+
    '<td colspan="1" class="sgstv">0.00</td>'+
    '<td colspan="1"><input class="form-control igstp"></td>'+
    '<td colspan="1" class="igstv">0.00</td>'+
    '<td colspan="1" class="tv">0.00</td>';
    $('.details').append(data);

    $('.dt').selectpicker('refresh');
    $('.dt2').selectpicker('refresh');
    
    $.each(unit_data, function(){
        $('.details').find('tr:eq('+count+')').find('#unit').append($('<option>',{
            'data-id': this.id,
            'title':this.symbol,
            'text': this.name,
        }));
    });
    $('.unit').selectpicker('refresh');
})


$('.submit').click(function(e) {
    swal({
        title: "Are you sure?",
        text: "Are you sure you want to create a new receipt?",
        type: "warning",
        showCancelButton: true,
      // confirmButtonColor: "#DD6B55",
        confirmButtonText: "Yes, add create new receipt!",
        closeOnConfirm: true,
        closeOnCancel: true,
        html: false
    }, function(isConfirm){
        if (isConfirm){
            setTimeout(function(){new_data()},600)            
        }
    })
});
    
function new_data(){
    var items=[];
    var proceed=true;
    vendorid=$('.vendor').find(':selected').data('id');
    warehouseid=$('.warehouse').find(':selected').data('id');
    invoice_no=$('.invoice').val()
    date=$('.date').val()
    duedate=$('.duedate').val()
    grand_discount_type=$('.gdt').find(':selected').data('id');
    grand_discount_value=$('.gd').val();
    subtotal=parseFloat($('.subtotal_receipt').html());
    // taxtotal=parseFloat($('.taxtotal_receipt').html());
    var cgsttotal=0, sgsttotal=0, igsttotal=0;
    total=parseFloat($('.total_receipt').html());
    
    if (vendorid == '' || typeof(vendorid) =='undefined' || warehouseid == '' || typeof(warehouseid) == 'undefined' ||
        $.trim(invoice_no) == '' || typeof(invoice_no) =='undefined' || $.trim(date) == '' || typeof(date) =='undefined'){
        proceed = false;
    }
    $(".details tr.data").each(function() {
        var product_id = $(this).find('td:nth-child(1) input').val();
        if (product_id == '' || product_id =='undefined'){
            proceed=false;
            swal("Oops...", "Please enter a product ", "error");
            $(this).closest('tr').addClass("has-error");
        }

        var quantity = $(this).find('td:nth-child(4) input').val();
        if (quantity == '' || quantity =='undefined'){
            proceed=false;
            swal("Oops...", "Please enter a quantity ", "error");
            $(this).closest('tr').addClass("has-error");
        }

        // var free = parseInt($(this).find('td:nth-child(5) input').val());

        // if (isNaN(free)){
            // free=0;
        // }
        
        // var free_tax = parseInt($(this).find('td:nth-child(6) input').val());
        // if (isNaN(free_tax)){
        //     free_tax=0;
        // }
        
        var unit_id = $(this).find('td:nth-child(6) :selected').data('id');
        if (unit_id == '' || unit_id =='undefined'){
            proceed=false;
            swal("Oops...", "Please enter the purchase unit ", "error");
            $(this).closest('tr').addClass("has-error");
        }

        var purchase = $(this).find('td:nth-child(7) input').val();
        if (purchase == '' || purchase =='undefined'){
            proceed=false;
            swal("Oops...", "Please enter the actual purchase rate ", "error");
            $(this).closest('tr').addClass("has-error");
        }

        var sales = $(this).find('td:nth-child(8) input').val();
        if (sales == '' || sales =='undefined'){
            proceed=false;
            swal("Oops...", "Please enter a tentative sales rate ", "error");
            $(this).closest('tr').addClass("has-error");
        }
        
        var mrp = $(this).find('td:nth-child(9) input').val();
        
        var disc_type = $(this).find('td:nth-child(10) :selected').data('id');
        var disc = parseFloat($(this).find('td:nth-child(11) input').val());
        if (isNaN(disc)){
            disc=0;
        }
        var disc_type_2 = $(this).find('td:nth-child(12) :selected').data('id');
        var disc_2 = parseFloat($(this).find('td:nth-child(13) input').val());
        if (isNaN(disc_2)){
            disc_2=0;
        }
        
        var cgst_p = parseFloat($(this).find('td:nth-child(15) input').val());
        var cgst_v = parseFloat($(this).find('td:nth-child(16)').html());
        if (isNaN(cgst_p)){
            cgst_p=0;
            cgst_v=0;
        }

        cgsttotal+=cgst_v
        
        var sgst_p = parseFloat($(this).find('td:nth-child(17) input').val());
        var sgst_v = parseFloat($(this).find('td:nth-child(18)').html());
        if (isNaN(sgst_p)){
            sgst_p=0;
            sgst_v=0;
        }

        sgsttotal+=sgst_v

        var igst_p = parseFloat($(this).find('td:nth-child(19) input').val());
        var igst_v = parseFloat($(this).find('td:nth-child(20)').html());
        if (isNaN(igst_p)){
            igst_p=0;
            igst_v=0;
        }

        igsttotal+=igst_v

        var taxable_total = $(this).find('td:nth-child(14)').html();
        var line_total = $(this).find('td:nth-child(21)').html();
        
        var item = {
            product_id : product_id,
            quantity: quantity,
            // free: free,
            // free_tax:free_tax,
            unit_id: unit_id,
            purchase: purchase,
            sales: sales,
            mrp: mrp,
            disc_type: disc_type,
            disc: disc,
            disc_type_2: disc_type_2,
            disc_2:disc_2,
            cgst_p: cgst_p,
            cgst_v:cgst_v,
            sgst_p: sgst_p,
            sgst_v: sgst_v,
            igst_p: igst_p,
            igst_v: igst_v,
            taxable_total:taxable_total,
            line_total: line_total,
        };
        items.push(item);
        console.log(items);
    });
    
    if (proceed){
        (function() {
            $.ajax({
                url : "save/" , 
                type: "POST",
                data:{supplier_invoice: invoice_no,
                    vendor:vendorid,
                    warehouse:warehouseid,
                    date:date.split("/").reverse().join("-"),
                    grand_discount_type: grand_discount_type,
                    grand_discount_value: grand_discount_value,
                    subtotal: subtotal,
                    // taxtotal: taxtotal,
                    cgsttotal: cgsttotal,
                    sgsttotal: sgsttotal,
                    igsttotal: igsttotal,
                    total: total,
                    duedate: duedate.split("/").reverse().join("-"),
                    bill_details: JSON.stringify(items),
                    calltype: "save",
                    csrfmiddlewaretoken: csrf_token},
                dataType: 'json',               
                // contentType: "application/json",
                        // handle a successful response
                success : function(jsondata) {
                    var show_success=true
                    if (show_success){
                        swal("Hooray", "New purchase receipt added", "success");
                        var url='/purchase/receipt/detailview/'+jsondata+'/'
                        location.href = url;
                        // setTimeout(location.reload(true),1000);
                    }
                    //console.log(jsondata);
                },
                // handle a non-successful response
                error : function() {
                    swal("Oops...", "Recheck your inputs. There were some errors!", "error");
                }
            });
        }());
    }
    else{
        swal("Oops...", "Please note that vendor and warehouse details must be filled."+
            "Also please check the highlightd rows", "error");
    }
}

});