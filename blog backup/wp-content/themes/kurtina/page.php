<?php get_header(); ?>
<div class="body_box">

<div class="body_left">

<!-- BLOG FORMAT -->
<?php if (have_posts()) : while (have_posts()) : the_post(); ?>
<div class="pagebody" id="post-<?php the_ID(); ?>">
<h1><?php the_title(); ?></h1>

<?php the_content('<p class="serif">Read the rest of this page &raquo;</p>'); ?>
<?php link_pages('<p><strong>Pages:</strong> ', '</p>', 'number'); ?>

</div>

<!-- BLOG FORMAT END -->	
<?php endwhile; endif; ?>  
<?php edit_post_link('Edit this entry.', '<p>', '</p>'); ?>


</div>
<?php get_sidebar(); ?>
