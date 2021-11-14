<div id="right">

<?php if ( !function_exists('dynamic_sidebar')
        || !dynamic_sidebar(2) ) : ?>
        
	<?php include (TEMPLATEPATH . '/searchform.php'); ?>
	<?php endif; ?>

</div> <!-- end of right -->