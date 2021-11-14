<?php
	/*
	
	Hi there,

	If you're planning on making modifications to this file, you'd rather use the HTML Inserts feature in the 
	theme options.
	
	Doing it this way will keep the theme easily updatable.

	Just wrap your css rules in a <style type="text/css"></style> tag pair, and put them in the first textbox on
	the HTML Inserts page (the "header.php" field).

	*/

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
	
	@header('Content-type: text/css');

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

/* Begin Typography & Colors */
body {
	font-size: 62.5%; /* Resets 1em to 10px */
	font-family: <?php echo $font_families[$mandigo_options['font_family']]['body']; ?>;
	color: #333;
}

.narrowcolumn .entry, .widecolumn .entry {
	line-height: <?php echo ($mandigo_options['font_family'] == 'serif' ? 1.5 : 1.4); ?>em;
}

.widecolumn {
	line-height: 1.6em;
}

small {
	font-size: 0.9em;
	line-height: 1.5em;
}

h1, h2, h3, h4, h5, h6 {
	font-weight: bold;
}

h1 { font-size: 1.6em; }
h2 { font-size: 1.4em; }
h3 { font-size: 1.2em; }
h4 { font-size: 1.1em; }
h5 { font-size: 1.0em; }
h6 { font-size: 0.9em; }

.inline-widgets #wp-calendar caption, .blogname, .blogdesc {
	font-family: <?php echo $font_families[$mandigo_options['font_family']]['header']; ?>;
	font-weight: bold;
}

#content {
	font-size: 1.2em;
}

.blogname {
	font-size: <?php echo ($mandigo_options['header_blogname_smaller_font'] ? 3 : 4); ?>em;
	letter-spacing: -.05em; 
	margin-top: <?php echo ($mandigo_options['header_blogname_smaller_font'] ? 25 : 15); ?>px;
}

.blogname, .blogname a, blogname a:hover, .blogname a:visited, .blogdesc {
	text-decoration: none;
	color: white;
}

.blogname, .blogdesc { 
	font-weight: bold;
	position: absolute;
	z-index: 100;
	margin-left: 15px;
}

.blogdesc { 
	font-size: 1.2em;
	margin-top: 60px; 
}

.posttitle, #comments, #respond .title, #respond.pre27, #trackbacks {
	font-family: <?php echo $font_families[$mandigo_options['font_family']]['titles']; ?>;
	font-weight: bold;
	font-size: 1.6em;
}

#respond .title, #respond.pre27, #trackbacks {
	clear: both;
}

.posttitle, .posttitle a, .posttitle a:hover, .posttitle a:visited {
	text-align: left;
	text-decoration: none;
	color: #333;
}

.posttitle-archive, .posttitle-search, #comments, #respond .title, #respond.pre27 {
	font-size: 1.5em;
}

.pagetitle {
	font-size: 1.6em;
}

.widgettitle, .sidebars li.linkcat h2 {
	font-size: 1.2em;
	font-weight: bold;
}

.inline-widgets .widgettitle, .inline-widgets #wp-calendar caption {
	font-size: 1.4em;
}

.inline-widgets .widgettitle {
	letter-spacing: -.05em;
}

.sidebars .widgettitle, #wp-calendar caption, cite {
	text-decoration: none;
}

.widgettitle a {
	color: #333;
}

.widecolumn .entry p {
	font-size: 1.05em;
}

.commentlist li, #commentform input, #commentform textarea {
	font-family: <?php echo $font_families[$mandigo_options['font_family']]['comments']; ?>;
	font-size: 0.9em;
}

.commentlist li {
	font-weight: bold;
}

.commentlist li li.comment {
	font-size: 1em;
}

.commentlist li .avatar {
	float: left;
	margin-right: 5px;
}

.commentlist.pre27 li .avatar {
	float: none;
	margin-right: 0;
	padding-left: 41px;
	min-height: 36px;
	background-repeat: no-repeat;
	background-position: top left;
}

