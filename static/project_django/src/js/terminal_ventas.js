var server = 'http://localhost/'
$(document).ready(function(){		 
	$("#pos-sale-ticket-invoice").html()
	$("#button-ticket-next").hide()
	$("#ticket_print_button").hide()	
	$('.prod_obj_data').click(function(){
		pauseAppendTicket(this)
	});

	$("#button-ticket-next").click(function(){
		$("#button-ticket-next").hide()
		$("#ticket_save_button").val('Guardar')
		$("#ticket_print_button").hide()
		$("#ticket_save_button").show()
		$('#boleta_terminal_venta').empty()
	});

	$(document).on('click','#btn-remove-product',function(){
  		$div_remove = $(this).parents(".ticket-content")  		
  		amount = $div_remove.find(".ticket-qty-total").find(".price_product_ticket").val()
  		getRestTotalAmount(amount)
  		$div_remove.remove();
	});

	$('#ticket_save_button').click(function(){
		list_ticket = []
		ticket = $('#boleta_terminal_venta').find('div').not('.ticket-qty-total')
        session_id = $('#session-id').val()
		$.each(ticket,function (){
			tck = []
			d_ticket = {}
			$.each($(this).find('li'),function(){
				tck.push($(this).text())
			})
			d_ticket['code'] = tck[0].replace('[','').replace(']','')
			d_ticket['name'] = tck[1]
			d_ticket['id'] = $(this).find('input#product_ian').val()			
			d_ticket['qty'] = $($(this).find('input#qty_id')).val()
			d_ticket['amount_total'] = $($(this).find('input.price_product_ticket')).val()
			d_ticket['price_unit'] = $($(this).find('input#prc_unit')).val()						
			list_ticket.push(d_ticket)
		});
		json_ticket = clearJson(list_ticket, session_id)
		send_to_server(json_ticket)
	});

	$('#ticket_print_button').click(function(){

	});	
	
	$('.order_line').change(function(){
		onchange_order_line(this)
	});	
    $('#save-button').click(function(){
        form = $('#form-session')
        form.submit();

    });

    $('#close-button').click(function(){
    	form = $('#form-close-session')
        form.submit();
    });

	$('#filtro_terminal_ventas').change(function(){
		var product = $('#filtro_terminal_ventas').val()
		$('#product_contain').html('')
	    $.get('', {'filter': product}, function(data){
	        $.each(data, function() {	        		
        		cont = "<div class='col-md-3 prod_obj_data'>" +
        				"<div class='thumbnail'>" +
        			 	"<img src='/media/"+this['model_pic']+"' alt='No Photo' class='img-thumbnail' style='width:180px;height:130px'>"+ 
        				"<div class='caption'>" +
    					"<label>"+this['name'] +"</label> "+ 
    					"<label>"+this['code'] +"</label><label>Precio: </label>"+
    					"<label>"+this['price_sale']+"</label>"+        					        				
        				"</div> </div> </div>"         				        				        	    
    			$('#product_contain').append(cont)
	        })	
	        $('#product_contain').find('div.prod_obj_data').attr('onclick', 'pauseAppendTicket(this);');
	    });					
	});

	$('#kanban-product-filter').keypress(function (e) {
		 var key = e.which;
		 if(key == 13)  // the enter key code
		  {
			var text = $('#kanban-product-filter').val();
			if (text == ''){
				$('#search-box-product-list').hide()			
				$('#original-box-product-list').show()			
			}else{
				get_product_id(text, false)							
			}
		  }
	}); 

});

function getTotalAmount(amount){
	am = parseFloat($("#footer-total").text())
	am += parseFloat(amount)
	$("#footer-total").text(am)

}

function getRestTotalAmount(amount){
	am = parseFloat($("#footer-total").text())
	am -= parseFloat(amount)
	$("#footer-total").text(am)

}

