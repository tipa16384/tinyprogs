<?php 
	// this file defines the default second sidebar
	// if you are using widgets, you do not need to edit this file
?>
	<td id="sidebar2">
	<ul class="sidebars">
<?php
	if (!function_exists('dynamic_sidebar') || !dynamic_sidebar('Sidebar 2')) {
		widget_mandigo_meta();
	}
?>
	</ul>
	</td>