.commentlist cite, .commentlist cite a {
	font-weight: bold;
	font-style: normal;
	font-size: 1.1em;
}

li.comment #respond {
	margin-top: 20px;
}

.commentlist p {
	font-weight: normal;
	line-height: 1.5em;
	text-transform: none;
}

#commentform p {
	font-family: <?php echo $font_families[$mandigo_options['font_family']]['comments']; ?>;
}

.commentmetadata {
	font-weight: normal;
}

.sidebars {
	font-family: <?php echo $font_families[$mandigo_options['font_family']]['sidebars']; ?>;
	font-size: 1em;
}

small, .sidebars ul li, .sidebars ol li, .nocomments, .postmetadata, strike {
	color: #777;
}

code {
	font: 1em 'Courier New', Courier, Fixed;
}

blockquote {
	color: #555;
	font-style: italic;
}

em {
<?php
	if ($mandigo_options['emphasize_as_bold']) {
?>
	font-style: normal;
	font-weight: bold;
<?php
	}
	else {
?>
	font-style: italic;
	font-weight: normal;
<?php
	}
?>
}

acronym, abbr, span.caps {
	font-size: 0.9em;
	letter-spacing: .07em;
}

a {
	text-decoration: none;
}

a:hover {
	text-decoration: underline;
}

#wp-calendar #prev a, #wp-calendar #next a {
	font-size: 9pt;
}

#wp-calendar a {
	text-decoration: none;
}

#wp-calendar caption {
	font-size: 1.2em;
	font-weight: bold;
}

#wp-calendar th {
	font-style: normal;
	text-transform: capitalize;
}

.text-shadow {
	color: #333;
}

.text-stroke-tl, .text-stroke-tr, .text-stroke-bl, .text-stroke-br {
	color: #000;
}

.narrowcolumn .postmetadata {
	text-align: left;
}

.four04 {
	font-weight: bold;
	font-size: 18pt;
	letter-spacing: -.1em;
	text-align: center;
	margin-top: 10px
}

.four04-big {
	font-size: 50pt;
	letter-spacing: -.05em;
	line-height: .6em;
	margin-top: .3em;
}

.dropcap {
	float: left;
	font-size: 3em;
	color: #666;
	line-height: 0.93em;
	margin-right: 3px;
}
/* End Typography & Colors */


/* Begin Structure */
* {
	padding: 0; 
	margin: 0;
}

p { margin: 1em 0; }

body {
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
	text-align: center;
	margin: 0 0 20px 0;
}

#page {
	margin: 20px auto;
	text-align: left;
	width: <?php echo ($mandigo_options['layout_width']-37); ?>px;
}

#header {
	background: url(images/header<?php echo ($mandigo_options['layout_width'] == 1024 ? '-1024' : ''); ?>.png);
	height: <?php echo (243-($mandigo_options['header_slim'] ? 100 : 0)); ?>px;
	width: <?php echo ($mandigo_options['layout_width']-37); ?>px;
}

#headerimg {
	position: relative;
	left: 13px; 
	top: 11px;
	height: <?php echo (226-($mandigo_options['header_slim'] ? 100 : 0)); ?>px;
	width: <?php echo ($mandigo_options['layout_width']-63); ?>px;
	z-index: 100;
<?php
	if (!isset($_GET['noheaderimg'])) {
?>
	background: url('schemes/<?php echo $mandigo_options['scheme']; ?>/images/head<?php echo ($mandigo_options['layout_width'] == 1024 ? '-1024' : ''); ?>.jpg') bottom center no-repeat;
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
	background: url(images/bg<?php echo ($mandigo_options['layout_width'] == 1024 ? '-1024' : ''); ?>.png);
	width: <?php echo ($mandigo_options['layout_width']-67); ?>px;
	padding: 9px 15px;
}

#main>table {
	width: 100%;
}