function clearJson(list_ticket, session_id){
	var ticket = {
					name : Math.floor((Math.random() * 9999999) + 1000000),
					date_order : new Date().toJSON().slice(0,10),
					amount_total : 0,
					session_id : session_id,
					lines : []
	}
	for (line in list_ticket){
		ticket.amount_total+= parseFloat(list_ticket[line].amount_total)
		ticket.lines.push({product_id: parseInt(list_ticket[line].id),
						 qty: parseInt(list_ticket[line].qty),
						 price_unit: parseFloat(list_ticket[line].price_unit),
						 amount_total: parseFloat(list_ticket[line].amount_total)})
	}
	ticket.lines = ticket.lines 
	return ticket
}


function edit_ticket(){
    var $check = $('input:checkbox:checked.check_table').map(function () {
    				return this.value;
				 }).get();
	
}

function find_ticket_in(list_product){
	var id_ticket = 'ticket_'+list_product[0].replace(/\s+/g, '')+list_product[1].replace(/\s+/g, '')
	var exist = valid_exist(id_ticket)
	if (!exist){
		cont = "<div class=\"ticket-content\" id='ticket_"+list_product[0].replace(/\s+/g, '')+list_product[1].replace(/\s+/g, '')+"'>" +
				"<ul>"+
				"<li><button id=\"btn-remove-product\" type=\"button\" class=\"btn btn-default btn-xs\">"+				
				"<span class=\"glyphicon glyphicon-remove-circle\" aria-hidden=\"true\"></span>"+
				"</button> ["+list_product[1]+"] </li>" +
				"<li>"+list_product[0]+"</li>"+
				"<li><div class=\"ticket-qty-total\"><label id='qty_id'>Cta</label>"+
				"<input type='text' id='qty_id' style='width: 40px;' value='1'/>"+
				"<input type='hidden' id='prc_unit' value='"+list_product[3]+"'/>"+
				"<input type='hidden' id='product_ian' value='"+list_product[4]+"'/>"+				
				"<label id='sg'>$</label> "+
				"<input type='text' class='price_product_ticket' value='"+list_product[3]+"'/></div></li>"+
				"</ul>"+
				"</div>"					
				ticket = $('#boleta_terminal_venta'+' #ticket_'+list_product[0])
				$('#boleta_terminal_venta').append($(cont))
				getTotalAmount(list_product[3])
	}else{
		qty=exist.find('input#qty_id').val()
		qty = parseInt(qty)+1
		exist.find('input#qty_id').val(qty)
		exist.find('input.price_product_ticket').val(qty * parseFloat(list_product[3]))		
		getTotalAmount(list_product[3])
	} 

}				

function valid_exist(id_ticket){
	console.log(id_ticket)
	var prueba = $('#boleta_terminal_venta > #'+id_ticket)
	if (prueba[0]){
		return $(prueba[0]) 
	}else{
		return false		
	}
	
	
}

function getCookie(c_name){
    if (document.cookie.length > 0)
    {
        c_start = document.cookie.indexOf(c_name + "=");
        if (c_start != -1)
        {
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if (c_end == -1) c_end = document.cookie.length;
            return unescape(document.cookie.substring(c_start,c_end));
        }
    }
    return "";
 }

function send_to_server(tickets){
	$.ajax({
		data: JSON.stringify(tickets), 
		error: function(XMLHttpRequest, textStatus, errorThrown) {
			console.log("An error has occurred: " + textStatus);
			console.log(XMLHttpRequest.responseText);
		    $("#button-ticket-next").show()
		    $("#ticket_print_button").show()
		    var cont = parseInt($("#success-send").val())
		    $("#error-send").val(cont+=1)
		    
		}, 
		success: function(data, textStatus, XMLHttpRequest) {
			$("#button-ticket-next").show()
			$("#ticket_save_button").hide()
			$("#ticket_print_button").show()
		    var cont = parseInt($("#success-send").val())
		    $("#success-send").val(cont+=1)

		}, 
		type: "POST", 
		headers: { "X-CSRFToken": getCookie("csrftoken") },
		url: server+"terminal/orderSerializer/"});
}

