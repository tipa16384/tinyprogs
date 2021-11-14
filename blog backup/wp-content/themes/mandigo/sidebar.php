<?php 
	// this file defines the default sidebar
	// if you are using widgets, you do not need to edit this file

	global $mandigo_options;

	// heading level for widget title (h1, h2, div, ...)
	$tag_widget = $mandigo_options['heading_level_widget_title'];
?>
	<td id="sidebar1">
		<ul class="sidebars">
<?php
	// if wp doesn't support sidebars, or if we are not using any widget in sidebar 1
	if (!function_exists('dynamic_sidebar') || !dynamic_sidebar('Sidebar 1')) {

		// our search widget, defined in functions.php
		widget_mandigo_search();
		
		// our calendar widget, defined in functions.php
		widget_mandigo_calendar();



		// if we are browsing a category archive
		if (is_category()) {
			$what_youre_doing = sprintf(
				__('You are currently browsing the archives for the \'%s\' category.', 'mandigo'),
				single_cat_title('', false)
			);
		}

		// if wp supports tags and this is a tag archive
		elseif (function_exists(is_tag) && is_tag()) {
			$what_youre_doing = sprintf(
				__('You are currently browsing the %s weblog archives for posts tagged \'%s\'.', 'mandigo'),
				sprintf(
					'<a href="%s/">%s</a>',
					get_bloginfo('home'),
					get_bloginfo('name')
				),
				single_tag_title('', false)
			);
		}
		
		
		// if this is a daily archive
		elseif (is_day()) {
			$what_youre_doing = sprintf(
				__('You are currently browsing the %s weblog archives for the day %s.', 'mandigo'),
				sprintf(
					'<a href="%s/">%s</a>',
					get_bloginfo('home'),
					get_bloginfo('name')
				),
				get_the_time(__('l, F jS, Y', 'mandigo'))
			);
		}
		
		
		// if this is a monthly archive
		elseif (is_month()) {
			$what_youre_doing = sprintf(
				__('You are currently browsing the %s weblog archives for %s.', 'mandigo'),
				sprintf(
					'<a href="%s/">%s</a>',
					get_bloginfo('home'),
					get_bloginfo('name')
				),
				get_the_time(__('F, Y', 'mandigo'))
			);
		}
		
		
		// if this is a yearly archive
		elseif (is_year()) {
			$what_youre_doing = sprintf(
				__('You are currently browsing the %s weblog archives for the year %s.', 'mandigo'),
				sprintf(
					'<a href="%s/">%s</a>',
					get_bloginfo('home'),
					get_bloginfo('name')
				),
				get_the_time('Y')
			);
		}
		
		
		// if this is a search result
		elseif (is_search()) {
			$what_youre_doing = sprintf(
				__('You have searched the %s weblog archives for %s. If you are unable to find anything in these search results, you can try one of these links.', 'mandigo'),
				sprintf(
					'<a href="%s/">%s</a>',
					get_bloginfo('home'),
					get_bloginfo('name')
				),
				'<strong>\''. wp_specialchars($s) .'\'</strong>'
			);
		}
		
		
		// otherwise, not sure when this is triggered
		elseif (isset($_GET['paged']) && !empty($_GET['paged'])) {
			$what_youre_doing = sprintf(
				__('You are currently browsing the %s weblog archives.', 'mandigo'),
				sprintf(
					'<a href="%s/">%s</a>',
					get_bloginfo('home'),
					get_bloginfo('name')
				)
			);
		}

		// make sure the variable has been set
		if ($what_youre_doing) {
?>
			<li><?php echo $what_youre_doing; ?></li>
<?php
		}
		
		
		// the list of pages
		wp_list_pages(
			array(
				'sort_column' => 'menu_order',
				'title_li'    => sprintf(
					'<%s class="widgettitle">%s</%s>',
					$tag_widget,
					str_replace('&', '%26', __('Pages', 'mandigo')),
					$tag_widget
				),
			)
		);
?>

			<li><<?php echo $tag_widget; ?> class="widgettitle"><?php _e('Categories', 'mandigo'); ?></<?php echo $tag_widget; ?>>
				<ul>
<?php
		// the list of categories
		wp_list_cats(
			array(
				'sort_column'  => 'name',
				'optioncount'  => 1,
				'hide_empty'   => 0,
				'hierarchical' => 1,
			)
		);
?>
				</ul>
			</li>

<?php
		// if wordpress supports tags
		if (function_exists('wp_tag_cloud')) {
?>
			<li><<?php echo $tag_widget; ?> class="widgettitle"><?php _e('Tags', 'mandigo'); ?></<?php echo $tag_widget; ?>>
				<?php wp_tag_cloud(); ?>
			</li>
<?php
		}

		// if this is the frontpage 
		if (is_home() || is_page()) {
			// put the blogroll
			get_links_list();
		}
		
		// our meta widget, defined in functions.php
		widget_mandigo_meta();
	}
?>
		</ul>
	</td>
