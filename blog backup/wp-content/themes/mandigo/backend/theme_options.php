<?php
	// add the links to the theme options pages, and required files
	add_action('admin_menu', 'add_mandigo_options_page'   );
	add_action('admin_head', 'add_mandigo_options_css'    );
	add_action('admin_head', 'add_mandigo_farbtastic_libs');

	// the functions that load the theme options page
	function add_mandigo_options_page() {
		global $dirs;
		add_theme_page(
			'Theme_Options',
			'<img src="'. $dirs['www']['backend'] .'images/attention_catcher.png" alt="" /> Theme Options',
			'edit_themes',
			'Theme_Options',
			'mandigo_options_page'
		);
	}
	function add_mandigo_options_css() {
		global $dirs;
		echo '<link rel="stylesheet" type="text/css" href="'. $dirs['www']['backend'] .'css/options.css" />';
	}
	
	
	
	// this function includes the required files for the colorpicker to work
	function add_mandigo_farbtastic_libs() {
		global $dirs;
		echo '<script type="text/javascript" src="'. $dirs['www']['backend'] .'js/farbtastic.js"></script>';
		echo '<link rel="stylesheet" type="text/css" href="'. $dirs['www']['backend'] .'css/farbtastic.css" />';
	}



	// this one validate hex color codes
	function mandigo_color($value, $default) { 
		if (!preg_match("/^#/", $value))
			$value = '#'. $value;
		if (!preg_match("/^#([0-9A-F]{3}){1,2}$/i", $value))
			$value = $default;
		return $value;
	}



	// this one escapes strings
	function mandigo_escape($string) {
		$string = str_replace('\\"', '&#34;', $string);
		$string = str_replace("\\'", '&#39;', $string);
		return $string;
	}



	// the BIG page
	function mandigo_options_page() {
		global $dirs, $schemes, $mandigo_options, $mandigo_version;

		if (isset($_GET['check'])) {
			$function = $_GET['check'];
			if (preg_match('/^mandigo_upgrade_/', $function)) {
				include_once(TEMPLATEPATH .'/backend/upgrade.php');
				if (function_exists($function))
					$function();
			}
		}

		if (isset($_GET['dismiss'])) {
			$mandigo_actions = get_option('mandigo_actions');
			$mandigo_actions[$_GET['dismiss']] = 0;
			update_option('mandigo_actions', $mandigo_actions);
		}

		// process the submitted form if any, prior to displaying the options page
		if (isset($_POST['updated'])) {
			// build an array of pages to exclude
			$header_navigation_exclude_pages = array();
			foreach ($_POST as $field => $value) {
				if (stristr($field, 'header_navigation_exclude_page_'))
					$header_navigation_exclude_pages[] = preg_replace("/.+_/", '', $field);

				if (preg_match("/title_scheme_/", $field))
					$mandigo_options[$field] = mandigo_escape($value);
				
				if ($field == 'background_color')         $mandigo_options[$field] = mandigo_color($value, '#44484F');
				if ($field == 'color_post_background')    $mandigo_options[$field] = mandigo_color($value, '#FAFAFA');
				if ($field == 'color_post_border')        $mandigo_options[$field] = mandigo_color($value, '#EEEEEE');
				if ($field == 'color_sidebar_background') $mandigo_options[$field] = mandigo_color($value, '#EEEEEE');
				if ($field == 'color_sidebar_border')     $mandigo_options[$field] = mandigo_color($value, '#DDDDDD');
			}
			
			foreach (
				array(
					'scheme',
					'scheme_randomize',
					'header_navigation_position',
					'header_navigation_no_submenus',
					'header_navigation_stripe',
					'background_pattern_file',
					'background_pattern_fixed',
					'background_pattern_repeat',
					'background_pattern_position',
					'sidebar_count',
					'sidebar_always_show',
					'sidebar_1_position',
					'sidebar_2_position',
					'sidebar_1_width',
					'sidebar_2_width',
					'header_blogname_smaller_font',
					'header_blogname_stroke',
					'header_blogname_shadow',
					'header_blogname_hide',
					'header_blogdesc_hide',
					'header_random_image',
					'header_slim',
					'header_clickable',
					'title_scheme_index',
					'title_scheme_single',
					'title_scheme_page',
					'title_scheme_category',
					'title_scheme_date',
					'title_scheme_search',
					'heading_level_blogname',
					'heading_level_blogdesc',
					'heading_level_post_title_multi',
					'heading_level_post_title_single',
					'heading_level_page_title',
					'heading_level_widget_title',
					'bold_links',
					'no_text_wrapping',
					'collapse_posts',
					'date_format',
					'date_position',
					'emphasize_as_bold',
					'clear_all_paragraphs',
					'no_image_borders',
					'dont_justify',
					'display_tags_after_content',
					'disable_animations',
					'comments_numbering',
					'comments_highlight_author',
					'comments_allow_markup',
					'comments_no_gravatars',
					'trackbacks_position',
					'fixes_comments_1',
					'fixes_comments_2',
					'fixes_whitespace_pre',
					'fixes_touch_content',
					'footer_statistics',
					'full_search_results',
					'drop_caps',
					'font_family',
					'no_comments_on_pages',
					'header_navigation_speed_appear',
					'header_navigation_speed_disappear',
					'fully_dynamic_stylesheet',
				)
				as $field
			) {
				$mandigo_options[$field] = $_POST[$field];
			}
			
			$mandigo_options['header_navigation_exclude_pages'] = $header_navigation_exclude_pages;
			$mandigo_options['layout_width'] = ($_POST['layout_width_1024'] ? 1024 : 800);
			update_option('mandigo_options', $mandigo_options);
			
			echo '<div class="updated fade"><p>Options updated.</p></div>';
		}
		
		// this remote path to the current scheme needs to be reset in some cases
		$dirs['www']['scheme'] = $dirs['www']['scheme'] . "$scheme/";

		// build a list of selectable schemes from the array we built earlier
		foreach ($schemes as $scheme) {
			$list_of_schemes .= sprintf(
				'<input type="radio" name="scheme" value="%s" %s /><img src="%s/preview.jpg" alt="%s" /> &nbsp;',
				$scheme,
				(
					$scheme == $mandigo_options['scheme']
					? 'checked="checked"'
					: ''
				),
				$dirs['www']['schemes'] . $scheme,
				$scheme
			);
		}

		// browse through the images/patterns/ dir for image files and build a stack of option fields
		$patternsdir = opendir($dirs['loc']['patterns']);
		$list_of_patterns = sprintf(
			'<option value=""%s>none</option>',
			(
				!$mandigo_options['background_pattern_file']
				? ' selected="selected"'
				: ''
			)
		);
		while (false !== ($file = readdir($patternsdir))) {
			if (preg_match("/\.(?:jpe?g|png|gif|bmp)$/i", $file))
			  $list_of_patterns .= sprintf(
				'<option value="%s" %s>images/patterns/%s</option>',
				$file,
				(
					$file == $mandigo_options['background_pattern_file']
					? ' selected="selected"'
					: ''
				),
				$file
			);
		}

		$list_of_pages = wp_list_pages(array('title_li' => '', 'echo' => 0));
		$list_of_pages = preg_replace('/<\/?a[^>]*>/', '', $list_of_pages);
		$list_of_pages = preg_replace('/page-item-([0-9]+)">/', 'page-item-$1"><input type="checkbox" name="header_navigation_exclude_page_$1" /> ', $list_of_pages);
		foreach ($mandigo_options['header_navigation_exclude_pages'] as $page)
			$list_of_pages = str_replace("header_navigation_exclude_page_$page", "header_navigation_exclude_page_$page\" checked='checked'", $list_of_pages);


		// build the list of pages, for the 'pages to be excluded' part
/*
		$pages = &get_pages('sort_column=menu_order');
		foreach ($pages as $page) {
			$list_of_pages .= sprintf(
				'%s<input type="checkbox" name="header_navigation_exclude_page_%s" %s /> %s<br />',
				($page->post_parent ? '&nbsp;&nbsp;&nbsp;' : ''),
				$page->ID,
				(
					@in_array($page->ID, $mandigo_options['header_navigation_exclude_pages'])
					? ' checked'
					: ''
				),
				$page->post_title
			);
		}
*/

		// check for pending user actions
		$mandigo_actions = get_option('mandigo_actions');
		if (is_array($mandigo_actions)) {
			foreach ($mandigo_actions as $upgrade_check => $has_errors) {
				if ($has_errors) {
					include_once(TEMPLATEPATH .'/backend/upgrade.php');
					$function = sprintf('%s_error', $upgrade_check);
					if (function_exists($function))
						$function();
				}
			}
		}

		$top = array(
			'<a href="http://wiki.onehertz.com/WordPress/Mandigo" target="_blank">Need help? Check out the Mandigo wiki</a>',
			'<a href="#versioncheck">Are you using the latest version?</a>',
			'<a href="http://www.onehertz.com/portfolio/wordpress/donate/" target="_blank">Do you enjoy Mandigo? Please consider making a donation</a>'
		);



		// output the beast
		echo '
		
		<div class="wrap">
		<span style="float: right; margin-top: 10px;">'. $top[array_rand($top)] .'</span>
		<form name="mandigo_options_form" method="post" action="?page=Theme_Options">
		<input type="hidden" name="updated" value="1" />
		<h2 style="clear: none;">Mandigo Options <span class="submit"><input type="submit" value="'. __('Update Options &raquo;') .'"/></span></h2>
		<div style="padding: 5px 0 20px 0;">
			<a href="#color_scheme">Color Scheme</a> | 
			<a href="#layout_opts">Layout</a> | 
			<a href="#header_opts">Header</a> | 
			<a href="#posts_opts">Posts</a> | 
			<a href="#comments_opts">Comments</a> | 
			<a href="#seo_opts">SEO</a> | 
			<a href="#layout_fixes">Layout Fixes</a> | 
			<a href="#misc_opts">Miscellaneous</a>
		</div>
	

		
		<fieldset class="options" id="color_scheme">
		<legend>Color Scheme</legend>
		'. $list_of_schemes .'
		<br />

		<input type="checkbox" name="scheme_randomize" ' .($mandigo_options['scheme_randomize'] ? 'checked="checked"' : '') .' /> I like them all, change schemes randomly!<br />

		<label>Background</label>
		<div id="picker" style="position: absolute; left: 600px;"></div>
		<script type="text/javascript">
			jQuery(document).ready(function() {
				var f = jQuery.farbtastic("#picker");
				jQuery("#picker").hide();
				jQuery(".colorpicker").each(function () { f.linkTo(this); }).focus(function() { f.linkTo(this); jQuery("#picker").fadeIn(); });
			});
			defaultColor = function(e, v) {
				var f = eval("document.forms.mandigo_options_form."+ e);
				f.value = v;
				f.focus();
			}
		</script>
		<table border="0">
			<tr>
				<td align="right" width="180">Background color:</td>
				<td>
					<input type="text" name="background_color" id="background_color" class="colorpicker" value="'. $mandigo_options['background_color'] .'" /> <a href="#" onclick="defaultColor(\'background_color\', \'#44484F\'); return false;">restore default</a>
				</td>
			</tr>
			<tr>
				<td align="right">Background pattern:</td>
				<td>
					<select name="background_pattern_file">
						'. $list_of_patterns .'
					</select>
				</td>
			</tr>
			<tr>
				<td align="right">Attachment :</td>
				<td>
					<input type="radio" name="background_pattern_fixed" value="0" '. ($mandigo_options['background_pattern_fixed'] ? '' : 'checked="checked"') .' />scroll &nbsp; 
					<input type="radio" name="background_pattern_fixed" value="1" '. ($mandigo_options['background_pattern_fixed'] ? 'checked="checked"' : '') .' />fixed
				</td>
			</tr>
			<tr>
				<td align="right">Repeat :</td>
				<td>
					<select name="background_pattern_repeat">
						<option value="repeat" '.    ($mandigo_options['background_pattern_repeat'] == 'repeat'    ? 'selected="selected"' : '') .'>both horizontally and vertically</option>
						<option value="repeat-x" '.  ($mandigo_options['background_pattern_repeat'] == 'repeat-x'  ? 'selected="selected"' : '') .'>horizontally only</option>
						<option value="repeat-y" '.  ($mandigo_options['background_pattern_repeat'] == 'repeat-y'  ? 'selected="selected"' : '') .'>vertically only</option>
						<option value="no-repeat" '. ($mandigo_options['background_pattern_repeat'] == 'no-repeat' ? 'selected="selected"' : '') .'>do not repeat</option>
					</select>
				</td>
			</tr>
			<tr>
				<td align="right">Position :</td>
				<td>
					<input type="text" name="background_pattern_position" value="'. mandigo_escape($mandigo_options['background_pattern_position']) .'" /> <a href="http://www.w3.org/TR/CSS21/colors.html#propdef-background-position" target="_blank">help</a>
				</td>
			</tr>
		</table>

		<label>Colors</label>
		<table>
			<tr>
				<td align="right" width="180">Posts background color :</td>
				<td><input type="text" name="color_post_background" id="color_post_background" class="colorpicker" value="'. $mandigo_options['color_post_background'] .'" /> <a href="#" onclick="defaultColor(\'color_post_background\', \'#FAFAFA\'); return false;">restore default</a></td>
			</tr>
			<tr>
				<td align="right">Posts border color :</td>
				<td><input type="text" name="color_post_border" id="color_post_border" class="colorpicker" value="'. $mandigo_options['color_post_border'] .'" /> <a href="#" onclick="defaultColor(\'color_post_border\', \'#EEEEEE\'); return false;">restore default</a></td>
			</tr>
			<tr>
				<td align="right">Sidebars background color :</td>
				<td><input type="text" name="color_sidebar_background" id="color_sidebar_background" class="colorpicker" value="'. $mandigo_options['color_sidebar_background'] .'" /> <a href="#" onclick="defaultColor(\'color_sidebar_background\', \'#EEEEEE\'); return false;">restore default</a></td>
			</tr>
			<tr>
				<td align="right">Sidebars border color :</td>
				<td><input type="text" name="color_sidebar_border" id="color_sidebar_border" class="colorpicker" value="'. $mandigo_options['color_sidebar_border'] .'" /> <a href="#" onclick="defaultColor(\'color_sidebar_border\', \'#DDDDDD\'); return false;">restore default</a></td>
			</tr>
		</table>
		</fieldset>

		
		
		<fieldset class="options" id="layout_opts">
		<legend>Layout Options</legend>
		<input type="checkbox" name="layout_width_1024" '. ($mandigo_options['layout_width'] == 1024 ? 'checked="checked"' : '') .' /> Use the 1024px theme look instead of the default 800px one<br />
		<input type="checkbox" name="sidebar_always_show" '. ($mandigo_options['sidebar_always_show'] ? 'checked="checked"' : '') .' /> Show sidebars even in single post view<br />

		Columns: <select name="sidebar_count">
				<option value="0" '.  ($mandigo_options['sidebar_count'] == 0 ? 'selected="selected"' : '') .'>1 column (no sidebar at all)</option>
				<option value="1" '.  ($mandigo_options['sidebar_count'] == 1 ? 'selected="selected"' : '') .'>2 columns (1 sidebar, default)</option>
				<option value="2" '.  ($mandigo_options['sidebar_count'] == 2 ? 'selected="selected"' : '') .'>3 columns (2 sidebars, 1024px must be selected)</option>
		</select>

		<label>Sidebars position</label>
		<table border="0">
			<tr>
				<td align="right">First sidebar :</td>
				<td>
					<input type="radio" name="sidebar_1_position" value="left" '.  ($mandigo_options['sidebar_1_position'] == 'left' ? 'checked="checked"' : '') .' />left &nbsp; 
					<input type="radio" name="sidebar_1_position" value="right" '. ($mandigo_options['sidebar_1_position'] != 'left' ? 'checked="checked"' : '') .' />right
				</td>
			</tr>
			<tr>
				<td align="right">Second sidebar :</td>
				<td>
					<input type="radio" name="sidebar_2_position" value="left" '.  ($mandigo_options['sidebar_2_position'] == 'left' ? 'checked="checked"' : '') .' />left &nbsp; 
					<input type="radio" name="sidebar_2_position" value="right" '. ($mandigo_options['sidebar_2_position'] != 'left' ? 'checked="checked"' : '') .' />right
				</td>
			</tr>
		</table>
		

		<label>Sidebars width</label>
		<table border="0">
			<tr>
				<td align="right">First sidebar :</td>
				<td>
					<input type="text" name="sidebar_1_width" id="sidebar_1_width" value="'.  $mandigo_options['sidebar_1_width'] .'" style="width: 4em" /> px <a href="#" onclick="jQuery(\'#sidebar_1_width\').attr(\'value\', 210); return false;">restore default</a>
				</td>
			</tr>
			<tr>
				<td align="right">Second sidebar :</td>
				<td>
					<input type="text" name="sidebar_2_width" id="sidebar_2_width" value="'.  $mandigo_options['sidebar_2_width'] .'" style="width: 4em" /> px <a href="#" onclick="jQuery(\'#sidebar_2_width\').attr(\'value\', 210); return false;">restore default</a>
				</td>
			</tr>
		</table>
		</fieldset>



		<fieldset class="options" id="header_opts">
		<legend>Header</legend>
		<input type="checkbox" name="header_clickable" '. ($mandigo_options['header_clickable'] ? 'checked="checked"' : '') .' /> Make the header clickable<br />
		<input type="checkbox" name="header_slim" '. ($mandigo_options['header_slim'] ? 'checked="checked"' : '') .' /> Use slim (100px smaller) headers<br />
		<input type="checkbox" name="header_random_image" '. ($mandigo_options['header_random_image'] ? 'checked="checked"' : '') .' /> Use random images from the user uploaded files or the images/headers/ subfolder<br />
		<cite>It is also possible to use a different image on each page (per-page header images). Please consult the <a href="themes.php?page=README">README page</a> for more information.</cite>

		<label>Blog Name &amp; Description</label>
		<input type="checkbox" name="header_blogname_smaller_font" '. ($mandigo_options['header_blogname_smaller_font'] ? 'checked="checked"' : '') .' /> Reduce the size font for the blog name (useful for looong titles)<br /> 
		<input type="checkbox" name="header_blogname_hide" '. ($mandigo_options['header_blogname_hide'] ? 'checked="checked"' : '') .' /> Do not display the blog name<br /> 
		<input type="checkbox" name="header_blogdesc_hide" '. ($mandigo_options['header_blogdesc_hide'] ? 'checked="checked"' : '') .' /> Do not display the tagline (blog description)<br />
		<input type="checkbox" name="header_blogname_shadow" '. ($mandigo_options['header_blogname_shadow'] ? 'checked="checked"' : '') .' /> Add a drop shadow to blog name and description<br /><br />

		Apply a black stroke to blog name and blog description for better readability on lighter header images:<br/><br/>
		<input type="radio" name="header_blogname_stroke" value="0"  '. ($mandigo_options['header_blogname_stroke'] ? '' : 'checked="checked"') .' /><img src="'. $dirs['www']['backend'] .'/images/options-blogname-stroke-off.jpg" alt="off" /> &nbsp; 
		<input type="radio" name="header_blogname_stroke" value="1"  '. ($mandigo_options['header_blogname_stroke'] ? 'checked="checked"' : '') .' /><img src="'. $dirs['www']['backend'] .'/images/options-blogname-stroke-on.jpg"  alt="on"  />

		<label>Navigation</label>
		<input type="checkbox" name="header_navigation_no_submenus" '. ($mandigo_options['header_navigation_no_submenus'] ? 'checked="checked"' : '') .' /> Disable submenus<br />
		Navigation position : <select name="header_navigation_position">
			<option value="left" '.   ($mandigo_options['header_navigation_position'] == 'left'   ? 'selected="selected"' : '') .'>left</option>
			<option value="center" '. ($mandigo_options['header_navigation_position'] == 'center' ? 'selected="selected"' : '') .'>center</option>
			<option value="right" '.  ($mandigo_options['header_navigation_position'] == 'right'  ? 'selected="selected"' : '') .'>right</option>
		</select><br />

		Submenu animation speed : appear <select name="header_navigation_speed_appear">
			<option value="slow" '.    ($mandigo_options['header_navigation_speed_appear'] == 'slow'    ? 'selected="selected"' : '') .'>slow</option>
			<option value="fast" '.    ($mandigo_options['header_navigation_speed_appear'] == 'fast'    ? 'selected="selected"' : '') .'>fast</option>
			<option value="instant" '. ($mandigo_options['header_navigation_speed_appear'] == 'instant' ? 'selected="selected"' : '') .'>instant</option>
		</select>,
		disappear <select name="header_navigation_speed_disappear">
			<option value="slow" '.    ($mandigo_options['header_navigation_speed_disappear'] == 'slow'    ? 'selected="selected"' : '') .'>slow</option>
			<option value="fast" '.    ($mandigo_options['header_navigation_speed_disappear'] == 'fast'    ? 'selected="selected"' : '') .'>fast</option>
			<option value="instant" '. ($mandigo_options['header_navigation_speed_disappear'] == 'instant' ? 'selected="selected"' : '') .'>instant</option>
		</select><br /><br />

		Apply a translucent black stripe to the header navigation for better readability on light backgrounds:<br/><br/>
		<input type="radio" name="header_navigation_stripe" value="0"  '. ($mandigo_options['header_navigation_stripe'] ? '' : 'checked="checked"') .' /><img src="'. $dirs['www']['backend'] .'/images/options-navigation-stripe-off.jpg" alt="off" /> &nbsp; 
		<input type="radio" name="header_navigation_stripe" value="1"  '. ($mandigo_options['header_navigation_stripe'] ? 'checked="checked"' : '') .' /><img src="'. $dirs['www']['backend'] .'/images/options-navigation-stripe-on.jpg"  alt="on"  />

		<label>Pages to Exclude from Header Navigation</label>
		<ul>
		'. $list_of_pages .'
		</ul>
		</fieldset>



		<fieldset class="options" id="posts_opts">
		<legend>Posts</legend>
		<input type="checkbox" name="drop_caps" '. ($mandigo_options['drop_caps'] ? 'checked="checked"' : '') .' /> Create drop caps<br />
		<input type="checkbox" name="collapse_posts" '. ($mandigo_options['collapse_posts'] ? 'checked="checked"' : '') .' /> Automatically collapse posts in archives & categories<br />
		<input type="checkbox" name="display_tags_after_content" '. ($mandigo_options['display_tags_after_content'] ? 'checked="checked"' : '') .' /> Display tags after the content instead of next to categories (WP2.3+)<br />
		<input type="checkbox" name="dont_justify" '. ($mandigo_options['dont_justify'] ? 'checked="checked"' : '') .' /> Align content to the left instead of using justify alignment<br />
		<input type="checkbox" name="emphasize_as_bold" '. ($mandigo_options['emphasize_as_bold'] ? 'checked="checked"' : '') .' /> Display &lt;em&gt; tags as bold
		
		<label>Font</label>
		Font family : <select name="font_family">
			<option value="sans-serif" '. ($mandigo_options['font_family'] == 'sans-serif' ? 'selected="selected"' : '') .'>sans-serif (default)</option>
			<option value="serif" '.      ($mandigo_options['font_family'] == 'serif'      ? 'selected="selected"' : '') .'>serif</option>
		</select><br />

		<label>Dates</label>
		Date Position: <select name="date_position">
			<option value="datestamp" '. ($mandigo_options['date_position'] == 'datestamp' ? 'selected="selected"' : '') .'>datestamp (default)</option>
			<option value="inline" '.    ($mandigo_options['date_position'] == 'inline'    ? 'selected="selected"' : '') .'>inline with post information</option>
			<option value="none" '.      ($mandigo_options['date_position'] == 'none'      ? 'selected="selected"' : '') .'>none</option>
		</select><br />
		
		Datestamp Format: <select name="date_format">
			<option value="dmY" '. ($mandigo_options['date_format'] == 'dmY' ? 'selected="selected"' : '') .'>dd/mm/yyyy</option>
			<option value="MdY" '. ($mandigo_options['date_format'] == 'MdY' ? 'selected="selected"' : '') .'>month/dd/yyyy</option>
		</select>
		
		<label>Images</label>
		<input type="checkbox" name="clear_all_paragraphs" '. ($mandigo_options['clear_all_paragraphs'] ? 'checked="checked"' : '') .' /> Clear all paragraphs (wraps text of one paragraph at most)<br />
		<input type="checkbox" name="no_text_wrapping" '. ($mandigo_options['no_text_wrapping'] ? 'checked="checked"' : '') .' /> Do not wrap text around images at all<br />
		<input type="checkbox" name="no_image_borders" '. ($mandigo_options['no_image_borders'] ? 'checked="checked"' : '') .' /> Display images without a border
		
		</fieldset>

		
		
		<fieldset class="options" id="comments_opts">
		<legend>Comments</legend>
		<input type="checkbox" name="comments_highlight_author" '. ($mandigo_options['comments_highlight_author'] ? 'checked="checked"' : '') .' /> Highlight comments made by the author of the current post<br />
		<input type="checkbox" name="comments_numbering" '. ($mandigo_options['comments_numbering'] ? 'checked="checked"' : '') .' /> Number comments<br />
		<input type="checkbox" name="comments_allow_markup" '. ($mandigo_options['comments_allow_markup']  ? 'checked="checked"' : '') .' /> Display allowed XHTML tags above the comment field<br />
		<input type="checkbox" name="comments_no_gravatars" '. ($mandigo_options['comments_no_gravatars']  ? 'checked="checked"' : '') .' /> Do not display gravatars<br />
		Display trackbacks: <select name="trackbacks_position">
				<option value="along" '.  ($mandigo_options['trackbacks_position'] == 'along' ? 'selected="selected"' : '') .'>along with comments, in chronological order</option>
				<option value="above" '.  ($mandigo_options['trackbacks_position'] == 'above' ? 'selected="selected"' : '') .'>above comments</option>
				<option value="below" '.  ($mandigo_options['trackbacks_position'] == 'below' ? 'selected="selected"' : '') .'>below comments</option>
				<option value="none"  '.  ($mandigo_options['trackbacks_position'] == 'none'  ? 'selected="selected"' : '') .'>do not display trackbacks at all</option>
		</select>
		</fieldset>


		
		<fieldset class="options" id="seo_opts">
		<legend>SEO Options</legend>

		<label>Custom &lt;title&gt; tags</label>
		Customize your title tag. Consult the <a href="themes.php?page=README">README page</a> for a list of available variables.
		<table>
			<tr>
				<td style="text-align: right;">Default (index.php):</td>
				<td><input type="text" name="title_scheme_index" size="60" value="'. mandigo_escape($mandigo_options['title_scheme_index']) .'" /></td>
			</tr>
			<tr>
				<td style="text-align: right;">Single posts (single.php):</td>
				<td><input type="text" name="title_scheme_single" size="60" value="'. mandigo_escape($mandigo_options['title_scheme_single']) .'" /></td>
			</tr>
			<tr>
				<td style="text-align: right;">Pages (page.php):</td>
				<td><input type="text" name="title_scheme_page" size="60" value="'. mandigo_escape($mandigo_options['title_scheme_page']) .'" /></td>
			</tr>
			<tr>
				<td style="text-align: right;">Category Archive (archive.php):</td>
				<td><input type="text" name="title_scheme_category" size="60" value="'. mandigo_escape($mandigo_options['title_scheme_category']) .'" /></td>
			</tr>
			<tr>
				<td style="text-align: right;">Date Archive (archive.php):</td>
				<td><input type="text" name="title_scheme_date" size="60" value="'. mandigo_escape($mandigo_options['title_scheme_date']) .'" /></td>
			</tr>
			<tr>
				<td style="text-align: right;">Search Results (search.php):</td>
				<td><input type="text" name="title_scheme_search" size="60" value="'. mandigo_escape($mandigo_options['title_scheme_search']) .'" /></td>
			</tr>
		</table>

		<label>Custom header levels</label>
		Customize which tags you want to use for the blog name, blog description, posts title, ... This does not affect styles.
		<table>
			<tr>
				<td style="text-align: right;">Blog name:</td>
				<td>
					<select name="heading_level_blogname">
						<option value="h1"'.  ($mandigo_options['heading_level_blogname'] == 'h1'  ? ' selected="selected"' : '') .'>h1</option>
						<option value="h2"'.  ($mandigo_options['heading_level_blogname'] == 'h2'  ? ' selected="selected"' : '') .'>h2</option>
						<option value="h3"'.  ($mandigo_options['heading_level_blogname'] == 'h3'  ? ' selected="selected"' : '') .'>h3</option>
						<option value="h4"'.  ($mandigo_options['heading_level_blogname'] == 'h4'  ? ' selected="selected"' : '') .'>h4</option>
						<option value="h5"'.  ($mandigo_options['heading_level_blogname'] == 'h5'  ? ' selected="selected"' : '') .'>h5</option>
						<option value="h6"'.  ($mandigo_options['heading_level_blogname'] == 'h6'  ? ' selected="selected"' : '') .'>h6</option>
						<option value="div"'. ($mandigo_options['heading_level_blogname'] == 'div' ? ' selected="selected"' : '') .'>div</option>
					</select>
				</td>
			</tr>
			<tr>
				<td style="text-align: right;">Blog description (tagline):</td>
				<td>
					<select name="heading_level_blogdesc">
						<option value="h1"'.  ($mandigo_options['heading_level_blogdesc'] == 'h1'  ? ' selected="selected"' : '') .'>h1</option>
						<option value="h2"'.  ($mandigo_options['heading_level_blogdesc'] == 'h2'  ? ' selected="selected"' : '') .'>h2</option>
						<option value="h3"'.  ($mandigo_options['heading_level_blogdesc'] == 'h3'  ? ' selected="selected"' : '') .'>h3</option>
						<option value="h4"'.  ($mandigo_options['heading_level_blogdesc'] == 'h4'  ? ' selected="selected"' : '') .'>h4</option>
						<option value="h5"'.  ($mandigo_options['heading_level_blogdesc'] == 'h5'  ? ' selected="selected"' : '') .'>h5</option>
						<option value="h6"'.  ($mandigo_options['heading_level_blogdesc'] == 'h6'  ? ' selected="selected"' : '') .'>h6</option>
						<option value="div"'. ($mandigo_options['heading_level_blogdesc'] == 'div' ? ' selected="selected"' : '') .'>div</option>
					</select>
				</td>
			</tr>
			<tr>
				<td style="text-align: right;">Post title (when showing multiple posts):</td>
				<td>
					<select name="heading_level_post_title_multi">
						<option value="h1"'.  ($mandigo_options['heading_level_post_title_multi'] == 'h1'  ? ' selected="selected"' : '') .'>h1</option>
						<option value="h2"'.  ($mandigo_options['heading_level_post_title_multi'] == 'h2'  ? ' selected="selected"' : '') .'>h2</option>
						<option value="h3"'.  ($mandigo_options['heading_level_post_title_multi'] == 'h3'  ? ' selected="selected"' : '') .'>h3</option>
						<option value="h4"'.  ($mandigo_options['heading_level_post_title_multi'] == 'h4'  ? ' selected="selected"' : '') .'>h4</option>
						<option value="h5"'.  ($mandigo_options['heading_level_post_title_multi'] == 'h5'  ? ' selected="selected"' : '') .'>h5</option>
						<option value="h6"'.  ($mandigo_options['heading_level_post_title_multi'] == 'h6'  ? ' selected="selected"' : '') .'>h6</option>
						<option value="div"'. ($mandigo_options['heading_level_post_title_multi'] == 'div' ? ' selected="selected"' : '') .'>div</option>
					</select>
				</td>
			</tr>
			<tr>
				<td style="text-align: right;">Post title (single post view):</td>
				<td>
					<select name="heading_level_post_title_single">
						<option value="h1"'.  ($mandigo_options['heading_level_post_title_single'] == 'h1'  ? ' selected="selected"' : '') .'>h1</option>
						<option value="h2"'.  ($mandigo_options['heading_level_post_title_single'] == 'h2'  ? ' selected="selected"' : '') .'>h2</option>
						<option value="h3"'.  ($mandigo_options['heading_level_post_title_single'] == 'h3'  ? ' selected="selected"' : '') .'>h3</option>
						<option value="h4"'.  ($mandigo_options['heading_level_post_title_single'] == 'h4'  ? ' selected="selected"' : '') .'>h4</option>
						<option value="h5"'.  ($mandigo_options['heading_level_post_title_single'] == 'h5'  ? ' selected="selected"' : '') .'>h5</option>
						<option value="h6"'.  ($mandigo_options['heading_level_post_title_single'] == 'h6'  ? ' selected="selected"' : '') .'>h6</option>
						<option value="div"'. ($mandigo_options['heading_level_post_title_single'] == 'div' ? ' selected="selected"' : '') .'>div</option>
					</select>
				</td>
			</tr>
			<tr>
				<td style="text-align: right;">Page title (\'Archives\', \'Search Results\'):</td>
				<td>
					<select name="heading_level_page_title">
						<option value="h1"'.  ($mandigo_options['heading_level_page_title'] == 'h1'  ? ' selected="selected"' : '') .'>h1</option>
						<option value="h2"'.  ($mandigo_options['heading_level_page_title'] == 'h2'  ? ' selected="selected"' : '') .'>h2</option>
						<option value="h3"'.  ($mandigo_options['heading_level_page_title'] == 'h3'  ? ' selected="selected"' : '') .'>h3</option>
						<option value="h4"'.  ($mandigo_options['heading_level_page_title'] == 'h4'  ? ' selected="selected"' : '') .'>h4</option>
						<option value="h5"'.  ($mandigo_options['heading_level_page_title'] == 'h5'  ? ' selected="selected"' : '') .'>h5</option>
						<option value="h6"'.  ($mandigo_options['heading_level_page_title'] == 'h6'  ? ' selected="selected"' : '') .'>h6</option>
						<option value="div"'. ($mandigo_options['heading_level_page_title'] == 'div' ? ' selected="selected"' : '') .'>div</option>
					</select>
				</td>
			</tr>
			<tr>
				<td style="text-align: right;">Widget title:</td>
				<td>
					<select name="heading_level_widget_title">
						<option value="h1"'.  ($mandigo_options['heading_level_widget_title'] == 'h1'  ? ' selected="selected"' : '') .'>h1</option>
						<option value="h2"'.  ($mandigo_options['heading_level_widget_title'] == 'h2'  ? ' selected="selected"' : '') .'>h2</option>
						<option value="h3"'.  ($mandigo_options['heading_level_widget_title'] == 'h3'  ? ' selected="selected"' : '') .'>h3</option>
						<option value="h4"'.  ($mandigo_options['heading_level_widget_title'] == 'h4'  ? ' selected="selected"' : '') .'>h4</option>
						<option value="h5"'.  ($mandigo_options['heading_level_widget_title'] == 'h5'  ? ' selected="selected"' : '') .'>h5</option>
						<option value="h6"'.  ($mandigo_options['heading_level_widget_title'] == 'h6'  ? ' selected="selected"' : '') .'>h6</option>
						<option value="div"'. ($mandigo_options['heading_level_widget_title'] == 'div' ? ' selected="selected"' : '') .'>div</option>
					</select>
				</td>
			</tr>
		</table>
		</fieldset>

		
		
		<fieldset class="options" id="layout_fixes">
		<legend>Layout Fixes</legend>
		If some of the theme functionnalities (random headers/schemes, custom headers) doesn\'t seem to be working, it could be due to the fact that CSS rules in the header have been cached:<br />
		<input type="checkbox" name="fully_dynamic_stylesheet" '. ($mandigo_options['fully_dynamic_stylesheet'] ? 'checked="checked"' : '') .' /> Use the legacy fully-dynamic stylesheet to defeat caching of CSS rules<br />
		<br />
		You may want to experiment with these settings if you encounter problems with the columns showing up wider than they normally should:<br />
		<input type="checkbox" name="fixes_whitespace_pre" '. ($mandigo_options['fixes_whitespace_pre'] ? 'checked="checked"' : '') .' /> Fix elements which use a "white-space: pre" style (prevents lines from being wrapped in IE)<br />
		<input type="checkbox" name="fixes_comments_1" '. ($mandigo_options['fixes_comments_1'] ? 'checked="checked"' : '') .' /> Split long urls in users comments at slashes (inserts linebreaks at /\'s)<br />
		<input type="checkbox" name="fixes_comments_2" '. ($mandigo_options['fixes_comments_2'] ? 'checked="checked"' : '') .' /> Replace long urls in users comments with "link"<br />
		<input type="checkbox" name="fixes_touch_content" '. ($mandigo_options['fixes_touch_content'] ? 'checked="checked"' : '') .' /> Force the browser to re-render the content column<br />
		</fieldset>



		<fieldset class="options" id="misc_opts">
		<legend>Miscellaneous Options</legend>

		<label>Pages</label>
		<input type="checkbox" name="no_comments_on_pages" '. ($mandigo_options['no_comments_on_pages'] ? 'checked="checked"' : '') .' /> Disallow comments on pages

		<label>Animations</label>
		<input type="checkbox" name="disable_animations" '. ($mandigo_options['disable_animations'] ? 'checked="checked"' : '') .' /> Disable js animations (also removes show/hide buttons in posts)

		<label>Readability</label>
		<input type="checkbox" name="bold_links" '. ($mandigo_options['bold_links'] ? 'checked="checked"' : '') .' /> Display all links in bold for better readability

		<label>Really miscellaneous options</label>
		<input type="checkbox" name="full_search_results" '. ($mandigo_options['full_search_results'] ? 'checked="checked"' : '') .' /> Display full search results, not just titles and metadata<br />
		<input type="checkbox" name="footer_statistics" '. ($mandigo_options['footer_statistics'] ? 'checked="checked"' : '') .' /> Display rendering time and SQL statistics in the footer<br />
		</fieldset>

		<fieldset class="options" id="donate">
		<legend>Support</legend>
		We have spent countless hours working on these themes, and we really appreciate any and all contributions that we receive to help our contributed efforts. If you enjoy Mandigo and you are the position to make a donation, we would be very grateful!
		<p><a href="http://www.onehertz.com/portfolio/wordpress/donate/" target="_blank"><img src="http://www.onehertz.com/img/paypal-logo.gif" alt="Make a donation" /></a>
		</fieldset>

		<span class="submit"><input type="submit" name="Submit" value="'.__('Update Options &raquo;').'"/></span>
		
		</form>

		</div>

		
		
		<div id="versioncheck" class="wrap">
		<h2>Version Checker</h2>
		<iframe src="http://www.onehertz.com/cgi-bin/wordpress:versioncheck.pl?theme=Mandigo&amp;version='. trim($mandigo_version) .'" width="100%" height="90" scrolling="auto" frameborder="0"></iframe>
		</div>
		
		
		<div id="preview" class="wrap">
		<h2 id="preview-post">Preview (updated when options are saved)</h2>
		<iframe src="../?preview=true" width="100%" height="600" ></iframe>
		</div>
		<script type="text/javascript">
			jQuery(document).ready(function() { jQuery("body").addClass("mandigo-options"); });
		</script>
		';
	} // end of mandigo_options_page()

?>
