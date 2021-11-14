<?php
	/*
	
	Hi there,

	If you're planning on making modifications to this file, you'd rather use the HTML Inserts feature in the 
	theme options.
	
	Doing it this way will keep the theme easily updatable.

	Just wrap your css rules in a <style type="text/css"></style> tag pair, and put them in the first textbox on
	the HTML Inserts page (the "header.php" field).

	*/



	// if get_option() is available, we're not using the fully dynamic stylesheet
	if (function_exists('get_option')) {
		global $no_default_header_img;
		$mandigo_options = get_option('mandigo_options');
		$stylesheet_directory = get_bloginfo('stylesheet_directory');
	}
	// otherwise we need to find a way to read the theme options from the database
	else {
		error_reporting(0);
		$fb = 0;

		// find the wp configuration file
		$d = 0; // search depth;
		while (!file_exists(str_repeat('../', $d) . 'wp-config.php')) if (++$d > 99) exit;
		$wpconfig = str_repeat('../', $d) . 'wp-config.php';



		// if this is a wpmu setup or we have been instructed to use the fallback method
		if ($_GET['fb'] || file_exists(str_repeat('../', $d) . 'wpmu-settings.php'))
			$fb++;
		elseif (file_exists($wpconfig))
			// evaluate constant definitions from wp-config.php so we can connect directly to the database and save some time
			foreach (explode("\n", file_get_contents($wpconfig)) as $line) {
				if (preg_match('/define.+?DB_|table_prefix/', $line))
					eval($line);
			}



		// if we seem to have the credentials to the database
		if (defined('DB_USER')) {
			$dbh = @mysql_connect(DB_HOST, DB_USER, DB_PASSWORD);
			@mysql_select_db(DB_NAME, $dbh);
			$r = @mysql_query(
				"SELECT option_name,option_value FROM ". $table_prefix ."options WHERE option_name REGEXP '^(mandigo_options|stylesheet|siteurl)$';",
				$dbh
			);
			while ($a = @mysql_fetch_row($r)) {
				$$a[0] = $a[1];
			}
			@mysql_free_result($r);
			
			$mandigo_options = unserialize($mandigo_options);
			
			// if the options array seems to be empty/incomplete, fallback
			if (!$mandigo_options['scheme'])
				$fb++;
			$stylesheet_directory = $siteurl .'/wp-content/themes/'. $stylesheet;
		}
		else $fb++;


		// fallback, fewer lines but way longer to process
		if ($fb) {
			// if we're here without 'fb' in the query string, then redirect to this same page and start over
			// this prevents constant redeclaration errors
			if (!$_GET['fb']) {
				$redirect = preg_replace('/(\?.*|$)/', '', $_SERVER['REQUEST_URI']) . '?fb=1';
				header("Location: $redirect");
				exit;
			}
			require_once($wpconfig);
			$mandigo_options      = get_option('mandigo_options');
			$stylesheet_directory = get_bloginfo('stylesheet_directory');
			status_header(200);
		}



		// boolean options
		foreach ($mandigo_options as $option => $value) {
			if ($value == 'on')  $mandigo_options[$option] = 1;
			if ($value == 'off') $mandigo_options[$option] = 0;
		}
		
		$no_default_header_img = $_GET['no_default_header_img'];
		
		// echo http headers and the static part of the stylesheet
		@header('Content-type: text/css');
		// echo file_get_contents('style.css');
		include 'style.css';
	}

	$ie      = preg_match("/MSIE [4-6]/", $_SERVER['HTTP_USER_AGENT']);
	$ie7     = stristr($_SERVER['HTTP_USER_AGENT'], 'MSIE 7');
	$safari  = stristr($_SERVER['HTTP_USER_AGENT'], 'Safari');
	$firefox = stristr($_SERVER['HTTP_USER_AGENT'], 'Firefox');
	
	$font_families = array(
		'serif'      => array(
			'body'       => "Georgia, 'Times New Roman', Serif",
			'header'     => "Georgia, 'Times New Roman', Serif",
			'titles'     => "Georgia, 'Times New Roman', Serif",
			'comments'   => "Georgia, 'Times New Roman', Serif",
			'datestamps' => "Georgia, 'Times New Roman', Serif",
			'sidebars'   => "Georgia, 'Times New Roman', Serif",
		),
		'sans-serif' => array(
			'body'       => "Arial, Sans-Serif",
			'header'     => "'Trebuchet MS', 'Lucida Grande', Verdana, Arial, Sans-Serif",
			'titles'     => "'Trebuchet MS', 'Lucida Grande', Verdana, Arial, Sans-Serif",
			'comments'   => "'Lucida Grande', Verdana, Arial, Sans-Serif",
			'datestamps' => "'Lucida Grande', 'Lucida Sans Unicode', Arial, Sans-Serif",
			'sidebars'   => "'Lucida Grande', Verdana, Arial, Sans-Serif",
		),
	);
?>

