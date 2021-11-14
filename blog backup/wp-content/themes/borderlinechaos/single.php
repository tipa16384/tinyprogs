<?php get_header(); ?>

<div id="sidebar">

	<div id="sidebox">

<div class="title"><?php bloginfo('description'); ?></div>

<?php /* If this is a category archive */ if (is_category()) { ?>				

			<p>You are currently browsing the <a href="<?php bloginfo('url'); ?>"><?php echo bloginfo('name'); ?></a> weblog archives

			for the '<?php echo single_cat_title(); ?>' category.</p>

			

			<?php /* If this is a yearly archive */ } elseif (is_day()) { ?>

			<p>You are currently browsing the <a href="<?php bloginfo('url'); ?>"><?php echo bloginfo('name'); ?></a> weblog archives.</p>

		

			

			<?php /* If this is a monthly archive */ } elseif (is_month()) { ?>

			<p>You are currently browsing the <a href="<?php bloginfo('url'); ?>"><?php echo bloginfo('name'); ?></a> weblog archives.</p>



      <?php /* If this is a yearly archive */ } elseif (is_year()) { ?>

			<p>You are currently browsing the <a href="<?php bloginfo('url'); ?>"><?php echo bloginfo('name'); ?></a> weblog archives.</p>

			

		 <?php /* If this is a monthly archive */ } elseif (is_search()) { ?>

			<p>You have searched the <a href="<?php bloginfo('url'); ?>"><?php echo bloginfo('name'); ?></a> weblog archives

			for <strong>'<?php echo $s; ?>'</strong>. If you are unable to find anything in these search results, we're really sorry.</p>



			<?php /* If this is a monthly archive */ } elseif (isset($_GET['paged']) && !empty($_GET['paged'])) { ?>

			<p>You are currently browsing the <a href="<?php bloginfo('url'); ?>"><?php echo bloginfo('name'); ?></a> weblog archives.</p>



			<?php } ?>



</div>

<br />

	<div id="sidebox1">

			<div class="title">Pages</div>

<ul>

<?php wp_list_pages('title_li='); ?>

</ul>

</div>



<br />

	<div id="sidebox2">

<div class="title">Categories</div>

				<?php list_cats(0, '', 'name', 'asc', '', 0, 0, 1, 1, 1, 1, 0,'','','','','28') ?>
</div>

<br />

	<div id="sidebox3">

<div class="title"><?php _e('Archives'); ?></div>

<?php wp_get_archives('type=monthly&format=other&after=<br />'); ?></div>



<br />

	<div id="sidebox4">

<form style="padding: 0px; margin-top: 0px; margin-bottom: 0px;" id="searchform" method="get" action="<?php bloginfo('url'); ?>">



<div class="title">Search:</div>

<p style="padding: 0px; margin-top: 0px; margin-bottom: 0px;"><input type="text" class="input" name="s" id="search" size="15" />

<input name="submit" type="submit" tabindex="5" value="<?php _e('GO'); ?>" /></p>

</form></div>

</div>

<div id="contentwrapper">

<div id="content">

<?php if (have_posts()) : while (have_posts()) : the_post(); ?>

		

<div class="postmetadata">

					<small>

						This entry was posted

											on <?php the_time('l, F jS, Y') ?> at <?php the_time() ?>

						and is filed under <?php the_category(', ') ?>.

						You can follow any responses to this entry through the <?php comments_rss_link('RSS 2.0'); ?> feed. 

						

						<?php if (('open' == $post-> comment_status) && ('open' == $post->ping_status)) {

							// Both Comments and Pings are open ?>

							You can <a href="#respond">leave a response</a>, or <a href="<?php trackback_url(display); ?>">trackback</a> from your own site.

						

						<?php } elseif (!('open' == $post-> comment_status) && ('open' == $post->ping_status)) {

							// Only Pings are Open ?>

							Responses are currently closed, but you can <a href="<?php trackback_url(display); ?> ">trackback</a> from your own site.

						

						<?php } elseif (('open' == $post-> comment_status) && !('open' == $post->ping_status)) {

							// Comments are open, Pings are not ?>

							You can skip to the end and leave a response. Pinging is currently not allowed.

			

						<?php } elseif (!('open' == $post-> comment_status) && !('open' == $post->ping_status)) {

							// Neither Comments, nor Pings are open ?>

							Both comments and pings are currently closed.			

						

						<?php } edit_post_link('Edit this entry.','',''); ?>

						

					

</small>

			

</div>	



	

		<div class="singlepost">

<br />
<br />
<br />

	 <a class="posttitle" href="<?php the_permalink() ?>" style="text-decoration:none;" rel="bookmark" title="Permanent Link: <?php the_title(); ?>"><?php the_title(); ?></a>

	<div class="cite"><?php the_time("l F dS Y") ?>, <?php the_time() ?> <?php edit_post_link(); ?><br />

<?php _e("Filed under:"); ?> <?php the_category(',') ?></div><br/>	

			<div class="entrytext">

				<?php the_content('<p class="serif">Read the rest of this entry &raquo;</p>'); ?>

	

				<?php link_pages('<p><strong>Pages:</strong> ', '</p>', 'number'); ?>

	

				</div>
	<br />
		</div>

	<br />

	<?php comments_template(); ?>

	

<div class="navigation">

			<div class="alignleft"><?php previous_post('&laquo; %','','yes') ?></div>

			<div class="alignright"><?php next_post(' % &raquo;','','yes') ?></div>

  				</div>

	<?php endwhile; else: ?>

	

		<p><?php _e('Sorry, no posts matched your criteria.'); ?></p>

	

<?php endif; ?>





</div>

<?php get_footer(); ?>