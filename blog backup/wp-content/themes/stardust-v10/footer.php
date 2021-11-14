<!-- begin footer -->
</div><!-- end content -->
</div><!-- end wrapper -->

<hr />

<?php get_sidebar(); ?>

<hr />

    <div id="footer">
    <p class="up"><a href="#header" title="Jump to the top of the page">top</a></p>
        <p class="credit"><!--<?php echo get_num_queries(); ?> queries. <?php timer_stop(1); ?> seconds. --> <?php echo sprintf(__("Powered by <a href='http://wordpress.org/' title='%s'><strong>WordPress</strong></a>"), __("Powered by WordPress")); ?> - Handcoded by <a href="http://www.tomstardust.com"title="TomStardust.com - Web Design for all">Tommaso Baldovino</a></p>
    </div>

</div><!-- end container -->

<?php wp_footer(); ?>
</body>
</html>