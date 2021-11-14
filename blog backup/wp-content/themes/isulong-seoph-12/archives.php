<?php
/*
Template Name: Archives
*/
?>

<?php get_header(); ?>


<div id="center"  class="column">



<?php include (TEMPLATEPATH . '/searchform.php'); ?>

<h2>Archives by Month:</h2>
  <ul>
    <?php wp_get_archives('type=monthly'); ?>
  </ul>

<h2>Archives by Subject:</h2>
  <ul>
     <?php wp_list_cats(); ?>
  </ul>

</div>	

<div id="left"  class="column"><?php get_sidebar(); ?>
</div>

<div id="right"  class="column"><?php require('rightbar.php'); ?>
</div>


<?php get_footer(); ?>
