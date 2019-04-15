$(document).ready(function (){
	$(document).on('click', '.checkbox', function(){
		$(this).parent().addClass('completed');
		$(this).attr('disabled', true);

		uid = $(this).attr('data-uid'); //запрос к серверу по соответствующему адресу, чтобы сохранить состояние
		console.log('Подтверждаем элемент' + this + uid);
		$.get("/tasks/complete/" + uid);
	});

	$(document).on('click', '.remove', function(){
		$(this).parent().remove();
		console.log('Удаляем элемент' + this);
	});

	$(document).on('click', '#needtodo', function(){
		$('.completed').remove();
		console.log('Только невыполненные');
	});

});