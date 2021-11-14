<div class="comments">
<?php if ( !empty($post->post_password) && $_COOKIE['wp-postpass_' . COOKIEHASH] != $post->post_password) : ?>
<p><?php _e('Enter your password to view comments.'); ?></p>
<?php return; endif; ?>

<?php if ( comments_open() ) : ?>
<b><?php comments_number(__('No Comments'), __('1 Comment'), __('% Comments')); ?> so far</b>
<?php else : // If there are no comments yet ?>
<?php endif; ?>
<br /><br />
<a name="comments"></a>
<?php if ( $comments ) : ?>

<?php foreach ($comments as $comment) : ?>
<div class="commentBox">
	<?php comment_text() ?>

    <i><?php comment_type(__('Comment'), __('Trackback'), __('Pingback')); ?> <?php _e('by'); ?> <?php comment_author_link() ?>
    <?php comment_date('m.d.y') ?> @ <a href="#comment-<?php comment_ID() ?>"><?php comment_time() ?></a> <?php edit_comment_link(__("Edit This"), ' |'); ?></i>
</div>
<br />

<?php endforeach; ?>

<?php else : // If there are no comments yet ?>

<?php endif; ?>

<br /><br />

<a name="postcomment"></a>
<a name="respond"></a>
<?php if ( comments_open() ) : ?>
<b><?php _e('Leave a comment'); ?></b><br />
<?php _e("Line and paragraph breaks automatic, e-mail address never displayed, <acronym title=\"Hypertext Markup Language\">HTML</acronym> allowed:"); ?> <code><?php echo allowed_tags(); ?></code>

<form action="<?php echo get_settings('siteurl'); ?>/wp-comments-post.php" method="post" id="commentform">

	<p>
	  <input type="text" name="author" id="author" class="textarea" value="<?php echo $comment_author; ?>" size="15" tabindex="1" />
	   <label for="author"><?php _e('Name'); ?></label> <?php if ($req) _e('(required)'); ?>
	<input type="hidden" name="comment_post_ID" value="<?php echo $post->ID; ?>" />
	<input type="hidden" name="redirect_to" value="<?php echo htmlspecialchars($_SERVER['REQUEST_URI']); ?>" />
	</p>

	<p>
	  <input type="text" name="email" id="email" value="<?php echo $comment_author_email; ?>" size="15" tabindex="2" />
	   <label for="email"><?php _e('E-mail'); ?></label> <?php if ($req) _e('(required)'); ?>
	</p>

	<p>
	  <input type="text" name="url" id="url" value="<?php echo $comment_author_url; ?>" size="15" tabindex="3" />
	   <label for="url"><?php _e('<acronym title="Uniform Resource Identifier">URI</acronym>'); ?></label>
	</p>

	<p>
	  <label for="comment"><?php _e('Your Comment'); ?></label>
	<br />
	  <textarea name="comment" style="border: 1px solid #000;" id="comment" cols="50" rows="6" tabindex="4"></textarea>
	</p>
	<p>
	  <input name="submit" id="submit" type="submit" tabindex="5" value="<?php _e('Say It!'); ?>" />
	</p>
	<?php do_action('comment_form', $post->ID); ?>
</form>

<?php else : // Comments are closed ?>

<?php endif; ?>
</div>
