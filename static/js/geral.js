let isBlack = false;
let isNoPonto = false;
let navClicked = false;
const corInicial = 'linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0))';

// Paralax
$(function () {
	$(window).scroll(function () {
		var window_scrolltop = $(this).scrollTop();

		// Passa por cada elemento com a classe .parallax
		$('.parallax').each(function () {
			var obj = $(this);

			// Garante que apenas trabalhemos no elemento que está visível na tela
			if (window_scrolltop >= obj.position().top - obj.height()
				&& window_scrolltop <= obj.position().top + obj.height()) {

				// O atributo data-divisor vai definir a velocidade do efeito
				var divisor = typeof obj.attr('data-divisor') == 'undefined' ? 4 : obj.attr('data-divisor');

				// Corrige a diferença do primeiro elemento
				if (obj.is(':first-child')) {
					var bg_pos = (window_scrolltop - obj.position().top) / divisor;
				} else {
					var bg_pos = (window_scrolltop - obj.position().top + (obj.height() - 100)) / divisor;
				}

				// Modifica a posição do bg
				obj.css({
					'background-position': '50% -' + bg_pos + 'px'
				});

				// Animação do primeiro texto
				obj.children('.text').css({
					'bottom': (window_scrolltop - obj.position().top + 100) + 'px'
				});

			} // Garante que apenas trabalhemos no elemento que está visível na tela
		}); // $('.parallax').each(function(){ ...
	}); // $(window).scroll(function(){ ...
});

// Visibilidade da navbar
$(function () {
	$(window).scroll(function () {
		var pontoDeMudancaDeCor = $("#nav").height() * 4;

		if ($(this).scrollTop() < pontoDeMudancaDeCor) {
			$(".transparencia").css('background', corInicial);
			isBlack = false;
			isNoPonto = false;
		} else {
			$(".transparencia").css('background', 'rgba(0,0,0,0.98)');
			isBlack = true;
			isNoPonto = true;
		}
	});
});


$(document).ready(function (e) {
	$('.navbar-toggler').click(function () {
		if (!isBlack && !isNoPonto){
			// $('.transparencia').css('background', 'rgba(0,0,0,0.9)');
			$('.transparencia').css('background', 'rgba(184, 112, 17, 1)');
			navClicked = true;
			isBlack = true;
		}
		else if(navClicked && !isNoPonto){
			$('.transparencia').css('background', corInicial);
			navClicked = false;
			isBlack = false;
		}
	});
});