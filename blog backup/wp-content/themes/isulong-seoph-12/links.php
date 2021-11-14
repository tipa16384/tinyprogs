<?php
/*
Template Name: Links
*/
?>

<?php get_header(); ?>


<div id="center"  class="column">

<h2>Links:</h2>
<ul>
<?php get_links_list(); ?>
</ul>
</div>

<div id="left"  class="column"><?php get_sidebar(); ?>
</div>

<div id="right"  class="column"><?php require('rightbar.php'); ?>
</div>

<?php get_footer(); ?>
