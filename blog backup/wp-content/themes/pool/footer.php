<div id="footer">
	<p>&copy; 
	<?php 
	$thisYear = mktime(); $thisYear = strftime("%Y", $thisYear);
	echo $thisYear,' ';
	bloginfo('name');
	?> | powered by <a href="http://wordpress.org">WordPress</a> | Designed by <a href="http://www.dewdropwebs.com">DewDrop</a> | <?php wp_loginout(); ?>
	</p>
</div><!-- end footer -->

</div>
</body>
</html>