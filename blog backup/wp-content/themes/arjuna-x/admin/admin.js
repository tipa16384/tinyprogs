// JavaScript Document

function getRadioValue(o) {
	if(!o) return "";
	var rl = o.length;
	if(rl == undefined)
		if(o.checked) return o.value;
		else return "";
	for(var i = 0; i < rl; i++) {
		if(o[i].checked) return o[i].value;
	}
	return "";
}

function headerMenu1_tD(o) {
		var v = getRadioValue(o);
		if(v=='pages') {
			document.getElementById('menus_1_sortBy_categories').style.display = 'none';
			document.getElementById('menus_1_sortBy_pages').style.display = 'block';
			document.getElementById('menus_1_include_categories').style.display = 'none';
			document.getElementById('menus_1_include_pages').style.display = '';
		} else if(v=='categories') {
			document.getElementById('menus_1_sortBy_categories').style.display = 'block';
			document.getElementById('menus_1_sortBy_pages').style.display = 'none';
			document.getElementById('menus_1_include_categories').style.display = '';
			document.getElementById('menus_1_include_pages').style.display = 'none';
		}
}
function headerMenu2_tD(o) {
		var v = getRadioValue(o);
		if(v=='pages') {
			document.getElementById('menus_2_sortBy_categories').style.display = 'none';
			document.getElementById('menus_2_sortBy_pages').style.display = 'block';
			document.getElementById('menus_2_include_categories').style.display = 'none';
			document.getElementById('menus_2_include_pages').style.display = '';
		} else if(v=='categories') {
			document.getElementById('menus_2_sortBy_categories').style.display = 'block';
			document.getElementById('menus_2_sortBy_pages').style.display = 'none';
			document.getElementById('menus_2_include_categories').style.display = '';
			document.getElementById('menus_2_include_pages').style.display = 'none';
		}
}

function customCSS_switch(o) {
	if (o.checked)
		document.getElementById('customCSS_input').style.display = 'block';
	else document.getElementById('customCSS_input').style.display = 'none';
}

function sidebar_twitterURL_switch(o) {
	if (o.checked)
		document.getElementById('sidebar_twitterURL').style.display = 'block';
	else document.getElementById('sidebar_twitterURL').style.display = 'none';
}

function sidebar_facebookURL_switch(o) {
	if (o.checked)
		document.getElementById('sidebar_facebookURL').style.display = 'block';
	else document.getElementById('sidebar_facebookURL').style.display = 'none';
}

function pagination_switch(o) {
		var v = getRadioValue(o);
		if(v=='1')
			document.getElementById('pagination_input').style.display = 'block';
		else if(v=='0')
			document.getElementById('pagination_input').style.display = 'none';
		
}

