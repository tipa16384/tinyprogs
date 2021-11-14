<?php get_header(); ?>

	<div id="content">
	
	<?php if (have_posts()) : ?>
	<?php while (have_posts()) : the_post(); ?>
	
	<div class="post" id="post-<?php the_ID(); ?>">
   	<h2><a href="<?php the_permalink() ?>" rel="bookmark" title="Permanent Link to <?php the_title(); ?>"><?php the_title(); ?></a></h2>

		<div class="entry">
		<?php the_content('Read More &raquo;'); ?>
		</div>
	
	</div>	
			
  	<?php endwhile; else: ?>

	<?php endif; ?>
	
	</div>
</div>

<div class="clear"></div>

<div id="footercontent">

	<div id="bottomwrap">
			
	<?php include (TEMPLATEPATH . "/bottom.php"); ?>
	<div class="clear"></div>
	</div>
</div>


<?php get_footer(); ?>