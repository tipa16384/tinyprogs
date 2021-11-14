<?php
	global $mandigo_options, $dirs;

	get_header();

	// heading levels for posts (h1, h2, div, ...)
	$tag_post_title_multi = $mandigo_options['heading_level_post_title_multi'];
	$tag_page_title       = $mandigo_options['heading_level_page_title'      ];

	// get sidebar keys
	global $wp_registered_sidebars;
	if ($wp_registered_sidebars) {
		foreach ($wp_registered_sidebars as $key => $value) {
			if ($value['name'] == 'Mandigo Top')
				$index_mandigo_top    = $key;
				
			if ($value['name'] == 'Mandigo Bottom')
				$index_mandigo_bottom = $key;
		}
	}

	// make sure our version of wordpress supports widgets
	if (function_exists('wp_get_sidebars_widgets') && function_exists('dynamic_sidebar'))
		$sidebars_widgets = wp_get_sidebars_widgets();

?>
	<td id="content" class="narrowcolumn"<?php if (mandigo_sidebox_conditions()) { ?> rowspan="2"<?php } ?>>
<?php
	// if we have widgets in the 'Mandigo Top' sidebar
	if ($sidebars_widgets[$index_mandigo_top]) {
?>

		<ul class="inline-widgets">
			<?php dynamic_sidebar('Mandigo Top'); ?>
		</ul>

<?php
	}
	
	// if we have posts
	if (have_posts()) {
		// main loop
		while (have_posts()) {
			the_post();
?>

		<div class="post" id="post-<?php the_ID(); ?>">
			<div class="postinfo">
				<?php mandigo_date_stamp(get_the_time('Y|M|m|d')); ?>
<?php
			// unless we disabled animations, display the buttons
			if (!$mandigo_options['disable_animations']) {
?>
				<span class="switch-post">
					<a href="javascript:toggleSidebars();" class="switch-sidebars"><img src="<?php echo $dirs['www']['icons']; ?>bullet_sidebars_hide.png" alt="" class="png" /></a><a href="javascript:togglePost(<?php the_ID(); ?>);" id="switch-post-<?php the_ID(); ?>"><img src="<?php echo $dirs['www']['icons']; ?>bullet_toggle_minus.png" alt="" class="png" /></a>
				</span>

<?php
			}
			
			// the post title
?>
				<<?php echo $tag_post_title_multi; ?> class="posttitle"><a href="<?php the_permalink() ?>" rel="bookmark" title="<?php printf(__('Permanent Link to %s', 'mandigo'), the_title('', '', false)); ?>"><?php the_title(); ?></a></<?php echo $tag_post_title_multi; ?>>
				<small>
<?php
			
			// post information
			if ($mandigo_options['date_position'] != 'inline') {
				printf(
					__('Posted by %s in %s', 'mandigo'),
					mandigo_author_link(get_the_author_ID(), get_the_author()),
					get_the_category_list(', ')
				);
			}
			else {
				printf(
					__('Posted on %s by %s in %s', 'mandigo'),
					get_the_time(__('F jS, Y', 'mandigo')),
					mandigo_author_link(get_the_author_ID(), get_the_author()),
					get_the_category_list(', ')
				);
			}

			// if wp supports tags, and unless we chose to display tags after the post
			if (function_exists('the_tags') && !$mandigo_options['display_tags_after_content'])
				the_tags(', '. __('tags', 'mandigo') .': ');

			// the "edit post" link, which displays when you are logged in
			edit_post_link(
				__('Edit', 'mandigo'),
				sprintf(
					' - <img src="%simages/edit.gif" alt="%s" /> ',
					$dirs['www']['scheme'],
					__('Edit this post', 'mandigo')
				),
				''
			);
?>
				</small>

			</div>

			<div class="entry">
<?php
			// the content itself!
			if (function_exists('has_excerpt') && has_excerpt()) the_excerpt();
			else the_content(__('Read the rest of this entry', 'mandigo') .' &raquo;');

			// if wp supports tags, and if we chose to display tags after the post
			if (function_exists('the_tags') && $mandigo_options['display_tags_after_content'])
				the_tags();
?>
			</div>

			<p class="clear">
				<img src="<?php echo $dirs['www']['scheme']; ?>images/comments.gif" alt="Comments" />
<?php
			// comments link
			comments_popup_link(
				__('No Comments', 'mandigo'). ' &#187;',
				__('1 Comment',   'mandigo'). ' &#187;',
				__('% Comments',  'mandigo'). ' &#187;'
			);
?>
			</p>
		</div>

<?php
		} // end of main loop
?>

		<div class="navigation">
			<div class="alignleft"><?php next_posts_link('&laquo; '. __('Previous Entries', 'mandigo')) ?></div>
			<div class="alignright"><?php previous_posts_link(__('Next Entries', 'mandigo') .' &raquo;') ?></div>
		</div>

<?php
	}
	
	// if have_posts() was false
	else {
?>

		<<?php echo $tag_page_title; ?> class="center"><?php _e('Not Found', 'mandigo'); ?></<?php echo $tag_page_title; ?>>
		<p class="center"><?php _e("Sorry, but you are looking for something that isn't here.", 'mandigo'); ?></p>

<?php
	}

	// if we have widgets in the 'Mandigo Bottom' sidebar
	if ($sidebars_widgets[$index_mandigo_bottom]) {
?>

		<ul class="inline-widgets">
			<?php dynamic_sidebar('Mandigo Bottom'); ?>
		</ul>

<?php
	}
?>
	</td>

<?php
	// if we have at least one sidebar to display
	if ($mandigo_options['sidebar_count']) {
		if (mandigo_sidebox_conditions())
			include (TEMPLATEPATH . '/sidebox.php');
	
		include (TEMPLATEPATH . '/sidebar.php');

		// if this is a 3-column layout
		if ($mandigo_options['layout_width'] == 1024 && $mandigo_options['sidebar_count'] == 2)
			include (TEMPLATEPATH . '/sidebar2.php');
	}

	get_footer();
?>
