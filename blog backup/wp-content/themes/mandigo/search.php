<?php 
	global $mandigo_options, $dirs;

	get_header();

	// heading levels for posts (h1, h2, div, ...)
	$tag_post_title_multi = $mandigo_options['heading_level_post_title_multi'];
	$tag_page_title       = $mandigo_options['heading_level_page_title'      ];
?>
	<td id="content" class="narrowcolumn"<?php if (mandigo_sidebox_conditions()) { ?> rowspan="2"<?php } ?>>

<?php
	if (have_posts()) {
?>

		<<?php echo $tag_page_title; ?> class="pagetitle"><?php _e('Search Results', 'mandigo'); ?></<?php echo $tag_page_title; ?>>

		<div class="navigation">
			<div class="alignleft"><?php next_posts_link('&laquo;&nbsp;'. __('Previous Entries', 'mandigo')) ?></div>
			<div class="alignright"><?php previous_posts_link(__('Next Entries', 'mandigo') .'&nbsp;&raquo;') ?></div>
		</div>

<?php
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
				<<?php echo $tag_post_title_multi; ?> class="posttitle posttitle-search"><a href="<?php the_permalink() ?>" rel="bookmark" title="<?php printf(__('Permanent Link to %s', 'mandigo'), the_title('', '', false)); ?>"><?php the_title(); ?></a></<?php echo $tag_post_title_multi; ?>>
				<small><?php the_time('l, F jS, Y') ?></small>

<?php
			// whether we display full search results or just titles
			if ($mandigo_options['full_search_results']) {
?>
				<div class="entry">
<?php
				// the content itself!
				if (function_exists('has_excerpt') && has_excerpt()) the_excerpt();
				else the_content(__('Read the rest of this entry', 'mandigo') .' &raquo;');
?>
				</div>
				<div class="clear"></div>

<?php
			}
?>
				<p class="postmetadata alt">
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
			
			echo ' | ';
			
			// if wp supports tags
			if (function_exists('the_tags'))
				the_tags(
					__('tags', 'mandigo') .': ',
					', ',
					' | '
				);
			
			// the "edit post" link, which displays when you are logged in
			edit_post_link(
				__('Edit', 'mandigo'), 
				'', 
				' | '
			);
			
			// link to comments
			comments_popup_link(
				__('No Comments', 'mandigo'). ' &#187;',
				__('1 Comment',   'mandigo'). ' &#187;',
				__('% Comments',  'mandigo'). ' &#187;'
			);
?>
				</p>
			</div>

<?php
		}
?>

		<div class="navigation">
			<div class="alignleft"><?php next_posts_link('&laquo;&nbsp;'. __('Previous Entries', 'mandigo')) ?></div>
			<div class="alignright"><?php previous_posts_link(__('Next Entries', 'mandigo') .'&nbsp;&raquo;') ?></div>
		</div>

<?php
	}
	
	// if have_posts() was false
	else {
?>

		<<?php echo $tag_page_title; ?> class="center"><?php _e('No posts found. Try a different search?', 'mandigo'); ?></<?php echo $tag_page_title; ?>>
		<p class="center"><?php _e('Sorry, no posts matched your search criteria. Please try and search again.', 'mandigo'); ?></p>

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
