    <div id="back">
    <?php if (isset($_SERVER["HTTP_REFERER"])) { ?>
        <span>&laquo; <a href="<?php echo $_SERVER['HTTP_REFERER'];?>" title="go back">go back</a></span>
    <?php } ?>        
        <a href="#documentContent" title="up to the page content">up to content</a> &raquo;</div>
    </div>
</div>


<div id="column2">
<?php if ( function_exists('dynamic_sidebar') && dynamic_sidebar('Left Sidebar') ) : else : ?>

<!-- Author information is disabled per default. Uncomment and fill in your details if you want to use it.
	<ul><li class="listHeader"><h2><?php _e('Author'); ?></h2></li>
		<li><p>A little something about you, the author. Nothing lengthy, just an overview.</p></li>
    </ul>
-->

    <ul><li class="listHeader"><h2><?php _e('Calendar'); ?></h2></li>
        <li class="calendar"><?php get_newcalendar() ?></li>
    </ul>

<?php if (function_exists('wp_theme_switcher')) { ?>
	<ul><li class="listHeader"><h2><?php _e('Themes'); ?></h2>
		<?php wp_theme_switcher('dropdown'); ?>
	</li></ul>
<?php } ?>

    <ul><li class="listHeader"><h2><?php _e('Latest Posts'); ?></h2></li>
        <?php wp_get_archives('type=postbypost&limit=10'); ?>
    </ul>

    <ul><li class="listHeader"><h2><?php _e('Archives'); ?></h2></li>
        <?php wp_get_archives('type=monthly'); ?>
    </ul>

    <ul><li class="listHeader"><h2><?php _e('Categories'); ?></h2></li>
        <?php wp_list_cats('sort_column=name&optioncount=1&hierarchical=0'); ?>
    </ul>

<?php endif; ?>
</div>

<div id="column3">
<?php if ( function_exists('dynamic_sidebar') && dynamic_sidebar('Right Sidebar') ) : else : ?>

	<ul class="icons"><li class="listHeader"><h2><?php _e('Subscribe'); ?></h2></li>	 
        <li><a href="<?php bloginfo('rss2_url'); ?>" title="Posts RSS feed" class="iconrss">rss posts</a></li>
		<li><a href="<?php bloginfo('comments_rss2_url'); ?>" title="Posts RSS feed" class="iconrss">rss comments</a></li>
    </ul>


<?php if (is_single()) { ?>
    <ul class="icons"><li class="listHeader"><h2><?php _e('Spread the Word'); ?></h2></li>
        <li><a class="s_delicious" href="http://del.icio.us/post?title=<?php the_title(); ?>&amp;url=<?php echo get_permalink() ?>" title="Submit <?php the_title(); ?> to del.icio.us" rel="nofollow">delicious</a></li>
        <li><a class="s_digg" href="http://digg.com/submit?phase=2&amp;title=<?php the_title(); ?>&amp;url=<?php echo get_permalink() ?>" title="Submit <?php the_title(); ?> to digg" rel="nofollow">digg</a></li>
        <li><a class="s_technorati" href="http://www.technorati.com/faves?add=<?php echo get_permalink() ?>" title="Submit <?php the_title(); ?> to technorati" rel="nofollow">technorati</a></li>
        <li><a class="s_reddit" href="http://reddit.com/submit?title=<?php the_title(); ?>&amp;url=<?php echo get_permalink() ?>" title="Submit <?php the_title(); ?> to reddit" rel="nofollow">reddit</a></li>
        <li><a class="s_magnolia" href="http://ma.gnolia.com/beta/bookmarklet/add?title=<?php the_title(); ?>&amp;description=<?php the_title(); ?>&amp;url=<?php echo get_permalink() ?>" title="Submit <?php the_title(); ?> to magnolia" rel="nofollow">magnolia</a></li>
        <li><a class="s_stumbleupon" href="http://www.stumbleupon.com/submit?title=<?php the_title(); ?>&amp;url=<?php echo get_permalink() ?>" title="Submit <?php the_title(); ?> to stumbleupon" rel="nofollow">stumbleupon</a></li>
        <li><a class="s_yahoo" href="http://myweb2.search.yahoo.com/myresults/bookmarklet?title=<?php the_title(); ?>&amp;popup=true&amp;u=<?php echo get_permalink() ?>" title="Submit <?php the_title(); ?> to yahoo bookmarks" rel="nofollow">yahoo</a></li>
        <li><a class="s_google" href="http://www.google.com/bookmarks/mark?op=add&amp;title=<?php the_title(); ?>&amp;bkmk=<?php echo get_permalink() ?>" title="Submit <?php the_title(); ?> to google bookmarks" rel="nofollow">google</a></li>
    </ul>
<?php } ?>

    <ul><li class="listHeader"><h2><?php _e('Blogroll'); ?></h2></li>
        <?php wp_get_linksbyname('Blogroll', 'before=<li>&after=</li>&orderby=name&show_description=0&show_updated=1') ?>
    </ul>

	<ul><li class="listHeader"><h2><?php _e('Meta'); ?></h2></li>
        <?php wp_register(); ?>
        <li><?php wp_loginout(); ?></li>
    	<li><a href="http://validator.w3.org/check/referer" title="Hopefully this page validates as XHTML 1.0 Strict">Valid <abbr title="eXtensible HyperText Markup Language">XHTML</abbr></a></li>
        <li><a href="http://jigsaw.w3.org/css-validator/check/referer" title="Valid CSS">Valid CSS</a></li>
    	<li><a href="http://gmpg.org/xfn/"><abbr title="XHTML Friends Network">XFN</abbr></a></li>
    	<li><a href="http://wordpress.org/" title="Powered by WordPress, state-of-the-art semantic personal publishing platform.">WordPress</a></li>
        <?php wp_meta(); ?>
    </ul>

<?php endif; ?>

</div>