<?php
	add_action('admin_menu', 'add_mandigo_readme_page');
	
	function add_mandigo_readme_page()  {
		global $dirs;
		add_theme_page(
			'README',
			'<img src="'. $dirs['www']['backend'] .'images/attention_catcher.png" alt="" /> README',
			'switch_themes',
			'README',
			'mandigo_readme_page'
		);
	}
	
	// the readme page
	function mandigo_readme_page() {
		$content = file_get_contents(TEMPLATEPATH.'/README.txt');
		$content = htmlspecialchars($content);
		$content = preg_replace('/(http:\S+)/', '<a href="\1">\1</a>', $content);
		echo '<div class="wrap">';
		echo '<pre>';
		echo $content;
		echo '</pre>';
		echo '</div>';
	}
?>
