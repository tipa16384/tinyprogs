<?php

if ( function_exists('register_sidebar') )
	register_sidebar(array(
		'name' => 'Left Sidebar',
		'before_widget' => '<ul>',
		'after_widget' => '</ul>',
		'before_title' => '<li class="listHeader"><h2>',
		'after_title' => '</h2></li>',
	));

if ( function_exists('register_sidebar') )
	register_sidebar(array(
		'name' => 'Right Sidebar',
		'before_widget' => '<ul>',
		'after_widget' => '</ul>',
		'before_title' => '<li class="listHeader"><h2>',
		'after_title' => '</h2></li>',
	));



function get_newcalendar($daylength = 1) {
	global $wpdb, $m, $monthnum, $year, $timedifference, $month, $month_abbrev, $weekday, $weekday_initial, $weekday_abbrev, $posts;

	$now = current_time('mysql');

	// Quick check. If we have no posts yet published, abort!
	if ( !$posts ) {
		$gotsome = $wpdb->get_var("SELECT ID from $wpdb->posts WHERE post_status = 'publish' AND post_date < '$now' ORDER BY post_date DESC LIMIT 1");
		if ( !$gotsome )
			return;
	}

	if ( isset($_GET['w']) )
		$w = ''.intval($_GET['w']);

	// week_begins = 0 stands for Sunday
	$week_begins = intval(get_settings('start_of_week'));
	$add_hours = intval(get_settings('gmt_offset'));
	$add_minutes = intval(60 * (get_settings('gmt_offset') - $add_hours));

	// Let's figure out when we are
	if ( !empty($monthnum) && !empty($year) ) {
		$thismonth = ''.zeroise(intval($monthnum), 2);
		$thisyear = ''.intval($year);
	} elseif ( !empty($w) ) {
		// We need to get the month from MySQL
		$thisyear = ''.intval(substr($m, 0, 4));
		$d = (($w - 1) * 7) + 6; //it seems MySQL's weeks disagree with PHP's
		$thismonth = $wpdb->get_var("SELECT DATE_FORMAT((DATE_ADD('${thisyear}0101', INTERVAL $d DAY) ), '%m')");
	} elseif ( !empty($m) ) {
		$calendar = substr($m, 0, 6);
		$thisyear = ''.intval(substr($m, 0, 4));
		if ( strlen($m) < 6 )
				$thismonth = '01';
		else
				$thismonth = ''.zeroise(intval(substr($m, 4, 2)), 2);
	} else {
		$thisyear = gmdate('Y', current_time('timestamp'));
		$thismonth = gmdate('m', current_time('timestamp'));
	}

	$unixmonth = mktime(0, 0 , 0, $thismonth, 1, $thisyear);

	// Get the next and previous month and year with at least one post
	$previous = $wpdb->get_row("SELECT DISTINCT MONTH(post_date) AS month, YEAR(post_date) AS year
		FROM $wpdb->posts
		WHERE post_date < '$thisyear-$thismonth-01'
		AND post_status = 'publish'
			ORDER BY post_date DESC
			LIMIT 1");
	$next = $wpdb->get_row("SELECT	DISTINCT MONTH(post_date) AS month, YEAR(post_date) AS year
		FROM $wpdb->posts
		WHERE post_date >	'$thisyear-$thismonth-01'
		AND post_date < '$now'
		AND MONTH( post_date ) != MONTH( '$thisyear-$thismonth-01' )
		AND post_status = 'publish' 
			ORDER	BY post_date ASC
			LIMIT 1");

	echo '<table summary="calendar" id="wp-calendar">
	<caption>' . $month[zeroise($thismonth, 2)] . ' ' . date('Y', $unixmonth) . '</caption>
	<thead>
	<tr>';

	$day_abbrev = $weekday_initial;
	if ( $daylength > 1 )
		$day_abbrev = $weekday_abbrev;

	$myweek = array();

	for ( $wdcount=0; $wdcount<=6; $wdcount++ ) {
		$myweek[]=$weekday[($wdcount+$week_begins)%7];
	}

	foreach ( $myweek as $wd ) {
		echo "\n\t\t<th abbr=\"$wd\" scope=\"col\" title=\"$wd\">" . $day_abbrev[$wd] . '</th>';
	}

	echo '
	</tr>
	</thead>

	<tfoot>
	<tr>';

	if ( $previous ) {
		echo "\n\t\t".'<td abbr="' . $month[zeroise($previous->month, 2)] . '" colspan="3" id="prev"><a href="' .
		get_month_link($previous->year, $previous->month) . '" title="' . sprintf(__('View posts for %1$s %2$s'), $month[zeroise($previous->month, 2)],
			date('Y', mktime(0, 0 , 0, $previous->month, 1, $previous->year))) . '">&laquo; ' . $month_abbrev[$month[zeroise($previous->month, 2)]] . '</a></td>';
	} else {
		echo "\n\t\t".'<td colspan="3" id="prev" class="pad">&nbsp;</td>';
	}

	echo "\n\t\t".'<td class="pad">&nbsp;</td>';

	if ( $next ) {
		echo "\n\t\t".'<td abbr="' . $month[zeroise($next->month, 2)] . '" colspan="3" id="next"><a href="' .
		get_month_link($next->year, $next->month) . '" title="' . sprintf(__('View posts for %1$s %2$s'), $month[zeroise($next->month, 2)],
			date('Y', mktime(0, 0 , 0, $next->month, 1, $next->year))) . '">' . $month_abbrev[$month[zeroise($next->month, 2)]] . ' &raquo;</a></td>';
	} else {
		echo "\n\t\t".'<td colspan="3" id="next" class="pad">&nbsp;</td>';
	}

	echo '
	</tr>
	</tfoot>

	<tbody>
	<tr>';

	// Get days with posts
	$dayswithposts = $wpdb->get_results("SELECT DISTINCT DAYOFMONTH(post_date)
		FROM $wpdb->posts WHERE MONTH(post_date) = '$thismonth'
		AND YEAR(post_date) = '$thisyear'
		AND post_status = 'publish'
		AND post_date < '" . current_time('mysql') . '\'', ARRAY_N);
	if ( $dayswithposts ) {
		foreach ( $dayswithposts as $daywith ) {
			$daywithpost[] = $daywith[0];
		}
	} else {
		$daywithpost = array();
	}



	if ( strstr($_SERVER['HTTP_USER_AGENT'], 'MSIE') || strstr(strtolower($_SERVER['HTTP_USER_AGENT']), 'camino') || strstr(strtolower($_SERVER['HTTP_USER_AGENT']), 'safari') )
		$ak_title_separator = "\n";
	else
		$ak_title_separator = ', ';

	$ak_titles_for_day = array();
	$ak_post_titles = $wpdb->get_results("SELECT post_title, DAYOFMONTH(post_date) as dom "
		."FROM $wpdb->posts "
		."WHERE YEAR(post_date) = '$thisyear' "
		."AND MONTH(post_date) = '$thismonth' "
		."AND post_date < '".current_time('mysql')."' "
		."AND post_status = 'publish'"
	);
	if ( $ak_post_titles ) {
		foreach ( $ak_post_titles as $ak_post_title ) {
				if ( empty($ak_titles_for_day['day_'.$ak_post_title->dom]) )
					$ak_titles_for_day['day_'.$ak_post_title->dom] = '';
				if ( empty($ak_titles_for_day["$ak_post_title->dom"]) ) // first one
					$ak_titles_for_day["$ak_post_title->dom"] = str_replace('"', '&quot;', wptexturize($ak_post_title->post_title));
				else
					$ak_titles_for_day["$ak_post_title->dom"] .= $ak_title_separator . str_replace('"', '&quot;', wptexturize($ak_post_title->post_title));
		}
	}


	// See how much we should pad in the beginning
	$pad = calendar_week_mod(date('w', $unixmonth)-$week_begins);
	if ( 0 != $pad )
		echo "\n\t\t".'<td colspan="'.$pad.'" class="pad">&nbsp;</td>';

	$daysinmonth = intval(date('t', $unixmonth));
	for ( $day = 1; $day <= $daysinmonth; ++$day ) {
		if ( isset($newrow) && $newrow )
			echo "\n\t</tr>\n\t<tr>\n\t\t";
		$newrow = false;

		if ( $day == gmdate('j', (time() + (get_settings('gmt_offset') * 3600))) && $thismonth == gmdate('m', time()+(get_settings('gmt_offset') * 3600)) && $thisyear == gmdate('Y', time()+(get_settings('gmt_offset') * 3600)) )
			echo '<td id="today">';
		else
			echo '<td>';

		if ( in_array($day, $daywithpost) ) // any posts today?
				echo '<a href="' . get_day_link($thisyear, $thismonth, $day) . "\" title=\"$ak_titles_for_day[$day]\">$day</a>";
		else
			echo $day;
		echo '</td>';

		if ( 6 == calendar_week_mod(date('w', mktime(0, 0 , 0, $thismonth, $day, $thisyear))-$week_begins) )
			$newrow = true;
	}

	$pad = 7 - calendar_week_mod(date('w', mktime(0, 0 , 0, $thismonth, $day, $thisyear))-$week_begins);
	if ( $pad != 0 && $pad != 7 )
		echo "\n\t\t".'<td class="pad" colspan="'.$pad.'">&nbsp;</td>';

	echo "\n\t</tr>\n\t</tbody>\n\t</table>";
}




?>