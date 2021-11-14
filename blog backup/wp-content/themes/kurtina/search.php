<?php get_header(); ?>
<div class="body_box">

<div class="body_left">

<div class="pagebody">
<?php if (have_posts()) : ?>

<h1>Search results</h1>

<div class="nextback">
<div class="back"><?php next_posts_link('&laquo; Previous Entries') ?></div>
<div class="next"><?php previous_posts_link('Next Entries &raquo;') ?></div>
</div>

<?php while (have_posts()) : the_post(); ?>

<div class="excerpt_box" id="post-<?php the_ID(); ?>">
<div class="titledate">
<?php the_time('j.m.y') ?> | <a href="<?php the_permalink() ?>" rel="bookmark" title="Permanent Link to <?php the_title(); ?>"><?php the_title(); ?></a>
</div>
<div class="thexcerpt"><?php the_excerpt(); ?></div>
</div>
<?php endwhile; ?>
<div class="nextback">
<div class="back"><?php next_posts_link('&laquo; Previous Entries') ?></div>
<div class="next"><?php previous_posts_link('Next Entries &raquo;') ?></div>
</div>

<?php else : ?>
<h1>Not found! Try another search.</h1>
<?php include (TEMPLATEPATH . '/searchform.php'); ?>

<?php endif; ?>
</div>
</div>
<?php get_sidebar(); ?>
