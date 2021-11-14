<?php
/*
Template Name: Links Template
*/

	global $mandigo_options, $dirs;

	get_header();

	// heading level for page title (h1, h2, div, ...)
	$tag_page_title = $mandigo_options['heading_level_page_title'];
?>
	<td id="content" class="<?php echo ($mandigo_options['sidebar_always_show'] ? 'narrow' : 'wide'); ?>column"<?php if (mandigo_sidebox_conditions($single = true)) { ?> rowspan="2"<?php } ?>>
		<div class="post">
<?php
	// unless we disabled animations, display the buttons
	if (!$mandigo_options['disable_animations']) {
?>
			<span class="switch-post">
				<a href="javascript:toggleSidebars();" class="switch-sidebars"><img src="<?php echo $dirs['www']['icons']; ?>bullet_sidebars_hide.png" alt="" class="png" /></a><a href="javascript:togglePost(<?php the_ID(); ?>);" id="switch-post-<?php the_ID(); ?>"><img src="<?php echo $dirs['www']['icons']; ?>bullet_toggle_minus.png" alt="" class="png" /></a>
			</span>

<?php
	}
?>

			<<?php echo $tag_page_title; ?> class="pagetitle"><?php the_title(); ?></<?php echo $tag_page_title; ?>>
			<ul>
				<?php get_links_list(); ?>
			</ul>

		</div>
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
