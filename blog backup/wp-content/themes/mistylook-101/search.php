<?php get_header();?>
<div id="content">
<div id="content-main">
<?php if (have_posts()) : ?>
		<?php $post = $posts[0]; // Hack. Set $post so that the_date() works. ?>
    
		<h2 class="pagetitle">Search Results for <?php echo "'".$s."'";?></h2>
		<?php while (have_posts()) : the_post(); ?>
				
			<div class="post" id="post-<?php the_ID(); ?>">
				<div class="posttitle">
					<h2><a href="<?php the_permalink() ?>" rel="bookmark" title="Permanent Link to <?php the_title(); ?>"><?php the_title(); ?></a></h2>
					<p class="post-info">
            Posted in <?php the_category(', ') ?>  on <?php the_time('F jS, Y') ?> <?php edit_post_link('Edit', '', ' | '); ?> <?php comments_popup_link('No Comments &#187;', '1 Comment &#187;', '% Comments &#187;'); ?> </p>
				</div>
				
				<div class="entry">
					<?php the_excerpt(); ?>
				</div>
				<?php comments_template(); ?>
			</div>
	
		<?php endwhile; ?>

		<p align="center"><?php posts_nav_link(' - ','&#171; Prev','Next &#187;') ?></p>
		
	<?php else : ?>

		<h2 class="center">Not Found</h2>
		<p class="center">Sorry, but you are looking for something that isn't here.</p>
	<?php endif; ?>
</div><!-- end id:content-main -->
<?php get_sidebar();?>
<?php get_footer();?>