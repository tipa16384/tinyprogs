<?php get_header(); ?>
<div class="body_box">

<div class="body_left">

<div class="pagebody">
<?php if (have_posts()) : ?>

<?php $post = $posts[0]; // Hack. Set $post so that the_date() works. ?>
<?php /* If this is a category archive */ if (is_category()) { ?>				
<h1>Archive for the '<?php echo single_cat_title(); ?>' Category</h1>

<?php /* If this is a daily archive */ } elseif (is_day()) { ?>
<h1>Archive for <?php the_time('F jS, Y'); ?></h1>

<?php /* If this is a monthly archive */ } elseif (is_month()) { ?>
<h1>Archive for <?php the_time('F, Y'); ?></h1>

<?php /* If this is a yearly archive */ } elseif (is_year()) { ?>
<h1>Archive for <?php the_time('Y'); ?></h1>

<?php /* If this is a search */ } elseif (is_search()) { ?>
<h1>Search Results</h1>

<?php /* If this is an author archive */ } elseif (is_author()) { ?>
<h1>Author Archive</h1>

<?php /* If this is a paged archive */ } elseif (isset($_GET['paged']) && !empty($_GET['paged'])) { ?>
<h1>Blog Archives</h1>

<?php } ?>

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
<p>Not found! Try another search.</p>
<?php include (TEMPLATEPATH . '/searchform.php'); ?>

<?php endif; ?>
</div>
</div>
<?php get_sidebar(); ?>