function onchange_order_line(args){
	var id = args.id
	var start_id = '#id_lines-'+id.substring( id.indexOf('-')+1 , id.lastIndexOf('-') )
	var qty = $(start_id+'-qty')
	var price_unit = $(start_id+'-price_unit')
	var price_total = $(start_id+'-amount_total')
	if (price_unit.val() != '' && qty.val() == ''){
		qty.val(1);
		price_total.val(qty.val() * price_unit.val())
	}
	else if((price_unit.val() == '' && qty.val() != '')){
		price_unit.val(0);
		price_total.val(qty.val() * price_unit.val())
	}
	else if (price_unit.val() != '' && qty.val() != ''){
		price_total.val(qty.val() * price_unit.val())
	}
	change_amount_total();
}
function change_amount_total(){
	count = parseInt($('#id_lines-TOTAL_FORMS').val())
	amount_total = 0
	if (count >  0 ){
		while (count >=0){
			amount = $('#id_lines-'+count.toString()+'-amount_total').val()
			if (amount >0){
				amount_total += parseFloat(amount)
			}	
			count--
		}
		$('#id_amount_total').val(amount_total)
	}
}

function pauseAppendTicket(args){
	var product = $(args).find('label')
	var list_product = []
	var id = $(args).find('input#product_ian').val()
	$.each(product, function(){
		list_product.push($(this).text())
	});
	list_product.push(parseInt(id))
	find_ticket_in(list_product)	
}

function get_product_id(name, code){
	if (name && code){
		var urll = server+"terminal/snippets/"+name+'/'+code		
	}else if (name != false){
		var urll = server+"terminal/snippets/"+name+'/'		
	}

	$.ajax({
		dataType: 'json',
		data: {'name': name, 'code' : code}, 
		type: "GET", 
		url: urll,
		error: function(XMLHttpRequest, textStatus, errorThrown) {
			$('#original-box-product-list').hide()			
		}, 
		success: function(data, textStatus, XMLHttpRequest) {
			$('#original-box-product-list').hide()			
			var filter_div = $('#search-box-product-list')
			for (x in data){
				var d = "<div class=\"col-md-4\">"+
						"<div class=\"product-box-kanban\" onclick=\"location.href='/terminal/product_product_form/edit/"+ data[x].id +"'\">"+
						"<table>"+
								"<tr>"+
								    "<td style=\"vertical-align: top; width:105px;\">"+
										"<img src=\""+ data[x].model_pic+"\" alt=\"No Photo\" class=\"img-thumbnail img-responsive\""+
									    "style=\"width:100px;height:90px\">"+
								    "</td>"+
								    "<td style=\"vertical-align: top;\">"+
								    	"<ul>"+
								    		"<li><h5><strong>"+ data[x].name +"</strong></h5></li>"+
								    		"<li><p><strong>codigo:</strong> "+ data[x].code +"</p></li>"+
								    		"<li><p><strong>precio:</strong> "+ data[x].price_sale +"</p></li>"+
								    		"<li><p><strong>ctd:</strong> "+ data[x].qty_available +"</p></li>"+
								    	"</ul>"+
								    "</td>"+
								"</tr>"+
							"</table>"+
						"</div>"+
						"</div>"				
				filter_div.append($(d))	
			}
			filter_div.show()
		}
	});	
} 


function cloneMore(selector, type) {
    var newElement = $(selector).clone(true);
    var total = $('#id_' + type + '-TOTAL_FORMS').val();
    newElement.find(':input').each(function() {
        var name = $(this).attr('name').replace('-' + (total-1) + '-','-' + total + '-');
        var id = 'id_' + name;
        $(this).attr({'name': name, 'id': id}).val('').removeAttr('checked');
    });
    newElement.find('label').each(function() {
        var newFor = $(this).attr('for').replace('-' + (total-1) + '-','-' + total + '-');
        $(this).attr('for', newFor);
    });
    total++;
    $('#id_' + type + '-TOTAL_FORMS').val(total);
    $(selector).after(newElement);
}