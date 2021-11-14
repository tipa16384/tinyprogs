<?php
/* Don't remove these lines. */
$blog = 1;
get_header();
?>
<body>
<div id="headerblock">
  <h1 id="header"><a href="<?php bloginfo('url'); ?>"><?php bloginfo('name'); ?></a></h1>
  <p><strong><?php bloginfo('description'); ?></strong></p>
  <p class="centerP">[powered by <a href="http://wordpress.org/" title="Powered by WordPress, state-of-the-art semantic personal publishing platform"><strong>WordPress</strong></a>.]</p>
</div> <!-- headerblock -->

<?php if (have_posts()) { while (have_posts()) { the_post(); ?>
<?php the_date('','<h2>','</h2>');?>
<div class="centreblock">
  <h3 class="storytitle" id="post-<?php the_ID(); ?>"><a href="<?php the_permalink() ?>" rel="bookmark" title="Permanent Link to <?php the_title(); ?>"><?php the_title(); ?></a></h3>
  <div class="meta"> by <span class="storyAuthor"><?php the_author() ?> </span> @ <?php the_time() ?>.<?php edit_post_link(); ?>
    Filed under <?php the_category(', ') ?>
  </div> <!-- meta -->

  <div class="storyContent">
<?php the_content(); ?>
  </div> <!-- story content -->

  <div class="storyLinks">
    <div class="feedback">
      <?php wp_link_pages(); ?>
      <?php comments_popup_link('[Comments (0)]', '[Comments (1)]', '[Comments (%)]'); ?>&nbsp;
      [<a href="<?php the_permalink() ?>" rel="bookmark" title="Permanent Link: <?php the_title(); ?>">link</a>]
    </div>
  </div> <!-- storyLinks -->

    <!--
    <?php trackback_rdf(); ?>
    -->

<?php comments_template(); ?>
</div> <!-- centreblock -->

<?php } } else { // end foreach, end if any posts
?>
<div class="centreblock">
<p>Sorry, no posts matched your criteria.</p>
</div> <!-- centreblock -->
<?php } // end else no posts
?>

<p class="centerP">
  [powered by <a href="http://wordpress.org/" title="Powered by WordPress, state-of-the-art semantic personal publishing platform"><strong>WordPress</strong></a>.]
</p>

<?php
include_once('leftcolumn.php');
include_once('rightcolumn.php');
?>

<p class="centerP"><?php echo $wpdb->num_queries; ?> queries. <?php echo number_format(timer_stop(),3); ?> seconds </p>
<?php do_action('wp_footer'); ?>
</body>
</html>