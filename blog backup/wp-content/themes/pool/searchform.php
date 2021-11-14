<form id="searchform" method="get" action="<?php bloginfo('home'); ?>/">
<input type="text" name="s" id="s" size="17" value="type, hit enter" onblur="setTimeout('closeResults()',2000); if (this.value == '') {this.value = '';}"  onfocus="if (this.value == 'type, hit enter') {this.value = '';}" />
<div style="visibility:hidden">
	<input name="sbutt" type="submit" value="Find" alt="Submit"  />
	</div>
</form>