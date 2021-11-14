<?php get_header(); ?>

	<div id="content" class="narrowcolumn">

	<?php
/*
Template Name: Archives
*/
?>

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

	<?php wp_list_cats('list=0'); ?></div>

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

<div id="content" class="widecolumn">
<P></P>
<b>Not Found!</b>
<P></P>
</div>	
</div>

<?php get_footer(); ?>


	</div>

<?php get_sidebar(); ?>

<?php get_footer(); ?>