body {
	font-family: <?php echo $font_families[$mandigo_options['font_family']]['body']; ?>;
	background-color: <?php echo $mandigo_options['background_color']; ?>;
<?php
	if ($mandigo_options['background_pattern_file']) {
?>
	background-image: url(<?php echo $stylesheet_directory; ?>/images/patterns/<?php echo $mandigo_options['background_pattern_file']; ?>);
	background-attachment: <?php echo ($mandigo_options['background_pattern_fixed'] ? 'fixed' : 'scroll'); ?>;
	background-repeat: <?php echo ($mandigo_options['background_pattern_repeat'] ? $mandigo_options['background_pattern_repeat'] : 'repeat'); ?>;
<?php
		if (isset($mandigo_options['background_pattern_position'])) {
?>
	background-position: <?php echo $mandigo_options['background_pattern_position']; ?>;
<?php
		}
	}
?>
}

<?php
	if ($mandigo_options['bold_links']) {
?>
a {
	font-weight: bold;
}
<?php
	}
?>

.narrowcolumn .entry, .widecolumn .entry {
	line-height: <?php echo ($mandigo_options['font_family'] == 'serif' ? 1.5 : 1.4); ?>em;
}

.inline-widgets #wp-calendar caption, .blogname, .blogdesc {
	font-family: <?php echo $font_families[$mandigo_options['font_family']]['header']; ?>;
}

.blogname {
	font-size: <?php echo ($mandigo_options['header_blogname_smaller_font'] ? 3 : 4); ?>em;
	margin-top: <?php echo ($mandigo_options['header_blogname_smaller_font'] ? 25 : 15); ?>px;
}

.posttitle, #comments, #respond .title, #respond.pre27, #trackbacks {
	font-family: <?php echo $font_families[$mandigo_options['font_family']]['titles']; ?>;
}

.commentlist li, #commentform input, #commentform textarea {
	font-family: <?php echo $font_families[$mandigo_options['font_family']]['comments']; ?>;
}

#commentform p {
	font-family: <?php echo $font_families[$mandigo_options['font_family']]['comments']; ?>;
}

.sidebars {
	font-family: <?php echo $font_families[$mandigo_options['font_family']]['sidebars']; ?>;
}

<?php
	if ($mandigo_options['emphasize_as_bold']) {
?>
em {
	font-style: normal;
	font-weight: bold;
}
<?php
	}
?>

#page {
	width: <?php echo ($mandigo_options['layout_width']-37); ?>px;
}

#header {
	background: url(<?php echo $stylesheet_directory; ?>/images/header<?php echo ($mandigo_options['layout_width'] == 1024 ? '-1024' : ''); ?>.png);
	height: <?php echo (243-($mandigo_options['header_slim'] ? 100 : 0)); ?>px;
	width: <?php echo ($mandigo_options['layout_width']-37); ?>px;
}

#headerimg {
	height: <?php echo (226-($mandigo_options['header_slim'] ? 100 : 0)); ?>px;
	width: <?php echo ($mandigo_options['layout_width']-63); ?>px;
<?php
	if (!isset($_GET['no_default_header_img'])) {
?>
	background: url(<?php echo $stylesheet_directory; ?>/schemes/<?php echo $mandigo_options['scheme']; ?>/images/head<?php echo ($mandigo_options['layout_width'] == 1024 ? '-1024' : ''); ?>.jpg) bottom center no-repeat;
<?php
	}
	
	if ($mandigo_options['header_clickable']) {
?>
	cursor: pointer;
<?php
	}
?>
}

#main {
	background: url(<?php echo $stylesheet_directory; ?>/images/bg<?php echo ($mandigo_options['layout_width'] == 1024 ? '-1024' : ''); ?>.png);
	width: <?php echo ($mandigo_options['layout_width']-67); ?>px;
}

#footer {
	background: url(<?php echo $stylesheet_directory; ?>/images/foot<?php echo ($mandigo_options['layout_width'] == 1024 ? '-1024' : ''); ?>.png);
}

.post {
	text-align: <?php echo ($mandigo_options['dont_justify'] ? 'left' : 'justify'); ?>;
	background: <?php echo $mandigo_options['color_post_background']; ?>; 
	border: 1px solid <?php echo $mandigo_options['color_post_border']; ?>; 
<?php
	if ($ie||$ie7) { // peekaboo
?>
	height: 1%;
<?php
	}
?>
}

<?php
	if ($mandigo_options['clear_all_paragraphs']) {
?>
.entry p {
	clear: both;
}
<?php
	}
?>

#footer {
	width: <?php echo ($mandigo_options['layout_width']-37); ?>px;
}

<?php
	if ($ie) {
?>
* a {
	position: relative;
}
<?php
	}
?>

.sidebars {
	background: <?php echo $mandigo_options['color_sidebar_background']; ?>;
	border: 1px solid <?php echo $mandigo_options['color_sidebar_border']; ?>;
}

#sidebar1 .sidebars {
	width: <?php echo $mandigo_options['sidebar_1_width']; ?>px;
}

