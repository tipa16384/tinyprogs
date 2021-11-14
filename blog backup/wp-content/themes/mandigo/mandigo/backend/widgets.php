<?php
	require_once(dirname(__FILE__) .'/../functions.php');

	global $mandigo_options;
	
	$tag_widget_title = $mandigo_options['heading_level_widget_title'];
	
	// if wp supports widgets, register the sidebars
	if (function_exists('register_sidebar')) {
		// sidebar #1
		register_sidebar(
			array(
				'before_title' => "<$tag_widget_title class=\"widgettitle\">",
				'after_title'  => "</$tag_widget_title>\n",
			)
		);
		
		// sidebar #2
		register_sidebar(
			array(
				'before_title' => "<$tag_widget_title class=\"widgettitle\">",
				'after_title'  => "</$tag_widget_title>\n",
			)
		);

		// top sidebar
		register_sidebar(
			array(
				'before_title' => "<$tag_widget_title class=\"widgettitle\">",
				'after_title'  => "</$tag_widget_title>\n",
				'name'         => 'Mandigo Top',
			)
		);

		// bottom sidebar
		register_sidebar(
			array(
				'before_title' => "<$tag_widget_title class=\"widgettitle\">",
				'after_title'  => "</$tag_widget_title>\n",
				'name'         => 'Mandigo Bottom',
			)
		);
		
		// sidebox
		if (mandigo_sidebox_conditions()) {
			register_sidebar(
				array(
					'before_title' => "<$tag_widget_title class=\"widgettitle\">",
					'after_title'  => "</$tag_widget_title>\n",
					'name'         => 'Mandigo Sidebox',
				)
			);
		}

	}



	/* -------------------------------------------------
				  SEARCH WIDGET
	-------------------------------------------------- */
	// define the widget
	function widget_mandigo_search() {
		global $tag_widget_title;
?>
			<li><<?php echo $tag_widget_title; ?> class="widgettitle"><?php _e('Search','mandigo'); ?></<?php echo $tag_widget_title; ?>>
				<?php include(TEMPLATEPATH . '/searchform.php'); ?>
			</li>
<?php
	}
	
	// if wp supports widgets, register it (make it available)
	if (function_exists('register_sidebar_widget'))
		register_sidebar_widget('Search', 'widget_mandigo_search');





	/* -------------------------------------------------
					CALENDAR WIDGET
	-------------------------------------------------- */
	// define the widget
	function widget_mandigo_calendar() {
		global $tag_widget_title;
?>
			<li><<?php echo $tag_widget_title; ?> class="widgettitle">&nbsp;</<?php echo $tag_widget_title; ?>>
				<?php get_calendar(); ?>
			</li>
<?php
	}
	// if wp supports widgets, register it (make it available)
	if (function_exists('register_sidebar_widget'))
		register_sidebar_widget('Calendar', 'widget_mandigo_calendar');





	/* -------------------------------------------------
					   META WIDGET
	-------------------------------------------------- */
	// define the widget
	function widget_mandigo_meta() {
		global $dirs, $tag_widget_title, $wpmu;
		
		// if the meta widget was given a custom name, it will be fetched from this variable
		$options = get_option('widget_meta');
?>
				<li>
					<<?php echo $tag_widget_title; ?> class="widgettitle"><?php echo ($options['title'] ? $options['title'] : __('Meta','mandigo')); ?></<?php echo $tag_widget_title; ?>>

					<span id="rss">
						<a href="<?php bloginfo('rss2_url'); ?>" title="RSS feed for <?php bloginfo('name'); ?>"><img src="<?php echo $dirs['www']['scheme']; ?>images/rss_l.gif" alt="Entries (RSS)" id="rssicon" /></a>
					</span>

					<ul>
						<?php wp_register(); ?>
						<li><?php wp_loginout(); ?></li>
<?php


		// if this is WordPress MU
		if ($wpmu) {
?>
						<li><a href="http://mu.wordpress.org/" title="Powered by WordPress MU, state-of-the-art semantic personal publishing platform.">WordPress MU</a></li>
<?php
		}
		
		// if this is the regular WordPress
		else {
?>
						<li><a href="http://wordpress.org/" title="Powered by WordPress, state-of-the-art semantic personal publishing platform.">WordPress</a></li>
<?php
		}

?>
						<li><a href="http://www.onehertz.com/portfolio/wordpress/" title="More Free WordPress themes by the same author" target="_blank">Mandigo theme</a></li>
						<?php wp_meta(); ?>
					</ul>
				</li>
<?php
	}

	// if wp supports widgets, register it (make it available)
	if (function_exists('register_sidebar_widget'))
		register_sidebar_widget('Meta', 'widget_mandigo_meta');
?>
