$(function(){

var has_attribute=false, attr_name, product_name, sku, vat_type, tax, reorder, unit, brand, group, has_batch,tax_array={}, manufac_array={},
    has_instance;


// var tax_array={};

$('.apply_reset').click(function(){
    // filter_applied=false;
    // $('select').val([]).selectpicker('refresh');
    // $('.invoice_summary').hide();
    $('.product_name').val('');
    $('.hsn_code').val('');
    $('#filter').modal('hide');
    load_products(1);
});

function apply_navbutton(jsondata, page_no){
    $('.navbtn').remove()
    for (i =jsondata['start']+1; i<=jsondata['end']; i++){
        if (i==page_no){
                    // $('.add_nav').append("<a href='#' class='btn nav_btn btn-sm btn-default' data=1 style='margin-right:0.2%'>"+i+"</a>")
            $('.add_nav').append("<button title='Your Current Page' class='btn btn-sm navbtn btn-info' "+
                "value="+i+" style='margin-right:0.2%'>"+i+"</button>")
        }
        else{
            $('.add_nav').append("<button title='Go to page no: "+i+"' class='btn btn-sm navbtn btn-default'"+
                " value="+i+" style='margin-right:0.2%'>"+i+"</button>")
        }
    }
}

$(".add_nav").on("click", ".navbtn", function(){
    load_products($(this).val());
});



load_products(1)

function load_products(page_no){
    $.ajax({
        url : "productdata/", 
        type: "GET",
        data:{ calltype:"all_products",
            page_no:page_no},
        dataType: 'json',
        // handle a successful response
        success : function(jsondata) {
            $('.prev_next').attr('hidden', false);
            $("#product_table .data").remove();
            $.each(jsondata['object'], function(){
                var url='/inventory/barcode/'+this.id+'/'
                // console.log(url)
                if ($.trim(this.rates).length>0){
                    $('#product_table').append("<tr class='data' align='center'>"+
                    "<td hidden='true'>"+this.id+"</td>"+
                    "<td class='link' style='text-decoration: underline; cursor: pointer'>"+this.name+"</td>"+
                    "<td>"+$.trim(this.hsn_code)+"</td>"+
                    "<td>"+this.sku+"</td>"+
                    "<td>"+$.trim(this.default_unit)+"</td>"+
                    "<td>"+$.trim(this.brand)+"</td>"+
                    "<td>"+$.trim(this.group)+"</td>"+
                    "<td>"+$.trim(this.remarks)+"</td>"+
                    "<td class='rate'>"+$.trim(this.rates[0].tentative_sales_rate)+"</td>"+
                    "<td hidden>"+$.trim(this.rates[0].id)+"</td>"+
                    "<td hidden>"+$.trim(this.rates[0].is_tax_included)+"</td>"+
                    "<td class='add_price'>Click to add sales rate</td>"+
                    "<td class='barcode'><a href="+url+">Click to download barcode</a></td>"+
                    "</tr>");
                }
                else{
                    $('#product_table').append("<tr class='data' align='center'>"+
                    "<td hidden='true'>"+this.id+"</td>"+
                    "<td class='link' style='text-decoration: underline; cursor: pointer'>"+this.name+"</td>"+
                    "<td>"+$.trim(this.hsn_code)+"</td>"+
                    "<td>"+this.sku+"</td>"+
                    "<td>"+$.trim(this.default_unit)+"</td>"+
                    "<td>"+$.trim(this.brand)+"</td>"+
                    "<td>"+$.trim(this.group)+"</td>"+
                    "<td>"+$.trim(this.remarks)+"</td>"+
                    "<td class='rate'></td>"+
                    "<td hidden></td>"+
                    "<td hidden></td>"+
                    "<td class='add_price'>Click to add sales rate</td>"+
                    "<td class='barcode'><a href="+url+">Click to download barcode</a></td>"+
                    "</tr>");   
                }
            })
            apply_navbutton(jsondata, page_no)
        },
        // handle a non-successful response
        error : function() {
            swal("Oops...", "No product is recorded yet.", "error");
        }
    });
}

load_unit()

function load_unit(){
    $.ajax({
        url : "/master/dimensionunit/unitdata/onlybase", 
        type: "GET",
        dataType: 'json',
        // handle a successful response
        success : function(jsondata) {
            $.each(jsondata, function(){
                    $('#unit').append($('<option/>',{
                        'data-id': this.id,
                        'text': this.name
                        }));
                    $('#unit').selectpicker('refresh')
                })
        },
        // handle a non-successful response
        error : function() {
            swal("Oops...", "No unit data exist.", "error");
        }
    });
}

load_tax()

function load_tax(){
    $.ajax({
        url : "/master/tax/getdata/", 
        type: "GET",
        dataType: 'json',
        // handle a successful response
        success : function(jsondata) {
            $.each(jsondata, function(){
                tax_array[this.name]=this.id;
                $('#tax_cgst').append($('<option/>',{
                    'data-id': this.id,
                    'text': this.name
                }));
                $('#tax_sgst').append($('<option/>',{
                    'data-id': this.id,
                    'text': this.name
                }));
                $('#tax_igst').append($('<option/>',{
                    'data-id': this.id,
                    'text': this.name
                }));
                $('#cgst_data_prod').append($('<option/>',{
                    'value': this.id,
                    'text': this.name
                }));
                $('#sgst_data_prod').append($('<option/>',{
                    'value': this.id,
                    'text': this.name
                }));
                $('#igst_data_prod').append($('<option/>',{
                    'value': this.id,
                    'text': this.name
                }));
            })
            $('#tax_cgst').selectpicker('refresh');
            $('#tax_sgst').selectpicker('refresh');
            $('#tax_igst').selectpicker('refresh');
            // $('#cgst_data_prod').selectpicker('refresh');
            // $('#sgst_data_prod').selectpicker('refresh');
            // $('#igst_data_prod').selectpicker('refresh');
        },
        // handle a non-successful response
        error : function() {
            swal("Oops...", "No tax data exist.", "error");
        }
    });
}

load_manufac()

function load_manufac(){
    $.ajax({
        url : "/master/manufacbrand/manufacdata/", 
        type: "GET",
        dataType: 'json',
        // handle a successful response
        success : function(jsondata) {
            $.each(jsondata, function(){
                tax_array[this.name]=this.id;
                manufac_array[this.name]=this.id;
                $('#manufac_data_prod').append($('<option/>',{
                    'value': this.id,
                    'text': this.name
                }));
            })
            // $('#manufac_data_prod').selectpicker('refresh');
        },
        // handle a non-successful response
        error : function() {
            swal("Oops...", "No manufacturer data exist.", "error");
        }
    });
}

load_attribute()

function load_attribute(){
    $.ajax({
        url : "attributedata/", 
        type: "GET",
        dataType: 'json',
        // handle a successful response
        success : function(jsondata) {
            attr_values=jsondata;
            $.each(attr_values, function(){
                    $('#selattr0').append($('<option/>',{
                        'data-id': this.id,
                        'text': this.name
                        }));                    
            })
        },
        // handle a non-successful response
        error : function() {
            swal("Hmm...", "No attribute data exist.", "error");
        }
    });
}


$("#product_table").on("click", ".barcode", function(){
    var newurl=$(this).closest('tr').find('td:nth-child(13) a').attr('href');
    $('a.barcodetag').attr('href', newurl);
    productid=$(this).closest('tr').find('td:nth-child(1)').html();
    productname=$(this).closest('tr').find('td:nth-child(2)').html();
    $('.id_barcode').val(productid)
    $('.name_barcode').val(productname)
    $('#modal_barcode').modal('show');
    // console.log(newurl);
});

$("#product_table").on("click", ".rate", function(){
    var prod_id=$(this).closest('tr').find('td:nth-child(1)').html();
    var name=$(this).closest('tr').find('td:nth-child(2)').html();
    var rate=$(this).closest('tr').find('td:nth-child(9)').html();
    var rate_id=$(this).closest('tr').find('td:nth-child(10)').html();
    var rate_is_tax=$(this).closest('tr').find('td:nth-child(11)').html();
    $('.product_name_update').html(name);
    $('.retail_rate_update').val(rate);
    $('.product_id_rate_update').html(prod_id);
    $('.retail_rate_id').html(rate_id);

    $('.is_tax_update').prop('checked', rate_is_tax);

    $('#retailRate').modal('show');
});

$('.update_rate').click(function(e) {
    swal({
        title: "Are you sure?",
        text: "Are you sure to update the product rate?",
        type: "warning",
        showCancelButton: true,
      // confirmButtonColor: "#DD6B55",
        confirmButtonText: "Yes, update product rate!",
        closeOnConfirm: true,
        closeOnCancel: true,
        html: false
    }, function(isConfirm){
        if (isConfirm){
            setTimeout(function(){update_rate()},600)
            // console.log("rate update called")            
        }
    })
});


function update_rate(){
    var proceed=true;
    new_rate=parseFloat($('.retail_rate_update').val());
    if (isNaN(new_rate) || new_rate<0){
        proceed = false;
        swal("Oops...", "Retail Sales Rate must be a number greater than zero.", "error");
    }
    rate_id = $('.retail_rate_id').html();
    prod_id = $('.product_id_rate_update').html();
    is_tax = $('.is_tax_update').is(":checked");
    // var is_present = $(this).find('td:nth-child(6) input').is(":checked");
    if (proceed){
        (function() {
            $.ajax({
                url : "productdata/" , 
                type: "POST",
                data:{new_rate: new_rate,
                    rate_id: rate_id,
                    is_tax: is_tax,
                    prod_id: prod_id,
                    calltype: "updaterate",
                    csrfmiddlewaretoken: csrf_token},
                dataType: 'json',               
                // handle a successful response
                success : function(jsondata) {
                    var show_success=true
                    if (show_success){
                        swal("Hooray", "Product retail sales rate updated", "success");
                        setTimeout(location.reload(true),1000);
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
}


$( ".has_attribute" ).change(function() {
    has_attribute = $( ".has_attribute" ).is(":checked");
    if (has_attribute){
        $('#attribute_details').prop('hidden',false);
    }
    else{
        $('#attribute_details').prop('hidden',true);        
    }
});



var next = 0;
    $("#add-more").click(function(e){
        e.preventDefault();
        var addto = "#attr" + next;
        var addRemove = "#attr" + next;
        next = next + 1;
        var newIn = ' <div id="attr'+ next +'" class="attr"><br>'+
            '<div class="form-group"><label class="control-label">Select Attribute</label>'+
            '<select class="form-control select attribute" id="selattr'+next+'"">'+
            '<option disabled selected hidden style="display: none" value>Select Attribute</option></select></div>'+
            '<div class="form-group"><label class="control-label">Attribute Value</label>'+
            '<input type="text" class="form-control value" placeholder="If arribute is colour, value can be: Blue, White, etc.">'+
            '</div></div>';
        var newInput = $(newIn);
        var removeBtn = '<button id="remove'+(next - 1)+'"class="btn btn-danger btn-xs remove-me">Remove Attribute</button>';
        var removeButton = $(removeBtn);
        $(addto).after(newInput);
        $(addRemove).after(removeButton);
        $("#attr" + next).attr('data-source',$(addto).attr('data-source'));
        $("#count").val(next);
        $.each(attr_values, function(){
            $('#selattr'+next).append($('<option/>',{
            'data-id': this.id,
            'text': this.name
            }));                    
        })
        
        $('.remove-me').click(function(e){
            e.preventDefault();
            var attrNum = this.id.charAt(this.id.length-1);
            var attrID = "#attr" + attrNum;
            $(this).remove();
            $(attrID).remove();
        });
    });


$('.submit').click(function(e) {
    swal({
        title: "Are you sure?",
        text: "Are you sure to add a new product?",
        type: "warning",
        showCancelButton: true,
      // confirmButtonColor: "#DD6B55",
        confirmButtonText: "Yes, add new product!",
        closeOnConfirm: true,
        closeOnCancel: true,
        html: false
    }, function(isConfirm){
        if (isConfirm){
            setTimeout(function(){new_product()},600)            
        }
    })
});

function new_product(){
    var proceed=true, attributes=[];
    product_name=$('.name').val()
    sku=$('.sku').val()
    barcode=$('.barcode_new').val()
    hsn=$('.hsn').val()
    // vat_type=$(".vattype").find(':selected').data('id');
    // tax=$(".tax").find(':selected').data('id');
    cgst=$(".cgst").find(':selected').data('id');
    sgst=$(".sgst").find(':selected').data('id');
    igst=$(".igst").find(':selected').data('id');
    reorder=$('.reorder').val()
    unit=$(".unit").find(':selected').data('id');
    brand=$(".brand").find(':selected').data('id');
    group=$(".group").find(':selected').data('id');
    has_batch = $( ".has_batch" ).is(":checked");
    has_instance = $( ".has_instance" ).is(":checked");
    has_attribute = $( ".has_attribute" ).is(":checked");
    if (has_attribute){
        $("#attribute_details").children('div').each(function() {
            var attribute_id = $(this).find('.attribute :selected').data('id');
            var value = $(this).children().last().find('.value').val();
            if (isNaN(attribute_id)){
                $(this).addclass('has-error')
            }
            var item = {
                attribute_id : attribute_id,
                value: value,            
            };
            attributes.push(item);            
        });
    }
    if (has_attribute){
        if (attributes.length < 1){
            proceed=false;
            swal("Oops...", "Please add atleast one attribute if has_attribute is selected.", "error");
        }
    }

    if (product_name == '' || product_name =='undefined' || sku == '' || sku =='undefined' || unit == '' || typeof(unit) =='undefined'){
        proceed = false;
        swal("Oops...", "Product must have a name and sku/product code.", "error");
    }
    if (proceed){
        (function() {
            $.ajax({
                url : "" , 
                type: "POST",
                data:{name: product_name,
                    sku: sku,
                    hsn: hsn,
                    barcode: barcode,
                    // vat_type: vat_type,
                    // tax:tax,
                    cgst:cgst,
                    sgst:sgst,
                    igst:igst,
                    reorder:reorder,
                    unit:unit,
                    brand:brand,
                    group: group,
                    has_batch: has_batch,
                    has_instance: has_instance,
                    has_attribute: has_attribute,
                    attributes:JSON.stringify(attributes),
                    calltype: "newproduct",
                    csrfmiddlewaretoken: csrf_token},
                dataType: 'json',               
                // contentType: "application/json",
                        // handle a successful response
                success : function(jsondata) {
                    var show_success=true
                    if (show_success){
                        swal("Hooray", "New product added", "success");
                        setTimeout(location.reload(true),1000);
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
        swal("Oops...", "Please note that product name, sku, tax type (if applicable) must be filled. Check the inputs.", "error");
    }
}




$('.submitattribute').click(function(e) {
    swal({
        title: "Are you sure?",
        text: "Are you sure to add a new attribute?",
        type: "warning",
        showCancelButton: true,
      // confirmButtonColor: "#DD6B55",
        confirmButtonText: "Yes, add new attribute!",
        closeOnConfirm: true,
        closeOnCancel: true,
        html: false
    }, function(isConfirm){
        if (isConfirm){
            setTimeout(function(){new_attribute()},600)            
        }
    })
});

    
function new_attribute(){
    var proceed=true;
    attr_name=$('.attributename').val()
    if (attr_name == '' || attr_name =='undefined'){
        proceed = false;
    }
    if (proceed){
        (function() {
            $.ajax({
                url : "" , 
                type: "POST",
                data:{name: attr_name,
                    calltype: "newattribute",
                    csrfmiddlewaretoken: csrf_token},
                dataType: 'json',               
                // contentType: "application/json",
                        // handle a successful response
                success : function(jsondata) {
                    var show_success=true
                    if (show_success){
                        swal("Hooray", "New attribute added", "success");
                        setTimeout(location.reload(true),1000);
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
        swal("Oops...", "Please note that an unique attribute name must be filled.", "error");
    }
}


$("#product_table").on("click", ".add_price", function(){
    productid=$(this).closest('tr').find('td:nth-child(1)').html();
    productname=$(this).closest('tr').find('td:nth-child(2)').html();
    productsku=$(this).closest('tr').find('td:nth-child(4)').html();
    $('#modal_product_rate').modal('show');
    $('.id_rate_prod').val(productid)
    $('.name_rate_prod').val(productname)
    $('.sku_rate_prod').val(productsku)
    $('.sales_rate_prod').val('')
});

$('.submitrate').click(function(e) {
    swal({
        title: "Are you sure?",
        text: "Are you sure to add a sales rate?",
        type: "warning",
        showCancelButton: true,
      // confirmButtonColor: "#DD6B55",
        confirmButtonText: "Yes, add new rate!",
        closeOnConfirm: true,
        closeOnCancel: true,
        html: false
    }, function(isConfirm){
        if (isConfirm){
            setTimeout(function(){new_rate()},600)            
        }
    })
});

    
function new_rate(){
    var proceed=true;
    productid=$('.id_rate_prod').val()
    rate=parseFloat($('.sales_rate_prod').val());
    is_tax = $( ".tax_rate_prod" ).is(":checked");
    if (isNaN(rate) || rate<0){
        proceed = false;
    }
    if (proceed){
        (function() {
            $.ajax({
                url : "" , 
                type: "POST",
                data:{productid: productid,
                    rate: rate,
                    is_tax: is_tax,
                    calltype: "newrate",
                    csrfmiddlewaretoken: csrf_token},
                dataType: 'json',               
                // contentType: "application/json",
                        // handle a successful response
                success : function(jsondata) {
                    var show_success=true
                    if (show_success){
                        swal("Hooray", "New sales rate added", "success");
                        setTimeout(location.reload(true),1000);
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
        swal("Oops...", "Please note that sales rate must be greater than zero.", "error");
    }
}

$("#product_table").on("click", ".link", function(){
    productid=$(this).closest('tr').find('td:nth-child(1)').html();
    $('.update').hide();
    $('.edit').show();
    $.ajax({
        url : "productdata/",
        type: "GET",
        data: { calltype:"one_product",
            productid:productid},
        dataType: 'json',
            // handle a successful response
        success : function(jsondata) {
            $('#modal_product_details').modal('show');
            $('.id_data_prod').val(jsondata['id'])
            $('.name_data_prod').val(jsondata['name'])
            $('.sku_data_prod').val(jsondata['sku'])
            $('.barcode_data_prod').val(jsondata['barcode'])
            $('.hsn_data_prod').val(jsondata['hsn_code'])            
            $('#cgst_data_prod').val(tax_array[jsondata['cgst']])
            $('#sgst_data_prod').val(tax_array[jsondata['sgst']])
            $('#igst_data_prod').val(tax_array[jsondata['igst']])
            $('#manufac_data_prod').val(tax_array[jsondata['manufacturer']])
            $('.editable').attr('disabled', true);
            // $('#cgst_data_prod').selectpicker('refresh');
            // $('#sgst_data_prod').selectpicker('refresh');
            // $('#igst_data_prod').selectpicker('refresh');
        },
            // handle a non-successful response
        error : function() {
            swal("Oops...", "There was error in processing product data. Please try again later", "error");
        }
    });
});

$('.edit').click(function(e) {
    $('.editable').attr('disabled', false);
    $('.edit').hide();
    $('.update').show();
});

$('.update').click(function(e) {
    
    swal({
        title: "Are you sure?",
        text: "Are you sure to update product data?",
        type: "warning",
        showCancelButton: true,
      // confirmButtonColor: "#DD6B55",
        confirmButtonText: "Yes, update data!",
        closeOnConfirm: true,
        closeOnCancel: true,
        html: false
    }, function(isConfirm){
        if (isConfirm){
            setTimeout(function(){update_data()},600)            
        }
    })
});

function update_data(){
    var proceed_update=true;
    pk=$('.id_data_prod').val()
    name_update=$('.name_data_prod').val()
    sku_update=$('.sku_data_prod').val()
    barcode_update=$('.barcode_data_prod').val()
    hsn_update=$('.hsn_data_prod').val()
    cgst_update=$('#cgst_data_prod').val()
    sgst_update=$('#sgst_data_prod').val()
    igst_update=$('#igst_data_prod').val()
    manufac_update=$('#manufac_data_prod').val()
    // zone=$(".zone").find(':selected').data('id');
    
    if (name_update == '' || typeof(name_update) =='undefined' || sku_update == '' || typeof(sku_update) =='undefined' ){
        proceed_update = false;
    }
    if (proceed_update){
        (function() {
            $.ajax({
                url : "productdata/" , 
                type: "POST",
                data:{pk: pk,
                    name: name_update,
                    sku:sku_update,
                    barcode: barcode_update,
                    hsn: hsn_update,
                    cgst:cgst_update,
                    sgst:sgst_update,
                    igst:igst_update,
                    manufac: manufac_update,
                    calltype: "updateproduct",
                    csrfmiddlewaretoken: csrf_token},
                dataType: 'json',               
                // contentType: "application/json",
                        // handle a successful response
                success : function(jsondata) {
                    var show_success=true
                    if (show_success){
                        swal("Hooray", "Product data updated.", "success");
                        setTimeout(location.reload(true),1000);
                    }
                    //console.log(jsondata);
                },
                // handle a non-successful response
                error : function() {
                    swal("Oops...", "Recheck your inputs. Remember, SKU must be unique. There were some errors!", "error");
                }
            });
        }());
    }
    else{
        swal("Oops...", "Please note that name & sku must be filled and SKU must be unique.", "error");
    }
}

$('.apply_filter').click(function(e){
    filter_data(1);
});

function filter_data(page_no) {
    $('.prev_next').attr('hidden', true);
    startswith = $('.product_name').val();
    hsncode = $('.hsn_code').val();
    skucode = $('.sku_code_search').val();
    barcode = $('.barcode_search').val();

    $.ajax({
        url : "productdata/", 
        type: "GET",
        data:{ calltype:"product_filter",
            startswith: startswith,
            hsncode: hsncode,
            skucode: skucode,
            barcode: barcode,
            csrfmiddlewaretoken: csrf_token},
        dataType: 'json',
        // handle a successful response
        success : function(jsondata) {
            // filter_applied=true;
            $("#product_table .data").remove();
            $('#filter').modal('hide');
            $.each(jsondata, function(){
                var url='/inventory/barcode/'+this.id+'/'
                // console.log(url)
                if ($.trim(this.rates).length>0){
                    $('#product_table').append("<tr class='data' align='center'>"+
                    "<td hidden='true'>"+this.id+"</td>"+
                    "<td class='link' style='text-decoration: underline; cursor: pointer'>"+this.name+"</td>"+
                    "<td>"+$.trim(this.hsn_code)+"</td>"+
                    "<td>"+this.sku+"</td>"+
                    "<td>"+$.trim(this.default_unit)+"</td>"+
                    "<td>"+$.trim(this.brand)+"</td>"+
                    "<td>"+$.trim(this.group)+"</td>"+
                    "<td>"+$.trim(this.remarks)+"</td>"+
                    "<td class='rate'>"+$.trim(this.rates[0].tentative_sales_rate)+"</td>"+
                    "<td hidden>"+$.trim(this.rates[0].id)+"</td>"+
                    "<td hidden>"+$.trim(this.rates[0].is_tax_included)+"</td>"+
                    "<td class='add_price'>Click to add sales rate</td>"+
                    "<td class='barcode'><a href="+url+">Click to download barcode</a></td>"+
                    "</tr>");
                }
                else{
                    $('#product_table').append("<tr class='data' align='center'>"+
                    "<td hidden='true'>"+this.id+"</td>"+
                    "<td class='link' style='text-decoration: underline; cursor: pointer'>"+this.name+"</td>"+
                    "<td>"+$.trim(this.hsn_code)+"</td>"+
                    "<td>"+this.sku+"</td>"+
                    "<td>"+$.trim(this.default_unit)+"</td>"+
                    "<td>"+$.trim(this.brand)+"</td>"+
                    "<td>"+$.trim(this.group)+"</td>"+
                    "<td>"+$.trim(this.remarks)+"</td>"+
                    "<td class='rate'></td>"+
                    "<td hidden></td>"+
                    "<td hidden></td>"+
                    "<td class='add_price'>Click to add sales rate</td>"+
                    "<td class='barcode'><a href="+url+">Click to download barcode</a></td>"+
                    "</tr>");   
                }
            })
            
            // apply_navbutton(jsondata, page_no);
            // $('.amount_invoiced').html('Rs.'+jsondata['total_value'])
            // $('.amount_pending').html('Rs.'+jsondata['total_pending'])
        },
        // handle a non-successful response
        error : function() {
            swal("Oops...", "No sales invoice exist.", "error");
        }
    });

}

});