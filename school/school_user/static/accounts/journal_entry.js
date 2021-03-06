$(function(){

//This variable will store the student list added via json

var date="";
var remarks="";
var journal_group="";
//This will help to remove the error modal.
function clearmodal(){
    window.setTimeout(function(){
        bootbox.hideAll();
    }, 2500);
}

//Add and delete are used to add/delete row
$(".delete").on('click', function() {
    $('.case:checkbox:checked').parents("tr").remove();
    $('.check_all').prop("checked", false); 
});

$(".addmore").on('click',function(){
    count=$('table tr').length;
    var new_row="<tr class='data'>"+
    "<td><input type='checkbox' class='case'/></td>"+
    "<td id='trn_col'></td>"+
    "<td><input type='text'  class='form-control accts_key'></td>"+
    "<td class='accountname'></td>"+
    "<td><input type='value' min='0' class='form-control debit' disabled='true'></td>"+
    "<td><input type='value' min='0' class='form-control credit' disabled='true'></td></tr>";
    $('table').append(new_row);
    // <select class='form-control selectpicker' id="trn_type">
    $('table').find('tr:eq('+count+')').find('#trn_col').append("<select class='form-control selectpicker'"+
        "data-live-search='true' id='trn_type'>"+
        "<option disabled selected hidden style='display: none' value>Debit/Credit</option>"+
        "<option data-id='Debit'>Debit</option>"+
        "<option data-id='Credit'>Credit</option>");
    $('.selectpicker').selectpicker('refresh');
    
    // $('table').find('tr:eq('+count+')').find('.accountname').append("<select class='form-control select' id='account'>"+
    //     // "data-live-search='true' id='trn_type'>"+
    //     "<option disabled selected hidden style='display: none' value>Select Account</option></select>");

    // $.each(accounts, function(){
    //   $('table').find('tr:eq('+count+')').find('#account').append($('<option>',{
    //     'text': this.name
    //     }));
    // $('#account').selectpicker('refresh');
    // });
});

$("#journal_table").on("change", "#trn_type", function(){
    if ((this.value) == 'Debit'){
        $(this).closest('tr').find('td:nth-child(5) input').attr('disabled',false);
        $(this).closest('tr').find('td:nth-child(6) input').attr('disabled',true);
        value=$(this).closest('tr').find('td:nth-child(6) input').val();
        $(this).closest('tr').find('td:nth-child(5) input').val(value);
        $(this).closest('tr').find('td:nth-child(6) input').val('');
    }
    else{
        $(this).closest('tr').find('td:nth-child(6) input').attr('disabled',false);
        $(this).closest('tr').find('td:nth-child(5) input').attr('disabled',true);
        value=$(this).closest('tr').find('td:nth-child(5) input').val();
        $(this).closest('tr').find('td:nth-child(6) input').val(value);
        $(this).closest('tr').find('td:nth-child(5) input').val('');
    }
});



//This is called after the class option is selected
$("#journal_table").on("change", ".accts_key", function(){
    // accountskey=parseInt($(".classsection").find(':selected').data('id'));
    var input = $(this).val();
    el=$(this)
    console.log(input);
    // console.log(classid);
    // $( ".classsection" ).prop('disabled',true); 
    // $( ".year" ).prop('disabled',false);
    (function() {
        $.ajax({
            url : "", 
            type : "POST", 
            data : { account_code: input,
                    calltype: 'account',
                    csrfmiddlewaretoken: csrf_token}, // data sent with the post request
            dataType: 'json',
                    // handle a successful response
            success : function(jsondata) {  
                //console.log(jsondata);
                el.closest('tr').find('td:nth-child(4)').html(jsondata['name']);
                el.closest('tr').find('td:nth-child(3) input').attr("disabled",true);
                    //console.log(jsondata); // log the returned json to the console
                    //alert(jsondata['sellingprice']);
            },
            // handle a non-successful response
            error : function() {
                bootbox.alert({
                    size: "small",
                    message: "Account does not exist.",
                    onEscape: true });// provide a bit more info about the error to the user
                clearmodal();
                }
        });
    }());
});

//This is for the reset button to work
// $( ".reset" ).click(function() {
//     location.reload(true);
// });

$( ".submit" ).confirm({
    title: 'Confirm!',
    icon: 'fa fa-spinner fa-spin',
    theme: 'black',
    backgroundDismiss: true,
    content: 'Are you sure to record the journal entry?',
    confirmButton: 'Yes!',
    cancelButton: 'No!',
    autoClose: 'cancel|6000',
    confirmButtonClass: 'btn-success',
    cancelButtonClass: 'btn-danger',
    animation: 'rotateY',
    closeAnimation: 'rotateXR',
    animationSpeed: 750,
    confirm: function(){
    //get all the input details
        var proceed=true;
        var items=[]; 
        var debit=0;
        var credit=0;
        date=$('.date').val();
        remarks=$('.remarks').val()
        journal_group=parseInt($(".journalgroup").find(':selected').data('id'));
        var value_identifier=1;
        var trn_identifier=1;
        if (date != "" && journal_group!= ""){
            var i=0
            $("tr.data").each(function() {
                value=0;
                i++;
                console.log(i);
                var trn_type =  $(this).find('td:nth-child(2)').find(':selected').text();
                console.log(trn_type);
                var code = $(this).find('td:nth-child(3) input').val();
                console.log(code);
                //trn_type is short for transaction type
                if (trn_type == "Debit"){
                    value=parseFloat($(this).closest('tr').find('td:nth-child(5) input').val());
                    debit+=value;
                }
                else if(trn_type == "Credit"){
                    value=parseFloat($(this).closest('tr').find('td:nth-child(6) input').val());
                    credit+=value;
                }
                else{
                    trn_identifier=0;
                }
                if (value<=0){
                    value_identifier = 0;
                }
                if (code=="" || trn_type=="" || isNaN(value)){
                    trn_identifier=0;
                }
                var item = {
                    code: code,
                    value: value,
                    transaction_type: trn_type       
                };
                items.push(item);
            });
            console.log (items);
        }
        else{
            proceed=false;
        }
        console.log ("Debit: "+debit+"Credit: "+credit);
        console.log(proceed);
        if (debit == credit && proceed){
            if (value_identifier ==1 & trn_identifier == 1){
                //Send ajax function to back-end         
                (function() {
                    $.ajax({
                        url : "", 
                        type: "POST",
                        data:{ details: JSON.stringify(items),
                            date: date,
                            remarks: remarks,
                            groupid: journal_group,
                            calltype: 'save',
                            csrfmiddlewaretoken: csrf_token},
                        dataType: 'json',               
                        // handle a successful response
                        success : function(jsondata) {
                            alert("Entry registered successfully");
                            location.href = redirect_url;
                            //console.log(jsondata);
                        },
                        // handle a non-successful response
                        error : function() {
                            bootbox.alert({
                            size: "medium",
                            message: "Attendance entry failed", 
                            onEscape: true });
                            clearmodal();
                        }
                    });
                }());
            }
            else{
                bootbox.alert({
                    size: "large",
                    message: "Value canot be negative or account has to be entered", 
                    onEscape: true });
                clearmodal();
            }
        }
        else{
            if (! proceed){
                bootbox.alert({
                    size: "large",
                    message: "Please select journal group and date.", 
                    onEscape: true });
                clearmodal();
            }
            else{
                bootbox.alert({
                    size: "large",
                    message: "Debit should be equal to credit & value should not be blank.", 
                    onEscape: true });
                clearmodal();                
            }
        }
                
    }, //bracket for confirm closing
});




});