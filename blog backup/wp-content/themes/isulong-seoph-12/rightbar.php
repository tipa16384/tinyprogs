
<div id="rightbar">

	<div class="entries-rss"><span class="rss-entries"><a href="<?php bloginfo('url'); ?>/feed/" title="Entries RSS feed">Recent Entries</a></span>
	  <ul><?php c2c_get_recent_posts(10,"<li>%post_URL%</li>"); ?></ul>
	</div>
	<div class="comments-rss"><span class="rss-comments"><a href="<?php bloginfo('url'); ?>/comments/feed/" title="Comments RSS feed">Recent Comments</a></span>
  		<ul><?php get_recent_comments(); ?></ul>
	</div>

</div>
