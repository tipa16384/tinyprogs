<?php get_header(); ?>

	<div id="content">
    <?php if (have_posts()) : while (have_posts()) : the_post(); ?>
		<div class="post" id="post-<?php the_ID(); ?>">
		<h2><?php the_title(); ?></h2>
			<div class="entry">
				<?php the_content('<p>Continue reading &raquo;</p>'); ?>
	
				<?php //if page is split into more than one
					link_pages('<p>Pages: ', '</p>', 'number'); ?>
			</div>
		</div>
	  <?php endwhile; endif; ?>
	<?php edit_post_link('Edit', '<p>', '</p>'); ?>
</div>

<?php include(TEMPLATEPATH."/left.php");?>
<?php include(TEMPLATEPATH."/right.php");?>

<?php get_footer(); ?>