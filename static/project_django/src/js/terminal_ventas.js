$(document).ready(function(){		 
	$("#pos-sale-ticket-invoice").html()

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
    					"<label>"+this['code'] +"</label></br><label>Precio: </label>"+
    					"<label>"+this['price_sale']+"</label>"+        					        				
        				"</div> </div> </div>"         				        				        	    
    			$('#product_contain').append(cont)
	        })	
	        $('#product_contain').find('div.prod_obj_data').attr('onclick', 'pauseAppendTicket(this);');
	    });					
	});
	
	$('.prod_obj_data').click(function(){
		pauseAppendTicket(this)
	});
	
	$('#ticket_save_button').click(function(){
		list_ticket = []
		ticket = $('#boleta_terminal_venta').find('div')
		$.each(ticket,function (){
			tck = []
			d_ticket = {}
			$.each($(this).find('label').not('#sg'),function(){
				tck.push($(this).text())
			})
			d_ticket['name'] = tck[0]
			d_ticket['code'] = tck[1]
			d_ticket['qty'] = $($(this).find('input#qty_id')).val()
			d_ticket['amount_total'] = $($(this).find('input.price_product_ticket')).val()
			d_ticket['price_unit'] = $($(this).find('input#prc_unit')).val()						
			list_ticket.push(d_ticket)
		});
		send_to_server(list_ticket)
	});

	$('#ticket_print_button').click(function(){
		var my_obj = [
				{
					 price_subtotal: 4118,
					 price_unit: 2059,
					 product_code: "1100003503502",
					 product_name: "FILTRO MEZCLA SR420 FS160 220",
					 qty: 2,
					 lotsplit_id: '34343',
					 discount : 0
			 	},
				{
					 price_subtotal: 4118,
					 price_unit: 2059,
					 product_code: "1100003503502",
					 product_name: "FILTRO MEZCLA SR420 FS160 220",
					 qty: 2,
					 lotsplit_id: '34343',
					 discount : 0
				 }
				 ]
		var ticket = {
			name  			: 'Fact0042307',
		    day 			: '27',
		    month 			: 'Noviembre',
		    year			: '15',
		    partner_name	: 'SERGIO VALDEBENITO BELMAR',
		    partner_vat		: '10.650.539-k',
		    partner_street	: 'CONDOR NORTE 269',
		    partner_city	: 'PANGUIPULLI',
		    partner_giro	: 'SERVICIO FERESTAL',
		    partner_phone	: '',
		    date	: '2015-01-11',
		    amount_text : 'SEISCIENTOS CINCUENTA Y CUATRO MIL PESOS',
		    amount_untaxed : '104.420',
		    amount_tax : '654.000',
		    amount_total : '654.000',
		    lines: my_obj,
		    pay_name : 'EFECTIVO POS'
		}

    	$("#pos-sale-ticket-invoice").empty()
	    	var t1 = "<div style=\"margin-top:95px;margin-left:525px;font-family:Courier;font-size:13px;\"><span height='75'>"+ ticket.name +"</span></div>\
					  <div style=\"margin-top:60px;margin-left:525px;height:30px;font-family:Courier;font-size:13px;\">\
					  	<span>" + ticket.day +"</span><span style=\"margin-left:30px;\">"+ ticket.month +"</span><span style=\"margin-left:30px;\">" + ticket.year +"</span>\
					  </div>\
					  <div style=\"height:30px;font-family:Courier;font-size:13px;margin-left:110px;margin-top:0px;\">\
					  	<span style=\"display:inline-block;width:360px;\">" + ticket.partner_name +"</span>\
					  	<span style=\"margin-left:110px;\">"+ ticket.partner_vat +"</span>\
					  </div>\
					  <div style=\"height:20px;font-family:Courier;font-size:13px;margin-left:110px;\">\
					  	<span style=\"display:inline-block;width:360px;\">"+ ticket.partner_street +"</span>\
					  	<span style=\"margin-left:110px;\"  >"+ ticket.partner_city +"</span>\
					  </div>\
					  <div style=\"height:20px;margin-top:0px;margin-left:110px;\">\
					  	<span style=\"font-family:Courier;font-size:13px;\">"+ ticket.pay_name +"</span>\
					  </div>\
					  <div style=\"height:20px;margin-top:50px;margin-left:180px;\">\
					  	<span style=\"font-family:Courier;font-size:13px;\">Vendedor:"+ ticket.pay_name +"</span>\
					  </div>"


	    	var t2 = '<div style=\"height:480px;width:750px;margin-top:50px;\"><table border=\"1\" style=\"margin-left:40px;\" >'
			for (line in  ticket.lines){
				cont ="<tr>\
						<td style=\"font-family:Courier;font-size:10px;\" width=\"50\" align=\"left\">"+ticket.lines[line].qty+"</td>\
						<td style=\"font-family:Courier;font-size:10px;\" width=\"120\" align=\"left\">"+ticket.lines[line].product_code+"</td>\
						<td style=\"font-family:Courier;font-size:10px;\" width=\"350\" align=\"left\">"+ticket.lines[line].product_name+"</td>\
						<td style=\"font-family:Courier;font-size:10px;\" width=\"30\" align=\"left\">"+ticket.lines[line].discount+"</td>\
						<td style=\"font-family:Courier;font-size:10px;margin-left:5px;\" width=\"110\"  align=\"right\">"+ticket.lines[line].price_unit+"</td>\
						<td style=\"font-family:Courier;font-size:10px;padding-right:15px;\" width=\"110\" align=\"right\">"+ticket.lines[line].price_subtotal+"</td>\
						</tr>"
				t2 = t2 + cont
			}
	    	t2 = t2+ "</table></div>"    		
			var t3 = "<div style=\"height:30px;width:700px;margin-left:100px;margin-top:0px;font-family:Courier;font-size:13px;\">\
			  	<span style=\"display:inline-block;width:390px;margin-left:0px;\">"+ticket.amount_text+"</span>\
			  	<span style=\"margin-left:240px;\">"+ticket.amount_untaxed+"</span>\
			    </div>\
			  <div style=\"height:30px;font-family:Courier;font-size:13px;\">\
			  	<span  style=\"margin-left:740px;\" >"+ticket.amount_tax+"</p></span>\
			  </div>\
			  <div style=\"height:30px;font-family:Courier;font-size:13px;\" >\
			  	<span style=\"margin-left:740px;\" > "+ticket.amount_total+"</span>\
			  </div>"


    	$("#pos-sale-ticket-invoice").html(t1+t2+t3);		
    	$("#pos-sale-ticket-invoice").printMe();		
	});	
	
	$('.order_line').change(function(){
		onchange_order_line(this)
	});
	

});

