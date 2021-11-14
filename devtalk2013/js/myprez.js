var setGrid = function(filters) {
	var ewall;
		
	ewall = new freewall("#container");
	ewall.fixSize({ block: $('.almostAlways'), width: 460, height: 162 });
	ewall.reset({
		selector: '.item',
		animate: true,
		cell: {
			width: 170,
			height: 170
		},
		onResize: function() {
			ewall.fitWidth();
		}
	});

	ewall.setFilter(filters);
	ewall.fitWidth();
}
	
var page = 0;
	
var homePage = function() {
	page = 0;
	fixGrid();
}
	
var nextPage = function() {
	if ($('.page'+(page+1)).length > 0) {
		page += 1;
		fixGrid();
	}
}
	
var prevPage = function() {
	if (page > 0) {
		page -= 1;
		fixGrid();
	}
}
	
var fixGrid = function() {
	var filter = '.always,.uncolored,.almostAlways';

	$('.home').off('click');
	$('.prev').off('click');
	$('.next').off('click');

	if ($('.page'+(page+1)).length > 0) {
		$('.next').on('click',nextPage);
		filter += ',.next';
	}
		
	if (page > 0) {
		$('.prev').on('click',prevPage);
		filter += ',.prev';
	}
		
	if (page > 0) {
		$('.home').on('click',homePage);
		filter += ',.home,.page'+page;
	} else {
		filter += ',.almostAlways,.colored,.homeTitle';
	}
		
	if (page == 0) {
		$('.uncolored').css({backgroundColor:'white'});
	} else {
		$('.uncolored').css({backgroundColor:'#CCC'});
	}
		
	setGrid(filter);
}
	
$(function() {
	setGrid('.item');
	homePage();
		
	$(window).trigger("resize");

	$(window).keydown(function (e) {
		switch (e.which) {
			case 39:
			case 106:
			case 32:
				nextPage();
				break;
			case 37:
			case 32:
				prevPage();
				break;
		}
	});
});
