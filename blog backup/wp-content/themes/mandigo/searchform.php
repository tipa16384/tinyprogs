<?php 
	global $dirs;
?>
<form method="get" id="searchform" action="<?php bloginfo('home'); ?>/">
<div><input type="text" value="<?php echo wp_specialchars($s, 1); ?>" name="s" id="s" /> 
<input type="image" id="searchsubmit" src="<?php echo $dirs['www']['scheme']; ?>images/search.gif" />
</div>
</form>
