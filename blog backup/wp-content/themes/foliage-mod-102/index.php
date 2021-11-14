<?php get_header(); ?>

	<div id="content">
	<?php if (have_posts()) : ?>
	<?php while (have_posts()) : the_post(); ?>
	
	<div class="post" id="post-<?php the_ID(); ?>">
	<h2><a href="<?php the_permalink() ?>" rel="bookmark" title="Permalink: <?php the_title(); ?>"><?php the_title(); ?></a> <span class="chrondate"><?php the_time('dMy') ?> | <?php comments_popup_link('0','1','%')?> <?php edit_post_link('e', '', ''); ?></span></h2>
				
				<div class="entry">
					<?php the_content('[...]'); ?>
				</div>
				
		</div>	
	
	<?php endwhile; ?>
	<?php else : ?>
	
	<h2>The landscaper ran off with the nanny</h2>

<p>You seemed to have found a mislinked file, page, or search query with no results. If you feel you have reached this page in error, double check the URL and try again. If you still find yourself on this page and believe the site is at fault, it really isn't. Blame the landscaper. If you happen to find him, tell him the hedges need pruning.</p>

	<?php endif; ?>
	
	<div class="nextprevious">
		<div class="left"><?php next_posts_link('&laquo; Previous') ?></div>
		<div class="right"><?php previous_posts_link('Next &raquo;') ?></div>
	</div>
	
	
	</div>
</div>

<div id="footercontent">

	<div id="bottomwrap">
			
	<?php include (TEMPLATEPATH . "/bottom.php"); ?>
	<div class="clear"></div>
	</div>
</div>

<div id="bottom">
<?php get_footer(); ?>