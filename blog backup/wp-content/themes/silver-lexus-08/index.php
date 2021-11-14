<?php get_header(); ?>

    <?php if (have_posts()) : ?>

        <?php while (have_posts()) : the_post(); ?>

        <div class="post" id="post-<?php the_ID(); ?>">

<div class="date">
    <span class="date1"><?php the_time('jS') ?></span>
    <span class="date2"><?php the_time('F') ?></span>
    <span class="date3"><?php the_time('Y') ?></span></div>

            <h2><a href="<?php the_permalink() ?>" rel="bookmark" title="Permanent Link to <?php the_title(); ?>"><?php the_title(); ?></a></h2>

            <div class="entry">
                <?php the_content('Read the rest of this entry &raquo;'); ?></div>

            <p class="pageInfo">posted in <?php the_category(', ', __(' and ')) ?> | <?php edit_post_link('<span class="iconEdit">Edit</span>', '', ' | '); ?> <span class="iconComment"><?php comments_popup_link('0 Comments', '1 Comment', '% Comments'); ?></span></p>

        </div>

        <?php endwhile; ?>

		<div id="page_nav">
			<div class="alignleft"><?php next_posts_link('&laquo; Previous Entries') ?></div>
			<div class="alignright"><?php previous_posts_link('Next Entries &raquo;') ?></div>
		</div>

    <?php else : ?>

    <h2 class="center">No posts found. Maybe try searching?</h2>
        <p><strong>We're really, really sorry, but there's nothing here!</strong></p>
        <p><em>Maybe you could try searching to see if you can find the post you were looking for.</em></p>

        <?php include (TEMPLATEPATH . '/searchform.php'); ?>

    <?php endif; ?>

<?php get_sidebar(); ?>

<?php get_footer(); ?>