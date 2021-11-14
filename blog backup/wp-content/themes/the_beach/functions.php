<?php

function kubrick_head() {
$head = "<style type='text/css'>n<!--";
$output = '';
if ( kubrick_header_image() ) {
$url =  kubrick_header_image_url() ;
$output .= "#header { background: url('$url') no-repeat bottom center; }n";
}
if ( false !== ( $color = kubrick_header_color() ) ) {
$output .= "#headerimg h1 a, #headerimg h1 a:visited, #headerimg .description { color: $color; }n";
}
if ( false !== ( $display = kubrick_header_display() ) ) {
$output .= "#headerimg { display: $display }n";
}
$foot = "--></style>n";
if ( '' != $output )
echo $head . $output . $foot;
}

add_action('wp_head', 'kubrick_head');

function kubrick_header_image() {
return apply_filters('kubrick_header_image', get_settings('kubrick_header_image'));
}

function kubrick_upper_color() {
if ( strstr( $url = kubrick_header_image_url(), 'header-img.php?' ) ) {
parse_str(substr($url, strpos($url, '?') + 1), $q);
return $q['upper'];
} else
return '69aee7';
}

function kubrick_lower_color() {
if ( strstr( $url = kubrick_header_image_url(), 'header-img.php?' ) ) {
parse_str(substr($url, strpos($url, '?') + 1), $q);
return $q['lower'];
} else
return '4180b6';
}

function kubrick_header_image_url() {
if ( $image = kubrick_header_image() )
$url = get_template_directory_uri() . '/images/' . $image;
else
$url = get_template_directory_uri() . '/images/kubrickheader.jpg';

return $url;
}

function kubrick_header_color() {
return apply_filters('kubrick_header_color', get_settings('kubrick_header_color'));
}

function kubrick_header_color_string() {
$color = kubrick_header_color();
if ( false === $color )
return 'white';

return $color;
}

function kubrick_header_display() {
return apply_filters('kubrick_header_display', get_settings('kubrick_header_display'));
}

function kubrick_header_display_string() {
$display = kubrick_header_display();
return $display ? $display : 'inline';
}

add_action('admin_menu', 'kubrick_add_theme_page');

function kubrick_add_theme_page() {
if ( $_GET['page'] == basename(__FILE__) ) {
if ( 'save' == $_REQUEST['action'] ) {
if ( isset($_REQUEST['njform']) ) {
if ( isset($_REQUEST['defaults']) ) {
delete_option('kubrick_header_image');
delete_option('kubrick_header_color');
delete_option('kubrick_header_display');
} else {
if ( '' == $_REQUEST['njfontcolor'] )
delete_option('kubrick_header_color');
else
update_option('kubrick_header_color', $_REQUEST['njfontcolor']);

if ( preg_match('/[0-9A-F]{6}|[0-9A-F]{3}/i', $_REQUEST['njuppercolor'], $uc) && preg_match('/[0-9A-F]{6}|[0-9A-F]{3}/i', $_REQUEST['njlowercolor'], $lc) ) {
$uc = ( strlen($uc[0]) == 3 ) ? $uc[0]{0}.$uc[0]{0}.$uc[0]{1}.$uc[0]{1}.$uc[0]{2}.$uc[0]{2} : $uc[0];
$lc = ( strlen($lc[0]) == 3 ) ? $lc[0]{0}.$lc[0]{0}.$lc[0]{1}.$lc[0]{1}.$lc[0]{2}.$lc[0]{2} : $lc[0];
update_option('kubrick_header_image', "header-img.php?upper=$uc&amp;lower=$lc");
}

if ( isset($_REQUEST['toggledisplay']) ) {
if ( false === get_settings('kubrick_header_display') )
update_option('kubrick_header_display', 'none');
else
delete_option('kubrick_header_display');
}
}
} else {

if ( isset($_REQUEST['headerimage']) ) {
if ( '' == $_REQUEST['headerimage'] )
delete_option('kubrick_header_image');
else
update_option('kubrick_header_image', $_REQUEST['headerimage']);
}

if ( isset($_REQUEST['fontcolor']) ) {
if ( '' == $_REQUEST['fontcolor'] )
delete_option('kubrick_header_color');
else
update_option('kubrick_header_color', $_REQUEST['fontcolor']);
}

if ( isset($_REQUEST['fontdisplay']) ) {
if ( '' == $_REQUEST['fontdisplay'] || 'inline' == $_REQUEST['fontdisplay'] )
delete_option('kubrick_header_display');
else
update_option('kubrick_header_display', 'none');
}
}
//print_r($_REQUEST);
header("Location: themes.php?page=functions.php&saved=true");
die;
}
add_action('admin_head', 'kubrick_theme_page_head');
}
add_theme_page('Customize Header', 'Header Image and Color', 'edit_themes', basename(__FILE__), 'kubrick_theme_page');
}