function enableIncludeMenuItems() {
	
	//First menu
	jQuery("#hm1ic_up").click(function() {
		jQuery("#hm1ec option:selected").each(function() {
			var tmp = '<option value="'+jQuery(this).attr('value')+'">'+jQuery(this).html()+'</option>';
			jQuery("#hm1ic").append(tmp);
			jQuery(this).remove();
		});
		return false;
	});
	jQuery("#hm1ic_down").click(function() {
		jQuery("#hm1ic option:selected").each(function() {
			var tmp = '<option value="'+jQuery(this).attr('value')+'">'+jQuery(this).html()+'</option>';
			jQuery("#hm1ec").append(tmp);
			jQuery(this).remove();
		});
		return false;
	});
	
	jQuery("#arjuna_update_theme").submit(function() {
		jQuery("#hm1ec option, #hm1ic option").attr('selected', 'selected');
	});

	jQuery("#hm1ip_up").click(function() {
		jQuery("#hm1ep option:selected").each(function() {
			var tmp = '<option value="'+jQuery(this).attr('value')+'">'+jQuery(this).html()+'</option>';
			jQuery("#hm1ip").append(tmp);
			jQuery(this).remove();
		});
		return false;
	});
	jQuery("#hm1ip_down").click(function() {
		jQuery("#hm1ip option:selected").each(function() {
			var tmp = '<option value="'+jQuery(this).attr('value')+'">'+jQuery(this).html()+'</option>';
			jQuery("#hm1ep").append(tmp);
			jQuery(this).remove();
		});
		return false;
	});
	
	jQuery("#arjuna_update_theme").submit(function() {
		jQuery("#hm1ep option, #hm1ip option").attr('selected', 'selected');
	});

	//Second menu
	jQuery("#hm2ic_up").click(function() {
		jQuery("#hm2ec option:selected").each(function() {
			var tmp = '<option value="'+jQuery(this).attr('value')+'">'+jQuery(this).html()+'</option>';
			jQuery("#hm2ic").append(tmp);
			jQuery(this).remove();
		});
		return false;
	});
	jQuery("#hm2ic_down").click(function() {
		jQuery("#hm2ic option:selected").each(function() {
			var tmp = '<option value="'+jQuery(this).attr('value')+'">'+jQuery(this).html()+'</option>';
			jQuery("#hm2ec").append(tmp);
			jQuery(this).remove();
		});
		return false;
	});
	
	jQuery("#arjuna_update_theme").submit(function() {
		jQuery("#hm2ec option, #hm2ic option").attr('selected', 'selected');
	});

	jQuery("#hm2ip_up").click(function() {
		jQuery("#hm2ep option:selected").each(function() {
			var tmp = '<option value="'+jQuery(this).attr('value')+'">'+jQuery(this).html()+'</option>';
			jQuery("#hm2ip").append(tmp);
			jQuery(this).remove();
		});
		return false;
	});
	jQuery("#hm2ip_down").click(function() {
		jQuery("#hm2ip option:selected").each(function() {
			var tmp = '<option value="'+jQuery(this).attr('value')+'">'+jQuery(this).html()+'</option>';
			jQuery("#hm2ep").append(tmp);
			jQuery(this).remove();
		});
		return false;
	});
	
	jQuery("#arjuna_update_theme").submit(function() {
		jQuery("#hm2ep option, #hm2ip option").attr('selected', 'selected');
	});
}

function ajax_savePanel(ID, set) {
	jQuery.ajax({
		type: "GET",
		url: jQuery('#arjuna_themeURL').val() + '/admin/ajax/savePanel.php',
		data: {
			ID: ID,
			set: set
		},
		dataType: 'json'
	});
}

tmp_farbtastic = null;

