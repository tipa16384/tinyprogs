<?php 
	global $mandigo_options, $dirs;

	get_header();

	// heading levels for post/page title (h1, h2, div, ...)
	$tag_post_title_single = $mandigo_options['heading_level_post_title_single'];
	$tag_page_title        = $mandigo_options['heading_level_page_title'      ];
?>
	<td id="content" class="<?php echo ($mandigo_options['sidebar_always_show'] ? 'narrow' : 'wide'); ?>column"<?php if (mandigo_sidebox_conditions($single = true)) { ?> rowspan="2"<?php } ?>>

<?php
	// if we have posts
	if (have_posts()) {
		// main loop
		while (have_posts()) {
			the_post();
?>

		<div class="navigation">
			<div class="alignleft"><?php previous_post_link('&laquo;&nbsp;%link') ?></div>
			<div class="alignright"><?php next_post_link('%link&nbsp;&raquo;') ?></div>
		</div>

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
				<<?php echo $tag_post_title_single; ?> class="posttitle"><a href="<?php echo get_permalink() ?>" rel="bookmark" title="Permanent Link: <?php the_title(); ?>"><?php the_title(); ?></a></<?php echo $tag_post_title_single; ?>>
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
?>
				</small>

			</div>

			<div class="entry">
<?php
			// the content itself!
			the_content(__('Read the rest of this entry', 'mandigo') .' &raquo;');

			link_pages(
				'<p><strong>'. __('Pages', 'mandigo') .':</strong> ',
				'</p>',
				'number'
			);

			// if wp supports tags, and if we chose to display tags after the post
			if (function_exists('the_tags') && $mandigo_options['display_tags_after_content'])
				the_tags();
?>

				<p class="postmetadata alt clear">
					<small>
<?php
			printf(
				__('This entry was posted on %s at %s and is filed under %s.', 'mandigo') .' ',
				get_the_time(__('l, F jS, Y', 'mandigo')) .' ',
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
					__('You can <a href="#respond">leave a response</a>, or <a href="%s" rel="trackback">trackback</a> from your own site.', 'mandigo') .' ',
					trackback_url(false)
				);
			}
			
			// if only pings are open
			elseif ($post->comment_status != 'open' && $post->ping_status == 'open') {
				printf(
					__('Responses are currently closed, but you can <a href="%s" rel="trackback">trackback</a> from your own site.', 'mandigo') .' ',
					trackback_url(false)
				);
			}
			
			// if only comments are open
			elseif ($post->comment_status == 'open' && $post->ping_status != 'open') {
				_e('You can <a href="#respond">skip to the end</a> and leave a response. Pinging is currently not allowed.', 'mandigo') .' ';
			}

			// if neither comments or pings are open
			elseif ($post->comment_status != 'open' && $post->ping_status != 'open') {
				_e('Both comments and pings are currently closed.', 'mandigo') .' ';
			}

			// the "edit post" link
			edit_post_link(
				__('Edit this entry.', 'mandigo'),
				'',
				''
			);
?>

					</small>
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
		if (mandigo_sidebox_conditions())
			include (TEMPLATEPATH . '/sidebox.php');
	
		include (TEMPLATEPATH . '/sidebar.php');

		// if this is a 3-column layout
		if ($mandigo_options['layout_width'] == 1024 && $mandigo_options['sidebar_count'] == 2)
			include (TEMPLATEPATH . '/sidebar2.php');
	}

	get_footer();
?>
