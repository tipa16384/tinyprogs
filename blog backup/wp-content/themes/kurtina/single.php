<?php get_header(); ?>
<div class="body_box">

<div class="body_left">

<!-- BLOG FORMAT -->
<?php if (have_posts()) : while (have_posts()) : the_post(); ?>

<div class="blogbox" id="post-<?php the_ID(); ?>">

<div class="entryheader">

<div class="datecolumn">
<div class="dateday"><?php the_time('jS') ?></div>
<div class="datemonthyear"><?php the_time('F') ?><br /><?php the_time('Y') ?></div>
</div>
<div class="titlecolumn">
<div class="entrytitle">
<a href="<?php the_permalink() ?>" rel="bookmark" title="Permanent Link to <?php the_title(); ?>"><?php the_title(); ?></a>
</div>
<div class="entrytitlecomment">
FILED: <?php the_category(', ') ?> <?php edit_post_link('Edit', '', ' | '); ?> <br /><?php comments_popup_link('No Comments', '1 Comment', '% Comments'); ?>
</div>
</div>

</div>


<div class="entrybody">
<?php the_content('<span class="entrymore">continue reading &raquo;</span>'); ?>
</div>

</div>
<!-- BLOG FORMAT END -->	
<div class="trackbacks">
This entry was posted
<?php /* This is commented, because it requires a little adjusting sometimes.
You'll need to download this plugin, and follow the instructions:
http://binarybonsai.com/archives/2004/08/17/time-since-plugin/ */
/* $entry_datetime = abs(strtotime($post->post_date) - (60*120)); echo time_since($entry_datetime); echo ' ago'; */ ?> 
on <?php the_time('l, F jS, Y') ?> at <?php the_time() ?>.
You can follow any responses to this entry through the <?php comments_rss_link('RSS 2.0'); ?> feed. 

<?php if (('open' == $post-> comment_status) && ('open' == $post->ping_status)) {
// Both Comments and Pings are open ?>
You can <a href="#respond">leave a response</a>, or <a href="<?php trackback_url(true); ?>" rel="trackback">trackback</a> from your own site.

<?php } elseif (!('open' == $post-> comment_status) && ('open' == $post->ping_status)) {
// Only Pings are Open ?>
Responses are currently closed, but you can <a href="<?php trackback_url(true); ?> " rel="trackback">trackback</a> from your own site.

<?php } elseif (('open' == $post-> comment_status) && !('open' == $post->ping_status)) {
// Comments are open, Pings are not ?>
You can skip to the end and leave a response. Pinging is currently not allowed.

<?php } elseif (!('open' == $post-> comment_status) && !('open' == $post->ping_status)) {
// Neither Comments, nor Pings are open ?>
Both comments and pings are currently closed.			

<?php } edit_post_link('Edit this entry.','',''); ?>				
</div>
<div class="commentsbody">
<?php comments_template(); ?>
</div>

<?php endwhile; else: ?>

<div class="pagebody"><p>Sorry, no posts matched your criteria.</p></div>

<?php endif; ?>
</div>
<?php get_sidebar(); ?>
