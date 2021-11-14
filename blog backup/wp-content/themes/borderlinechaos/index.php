<?php get_header(); ?>
<?php get_sidebar(); ?>
<div id="contentwrapper">
<div id="content">

<?php
if ($posts) {
foreach($posts as $post) { start_wp();
?>
<br />
<div class="post">
	 <a class="posttitle" href="<?php the_permalink() ?>" style="text-decoration:none;" rel="bookmark" title="Permanent Link: <?php the_title(); ?>"><?php the_title(); ?></a>
	<div class="cite"><?php the_time("l F dS Y") ?>, <?php the_time() ?> <?php edit_post_link(); ?><br />
<?php _e("Filed under:"); ?> <?php the_category(',') ?></div>
<div class="commentPos"><?php wp_link_pages(); ?><?php comments_popup_link(__(' Comments?'), __('1 Comment'), __('% Comments')); ?></div><br />
	
		<?php the_content(); ?>

	
	<br />
	


	<!--
	<?php trackback_rdf(); ?>
	-->

<?php comments_template(); // Get wp-comments.php template ?>
</div>
<?php } // closes printing entries with excluded cats ?>

<?php } else { ?>
<?php _e('Sorry, no posts matched your criteria.'); ?>
<?php } ?>

 <div class="right"><?php posts_nav_link('','','previous &raquo;') ?></div>
 <div class="left"><?php posts_nav_link('','&laquo; newer ','') ?></div>

<br /><br />

</div></div>

<?php get_footer(); ?>
