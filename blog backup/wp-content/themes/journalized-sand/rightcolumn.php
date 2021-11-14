  <div id="rightside">
    <div class="rightsideSection">
      <p><strong>95.</strong> <i>We are waking up and linking to each other. We are watching. But we are not waiting.</i><br/>
      &mdash; <a href="http://www.cluetrain.com/" title="The Cluetrain Manifesto">The Cluetrain Manifesto</a>
      </p>
    </div>

    <h4>general links:</h4>
    <div class="rightsideSection">
      <ul>
<?php wp_get_linksbyname('general'); ?>
      </ul>
    </div>

    <h4>I read:</h4>
    <div class="rightsideSection">
      <ul>
<?php wp_get_linksbyname('I Read'); ?>
      </ul>
    </div>

    <h4>bloggy links</h4>
    <div class="rightsideSection">
      <ul>
<?php wp_get_links(6); ?>
      </ul>
    </div>

    <h4>respect to:</h4>
    <div class="rightsideSection">
      <ul>
<?php wp_get_links(4); ?>
      </ul>
    </div>

<?php if (function_exists('wp_theme_switcher')) { ?>
    <h4><?php _e('Themes'); ?>:</h4>
    <div class="rightsideSection">
<?php wp_theme_switcher(); ?>
    </div>
<?php } ?>


  </div> <!-- end right column -->