.narrowcolumn, .widecolumn { width: 100%; }

.narrowcolumn, .widecolumn, #sidebar1, #sidebar2, #sidebox {
	vertical-align: top;
	padding: 0 3px;
}

.alt {
	background-color: #fafafa;
	border-top: 1px solid #eee;
	border-bottom: 1px solid #eee;
}

.postmetadata {
	background-color: #fff;
}

#footer {
	background: url(images/foot<?php echo ($mandigo_options['layout_width'] == 1024 ? '-1024' : ''); ?>.png);
	border: none;
}

.post {
	position: relative;
	clear: both;
	text-align: <?php echo ($mandigo_options['dont_justify'] ? 'left' : 'justify'); ?>;
	padding: 5px 15px;
	margin: 0 auto 9px auto;
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

.narrowcolumn .postdata {
	padding-top: 5px;
}

.widecolumn .postmetadata {
	margin: 30px 0;
}

.smallattachment {
	text-align: center;
	width: 128px;
	margin: 5px 5px 5px 0px;
}

.attachment {
	text-align: center;
	margin: 5px 0px;
}

.postmetadata, .entry, .inline-widgets, .clear {
	clear: both;
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
	margin: 0 auto;
	width: <?php echo ($mandigo_options['layout_width']-37); ?>px;
	height: 68px;
}

#footer p {
	margin: 0;
	padding: 10px 0 0 0;
	text-align: center;
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
	padding: 5px;
	overflow: hidden;
}

#sidebar1 .sidebars {
	width: <?php echo $mandigo_options['sidebar_1_width']; ?>px;
}

#sidebar2 .sidebars {
	width: <?php echo $mandigo_options['sidebar_2_width']; ?>px;
}

#sidebox {
	height: 1%;
	padding-bottom: 6px;
}

.pagetitle {
	text-align: center;
}

.post .pagetitle {
	margin-top: inherit;
	text-align: left;
	font-size: 1.5em;
}

.sidebars .widgettitle {
	margin: 5px 0 0 0;
}

.comments {
	margin: 40px auto 20px;
}

.text-shadow    { position: absolute; top: +2px; left: +2px; z-index: 98; }
.text-stroke-tl { position: absolute; top: -1px; left: -1px; }
.text-stroke-tr { position: absolute; top: -1px; left: +1px; }
.text-stroke-bl { position: absolute; top: +1px; left: -1px; }
.text-stroke-br { position: absolute; top: +1px; left: +1px; }
.text-stroke-tl, .text-stroke-tr, .text-stroke-bl, .text-stroke-br { z-index: 99; }

