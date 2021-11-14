<?php get_header();?>
<div id="content">
<div id="content-main">
		<?php if ($posts) {
				$AsideId = get_settings('mistylook_asideid');
				function stupid_hack($str)
				{
					return preg_replace('|</ul>\s*<ul class="asides">|', '', $str);
				}
				ob_start('stupid_hack');
				foreach($posts as $post)
				{
					start_wp();
				?>
				<?php if ( !in_category($AsideId) ) : ?>
				<div class="post" id="post-<?php the_ID(); ?>">
				<div class="posttitle">
					<h2><a href="<?php the_permalink() ?>" rel="bookmark" title="Permanent Link to <?php the_title(); ?>"><?php the_title(); ?></a></h2>
					<p class="post-info"><?php the_time('F jS, Y') ?> by <?php the_author_posts_link() ?> </p>
				</div>
				
				<div class="entry">
					<?php the_content('Continue Reading &raquo;'); ?>
					<?php wp_link_pages(); ?>
				</div>
		
				<p class="postmetadata">Posted in <?php the_category(', ') ?> | <?php edit_post_link('Edit', '', ' | '); ?>  <?php comments_popup_link('No Comments &#187;', '1 Comment &#187;', '% Comments &#187;'); ?></p>
				<?php comments_template(); ?>
			</div>
			<?php endif; // end if in category ?>
			<?php
				}
			}
			else
			{ ?>
				<h2 class="center">Not Found</h2>
				<p class="center">Sorry, but you are looking for something that isn't here.</p>
			<?php }
		?>
		<p align="center"><?php posts_nav_link(' - ','&#171; Prev','Next &#187;') ?></p>
</div><!-- end id:content-main -->
<?php get_sidebar();?>
<?php get_footer();?>
