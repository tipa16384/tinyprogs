
<div id="footer">
    <p>&copy; <?php the_time('Y') ?> <a href="<?php bloginfo('url'); ?>"><?php bloginfo('name'); ?></a>.</p>
    <p><?php bloginfo('name'); ?> is proudly powered by <a href="http://www.thesouthernhighlands.com.au/theme" title="Tulip Time Theme">Tulip Time</a> and <a href="http://wordpress.org/" title="Wordpress">WordPress</a>.</p>
</div>

</div>

<?php wp_footer(); ?>

<div id="navigation">
    <ul id="nav">
        <li><a href="<?php echo get_settings('home'); ?>/" title="Home: <?php bloginfo('name'); ?>">Home</a></li>
        <?php wp_list_pages('sort_column=menu_order&title_li='); ?>
        <li><a href="<?php bloginfo('rss2_url'); ?>">RSS</a></li></ul></div>

<div id="breadcrumbs">
<?php
function CPbreadcrumbs() {
    $CPtheFullUrl = $_SERVER["REQUEST_URI"];
    $CPurlArray=explode("/",$CPtheFullUrl);
    echo 'You are here : <a href="/">Home</a>';
    while (list($CPj,$CPtext) = each($CPurlArray)) {
        $CPdir='';
        if ($CPj > 1) {
            $CPi=1;
            while ($CPi < $CPj) {
                $CPdir .= '/' . $CPurlArray[$CPi];
                $CPtext = $CPurlArray[$CPi];
                $CPi++;
            }
            if($CPj < count($CPurlArray)-1) echo ' &raquo; <a href="'.$CPdir.'">' . str_replace("-", " ", $CPtext) . '</a>';
        }
    }
    echo wp_title();
}
CPbreadcrumbs();?></div>

<div id="searchCSS">
    <?php include (TEMPLATEPATH . '/searchform.php'); ?></div>

        <!-- <?php echo get_num_queries(); ?> queries. <?php timer_stop(1); ?> seconds. -->

</body>
</html>
