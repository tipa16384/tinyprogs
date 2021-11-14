<?php 
	// this file defines the sidebox, a special widget container that
	// spans two sidebars when they are aligned on the right side

	global $wp_registered_sidebars;
	if (function_exists('wp_get_sidebars_widgets')) // WP2.2+
		$_widgets = wp_get_sidebars_widgets(); // needed, for some reason $sidebars_widgets is empty on some pages
	if ($wp_registered_sidebars) {
		foreach ($wp_registered_sidebars as $key => $value) {
			if ($value['name'] == 'Mandigo Sidebox')
				$index_sidebox = $key;
		}
	}
	if (function_exists('dynamic_sidebar') && $_widgets[$index_sidebox]) {
?>
	<td colspan="2" id="sidebox">
	<ul class="sidebars">
	<?php dynamic_sidebar('Mandigo Sidebox'); ?>
	</ul>
	</td>
</tr>
<tr>
<?php } ?>
