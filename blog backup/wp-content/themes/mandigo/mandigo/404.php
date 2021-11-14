<?php
	global $mandigo_options, $dirs;

	get_header();

?>
	<td id="content" class="narrowcolumn"<?php if (mandigo_sidebox_conditions()) { ?> rowspan="2"<?php } ?>>

		<div class="four04">
			<span class="four04-big">404</span><br />
			Not Found
		</div>

	</td>

<?php
	// if we have at least one sidebar to display
	if ($mandigo_options['sidebar_count']) {
		if (mandigo_sidebox_conditions())
			include (TEMPLATEPATH . '/sidebox.php');
	
		include (TEMPLATEPATH . '/sidebar.php');

		// if this is a 3-column layout
		if ($mandigo_options['layout_width'] == 1024 && $mandigo_options['sidebar_count'] == 2)
			include (TEMPLATEPATH . '/sidebar2.php');
	}

	get_footer(); 
?>
