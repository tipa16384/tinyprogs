<div id="sidebar">

<?php if ( !function_exists('dynamic_sidebar') || !dynamic_sidebar(1) ) : ?>   
	<h2>Recent Posts</h2>
	<ul>
	<?php get_archives('postbypost', 10); ?>
	<li class='footbar'>&nbsp;</li>
	</ul>
	
	<h2>Archives</h2>
	<ul>
	<?php wp_get_archives('type=monthly'); ?>
	<li class='footbar'>&nbsp;</li>
	</ul>

	<h2>Topics</h2>			
	<ul><?php wp_list_cats('sort_column=name'); ?>
	<li class='footbar'>&nbsp;</li>
	</ul>

<?php /* If this is the frontpage */ if ( is_home() || is_page() ) { ?>				
	<h2>Meta</h2>
	<ul>
	<?php wp_register(); ?>
	<li><?php wp_loginout(); ?></li>
	<li><a href="http://wordpress.org/" title="Powered by WordPress, state-of-the-art semantic personal publishing platform.">WordPress</a></li>
	<?php wp_meta(); ?>
	<li class='footbar'>&nbsp;</li>
	</ul>
	<?php } ?>
	
<?php endif; ?>

</div> <!-- end of sidebar -->