<?php
/**
 * @package XFire_Stats
 * @author Brenda Holloway
 * @version 0.2
 */
/*
Plugin Name: Xfire Stats
Plugin URI: http://westkarana.com/index.php/xfire-plugin
Description: Displays your XFire stats!
Author: Brenda Holloway
Version: 0.2
Author URI: http://westkarana.com
*/

function xfirestats_init() {

	if ( !function_exists('register_sidebar_widget') || !function_exists('register_widget_control'))
		return;

function get_web_page($url) {
	$options = array(
		CURLOPT_RETURNTRANSFER => true,
		CURLOPT_HEADER => false,
		CURLOPT_FOLLOWLOCATION => true,
		CURLOPT_ENCODING => "",
		CURLOPT_USERAGENT => "wordpress widget",
		CURLOPT_AUTOREFERER => true,
		CURLOPT_CONNECTTIMEOUT => 120,
		CURLOPT_TIMEOUT => 120,
		CURLOPT_MAXREDIRS => 10);

	$ch = curl_init($url);
	curl_setopt_array( $ch, $options );
	$content = curl_exec( $ch );
	$err = curl_errno( $ch );
	$errmsg = curl_error( $ch );
	$xmlheader = curl_getinfo( $ch );
	curl_close( $ch );

	$xmlheader['errno'] = $err;
	$xmlheader['errmsg'] = $errmsg;
	$xmlheader['content'] = $content;
	return $xmlheader;
}

$game = "No game";
$time = 0;
$lasttag = "none";
$gameid = "";
$firstline = true;
$output = "";
$gamearr = array();

function startTag($parser, $data, $attrs) {
	global $lasttag;
	$lasttag = $data;
	//echo '<li>tag is ' . $data . '</li>';
}

function formatTime($time) {
		$hours = (int)($time/3600);
		$mins = (int)($time/60) - ($hours*60);
		$secs = $time%60;
		if ($secs >= 30) $mins++;
		if ($mins > 60) { $hours++; $mins-=60; }
		return sprintf("%d:%02d",$hours,$mins);
}

function endTag($parser, $data) {
	global $game, $time, $gameid, $gamearr;
	if (!strcmp($data,"GAME") && (int)$time > 0) {
		$gamearr[$gameid] = array(-((int)$time),$gameid,(int)$time,$game);
	}
}

function contents($parser, $data) {
	global $lasttag, $game, $time, $gameid;
	$data = trim($data);
	if (strlen($data) == 0) return;
	//echo "<li>$lasttag data is $data</li>";

	if (!strcmp($lasttag,"LONGNAME"))
		$game = $data;
	if (!strcmp($lasttag,"WEEKTIME"))
		$time = $data;
	if (!strcmp($lasttag,"SHORTNAME"))
		$gameid = $data;
}

function xfirestats_widget($args) {
	global $lasttag, $game, $time, $gameid, $output, $firstline, $gamearr;

	extract($args);

	$game = "No game";
	$time = 0;
	$lasttag = "none";
	$gameid = "";
	$firstline = true;
	$gamearr = array();
	$output = /*"<ul>";*/ '<table border=0 cellspacing=2 width=100%>';

   $title = get_option('xfirestats-title');
   
   if (empty($title))
   	$title = "XFire Weekly Stats";

	echo $before_widget;
	echo $before_title . $title . $after_title;

   // Collect our widget's options.
   $player = get_option('xfirestats-playername');

	if (empty($player)) {
		$output .= '<tr><td align=center><b>No XFire Id assigned</b></td></tr>';
	} else {

		$url = 'http://www.xfire.com/xml/' . $player . '/gameplay/';
		$xmlheader = get_web_page( $url );

		$xml_parser = xml_parser_create();
		xml_set_element_handler($xml_parser,"startTag","endTag");
		xml_set_character_data_handler($xml_parser,"contents");

		if (!(xml_parse($xml_parser, $xmlheader['content'], false))){
			die("Error on line " . xml_get_current_line_number($xml_parser));
		}

		xml_parser_free($xml_parser);
		
		sort($gamearr);
		
		foreach ($gamearr as $key => $arr) {
			$output .= '<tr><td valign=top align=left>';
			$output .= '<a href="http://http://www.xfire.com/games/'.$arr[1].'/">';
			$output .= $arr[3];
			$output .= '</a></td><td valign=top align=right>';
			$output .= formattime($arr[2]);
			$output .= '</td></tr>';
		}
	}
		
	$output .= /*'</ul>';*/ '</table>';
	
	echo $output;
	
	echo $after_widget;
}

    function widget_mywidget_control() {

        // Collect our widget's options.
        $player = get_option('xfirestats-playername');
        $title = get_option('xfirestats-title');
        
        // This is for handing the control form submission.
        if ( $_POST['xfirestats-submit'] ) {
            // Clean up control form submission options
            $newplayer = strip_tags(stripslashes($_POST['xfirestats-player']));
            $newtitle = strip_tags(stripslashes($_POST['xfirestats-title']));
            
            if (strcmp($player,$newplayer)) {
            	$player = $newplayer;
	            update_option('xfirestats-playername', $player);
            }
            
            if (strcmp($title,$newtitle)) {
            	$title = $newtitle;
	            update_option('xfirestats-title', $title);
            }
        }

        // Format options as valid HTML. Hey, why not.
        $player = htmlspecialchars($player, ENT_QUOTES);
        $title = htmlspecialchars($title, ENT_QUOTES);

// The HTML below is the control form for editing options.
?>
        <div>
        <label for="xfirestats-player" style="line-height:35px;display:block;">XFire Id: <input type="text" id="xfirestats-player" name="xfirestats-player" value="<?php echo $player; ?>" /></label>
        <label for="xfirestats-title" style="line-height:35px;display:block;">Widget Title: <input type="text" id="xfirestats-title" name="xfirestats-title" value="<?php echo $title; ?>" /></label>
        <input type="hidden" name="xfirestats-submit" id="xfirestats-submit" value="1" />
        </div>
    <?php
    // end of widget_mywidget_control()
    }

register_sidebar_widget('XFire Stats', 'xfirestats_widget');
    // This registers the (optional!) widget control form.
    register_widget_control('XFire Stats', 'widget_mywidget_control');
}

if(defined('xfs_loaded')) {
	return;
}
define('xfs_loaded', 1);

add_action('plugins_loaded', 'xfirestats_init');

?>
