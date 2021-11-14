<?php get_header(); ?>

<div id="content">

<?php if (have_posts()) : ?>
	<!-- first pass: show only the latest post -->
	<?php query_posts("showposts=1"); ?>
	<?php while (have_posts()) : the_post(); ?>
	<div class="homeTop" id="post-<?php the_ID(); ?>">
		<h1><a href="<?php the_permalink() ?>" rel="bookmark" title="Permanent Link to <?php the_title(); ?>"><?php the_title(); ?></a></h1>
	
	<div class="post-date">
	<span class="post-month"><?php the_time('M') ?></span> 
	<span class="post-day"><?php the_time('d') ?></span>
	<span class="post-year"><?php the_time('Y') ?></span>
	</div>
	<small>By <?php the_author() ?> <?php edit_post_link('(edit)'); ?></small>
	
			<div class="entry">
				<?php the_excerpt(); ?> 
				<a href="<?php the_permalink() ?>" class="readmore" rel="bookmark" title="Permanent Link to <?php the_title(); ?>">Continue Reading&rarr;</a>
			</div>
		<p class="postmetadata"><?php the_tags('Tags: ', ', ', '.<br />'); ?> Filed under: <?php the_category(', ') ?> | <?php comments_popup_link('No Comments &#187;', '1 Comment &#187;', '% Comments &#187;'); ?></p>
		</div> 
	<?php endwhile; ?>
	
	<!-- second pass: show remaining posts -->
	<?php query_posts("showposts=4&offset=1"); ?>
	<?php while (have_posts()) : the_post(); ?>
	<div class="homeOther" id="post-<?php the_ID(); ?>">
		<h1><a href="<?php the_permalink() ?>" rel="bookmark" title="Permanent Link to <?php the_title(); ?>"><?php the_title(); ?></a></h1>
		
	<div class="post-date">
	<span class="post-month"><?php the_time('M') ?></span> 
	<span class="post-day"><?php the_time('d') ?></span>
	<span class="post-year"><?php the_time('Y') ?></span>
	</div>
	<small>By <?php the_author() ?> <?php edit_post_link('(edit)'); ?></small>
				
			<div class="entry">
				<?php the_excerpt(); ?> 
				<a href="<?php the_permalink() ?>" class="readmore" rel="bookmark" title="Permanent Link to <?php the_title(); ?>">Continue Reading&rarr;</a>
			</div>
		<p class="postmetadata"><?php the_tags('Tags: ', ', ', '.<br />'); ?> Filed under: <?php the_category(', ') ?> | <?php comments_popup_link('No Comments &#187;', '1 Comment &#187;', '% Comments &#187;'); ?></p>
		</div> 
	<?php endwhile; ?>

<?php else: ?>
	<p>Sorry, there was an error reading posts.</p>
<?php endif; ?>


<div class="navigation">
<?php if(function_exists('wp_pagenavi')) { wp_pagenavi(); } ?>
</div>
			
</div><!-- end content -->

<?php include(TEMPLATEPATH."/left.php");?>
<?php include(TEMPLATEPATH."/right.php");?>

<?php get_footer(); ?>