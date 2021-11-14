<div id="sidebar">
<ul>
<?php if ( function_exists('dynamic_sidebar') && dynamic_sidebar() ) : else : ?>
<?php if(is_home()) { ?>
<li class="sidebox">
	<h2>About <?php bloginfo('name'); ?></h2>
	<p>
	<!-- img src="<?php bloginfo('stylesheet_directory');?>/img/profile.jpg" alt="Profile" class="profile" / -->
	<!-- <strong><?php bloginfo('name');?></strong><br/><?php bloginfo('description');?>. -->
	Musings on games (especially MMORPGs), work, my kids, and life.
	<!-- br/ -->
	There are <?php global $numposts; echo $numposts; ?> Posts and <?php global $numcmnts; echo $numcmnts;?> Comments so far.
	</p>	
</li>
<?php } ?>

<?php if(is_home()) { ?>
<li class="sidebox">
<h2><?php _e('Quick Notes'); ?></h2>
<?php rewind_posts(); ?>
<?php
if ($posts) : foreach ($posts as $post) : start_wp();
?>
<?php if (in_category(36)) { ?>
<div class="asides_sidebar">
 <?php echo $post->post_excerpt ?> <?php the_content(); ?>
 <small><?php comments_popup_link(__('#'), __('(1)'), __('(%)')); ?>
   <?php edit_post_link('Edit', ' — '); ?></small>
</div>
<?php } ?>
<?php endforeach; else: ?>
<p><?php _e('Sorry, no posts matched your criteria.'); ?></p>
<?php endif; ?>
</li>
<?php } ?>

<?php if(is_home()) {
if (function_exists('src_simple_recent_comments')) { 
	src_simple_recent_comments(7,60,'<li class="sidebox"><h2>Recent Comments</h2>','</li>');
	} 
}
?>


<?php if(is_home()) { ?>
<li class="sidebox">
	<ul>
	<?php get_links_list('name'); ?>
	</ul>	
	</li>
<?php } ?>


<li class="sidebox">
	<h2><?php _e('Archives'); ?></h2>
	<ul><?php wp_get_archives('type=monthly&show_post_count=true'); ?></ul>
</li>

<li class="sidebox">
	<h2><?php _e('Tags'); ?></h2>
	<ul>
		<?php wp_list_cats('optioncount=1');    ?>
	</ul>		
</li>

<!-- li class="sidebox">
	<h2><?php _e('Pages'); ?></h2>
	<ul><?php wp_list_pages('title_li=' ); ?></ul>	
</li -->

<?php if(is_home()) { ?>
<li class="sidebox">
	<h2><?php _e('Meta'); ?></h2>
	<ul>
		<?php wp_register(); ?>
		<li><?php wp_loginout(); ?></li>
		<li><a href="http://validator.w3.org/check/referer" title="This page validates as XHTML 1.0 Transitional">Valid <abbr title="eXtensible HyperText Markup Language">XHTML</abbr></a></li>
		<li><a href="http://gmpg.org/xfn/"><abbr title="XHTML Friends Network">XFN</abbr></a></li>
		<li><a href="http://wordpress.org/" title="Powered by WordPress, state-of-the-art semantic personal publishing platform.">WordPress</a></li>
		<?php wp_meta(); ?>
	</ul>	
</li>
<?php }?>
  <?php endif; ?>
</ul>
</div><!-- end id:sidebar -->
</div><!-- end id:content -->
</div><!-- end id:container -->
