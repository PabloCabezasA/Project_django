$('#myModal').on('shown.bs.modal', function () {
	  $('#myInput').focus()
})

$(document).ready(function(){

	$('.select_level1').change(function() { 
    	ajax_find_obras();
    });
	
	$('#add_more').click(function() { 
    	cloneMore('#book-', 'autor_autor_obras_set');
    });	

	$('input[readonly = readonly]').addClass('inp_readonly')
});

function texto_italico(){
	$('#about-me').addClass('special')
}

function texto_tamaño(){
	$('#about-me').addClass('main-text')
}

function seleccionar_hijo(){
	$('#about-me p').addClass('autor-bio');
	$('.supplies li:nth-child(2)').addClass('items');
	$('p img:not([alt])').addClass('needs-alt')
	$('p img[alt=\'cool\']').addClass('needs-alt')
	$('.imagenes').addClass('needs-alt')
}

function cloneMore(selector, type) {
    var total = $('#id_' + type + '-TOTAL_FORMS').val();
    selector = selector + (total-1).toString()
    var newElement = $(selector).clone(true);
    newElement.id = 'book-'+ total.toString();
    newElement[0].id = 'book-'+ total.toString();
    console.log(newElement.find(':input'))
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

function my_js_callback(data){
    alert(data.message);
}

function ajax_find_obras(){
	var catid;
	$(".select_level1 option:selected").each(function() {
		option = $( this ).val();
    });
    $.get('/curso1/', {category_id: option}, function(data){
               $('#like_count').html(data);
               $('#likes').hide();
           });}			