arjuna_CWA = {
	contentWidth: 0,
	constraint: 920,
	sliderConstraint: 500,
	minContentArea: 460,
	minSidebar: 140,
	maxSidebar: 460,
	previewAvailWidth: 93,
	
	//calculated
	constraintRatio: 0,
	enabledLeft: false,
	enabledRight: false,
	
	init: function() {
		this.constraintRatio = arjuna_CWA.sliderConstraint / arjuna_CWA.constraint;
		
		if(jQuery('#content-area-width-slider').hasClass('both'))
			this.enabledLeft = this.enabledRight = true;
		if(jQuery('#content-area-width-slider').hasClass('left'))
			this.enabledLeft = true;
		if(jQuery('#content-area-width-slider').hasClass('right'))
			this.enabledRight = true;
		
		this.calculateContentArea();
		//this.setRealContentArea(jQuery('#real-content-area-width').val());
		
		this.enableSliders();
		this.enableCustom();
	},
	
	enableSliders: function() {
		//set initial position
		var left = jQuery('#left-sidebar-width').val() * this.constraintRatio;
		var right = jQuery('#right-sidebar-width').val() * this.constraintRatio;
		var leftHandle = left - 7;
		var rightHandle = jQuery('#slide-right-constraint').outerWidth() - right;
		
		if(this.enabledLeft)
			jQuery('#slide-left-constraint .slide-left').css('width', left);
		if(this.enabledRight)
			jQuery('#slide-right-constraint .slide-right').css('width', right);
		
		if(this.enabledLeft)
			jQuery('#slide-left-handle').css('left', leftHandle);
		if(this.enabledRight)
			jQuery('#slide-right-handle').css('left', rightHandle);
			
		this.adjustPreview();
		
		jQuery('#slide-left-handle').draggable({
			containment: "#slide-left-constraint",
			scroll: false,
			drag: function(e, ui) {
				//calculate sidebar width
				var sidebarWidth = ui.position.left + 7;
				
				//calculate actual widths
				var actualLeftSidebar = Math.floor(sidebarWidth / arjuna_CWA.constraintRatio);
				var actualRightSidebar = arjuna_CWA.enabledRight ? jQuery('#right-sidebar-width').val() : 0;
				var actualContent = arjuna_CWA.constraint - actualLeftSidebar - actualRightSidebar;
				
				//check conditions and constrain if necessary
				
				//...minimum content area width
				if(actualContent < arjuna_CWA.minContentArea) {
					//move right sidebar until that reaches minimum, then constrain
					actualRightSidebar = actualContent - actualLeftSidebar;
					if(actualRightSidebar < arjuna_CWA.minSidebar) {
						actualRightSidebar = arjuna_CWA.enabledRight ? arjuna_CWA.minSidebar : 0;
						actualContent = arjuna_CWA.minContentArea;
						actualLeftSidebar = arjuna_CWA.constraint - actualContent - actualRightSidebar;
					}
				}
				
				//all conditions done and values adjusted accordingly, set both sidebars
				arjuna_CWA.setActualValues(actualLeftSidebar, actualRightSidebar);
				
				//arjuna_CWA.adjustPreview(contentArea);
			},
			stop: function(e, ui) {
				//set handle to actual position
				arjuna_CWA.setActualValues(jQuery('#left-sidebar-width').val(), jQuery('#right-sidebar-width').val());
			}
		});
		
		jQuery('#slide-right-handle').draggable({
			containment: "#slide-right-constraint",
			scroll: false,
			drag: function(e, ui) {
				//calculate sidebar width
				var sidebarWidth = jQuery('#slide-right-constraint').outerWidth() - ui.position.left;
				
				//calculate actual widths
				var actualLeftSidebar = arjuna_CWA.enabledLeft ? jQuery('#left-sidebar-width').val() : 0;
				var actualRightSidebar = Math.floor(sidebarWidth / arjuna_CWA.constraintRatio);
				var actualContent = arjuna_CWA.constraint - actualRightSidebar - actualLeftSidebar;
				
				//check conditions and constrain if necessary
				
				//...minimum content area width
				if(actualContent < arjuna_CWA.minContentArea) {
					//move left sidebar until that reaches minimum, then constrain
					actualLeftSidebar = actualContent - actualRightSidebar;
					if(actualLeftSidebar < arjuna_CWA.minSidebar) {
						actualLeftSidebar = arjuna_CWA.enabledLeft ? arjuna_CWA.minSidebar : 0;
						actualContent = arjuna_CWA.minContentArea;
						actualRightSidebar = arjuna_CWA.constraint - actualContent - actualLeftSidebar;
					}
				}
				
				//all conditions done and values adjusted accordingly, set both sidebars
				arjuna_CWA.setActualValues(actualLeftSidebar, actualRightSidebar);
				
				//arjuna_CWA.adjustPreview(contentArea);
			},
			stop: function(e, ui) {
				//set handle to actual position
				arjuna_CWA.setActualValues(jQuery('#left-sidebar-width').val(), jQuery('#right-sidebar-width').val());
			}
		});
	},
	
	enableCustom: function() {
		jQuery('#left-sidebar-width').change(function() {
			//calculate actual widths
			var actualLeftSidebar = jQuery(this).val();
			var actualRightSidebar = arjuna_CWA.enabledRight ? jQuery('#right-sidebar-width').val() : 0;
			var actualContent = jQuery('#content-area-width').val();
			
			//conditions
			
			//...minimum and maximum
			if(actualLeftSidebar < arjuna_CWA.minSidebar)
				actualLeftSidebar = arjuna_CWA.minSidebar;
				
			if(actualLeftSidebar > arjuna_CWA.maxSidebar)
				actualLeftSidebar = arjuna_CWA.maxSidebar;
			
			//adjustments
			
			//...first add to or subtract from content area
			actualContent = arjuna_CWA.constraint - actualLeftSidebar - actualRightSidebar;
			//subtract from other sidebar if necessary
			if(actualContent < arjuna_CWA.minContentArea) {
				actualContent = arjuna_CWA.minContentArea;
				if(arjuna_CWA.enabledRight) {
					actualRightSidebar = arjuna_CWA.constraint - actualContent - actualLeftSidebar;
					if(actualRightSidebar < arjuna_CWA.minSidebar) {
						actualRightSidebar = arjuna_CWA.minSidebar;
						actualLeftSidebar = arjuna_CWA.constraint - actualContent - actualRightSidebar;
					}
				} else actualLeftSidebar = arjuna_CWA.constraint - actualContent;
				
				
			}
			
			arjuna_CWA.setActualValues(actualLeftSidebar, actualRightSidebar);
		}).keydown(function(e) {
			if (e.keyCode == 13) {
				jQuery(this).blur().change();
				//e.preventDefault();
				//e.stopPropagation();
				return false;
			}
		});
		
		jQuery('#right-sidebar-width').change(function() {
			//calculate actual widths
			var actualLeftSidebar = arjuna_CWA.enabledLeft ? jQuery('#left-sidebar-width').val() : 0;
			var actualRightSidebar = jQuery(this).val();
			var actualContent = jQuery('#content-area-width').val();
			
			//conditions
			
			//...minimum and maximum
			if(actualRightSidebar < arjuna_CWA.minSidebar)
				actualRightSidebar = arjuna_CWA.minSidebar;
				
			if(actualRightSidebar > arjuna_CWA.maxSidebar)
				actualRightSidebar = arjuna_CWA.maxSidebar;
			
			//adjustments
			
			//...first add to or subtract from content area
			actualContent = arjuna_CWA.constraint - actualLeftSidebar - actualRightSidebar;
			//subtract from other sidebar if necessary
			if(actualContent < arjuna_CWA.minContentArea) {
				actualContent = arjuna_CWA.minContentArea;
				if(arjuna_CWA.enabledLeft) {
					actualLeftSidebar = arjuna_CWA.constraint - actualContent - actualRightSidebar;
					if(actualLeftSidebar < arjuna_CWA.minSidebar) {
						actualLeftSidebar = arjuna_CWA.minSidebar;
						actualRightSidebar = arjuna_CWA.constraint - actualContent - actualLeftSidebar;
					}
				} else actualRightSidebar = arjuna_CWA.constraint - actualContent;
				
				
			}
			
			arjuna_CWA.setActualValues(actualLeftSidebar, actualRightSidebar);
		}).keydown(function(e) {
			if (e.keyCode == 13) {
				jQuery(this).blur().change();
				//e.preventDefault();
				//e.stopPropagation();
				return false;
			}
		});
	},
	
	calculateContentArea: function() {
		var left = this.enabledLeft ? jQuery('#left-sidebar-width').val() : 0;
		var right = this.enabledRight ? jQuery('#right-sidebar-width').val() : 0;
		var contentArea = this.constraint - left - right;
		
		jQuery('#content-area-width').val(contentArea);
	},
	
	setLeftSlider: function(actualWidth) {
		//get slider width
		var width = actualWidth * this.constraintRatio;
		
		//set slide
		jQuery('#slide-left-constraint .slide-left').width(width);
		//set handle
		var left = width - 7;
		jQuery('#slide-left-handle').css('left', left);
	},
	setRightSlider: function(actualWidth) {
		//get slider width
		var width = actualWidth * this.constraintRatio;
		
		//set slide
		jQuery('#slide-right-constraint .slide-right').width(width);
		//set handle
		jQuery('#slide-right-handle').css('left', jQuery('#slide-right-constraint').outerWidth() - width);
	},
	
	setActualValues: function(actualLeft, actualRight) {
		if(actualLeft == 0)
			this.enabledLeft = false;
		else this.enabledLeft = true;
		
		if(actualRight == 0)
			this.enabledRight = false;
		else this.enabledRight = true;
		
		var actualContent = this.constraint - actualLeft - actualRight;
		
		if(this.enabledLeft)
			this.setLeftSlider(actualLeft);
		if(this.enabledRight)
			this.setRightSlider(actualRight);
		
		//set values
		jQuery('#left-sidebar-width').val(actualLeft);
		jQuery('#content-area-width').val(actualContent);
		jQuery('#right-sidebar-width').val(actualRight);
		
		this.adjustPreview();
	},
	
	updateCustom: function(contentArea) {
		jQuery('#content-area-width').val(contentArea);
		jQuery('#sidebar-width').val(arjuna_CWA.constraint - contentArea);
	},
	
	adjustPreview: function() {
		//get actual values
		var actualLeftSidebar = arjuna_CWA.enabledLeft ? jQuery('#left-sidebar-width').val() : 0;
		var actualRightSidebar = arjuna_CWA.enabledRight ? jQuery('#right-sidebar-width').val() : 0;
		var actualContent = jQuery('#content-area-width').val();
		
		//calc available width
		//one col must be deducted 4px
		var availWidth = arjuna_CWA.previewAvailWidth - 4;
		if(actualLeftSidebar != 0)
			availWidth -= 4;
		if(actualRightSidebar != 0)
			availWidth -= 4;
		
		//get relative values
		var constraint = availWidth / arjuna_CWA.constraint;
		
		var leftSidebar = actualLeftSidebar * constraint;
		var rightSidebar = actualRightSidebar * constraint;
		var contentArea = availWidth - leftSidebar - rightSidebar;
		
		jQuery('#preview-sidebar-left').css('width', leftSidebar);
		jQuery('#preview-content-area').css('width', contentArea);
		jQuery('#preview-sidebar-right').css('width', rightSidebar);
	}
};

