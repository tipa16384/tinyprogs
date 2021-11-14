<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">

<head profile="http://gmpg.org/xfn/11">
<title>
		<?php bloginfo('name'); ?>
		<?php if ( !(is_404()) &&
                 (is_single()) or
                 (is_page()) or
                 (is_archive()) )
      { ?> &raquo; <?php } ?>
		<?php wp_title(''); ?>
</title>

	<meta name="generator" content="WordPress <?php bloginfo('version'); ?>" /> <!-- leave this for stats -->
 	<meta http-equiv="Content-Type" content="<?php bloginfo('html_type'); ?>; charset=<?php bloginfo('charset'); ?>" />
	<link rel="stylesheet" href="<?php bloginfo('stylesheet_url'); ?>" type="text/css" media="screen" />
	
	<link rel="alternate" type="application/rss+xml" title="<?php bloginfo('name'); ?> RSS Feed" href="<?php bloginfo('rss2_url'); ?>" />
<link rel="pingback" href="<?php bloginfo('pingback_url'); ?>" />
	
	<script type="text/javascript" src="<?php bloginfo('template_directory'); ?>/js/prototype.js"></script>
	<script type="text/javascript" src="<?php bloginfo('template_directory'); ?>/js/effects.js"></script>
	<script type="text/javascript" src="<?php bloginfo('template_directory'); ?>/js/combo.js"></script>
	<script type="text/javascript" src="<?php bloginfo('template_directory'); ?>/js/global.js"></script>

<?php wp_head(); ?>
</head>

<body>


<a name="top"></a>
<div id="top">
	<div id="shelfwrap" style="display: none;">
	
		<div id="shelf">
		
			<div class="left">
			
				<h3>About</h3>	
				<p>"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. <a href="#" title="Read more">[...]</a></p>
				
				<ul id="navigation">
				<li><span>Return to the frontpage</span> <a href="#">Journal</a><br /></li>
				<li><span>About the author</span> <a href="#">About</a><br /></li>
				<li><span>Visual sweets</span> <a href="#">Portfolio</a><br /></li>
				<li><span>Noteworthy</span> <a href="#bottomcontent">Recents</a><br /></li>
				<li><span>View the archives</span> <a href="#">Archives</a><br /></li>
				<li><span>Content syndication</span> <a href="#">Subscribe</a><br /></li>
				<li><span>Drop a line or two</span> <a href="#">Contact</a><br /></li>
				</ul>
				
			<div id="searchbar">
				<?php include (TEMPLATEPATH . "/searchform.php"); ?>
			</div>
			
			</div>
			
			<div class="right">
			
			<h3>Recent</h3>	
			<p>"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt.</p>
			
			<ul id="recentposts">
			<?php get_archives('postbypost', 9); ?>
			</ul>
			
			</div>
			
		</div>
	<div class="clear"></div>
	</div>
	
<div id="shelfbreak"></div>

<div id="banner">
<div id="foliage">
<div id="pull"><a href="javascript:Effect.Combo('shelfwrap', {duration: 0.8});">Toggle Menu</a>
</div>
</div>
</div>