function kubrick_theme_page_head() {
?>
<script type="text/javascript" src="../wp-includes/js/colorpicker.js"></script>
<script type='text/javascript'>
function pickColor(color) {
ColorPicker_targetInput.value = color;
kUpdate(ColorPicker_targetInput.id);
}
function PopupWindow_populate(contents) {
contents += '<br /><p style="text-align:center;margin-top:0px;"><input type="button" value="Close Color Picker" onclick="cp.hidePopup('prettyplease')"></input></p>';
this.contents = contents;
this.populated = false;
}
function PopupWindow_hidePopup(magicword) {
if ( magicword != 'prettyplease' )
return false;
if (this.divName != null) {
if (this.use_gebi) {
document.getElementById(this.divName).style.visibility = "hidden";
}
else if (this.use_css) {
document.all[this.divName].style.visibility = "hidden";
}
else if (this.use_layers) {
document.layers[this.divName].visibility = "hidden";
}
}
else {
if (this.popupWindow && !this.popupWindow.closed) {
this.popupWindow.close();
this.popupWindow = null;
}
}
return false;
}
function colorSelect(t,p) {
if ( cp.p == p && document.getElementById(cp.divName).style.visibility != "hidden" )
cp.hidePopup('prettyplease');
else {
cp.p = p;
cp.select(t,p);
}
}
function PopupWindow_setSize(width,height) {
this.width = 162;
this.height = 210;
}

var cp = new ColorPicker();
function advUpdate(val, obj) {
document.getElementById(obj).value = val;
kUpdate(obj);
}
function kUpdate(oid) {
if ( 'uppercolor' == oid || 'lowercolor' == oid ) {
uc = document.getElementById('uppercolor').value.replace('#', '');
lc = document.getElementById('lowercolor').value.replace('#', '');
hi = document.getElementById('headerimage');
hi.value = 'header-img.php?upper='+uc+'&lower='+lc;
document.getElementById('header').style.background = 'url("<?php echo get_template_directory_uri(); ?>/images/'+hi.value+'") center no-repeat';
document.getElementById('advuppercolor').value = '#'+uc;
document.getElementById('advlowercolor').value = '#'+lc;
}
if ( 'fontcolor' == oid ) {
document.getElementById('header').style.color = document.getElementById('fontcolor').value;
document.getElementById('advfontcolor').value = document.getElementById('fontcolor').value;
}
if ( 'fontdisplay' == oid ) {
document.getElementById('headerimg').style.display = document.getElementById('fontdisplay').value;
}
}
function toggleDisplay() {
td = document.getElementById('fontdisplay');
td.value = ( td.value == 'none' ) ? 'inline' : 'none';
kUpdate('fontdisplay');
}
function toggleAdvanced() {
a = document.getElementById('jsAdvanced');
if ( a.style.display == 'none' )
a.style.display = 'block';
else
a.style.display = 'none';
}
function kDefaults() {
document.getElementById('headerimage').value = '';
document.getElementById('advuppercolor').value = document.getElementById('uppercolor').value = '#69aee7';
document.getElementById('advlowercolor').value = document.getElementById('lowercolor').value = '#4180b6';
document.getElementById('header').style.background = 'url("<?php echo get_template_directory_uri(); ?>/images/kubrickheader.jpg") center no-repeat';
document.getElementById('header').style.color = '#FFFFFF';
document.getElementById('advfontcolor').value = document.getElementById('fontcolor').value = '';
document.getElementById('fontdisplay').value = 'inline';
document.getElementById('headerimg').style.display = document.getElementById('fontdisplay').value;
}
function kRevert() {
document.getElementById('headerimage').value = '<?php echo kubrick_header_image(); ?>';
document.getElementById('advuppercolor').value = document.getElementById('uppercolor').value = '#<?php echo kubrick_upper_color(); ?>';
document.getElementById('advlowercolor').value = document.getElementById('lowercolor').value = '#<?php echo kubrick_lower_color(); ?>';