.switch-post {
	float: right;
	position: relative;
	right: -10px;
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

.commentlist .switch-post {
	right: -5px;
}

.catdesc {
	padding: 0 10px;
	text-align: justify;
	font-style: italic;
}
/* End Structure */



/* Begin Images */
.entry img {
	float: <?php echo ($mandigo_options['no_text_wrapping'] ? 'none' : 'left'); ?>;
	margin: 3px 10px 3px 0;
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

img.nofloat, img.nowrap, .nofloat img, .nowrap img, .smallattachment img, .attachment img, .entry img.wp-smiley {
	float: none;
}

.entry img.wp-smiley {
	border: 0;
	padding: 0;
	margin: 0;
	background: transparent;
}

img.noborder, .noborder img {
	background: inherit;
	border: 0;
	padding: inherit;
}

img.centered {
	display: block;
	margin-left: auto;
	margin-right: auto;
	float: none;
}

img.alignright, img.alignleft {
	display: inline;
}

.entry .alignright {
	clear: right;
	float: right;
	margin: 3px 0 3px 10px;
}

.entry .alignleft  {
	clear: left;
	float: left;
	margin: 3px 10px 3px 0;
}

.entry .aligncenter {
	float: none;
	clear: both;
	display: block;
	margin: 3px auto 3px auto;
}

.entry .alignnone {
	float: none;
}
/* End Images */



/* Begin Lists */
ol, ul {
	padding: 0 0 0 20px;
}

ol ol, ol ul, ul ul, ul ol {
	padding: 0 0 0 10px;
}

ul {
	margin-left: 0;
	list-style: none;
	list-style-type: circle;
} 

li {
	margin: 3px 0 4px 5px;
}

.postdata ul, .postmetadata li {
	display: inline;
	list-style-type: none;
	list-style-image: none;
}

.sidebars li {
	list-style-image: url(schemes/<?php echo $mandigo_options['scheme']; ?>/images/star.gif);
	margin: 0 0 15px 25px;
<?php
	if ($ie) {
?>
	margin: 10px 0 15px 20px;
<?php
	}
?>
}

.sidebars ul, .sidebars ol {
	padding: 0;
}

.sidebars ul li {
	list-style-type: circle;
	list-style-image: none;
	margin: 0;
}

ol, .sidebars ol {
	list-style: decimal outside;
	list-style-image: none;
}

.sidebars p, .sidebars select {
	margin: 5px 0 8px 0;
}

.sidebars ul, .sidebars ol {
	margin: 5px 0 0 5px;
}

.sidebars ul ul, .sidebars ol {
	margin: 0 0 0 10px;
}

.sidebars ul li, .sidebars ol li {
	margin: 3px 0 0 0;
}
/* End Entry Lists */



/* Begin Form Elements */
#searchform {
	margin: 0 auto;
	padding: 0 3px; 
	text-align: center;
}

#content #searchform {
	margin-bottom: 10px;
	text-align: left;
}

.sidebars #searchform #s {
	border: 1px dashed #ddd; 
	width: 140px;
	padding: 2px;
}

#content #searchform #s {
	border: 1px dashed #bbb; 
	width: 200px;
	padding: 2px;
}

.sidebars #searchsubmit, #content #searchsubmit {
	position: relative;
	top: 6px;
}

.entry form {
	text-align: center;
}

select {
	width: 130px;
}

#commentform { 
	margin-bottom: 1em;
	width: 99%;
}

#commentform input {
	width: 170px;
	padding: 2px;
	margin: 5px 5px 1px 0;
}

#commentform textarea {
	width: 99%;
	padding: 2px;
}

#commentform #submit {
	margin: 0 1em 0 0;
	float: right;
}
/* End Form Elements */



/* Begin Comments*/
.alt {
	margin: 0;
	padding: 10px;
}

.commentlist {
	text-align: justify;
<?php
	if ($mandigo_options['comments_numbering']) {
?>
	margin-left: 2em;
<?php
	}
?>
	margin-bottom: 15px;
}

.commentlist li {
	margin: 15px 0 3px 0;
	padding: 5px 10px 3px 10px;
	list-style: <?php echo ($mandigo_options['comments_numbering'] ? 'decimal outside' : 'none'); ?>;
}

.commentlist p {
	margin: 10px 5px 10px 0;
}

#commentform p {
	margin: 5px 0;
}

.nocomments {
	text-align: center;
}

.commentmetadata {
	display: block;
}

.bypostauthor {
	background: #EEE;
	color: #000;
	border-top: 1px solid #CCC;
	border-bottom: 1px solid #CCC;
<?php
	/* alternate settings
	background: #666;
	color: #FFF;
	*/
?>
}
/* End Comments */



/* Begin Calendar */
#wp-calendar {
	empty-cells: show;
	margin: 0 !important; margin-top: -1.5em<?php echo ($safari||$ie7 ? ' !important;' : ''); ?>;
	width: 155px;
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
div#wp-calendar caption {
	padding-top: 1.5em;
}
div#wp-calendar .nav {
	margin: <?php echo ($ie||$ie7||$safari ? ($ie7 ? 0 : '1.5em') .' 0 -1.5em 0' : 0); ?>;
	position: relative;
}
/* end dirty fix */

