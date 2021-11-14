<?php
	function mandigo_upgrade($from, $to) {
		global $mandigo_options, $global;
		
		if (version_compare($from, '1.34') === -1)
			mandigo_upgrade_134($from);
		
		if (version_compare($from, '1.39') === -1)
			mandigo_upgrade_139($from);
		
		$mandigo_options['version'] = $to;
		
		update_option('mandigo_options', $mandigo_options);
	}



	// v1.34
	function mandigo_upgrade_134($from) {
		global $mandigo_options;
		
		// populate the new options array with current values
		$mandigo_options = array(
			'scheme'                          => get_option('mandigo_scheme'),
			'scheme_randomize'                => get_option('mandigo_scheme_random'),
			
			'header_navigation_position'      => get_option('mandigo_headnav_alignment'),
			'header_navigation_no_submenus'   => get_option('mandigo_no_submenus'),
			'header_navigation_exclude_pages' => explode(',', get_option('mandigo_exclude_pages')),
			'header_navigation_stripe'        => get_option('mandigo_headoverlay'),
			
			'background_color'                => get_option('mandigo_bgcolor'),
			'background_pattern_file'         => get_option('mandigo_wp'),
			'background_pattern_fixed'        => get_option('mandigo_wp_fixed'),
			'background_pattern_repeat'       => get_option('mandigo_wp_repeat'),
			'background_pattern_position'     => get_option('mandigo_wp_position'),
			
			'color_post_background'           => get_option('mandigo_posts_bgcolor'),
			'color_post_border'               => get_option('mandigo_posts_bdcolor'),
			'color_sidebar_background'        => get_option('mandigo_sidebars_bgcolor'),
			'color_sidebar_border'            => get_option('mandigo_sidebars_bdcolor'),
			
			'layout_width'                    => (get_option('mandigo_1024') ? 1024 : 800),
			'sidebar_count'                   => (get_option('mandigo_nosidebars') ? 0 : (get_option('mandigo_3columns') ? 2 : 1)),
			'sidebar_always_show'             => get_option('mandigo_always_show_sidebars'),
			'sidebar_1_position'              => (get_option('mandigo_sidebar1_left') ? 'left' : 'right'),
			'sidebar_2_position'              => (get_option('mandigo_sidebar2_left') ? 'left' : 'right'),
			
			'header_blogname_smaller_font'    => get_option('mandigo_small_title'),
			'header_blogname_shadow'          => get_option('mandigo_drop_shadow'),
			'header_blogname_stroke'          => get_option('mandigo_stroke'),
			'header_blogname_hide'            => get_option('mandigo_hide_blogname'),
			'header_blogdesc_hide'            => get_option('mandigo_hide_blogdesc'),
			'header_random_image'             => get_option('mandigo_headers_random'),
			'header_slim'                     => get_option('mandigo_slim_header'),
			
			'title_scheme_index'              => get_option('mandigo_title_scheme_index'),
			'title_scheme_single'             => get_option('mandigo_title_scheme_single'),
			'title_scheme_page'               => get_option('mandigo_title_scheme_page'),
			'title_scheme_category'           => get_option('mandigo_title_scheme_category'),
			'title_scheme_date'               => get_option('mandigo_title_scheme_date'),
			'title_scheme_search'             => get_option('mandigo_title_scheme_search'),
			
			'heading_level_blogname'          => get_option('mandigo_tag_blogname'),
			'heading_level_blogdesc'          => get_option('mandigo_tag_blogdesc'),
			'heading_level_post_title_multi'  => get_option('mandigo_tag_posttitle_multi'),
			'heading_level_post_title_single' => get_option('mandigo_tag_posttitle_single'),
			'heading_level_page_title'        => get_option('mandigo_tag_pagetitle'),
			'heading_level_widget_title'      => get_option('mandigo_tag_sidebar'),
			
			'bold_links'                      => get_option('mandigo_bold_links'),
			'no_text_wrapping'                => get_option('mandigo_nofloat'),
			'collapse_posts'                  => get_option('mandigo_collapse_posts'),
			'date_format'                     => get_option('mandigo_date_format'),
			'emphasize_as_bold'               => (get_option('mandigo_em_italics') ? true : false),
			'clear_all_paragraphs'            => get_option('mandigo_clear_all_paragraphs'),
			'no_image_borders'                => get_option('mandigo_noborder'),
			'dont_justify'                    => get_option('mandigo_nojustify'),
			'display_tags_after_content'      => get_option('mandigo_tags_after'),
			'disable_animations'              => get_option('mandigo_no_animations'),
			
			'comments_numbering'              => get_option('mandigo_number_comments'),
			'comments_highlight_author'       => get_option('mandigo_author_comments'),
			'comments_allow_markup'           => get_option('mandigo_xhtml_comments'),
			'comments_no_gravatars'           => get_option('mandigo_disable_comment_gravatars'),
			'trackbacks_position'             => get_option('mandigo_trackbacks'),
			
			'fixes_comments_1'                => get_option('mandigo_fixes_comments_1'),
			'fixes_comments_2'                => get_option('mandigo_fixes_comments_2'),
			'fixes_whitespace_pre'            => get_option('mandigo_fixes_whitespace_pre'),
			'fixes_touch_content'             => get_option('mandigo_fixes_touch_content'),
			
			'footer_statistics'               => get_option('mandigo_footer_stats'),
			'full_search_results'             => get_option('mandigo_full_search_results'),
		);
		
		// delete old options
		foreach (
			array(
				'mandigo_scheme',
				'mandigo_scheme_random',
				'mandigo_headnav_alignment',
				'mandigo_headnav_left',
				'mandigo_no_submenus',
				'mandigo_exclude_pages',
				'mandigo_headoverlay',
				'mandigo_bgcolor',
				'mandigo_wp',
				'mandigo_wp_fixed',
				'mandigo_wp_repeat',
				'mandigo_wp_position',
				'mandigo_posts_bgcolor',
				'mandigo_posts_bdcolor',
				'mandigo_sidebars_bgcolor',
				'mandigo_sidebars_bdcolor',
				'mandigo_1024',
				'mandigo_nosidebars',
				'mandigo_3columns',
				'mandigo_always_show_sidebars',
				'mandigo_sidebar1_left',
				'mandigo_sidebar2_left',
				'mandigo_small_title',
				'mandigo_stroke',
				'mandigo_drop_shadow',
				'mandigo_hide_blogname',
				'mandigo_hide_blogdesc',
				'mandigo_headers_random',
				'mandigo_slim_header',
				'mandigo_title_scheme_index',
				'mandigo_title_scheme_single',
				'mandigo_title_scheme_page',
				'mandigo_title_scheme_category',
				'mandigo_title_scheme_date',
				'mandigo_title_scheme_search',
				'mandigo_tag_blogname',
				'mandigo_tag_blogdesc',
				'mandigo_tag_posttitle_multi',
				'mandigo_tag_posttitle_single',
				'mandigo_tag_pagetitle',
				'mandigo_tag_sidebar',
				'mandigo_bold_links',
				'mandigo_nofloat',
				'mandigo_floatright',
				'mandigo_collapse_posts',
				'mandigo_date_format',
				'mandigo_em_italics',
				'mandigo_clear_all_paragraphs',
				'mandigo_noborder',
				'mandigo_nojustify',
				'mandigo_tags_after',
				'mandigo_no_animations',
				'mandigo_number_comments',
				'mandigo_author_comments',
				'mandigo_xhtml_comments',
				'mandigo_disable_comment_gravatars',
				'mandigo_trackbacks',
				'mandigo_fixes_comments_1',
				'mandigo_fixes_comments_2',
				'mandigo_fixes_whitespace_pre',
				'mandigo_fixes_touch_content',
				'mandigo_footer_stats',
				'mandigo_full_search_results',
			) as $old_option
		) {
			delete_option($old_option);
		}
		
		mandigo_upgrade_files_134();
	}
	function mandigo_upgrade_files_134() {
		// move files
		$files = array( // old => new
			'/options.css'                  => '/backend/css/options.css',
			'/farbtastic.css'               => '/backend/css/farbtastic.css',
			'/js/farbtastic.js'             => '/backend/js/farbtastic.js',
 			'/images/farbtastic_marker.png' => '/backend/images/farbtastic_marker.png',
 			'/images/farbtastic_mask.png'   => '/backend/images/farbtastic_mask.png',
 			'/images/farbtastic_wheel.png'  => '/backend/images/farbtastic_wheel.png',
 			'/option-headoverlay-on.jpg'    => '/backend/images/options-navigation-stripe-on.jpg',
 			'/option-headoverlay-off.jpg'   => '/backend/images/options-navigation-stripe-off.jpg',
 			'/option-stroke-on.jpg'         => '/backend/images/options-blogname-stroke-on.jpg',
 			'/option-stroke-off.jpg'        => '/backend/images/options-blogname-stroke-off.jpg',
 			'/images/attention_catcher.png' => '/backend/images/attention_catcher.png',
		);
		foreach ($files as $old => $new) {
			if (file_exists(TEMPLATEPATH . $old)) {
				if (file_exists(TEMPLATEPATH . $new))
					@unlink(TEMPLATEPATH . $old);
				else
					@rename(
						TEMPLATEPATH . $old,
						TEMPLATEPATH . $new
					);
			}
		}

		// delete files
		if (file_exists(TEMPLATEPATH .'/js/jquery.dimensions.js'))
			@unlink(TEMPLATEPATH .'/js/jquery.dimensions.js');

		// make sure files have been moved/deleted
		mandigo_post_upgrade_check_134();
	}


	function mandigo_post_upgrade_check_134() {
		$mandigo_actions = get_option('mandigo_actions');
		// if any of these files is still in the theme root directory, then something went wrong during the upgrade
		$errors = 0;
		foreach (
			array(
				'options.css',
				'/farbtastic.css',
				'/js/farbtastic.js',
				'/js/jquery.dimensions.js',
				'/images/farbtastic_marker.js',
				'/images/farbtastic_mask.js',
				'/images/farbtastic_wheel.js',
				'/option-headoverlay-on.jpg',
				'/option-headoverlay-off.jpg',
				'/option-stroke-on.jpg',
				'/option-stroke-off.jpg',
				'/images/attention_catcher.png',
			) as $file
		) {
			if (file_exists(TEMPLATEPATH .'/'. $file))
				$errors++;
		}
		$mandigo_actions['mandigo_upgrade_files_134'] = $errors;
		update_option('mandigo_actions', $mandigo_actions);
	}
	function mandigo_upgrade_files_134_error() {
		global $wpmu;
		if ($wpmu && !is_site_admin()) return;
		echo '
			<div class="error">
				<p style="float: right;"><small><a href="?page=Theme%20Options&amp;dismiss=mandigo_upgrade_files_134">Dismiss</a></small></p>
				<p>Mandigo has detected that some files had not been moved during the upgrade to version 1.34.</p>
				<p>Please <a href="http://wiki.onehertz.com/WordPress/Mandigo/Upgrading" target="_blank">check the upgrade notes</a> and make sure the theme directory is writable by the web server, then <a href="?page=Theme%20Options&amp;check=mandigo_upgrade_files_134">click here to recheck</a>.</p>
			</div>
		';
	}





	// v1.39
	function mandigo_upgrade_139($from) {
		global $mandigo_options;
		
		$mandigo_options['date_position'] = ($mandigo_options['no_datestamps'] ? 'none' : 'datestamp');
	}
?>
