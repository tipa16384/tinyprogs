<?php $arjunaOptions = arjuna_get_options(); ?>
<?php
if ($arjunaOptions['sidebar']['display'] == 'both') {
	$available = 920;
	$sidebarLeft = $arjunaOptions['sidebar']['widthLeft'];
	$sidebarRight = $arjunaOptions['sidebar']['widthRight'];
	$contentArea = $available - $sidebarLeft - $sidebarRight;
	
	$sidebarLeft_leftRight = floor(($sidebarLeft - 50) / 2);
	$sidebarRight_leftRight = floor(($sidebarRight - 50) / 2);
	
	print '<style type="text/css">';
		print '.contentWrapper .contentArea {width:'.$contentArea.'px;}';
		print '.contentWrapper .sidebarsLeft {width:'.$sidebarLeft.'px;}';
		print '.contentWrapper .sidebarsRight {width:'.$sidebarRight.'px;}';
		print '.contentWrapper .sidebarsLeft .sidebarLeft, .contentWrapper .sidebarsLeft .sidebarRight {width:'.$sidebarLeft_leftRight.'px;}';
		print '.contentWrapper .sidebarsRight .sidebarLeft, .contentWrapper .sidebarsRight .sidebarRight {width:'.$sidebarRight_leftRight.'px;}';
	print '</style>';
} elseif ($arjunaOptions['sidebar']['display'] == 'left') {
	$available = 920;
	$sidebarLeft = $arjunaOptions['sidebar']['widthLeft'];
	$contentArea = $available - $sidebarLeft;
	
	$sidebarLeft_leftRight = floor(($sidebarLeft - 50) / 2);
	
	print '<style type="text/css">';
		print '.contentWrapper .contentArea {width:'.$contentArea.'px;}';
		print '.contentWrapper .sidebarsLeft {width:'.$sidebarLeft.'px;}';
		print '.contentWrapper .sidebarsLeft .sidebarLeft, .contentWrapper .sidebarsLeft .sidebarRight {width:'.$sidebarLeft_leftRight.'px;}';
	print '</style>';
} elseif ($arjunaOptions['sidebar']['display'] == 'right') {
	$available = 920;
	$sidebarRight = $arjunaOptions['sidebar']['widthRight'];
	$contentArea = $available - $sidebarRight;
	
	$sidebarRight_leftRight = floor(($sidebarRight - 50) / 2);
	
	print '<style type="text/css">';
		print '.contentWrapper .contentArea {width:'.$contentArea.'px;}';
		print '.contentWrapper .sidebarsRight {width:'.$sidebarRight.'px;}';
		print '.contentWrapper .sidebarsRight .sidebarLeft, .contentWrapper .sidebarsRight .sidebarRight {width:'.$sidebarRight_leftRight.'px;}';
	print '</style>';
}
?>