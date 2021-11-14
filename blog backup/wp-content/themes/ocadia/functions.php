<?php

if ( function_exists('register_sidebar') )
    register_sidebar(array(
		'before_widget' => '<li id="%1$s" class="widget %2$s"><div>',
		'after_widget' => "</div></li>\n",
		'before_title' => '<h2>',
		'after_title' => "</h2>\n",
    ));

include(dirname(__FILE__).'/themetoolkit.php');

themetoolkit(
	'ocadia',
	array(    
	'sidebar' => 'Sidebar transparency {radio|transparent|Transparent|opaque|Opaque}',
	),
	__FILE__
);
	
function ocadia_sidebar() {
	global $ocadia;
	if ($ocadia->option['sidebar'] == "opaque") { 
	  echo '#sidebar ul {
			  background: url('; bloginfo('template_directory'); echo '/images/sidebar2b.gif) repeat-y;
			}
			#sidebar ul li {
			  background: url('; bloginfo('template_directory'); echo '/images/sidebar-bottomb.gif) no-repeat bottom left;
			}
			#sidebar h2 {
			  background: url('; bloginfo('template_directory'); echo '/images/sidebar-topb.gif) no-repeat;
			}
			#sidebar #search p, .widget_search div div {			
			  background: url('; bloginfo('template_directory'); echo '/images/sidebar-topb.gif) no-repeat;
			}
			#calendar div {
			  background: url('; bloginfo('template_directory'); echo '/images/sidebar-topb.gif) no-repeat;	
			}';
	} 
}

if (!$ocadia->is_installed()) { 
	$set_defaults['sidebar'] = 'transparent'; 
	$result = $ocadia->store_options($set_defaults); 
} 

?>