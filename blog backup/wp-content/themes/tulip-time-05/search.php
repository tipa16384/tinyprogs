<?php get_header(); ?>

	<?php if (have_posts()) : ?>

		<h2 class="pagetitle">Search Results</h2>

        <p>Thanks for searching the <?php bloginfo('name'); ?> site. Below we've listed some results that we hope are the sorts of things you were looking for.</p>
        <p>If they're not exactly the type thing you want to find, why not try using broader search terms to see what happens.</p>
        <p>Thanks for using <?php bloginfo('name'); ?>.</p>

		<?php while (have_posts()) : the_post(); ?>

			<div class="post">
				<h3 id="post-<?php the_ID(); ?>"><a href="<?php the_permalink() ?>" rel="bookmark" title="Permanent Link to <?php the_title(); ?>"><?php the_title(); ?></a></h3>
				<small><?php the_time('l, F jS, Y') ?></small>

				<p class="postmetadata">Posted in <?php the_category(', ') ?> | <?php edit_post_link('Edit', '', ' | '); ?>  <?php comments_popup_link('No Comments &#187;', '1 Comment &#187;', '% Comments &#187;'); ?></p>
			</div>

		<?php endwhile; ?>

	<?php else : ?>

		<h2 class="center">No posts found. Try a different search?</h2>
        <p><strong>We're really, really sorry, but your search has zero results!</strong></p>
        <p>You should consider broadening your search query. We do try our best sometimes to display the correct results, but that gets tough if there are no results to display!</p>
        <p><em>Maybe you could try searching again, but with some broader terms. Who knows, maybe it'll help you find what you're looking for!</em></p>

		<?php include (TEMPLATEPATH . '/searchform.php'); ?>

	<?php endif; ?>

<?php get_sidebar(); ?>

<?php get_footer(); ?>