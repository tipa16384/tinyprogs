<?php get_header(); ?>

	<div id="content">			
  	<?php if (have_posts()) : while (have_posts()) : the_post(); ?>
	
		<div class="post" id="post-<?php the_ID(); ?>">
		<div class="navigation">
			<div class="alignleft"><?php previous_post_link('&laquo; %link') ?></div>
			<div class="alignright"><?php next_post_link('%link &raquo;') ?></div>
		</div>
		<div class="clear"></div>
			<h1><a href="<?php echo get_permalink() ?>" rel="bookmark" title="Permanent Link: 
			<?php the_title(); ?>"><?php the_title(); ?></a></h1>
	
			<div class="entry">
				<?php the_content('<p>Continue reading &raquo;</p>'); ?>
	
				<p class="postmetadata alt">
				<small>Posted: <?php the_time('m|j|y') ?> at <?php the_time() ?>. 
				Filed under: <?php the_category(', ') ?>.  
				<br /><?php the_tags('Tags: ', ', '); ?><br />
				New here? Follow this entry via <?php comments_rss_link('RSS 2.0'); ?>. <?php edit_post_link('[edit]'); ?>
						
				<?php if (('open' == $post-> comment_status) && ('open' == $post->ping_status)) {
				// Both Comments and Pings are open ?>
				<a href="#respond">Comment</a> | <a href="<?php trackback_url(true); ?>" rel="trackback">Trackback</a>
						
				<?php } elseif (!('open' == $post-> comment_status) && ('open' == $post->ping_status)) {
				// Only Pings are Open ?>
				Comments are closed, but you can <a href="<?php trackback_url(true); ?> " rel="trackback">trackback</a> from your own site.
						
				<?php } elseif (('open' == $post-> comment_status) && !('open' == $post->ping_status)) {
				// Comments are open, Pings are not ?>
				Pinging is currently disabled.
			
				<?php } elseif (!('open' == $post-> comment_status) && !('open' == $post->ping_status)) {
				// Neither Comments, nor Pings are open ?>
				Comments and pings are currently closed.			
						
				<?php } edit_post_link('Moderate','',''); ?>
				</small>
				</p>
	
			</div>
		</div>
		
	<div id="comments">
		<?php comments_template(); ?>
	</div>
	<?php endwhile; else: ?>
	
	<p>Sorry, no posts matched your criteria.</p>
	
	<?php endif; ?>
	
	</div>

<?php include(TEMPLATEPATH."/left.php");?>
<?php include(TEMPLATEPATH."/right.php");?>

<?php get_footer(); ?>