#wp-calendar #next a {
	padding-right: 10px;
	text-align: right;
}

#wp-calendar #prev a {
	padding-left: 10px;
	text-align: left;
}

#wp-calendar a {
	display: block;
}

#wp-calendar #today {
	background: #fff;
}

#wp-calendar caption {
	text-align: left;
	width: 100%;
}

#wp-calendar th {
	padding: 3px 0;
	text-align: center;
}
#wp-calendar td {
	padding: 3px 0;
	text-align: center;
}
/* End Calendar */



/* Begin Various Tags & Classes */
acronym, abbr, span.caps {
	cursor: help;
}

acronym, abbr {
	border-bottom: 1px dashed #999;
}

blockquote {
	margin: 15px 10px 0 10px;
	padding: 0 20px 0 20px;
	border: 1px dashed #ddd;
	border-left: 0;
	border-right: 0;
	background: #fff;
}

.center {
	text-align: center;
}

a img {
	border: none;
}

.navigation .alignleft	{ 
	padding: 20px 0;
	width: 50%;
	float: left;
	text-align: left;
}

.navigation .alignright {
	padding: 20px 0;
	width: 50%;
	float: right;
	text-align: right;
}

.datestamp div {
	color: #fff;
	text-align: center;
	line-height: 1.4em;
	font-family: <?php echo $font_families[$mandigo_options['font_family']]['datestamps']; ?>;
	padding: 1px;
	width: 2.9em;
}

.datestamp {
	display: inline;
	padding: 1px;
	float: left;
	margin-right: 1em;
}

.datestamp span {
	display: block;
}

.cal1 {
	font-size: 1.5em;
	letter-spacing: .2em;
	padding-left: .2em
}
.cal1x {
	letter-spacing: 0em;
	padding-left: 0em
}

.cal2 {
	font-weight: bold;
	font-size: 2em;
	line-height: .7em;
}

.cal3 {
	font-size: .8em;
	line-height: 1em;
<?php
	if ($mandigo_options['font_family'] == 'serif') {
?>
	margin-top: 0.4em;
<?php
	}
?>
}

.pages {
	display: inline;
	position: absolute;
	left: 0;
	bottom: 0;
	text-align: <?php echo $mandigo_options['header_navigation_position']; ?>;
	padding: .6em 0;
	width: 100%;
	list-style-type: none;
}

.pages li {
	display: inline;
	margin: 0 1em;
}

.pages a, .pages a:hover {
	font-size: 1.5em;
	font-weight: bold;
	color: #FFF;
	letter-spacing: -.08em !important; letter-spacing: -.1em;
}

.pages ul {
	display: none;
	position: absolute;
	background: #111;
	padding: 5px 0;
	z-index: 101;
}

.pages ul li {
	display: block;
	padding: 3px 0;
	margin: 3px 10px;
	border-top: 1px solid #333;
	font-size: 85%;
}

.pages ul li a {
	color: #CCC;
}

.wp-pagenavi {
	clear: both;
}

.wp-pagenavi span.pages {
	position: static;
}

.postinfo {
	padding-bottom: 1em;
}

.postinfo .posttitle {
	line-height: .9em;
}

.head_overlay {
	background: url(images/head_overlay.<?php echo ($ie ? 'gif' : 'png'); ?>);
}

#rss {
	float: right;
	padding-right: 4px;
}

.inline-widgets {
	padding-left: 0;
}

.inline-widgets li {
	list-style-type: none;
}

.inline-widgets li ul {
	padding-left: 2em;
}

.inline-widgets li li {
	list-style-type: circle;
}

.textwidget {
	padding-right: 10px;
}

.googlemap img {
	background: inherit;
}
/* End Various Tags & Classes*/



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
	background-image: url(schemes/<?php echo $mandigo_options['scheme']; ?>/images/star.gif);
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
