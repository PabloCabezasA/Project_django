$(document).ready(function(){
	$('#filtro_terminal_ventas').change(function(){
		var product = $('#filtro_terminal_ventas').val()
		$('#product_contain').html('')
	    $.get('', {'filter': product}, function(data){
	        $.each(data, function() {	        		
        		cont = "<div class='col-md-3'><div class='thumbnail'>" +
        			 	"<img src='/media/"+this['model_pic']+"' alt='No Photo' class='img-thumbnail' style='width:180px;height:130px'>"+ 
        				"<div class='caption'>" +
    					"<label>"+this['name'] +"</label> "+ 
    					"<label>"+this['code'] +"</label></br><label>Precio: </label>"+
    					"<label>"+this['price_sale']+"</label>"+        					        				
        				"</div> </div> </div>"         				        				
        	    $('#product_contain').append(cont)
	        })	    	
	    });					
	});
	
	$('.prod_obj_data').click(function(){
		var product = $(this).find('label')
		var list_product = []
		$.each(product, function(){
			list_product.push($(this).text())
		});
		find_ticket_in(list_product)
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
			d_ticket['amount_total'] = $($(this).find('input')).val()
			list_ticket.push(d_ticket)
		});
		send_to_server(list_ticket)
	});
});

function find_ticket_in(list_product){
	cont = "<div id='ticket_"+list_product[0]+"'>" +
			"<label>"+list_product[0]+"</label> " +
			"<label>"+list_product[1]+"</label> "+
			"<label id='sg'>$</label> "+
			"<input type='text' class='price_product_ticket' value='"+list_product[3]+"'/>"+
			"</div>"				
	
	ticket = $('#boleta_terminal_venta'+' #ticket_'+list_product[0])
	console.log(ticket)
	$('#boleta_terminal_venta').append(cont)
}

function send_to_server(tickets){
	$.ajax({
		data: {'list':JSON.stringify(tickets)}, 
		error: function(XMLHttpRequest, textStatus, errorThrown) {
			console.log("An error has occurred: " + textStatus);
		}, 
		success: function(data, textStatus, XMLHttpRequest) {
			try
			{updatePage(JSON.parse(data));
			}
			catch(error)
			{
				console.log("There was an error updating your"+
			"shopping cart. Please call customer service at"+
			"800-555-1212");
			}
		}, 
		type: "GET", 
		url: "save_data"});
}