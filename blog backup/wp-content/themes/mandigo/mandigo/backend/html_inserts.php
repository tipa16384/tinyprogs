<?php
	add_action('admin_menu', 'add_mandigo_inserts_page');

	function add_mandigo_inserts_page() {
		global $dirs;
		add_theme_page(
			'HTML Inserts',
			'<img src="'. $dirs['www']['backend'] .'/images/attention_catcher.png" alt="" /> HTML Inserts',
			'edit_themes',
			'HTML Inserts',
			'mandigo_inserts_page'
		);
	}
	
	function mandigo_set_insert($key, $value) {
		update_option('mandigo_inserts_'.$key, str_replace("\\", "", $value));
	}
	
	// the HTML inserts page
	function mandigo_inserts_page() {
		if (isset($_POST['updated'])) {
			mandigo_set_insert('header',  $_POST['header' ]);
			mandigo_set_insert('body'  ,  $_POST['body'   ]);
			mandigo_set_insert('top'   ,  $_POST['top'    ]);
			mandigo_set_insert('footer',  $_POST['footer' ]);
			mandigo_set_insert('veryend', $_POST['veryend']);
			echo '<div class="updated fade"><p>Options updated.</p></div>';
		}

	echo '
		<div class="wrap">
		<form name="mandigo_options_form" method="post" action="?page=HTML%20Inserts">
		<input type="hidden" name="updated" value="1" />
		
		<h2>Mandigo Options <span class="submit" style="border: none;"><input type="submit" value="'. __('Update Inserts &raquo;') .'"/></span></h2>
		
		<fieldset class="options">
		<legend>HTML Inserts</legend>

		<p>The fields on this page allow you to save pieces of code required by third-party plugins and widgets. You can also use them to save Google Maps/Analytics/AdSense javascript snippets, or whatever you want.</p>
		
		<p>Putting your code snippets in these fields rather than editing the source files will keep the theme in an upgradable state.</p>

		<p>Please note that NO validation is made on the field values, so be careful not to paste invalid code. Also note that backslashes will be stripped.</p>

		<label><b>header.php</b></label><br/>
                right before &lt;/HEAD&gt; (<i>useful for links to external stylesheets, javascript files. This is also the <strong>best place</strong> for your css rules</i>):<br />
		<textarea name="header" rows=7 style="width: 100%">'. str_replace("\\", "", get_option('mandigo_inserts_header')) .'</textarea><br /><br />

                custom &lt;BODY&gt; tag (<i>useful for onload actions</i>):<br />
		<textarea name="body" rows=1 style="width: 100%">'. str_replace("\\", "", get_option('mandigo_inserts_body')) .'</textarea><br /><br />

                right before the content and sidebars area. This differs from the top widget container in that it displays on all pages, and it spans the whole layout width.<br />
		<textarea name="top" rows=7 style="width: 100%">'. str_replace("\\", "", get_option('mandigo_inserts_top')) .'</textarea><br /><br />

		<label><b>footer.php</b></label><br/>
                before the "Powered by WordPress" credits, still inside the #main div. This differs from the bottom widget container in that it displays on all pages, and it spans the whole layout width.<br />
		<textarea name="footer" rows=7 style="width: 100%">'. str_replace("\\", "", get_option('mandigo_inserts_footer')) .'</textarea><br /><br />

                outside the main frame, right before the closing &lt;/body&gt; tag. This is the best place for your Google analytics code and other final sippets.<br />
		<textarea name="veryend" rows=7 style="width: 100%">'. str_replace("\\", "", get_option('mandigo_inserts_veryend')) .'</textarea><br /><br />

		</fieldset>
					
		<p class="submit"><input type="submit" name="Submit" value="'.__('Update Inserts &raquo;').'"/></p>
		</form>
		</div>
		<script type="text/javascript">
			jQuery(document).ready(function() { jQuery("body").addClass("mandigo-options"); });
		</script>
		';
  }
?>