arjuna_SB = {
	init: function() {
		jQuery('#sidebar-buttons .checkbox').click(function() {
			var s = jQuery(this).closest('tr');
			if(jQuery(this).is(':checked'))
				s.removeClass("disabled");
			else s.addClass("disabled");
		});
		
		jQuery('#sidebar-buttons input[type=text]').focus(function() {
			jQuery(this).closest('tr').removeClass("disabled");
			jQuery(this).closest('tr').find('.checkbox').attr('checked', 'checked');
		});
		
		jQuery('#sidebar-buttons input.URL[type=text]').blur(function() {
			if(jQuery(this).val() == '') {
				jQuery(this).closest('tr').addClass("disabled");
				jQuery(this).closest('tr').find('.checkbox').attr('checked', '');
			}
		});
	}
};

jQuery(function() {
	jQuery('.srsContainer h4.title')
	.click(function() {
		if(jQuery(this).parent().hasClass('srsContainerClosed')) {
			jQuery(this).parent().removeClass('srsContainerClosed');
			ajax_savePanel(jQuery(this).parent().attr('self:ID'), 1);
		} else {
			jQuery(this).parent().addClass('srsContainerClosed');
			ajax_savePanel(jQuery(this).parent().attr('self:ID'), 0);
		}
	})
	.mouseover(function() { jQuery(this).addClass('over'); })
	.mouseout(function() { jQuery(this).removeClass('over'); });
	
	enableIncludeMenuItems();
	
	if(jQuery('#backgroundColor_picker').length > 0) {
		tmp_farbtastic = jQuery.farbtastic('#backgroundColor_picker div.inner', function(color) {
			jQuery('#backgroundColor').val(color);
			jQuery('#backgroundColor_picker').css('background-color', color);
			//jQuery('#backgroundColor_picker div.inner').fadeOut(500);
		}).setColor(jQuery('#backgroundColor').val());
		
		jQuery('#backgroundColor_picker').click(function(e) {
			jQuery('div.inner', this).fadeIn(500);
			jQuery('#backgroundStyle_solid').attr('checked', 'checked');
			e.stopPropagation();
			return false;
		});
		
		jQuery("#backgroundColor_picker div.inner").click(function(e) {
			e.stopPropagation();
			return false;
		});
		jQuery("body").click(function() {
			jQuery('#backgroundColor_picker div.inner').fadeOut(500);
		});
	}
	
	arjuna_CWA.init();
	arjuna_SB.init();
	
	jQuery('#sidebarDisplay_right').click(function() {
		jQuery('#content-area-width-slider').addClass('right').removeClass('left none both');
		arjuna_CWA.setActualValues(0, 250);
		jQuery('#sidebarDisplay-both-container').hide();
		jQuery('#sidebar-width-panel').show();
	});
	jQuery('#sidebarDisplay_left').click(function() {
		jQuery('#content-area-width-slider').addClass('left').removeClass('right none both');
		arjuna_CWA.setActualValues(250, 0);
		jQuery('#sidebarDisplay-both-container').hide();
		jQuery('#sidebar-width-panel').show();
	});
	jQuery('#sidebarDisplay_none').click(function() {
		jQuery('#sidebar-width-panel').hide();
		jQuery('#sidebarDisplay-both-container').hide();
		jQuery('#content-area-width-slider').addClass('none').removeClass('left right both');
	});
	jQuery('#sidebarDisplay_both').click(function() {
		arjuna_CWA.setActualValues(200, 200);
		jQuery('#content-area-width-slider').addClass('both').removeClass('left right none');
		jQuery('#sidebar-width-panel').show();
		jQuery('#sidebarDisplay-both-container').show();
	});
	
	jQuery('#menus-1-useNavMenus input[name=menus_1_useNavMenus]').change(function() {
		if(jQuery('#menus-1-useNavMenus input[name=menus_1_useNavMenus]:checked').val() == '0')
			jQuery('#menus-1-useNavMenus-legacy').show();
		else jQuery('#menus-1-useNavMenus-legacy').hide();
	});
	
	jQuery('#menus-2-useNavMenus input[name=menus_2_useNavMenus]').change(function() {
		if(jQuery('#menus-2-useNavMenus input[name=menus_2_useNavMenus]:checked').val() == '0')
			jQuery('#menus-2-useNavMenus-legacy').show();
		else jQuery('#menus-2-useNavMenus-legacy').hide();
	});
	
	jQuery('#useFeedburner input[name=useFeedburner]').change(function() {
		if(jQuery('#useFeedburner input[name=useFeedburner]:checked').val() == '1')
			jQuery('#useFeedburner-feedburner').show();
		else jQuery('#useFeedburner-feedburner').hide();
	});
	
	jQuery('#search-enabled').click(function() {
		if(jQuery(this).is(':checked'))
			jQuery('#search-enabled-container').show();
		else jQuery('#search-enabled-container').hide();
	});
	
	jQuery('#enableTwitter input[name=twitterWidget_enabled]').change(function() {
		if(jQuery('#enableTwitter input[name=twitterWidget_enabled]:checked').val() == '1')
			jQuery('#enableTwitter-options').show();
		else jQuery('#enableTwitter-options').hide();
	});
	
	jQuery('#sidebarButtons_RSS_extended').click(function() {
		if(jQuery(this).is(':checked'))
			jQuery('#sidebar-buttons tr.rss').addClass('rss-extended');
		else jQuery('#sidebar-buttons tr.rss').removeClass('rss-extended');
	});
	
	jQuery('#copyright-owner')
	.focus(function() {
		jQuery('#copyright-owner-box input[name=coprightOwnerType][value=custom]').attr('checked', true);
	})
	.blur(function() {
		if(jQuery(this).val() == "")
			jQuery('#copyright-owner-box input[name=coprightOwnerType][value=default]').attr('checked', true);
	});
	
	_colorSchemes = [
		'lightBlue',
		'darkBlue',
		'khaki',
		'seaGreen',
		'lightRed',
		'purple',
		'lightGray',
		'darkGray',
		'regimentalBlue',
		'bristolBlue'
	];
	
	for(var i=0; i<_colorSchemes.length; i++) {
		var color = _colorSchemes[i];
		jQuery('#icon-'+color)
		.attr('color', color)
		.click(function() {
			var color = jQuery(this).attr('color');
			jQuery('#headerImage_'+color).attr('checked', 'checked').change();
		});
		jQuery('#headerImage_'+color)
		.attr('color', color)
		.change(function() {
			var color = jQuery(this).attr('color');
			jQuery('#icon-footerStyle2').removeClass(_colorSchemes.join(' ')).addClass(color);
		});
	}
	
	jQuery('#icon-footerStyle1').click(function() {
		jQuery('#footerStyle_style1').attr('checked', 'checked').change();
	});
	jQuery('#icon-footerStyle2').click(function() {
		jQuery('#footerStyle_style2').attr('checked', 'checked').change();
	});
});
