  <div id="leftside">
    <div class="leftsideSection">
      <p><strong>jour&#183;nal</strong> <i>n.</i> A personal record of occurrences, experiences,
        and reflections kept on a regular basis; a diary.
      </p>
    </div>
    <p><a href="http://www.spreadfirefox.com/"><img alt="Get Firefox!" title="Get Firefox!" src="http://sfx-images.mozilla.org/affiliates/Buttons/110x32/rediscover.gif"/></a></p>

    <h4>internal links:</h4>
    <div class="leftsideSection">
      <ul>
        <li><a href="<?php echo get_settings('siteurl') ?>" title="Blog Home">Blog Home</a></li>
        <?php wp_register(); ?>
        <li><?php wp_loginout(); ?></li>
<?php wp_list_pages('title_li='); ?>
      </ul>
    </div>

    <h4>categories:</h4>
    <div class="leftsideSection">
    <ul>
<?php list_cats(1, 'All', 'name', 'asc', '', 1, 0, 1, 1, 1); ?>
    </ul>
    </div>

    <h4>search blog:</h4>
    <div class="leftsideSection">
      <form method="get" id="searchform" action="<?php echo $_SERVER['PHP_SELF']; ?>">
        <div><input type="text" value="<?php echo wp_specialchars($s, 1); ?>" name="s" id="s" />
          <input type="submit" id="searchsubmit" value="Search" />
        </div>
      </form>
    </div>

    <h4>archives:</h4>
    <div class="leftsideSection">
<?php get_calendar(); ?>
      <ul>
<?php get_archives('monthly',6); ?>
      </ul>
    </div>

    <h4>hearing:</h4>
    <div class="leftsideSection">
      <ul>
<?php wp_get_linksbyname('Music'); ?>
      </ul>
    </div>

    <h4>other:</h4>
    <div class="leftsideSection">
      <ul>
        <li><a href="<?php bloginfo('rss2_url'); ?>" title="Syndicate this site using RSS"><abbr title="Really Simple Syndication">RSS</abbr> 2.0</a></li>
        <li><a href="<?php bloginfo('comments_rss2_url'); ?>" title="The latest comments to all posts in RSS">Comments <abbr title="Really Simple Syndication">RSS</abbr> 2.0</a></li>
        <li><a href="http://feeds.archive.org/validator/check?url=<?php bloginfo('rss2_url'); ?>" title="This feed validates as RSS.">Valid RSS</a></li>
        <li><a href="http://validator.w3.org/check/referer" title="This page validates as XHTML 1.0 Transitional">Valid <abbr title="eXtensible HyperText Markup Language">XHTML</abbr></a></li>
        <li><a href="http://gmpg.org/xfn/"><abbr title="XHTML Friends Network">XFN</abbr></a></li>

        <li>Theme copyright &copy; 2002&#8211;<?php echo date('Y'); ?> <a href="http://zed1.com/journalized/">Mike Little</a>.</li>
      </ul>
    </div>
  </div> <!-- end left side -->