function edit_ticket(){
    var $check = $('input:checkbox:checked.check_table').map(function () {
    				return this.value;
				 }).get();
	
}

function find_ticket_in(list_product){
	var id_ticket = 'ticket_'+list_product[0].replace(/\s+/g, '')+list_product[1].replace(/\s+/g, '')
	var exist = valid_exist(id_ticket)
	if (!exist){
		cont = "<div id='ticket_"+list_product[0].replace(/\s+/g, '')+list_product[1].replace(/\s+/g, '')+"'>" +
				"<label>"+list_product[0]+"</label> " +
				"<label>"+list_product[1]+"</label> "+
				"<label id='qty_id'>Cta</label> "+
				"<input type='text' id='qty_id' style='width: 40px;' value='1'/>"+
				"<input type='hidden' id='prc_unit' value='"+list_product[3]+"'/>"+
				"<label id='sg'>$</label> "+
				"<input type='text' class='price_product_ticket' value='"+list_product[3]+"'/>"+
				"</div>"					
				ticket = $('#boleta_terminal_venta'+' #ticket_'+list_product[0])
				$('#boleta_terminal_venta').append(cont)
	}else{
		qty=exist.find('input#qty_id').val()
		qty = parseInt(qty)+1
		exist.find('input#qty_id').val(qty)
		exist.find('input.price_product_ticket').val(qty * parseFloat(list_product[3]))		
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

function send_to_server(tickets){
	$.ajax({
		data: {'list':JSON.stringify(tickets)}, 
		error: function(XMLHttpRequest, textStatus, errorThrown) {
			console.log("An error has occurred: " + textStatus);
		}, 
		success: function(data, textStatus, XMLHttpRequest) {
			try
			{
				console.log(data)
				updatePage(JSON.parse(data));
			}
			catch(error)
			{
			console.log("There was an error updating your"+ error);
			}
		}, 
		type: "POST", 
		url: "http://localhost:8000/terminal/orderSerializer/"});
}

function onchange_order_line(args){
	var id = args.id
	var start_id = '#id_terminal_order_line_set-'+id.substring( id.indexOf('-')+1 , id.lastIndexOf('-') )
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
	count = parseInt($('#id_terminal_order_line_set-TOTAL_FORMS').val())
	amount_total = 0
	if (count >  0 ){
		while (count >=0){
			amount = $('#id_terminal_order_line_set-'+count.toString()+'-amount_total').val()
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
	$.each(product, function(){
		list_product.push($(this).text())
	});
	find_ticket_in(list_product)	
}

function get_product_id(name, code){
	$.ajax({
		dataType: 'json',
		data: {'name': name, 'code' : code}, 
		type: "GET", 
		url: "http://localhost:8000/terminal/snippets/"+name+'/'+code,
		error: function(XMLHttpRequest, textStatus, errorThrown) {
			console.log("An error has occurred: " + textStatus);
		}, 
		success: function(data, textStatus, XMLHttpRequest) {
			console.log(data)
		}
	});
} 