<?php 
	global $mandigo_options, $dirs;

	get_header();

	// heading levels for attachment name (h1, h2, div, ...)
	$tag_page_title = $mandigo_options['heading_level_page_title'      ];
?>
	<td id="content" class="<?php echo ($mandigo_options['sidebar_always_show'] ? 'narrow' : 'wide'); ?>column"<?php if (mandigo_sidebox_conditions($single = true)) { ?> rowspan="2"<?php } ?>>

<?php
	// if we have posts
	if (have_posts()) {
		// main loop
		while (have_posts()) {
			the_post();

			$attachment_link = get_the_attachment_link(
				$post->ID,
				true,
				array(450, 800)
			); // This also populates the iconsize for the next line
			
			$_post = &get_post($post->ID);
			
			$classname = (
				$_post->iconsize[0] <= 128
				? 'small'
				: ''
			);
			$classname .= 'attachment';
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
	
			// the attachment name
?>
			<<?php echo $tag_page_title; ?> class="pagetitle"><a href="<?php echo get_permalink($post->post_parent); ?>" rel="attachment"><?php echo get_the_title($post->post_parent); ?></a> &raquo; <a href="<?php echo get_permalink() ?>" rel="bookmark" title="Permanent Link: <?php the_title(); ?>"><?php the_title(); ?></a></<?php echo $tag_page_title; ?>>

			<div class="entry">
				<p class="<?php echo $classname; ?>"><?php echo $attachment_link; ?><br /><?php echo basename($post->guid); ?></p>

<?php
			// the content itself!
			the_content(__('Read the rest of this entry', 'mandigo') .' &raquo;');

			link_pages(
				'<p><strong>'. __('Pages', 'mandigo') .':</strong> ',
				'</p>',
				'number'
			);
?>

				<p class="postmetadata alt">
					<small>
<?php
			printf(
				__('This entry was posted on %s at %s and is filed under %s.', 'mandigo') .' ',
				get_the_time(__('l, F jS, Y', 'mandigo')),
				get_the_time(),
				get_the_category_list(', ')
			);

			// link to rss feed
			printf(
				__('You can follow any responses to this entry through the %s feed.', 'mandigo') .' ',
				'<a href="'. comments_rss() .'">RSS 2.0</a>'
			);
			
			// if both comments and pings are open
			if ($post->comment_status == 'open' && $post->ping_status == 'open') {
				printf(
					__('You can <a href="#respond">leave a response</a>, or <a href="%s" rel="trackback">trackback</a> from your own site.', 'mandigo'),
					trackback_url(false)
				);
			}
			
			// if only pings are open
			elseif ($post->comment_status != 'open' && $post->ping_status == 'open') {
				printf(
					__('Responses are currently closed, but you can <a href="%s" rel="trackback">trackback</a> from your own site.', 'mandigo'),
					trackback_url(false)
				);
			}
			
			// if only comments are open
			elseif ($post->comment_status == 'open' && $post->ping_status != 'open') {
				_e('You can <a href="#respond">skip to the end</a> and leave a response. Pinging is currently not allowed.', 'mandigo');
			}

			// if neither comments or pings are open
			elseif ($post->comment_status != 'open' && $post->ping_status != 'open') {
				_e('Both comments and pings are currently closed.', 'mandigo');
			}

			// the "edit post" link
			edit_post_link(
				__('Edit this entry.', 'mandigo'),
				' ',
				''
			);
?>					</small>
				</p>
			</div>
		</div>

<?php
			// include the comments template
			comments_template();
		} // end of main loop
	}
	
	// if have_posts() was false
	else {
?>

		<<?php echo $tag_page_title; ?>><?php _e('Sorry, no posts matched your criteria.', 'mandigo'); ?></<?php echo $tag_page_title; ?>>

<?php
	}
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
