

<?php get_header(); ?>

	<div id="singlecontent">
	
	<?php if (have_posts()) : ?>
	<?php while (have_posts()) : the_post(); ?>
	
	<div class="post" id="post-<?php the_ID(); ?>">
   	<h2><a href="<?php the_permalink() ?>" rel="bookmark" title="Permanent Link to <?php the_title(); ?>"><?php the_title(); ?></a></h2>
		<div class="entrymeta"><p>Stamped: <?php the_time('F jS, Y') ?> <?php edit_post_link('e','',''); ?> | <a href="javascript:Effect.Combo('relatedposts', {duration: 0.8});" title="View similar posts">Toggle Similar</a><br />Tagged: <?php UTW_ShowTagsForCurrentPost("commalist") ?></p></div>

		<div class="entry">
		<div id="relatedposts" style="display: none;">
			<h3>Similarly tagged posts</h3>
			<ul class="utwrelposts"><?php UTW_ShowRelatedPostsForCurrentPost("posthtmllist") ?></ul>
		</div>
		<?php the_content('[...]'); ?>
		</div>
	
	</div>	
	
	<?php comments_template(); ?>
			
  	<?php endwhile; else: ?>
	
	<h2>The landscaper ran off with the nanny</h2>

<p>You seemed to have found a mislinked file, page, or search query with no results. If you feel you have reached this page in error, double check the URL and try again. If you still find yourself on this page and believe the site is at fault, it really isn't. Blame the landscaper. If you happen to find him, tell him the hedges need pruning.</p>

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