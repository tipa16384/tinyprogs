<?php
	global $mandigo_options, $dirs;

	get_header();

	// heading level for page title (h1, h2, div, ...)
	$tag_post_title_single = $mandigo_options['heading_level_post_title_single'];
?>
	<td id="content" class="<?php echo ($mandigo_options['sidebar_always_show'] ? 'narrow' : 'wide'); ?>column"<?php if (mandigo_sidebox_conditions($single = true)) { ?> rowspan="2"<?php } ?>>

<?php
	// if we have posts
	if (have_posts()) {
		// main loop
		while (have_posts()) {
			the_post();
?>

		<div class="post" id="post-<?php the_ID(); ?>">
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
		<<?php echo $tag_post_title_single; ?> class="posttitle"><?php the_title(); ?></<?php echo $tag_post_title_single; ?>>
			<div class="entry">
<?php
			// the content itself!
			the_content(__('Read the rest of this entry', 'mandigo') .' &raquo;');

			link_pages(
				'<p><strong>'. __('Pages', 'mandigo') .':</strong> ',
				'</p>',
				'number'
			);
?>
				<div class="clear"></div>
			</div>
		</div>
<?php
			// the "edit page" link
			edit_post_link(
				__('Edit this entry.', 'mandigo'),
				'',
				''
			);
		}
	}

	// include the comments template, unless they're disallowed on pages
	if (!$mandigo_options['no_comments_on_pages'])
		comments_template();
?>

	</td>

<?php
	// if we have at least one sidebar to display
	if ($mandigo_options['sidebar_always_show'] && $mandigo_options['sidebar_count']) {
		if (mandigo_sidebox_conditions($single = true))
			include (TEMPLATEPATH . '/sidebox.php');
	
		include (TEMPLATEPATH . '/sidebar.php');

		// if this is a 3-column layout
		if ($mandigo_options['layout_width'] == 1024 && $mandigo_options['sidebar_count'] == 2)
			include (TEMPLATEPATH . '/sidebar2.php');
	}

	get_footer();
?>