#sidebar2 .sidebars {
	width: <?php echo $mandigo_options['sidebar_2_width']; ?>px;
}

<?php
	if ($ie) {
?>
.switch-post img {
	width: 11px !important;
	height: 11px !important;
}
<?php
	}
?>

.entry img {
	float: <?php echo ($mandigo_options['no_text_wrapping'] ? 'none' : 'left'); ?>;
<?php
	if (!$mandigo_options['no_image_borders']) {
?>
	background: #fff;
	border: 1px solid #333;
	padding: 3px;
<?php
	}
?>
}

.sidebars li {
	list-style-image: url(<?php echo $stylesheet_directory; ?>/schemes/<?php echo $mandigo_options['scheme']; ?>/images/star.gif);
<?php
	if ($ie) {
?>
	margin: 10px 0 15px 20px;
<?php
	}
?>
}

.commentlist {
<?php
	if ($mandigo_options['comments_numbering']) {
?>
	margin-left: 2em;
<?php
	}
?>
}

.commentlist li {
	list-style: <?php echo ($mandigo_options['comments_numbering'] ? 'decimal outside' : 'none'); ?>;
}

#wp-calendar {
	margin: 0 !important; margin-top: -1.5em<?php echo ($safari || $ie7 ? ' !important;' : ''); ?>;
}

#wp-calendar caption {
	margin-top: -1.4em;
<?php
	if ($safari) {
?>
	margin-bottom: 1.5em;
<?php
	}
?>
}

/* dirty fix for the event calendar plugin */
div#wp-calendar .nav {
	margin: <?php echo ($ie || $ie7 || $safari ? ($ie7 ? 0 : '1.5em') .' 0 -1.5em 0' : 0); ?>;
}
/* end dirty fix */

.datestamp div {
	font-family: <?php echo $font_families[$mandigo_options['font_family']]['datestamps']; ?>;
}

.cal3 {
<?php
	if ($mandigo_options['font_family'] == 'serif') {
?>
	margin-top: 0.4em;
<?php
	}
?>
}

.pages {
	text-align: <?php echo $mandigo_options['header_navigation_position']; ?>;
}

.pages ul li.has_sub {
	background: url(<?php echo $stylesheet_directory; ?>/images/icons/bullet_arrow_right.png) no-repeat center right;
}

.head_overlay {
	background: url(<?php echo $stylesheet_directory; ?>/images/head_overlay.<?php echo ($ie ? 'gif' : 'png'); ?>);
}




<?php 
	// the following set of rules are loaded only if a right-to-left script (eg. Hebrew, Arabic) is being used.
	if (preg_match('/^(ar|he_IL)$/', WPLANG)) {
?>
/* RTL scripts support */
.pages, #content, .sidebars, #footer {
	direction: rtl;
}

.blogname, .blogdesc { 
	width: <?php echo ($mandigo_options['layout_width']-78); ?>px;
	text-align: right;
	padding-left: 0;
	margin-left: 0;
	margin-right: 15px;
}

.datestamp {
	float: right;
	margin-right: 0;
	margin-left: 1em;
}

.narrowcolumn .postmetadata, #content #searchform, #respond, #commentform p, .sidebars, #wp-calendar caption, .posttitle {
	text-align: right;
}

.entry img { 
	float: <?php echo ($mandigo_options['no_text_wrapping'] ? 'none' : 'right'); ?>;
	margin: 3px 0 3px 10px;
}

#commentform input {
	margin: 5px 0 1px 5px;
}

#commentform #submit {
	margin: 0 0 0 1em;
}

#commentform #submit, #rss {
	float: left;
}

ol, ul {
	padding: 0 20px 0;
}

ol ol, ol ul, ul ul, ul ol {
	padding: 0 10px 0 0;
}

ul {
	margin-right: 0;
} 

li {
	margin: 3px 5px 4px 0;
}

.sidebars li {
	margin: 0 25px 15px 0;
<?php
		if ($ie) {
?>
	margin: 10px 20px 15px 0;
<?php
		}
?>
}

<?php
		if ($firefox) {
?>
.pages li {
	display: table-cell;
	padding: 0 1em;
}

.sidebars>li {
	list-style-image: none;
	list-style-type: none;
}

.sidebars>li .widgettitle {
	background-image: url(<?php echo $stylesheet_directory; ?>/schemes/<?php echo $mandigo_options['scheme']; ?>/images/star.gif);
	background-repeat: no-repeat;
	background-position: top right;
	margin-right: -20px;
	padding-right: 20px;
}
<?php
		}
?>

.sidebars p, .sidebars select {
	margin: 5px 0 8px 0;
}

.sidebars ul, .sidebars ol {
	margin: 5px 5px 0 0;
}

.sidebars ul ul, .sidebars ol {
	margin: 0 10px 0 0;
}

.switch-post {
	float: left;
}
<?php 
	} // end of rtl scripts specific rules
?>
