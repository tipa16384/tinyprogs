<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">

<head profile="http://gmpg.org/xfn/11">
<meta http-equiv="Content-Type" content="<?php bloginfo('html_type'); ?>; charset=<?php bloginfo('charset'); ?>" />

<title><?php wp_title('', display); ?><?php if(wp_title(' ', false)) { echo ' &raquo; '; } ?><?php bloginfo('name'); ?></title>

    <meta name="description" content="<?php if ( is_single() ) {
            single_post_title('', true); 
        } else {
            bloginfo('name'); echo " - "; bloginfo('description');
        }
        ?>" />

    <meta name="generator" content="WordPress <?php bloginfo('version'); ?>" /> <!-- leave this for stats -->

    <link rel="stylesheet" href="<?php bloginfo('stylesheet_url'); ?>" type="text/css" media="screen" />
    <link rel="alternate" type="application/rss+xml" title="<?php bloginfo('name'); ?> RSS Feed" href="<?php bloginfo('rss2_url'); ?>" />
    <link rel="pingback" href="<?php bloginfo('pingback_url'); ?>" />

<?php wp_head(); ?>
</head>
<body>

<div id="newheader">
    <ul id="headerimage">
        <li><h1><a href="<?php echo get_settings('home'); ?>/"><?php bloginfo('name'); ?></a></h1></li>
        <li><h2><?php if ( is_home() || is_page() ) { ?><?php bloginfo('description'); ?><?php } else { ?><?php the_title(); ?><?php } ?></h2></li>
    </ul>
</div>

<div id="wrapper">

<div id="highlands">
	<div id="column1">

    <a href="#" name="documentContent"></a>