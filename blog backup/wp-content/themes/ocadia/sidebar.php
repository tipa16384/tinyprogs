</div>

<div id="sidebar">
<ul>
<?php if ( !function_exists('dynamic_sidebar') || !dynamic_sidebar() ) : ?>

	<li id="search">
		<?php include (TEMPLATEPATH . '/searchform.php'); ?>
	</li> 

	<?php wp_list_pages('title_li=<h2>' . __('Pages') . '</h2>' ); ?>

	<li id="archives">
		<h2><?php _e('Archives'); ?></h2>
		<ul>
		<?php wp_get_archives('type=monthly'); ?>
		</ul>
	</li>

	<?php /* Uncomment this to display the calendar 
	<li id="calendar"><div>
		<?php get_calendar(); ?>
	</div></li>
	*/ ?>

	
	<li id="categories">
		<h2><?php _e('Categories'); ?></h2>
		<ul>
		<?php wp_list_cats(); ?> 
		</ul>
	</li>
	
	<?php if (function_exists('wp_theme_switcher')) { ?>
	<li>
		<h2><?php _e('Themes'); ?></h2>
		<?php wp_theme_switcher(); ?>
	</li>
	<?php } ?>
		
	<?php if (is_home()) { get_links_list(); } ?>
				
	<li id="meta">
		<h2><?php _e('Meta'); ?></h2>
		<ul>
		<?php wp_register(); ?>
		<li><?php wp_loginout(); ?></li>
		<li><a href="<?php bloginfo('rss2_url'); ?>" title="<?php _e('Syndicate this site using RSS'); ?>"><?php _e('Entries <abbr title="Really Simple Syndication">RSS</abbr>'); ?></a></li>
		<li><a href="<?php bloginfo('comments_rss2_url'); ?>" title="<?php _e('The latest comments to all posts in RSS'); ?>"><?php _e('Comments <abbr title="Really Simple Syndication">RSS</abbr>'); ?></a></li>
		<li><a href="http://wordpress.org" title="<?php _e('Powered by Wordpress, state-of-the-art semantic personal publishing platform.'); ?>">Wordpress</a></li>
		<?php wp_meta(); ?>
		</ul>
	</li>
	
<?php endif; ?>
</ul>
</div>
