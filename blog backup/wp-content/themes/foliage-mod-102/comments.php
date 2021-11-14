<?php // Do not delete these lines
	if ('comments.php' == basename($_SERVER['SCRIPT_FILENAME']))
		die ('Please do not load this page directly. Thanks!');

        if (!empty($post->post_password)) { // if there's a password
            if ($_COOKIE['wp-postpass_' . COOKIEHASH] != $post->post_password) {  // and it doesn't match the cookie
				?>
				
				<p class="nocomments">This post is password protected. Enter the password to view comments.<p>
				
				<?php
				return;
            }
        }

		/* This variable is for alternating comment background */
		$oddcomment = 'alt';
?>

<!-- You can start editing here. -->
		
<div id="commentscolumn">

<?php if ($comments) : ?>
	<h3 class="comments"><?php comments_number('No Responses', 'One Response', '% Responses' );?></h3>

<div class="commentnote">Note that comments are displayed in reverse chronological order with topmost comments being freshest. <a href="#respond">Comment</a> | <?php comments_rss_link('Subscribe'); ?></div>	

	<ul class="commentlist">
	
	<?php $comments = array_reverse($comments, true); /* reverse comments */ ?>
	<?php foreach ($comments as $comment) : ?>

		<li class="<?php if ($comment->comment_author_email == "your@email.com") echo 'author'; else if ($comment->comment_author_email == "guest@email.com") echo 'specialguest'; else echo $oddcomment; ?> item" id="comment-<?php comment_ID() ?>">
		
		<div class="commententry">
		<?php comment_author_link() ?> says so:<br /><span style="text-transform: lowercase;"><a href="#comment-<?php comment_ID() ?>" title="Comment Permalink"><?php comment_date('F jS, Y') ?></a> | <?php if (function_exists('quoter_comment')) { quoter_comment(); } ?> <?php edit_comment_link('| e','',''); ?></span>
		
			<?php if ($comment->comment_approved == '0') : ?>
			<em>Your comment looks dirty</em>
			<?php endif; ?>
			
			<?php comment_text() ?> 
		
		</div><!-- close comment -->

		</li>

	<?php /* Changes every other comment to a different class */	
		if ('alt' == $oddcomment) $oddcomment = '';
		else $oddcomment = 'alt';
	?>

	<?php endforeach; /* end for each comment */ ?>

	</ul>

 <?php else : // this is displayed if there are no comments so far ?>
	<h3 class="comments"><?php comments_number('No Responses', 'One Response', '% Responses' );?></h3>
	<div class="commentnote">Note that comments are displayed in reverse chronological order with topmost comments being freshest. <a href="#respond">Comment | <?php comments_rss_link('Subscribe'); ?></a></div>	
		<ul class="commentlist">
			<li>
			<div class="commententry">
				<?php comment_text() ?> 
			</div><!-- close comment -->
			</li>
		</ul>

  <?php if ('open' == $post->comment_status) : ?> 
		<!-- If comments are open, but there are no comments. -->
		
	 <?php else : // comments are closed ?>
		<!-- If comments are closed. -->
		<p class="commententry">Comments are closed.</p>
		
	<?php endif; ?>
<?php endif; ?>

</div><!-- close commentscolumn -->


<?php if ('open' == $post->comment_status) : ?>

<div id="commentwrap">
<h3 id="respond">Leave a Reply</h3>
<?php if ( get_option('comment_registration') && !$user_ID ) : ?>
<p>You must be <a href="<?php echo get_option('siteurl'); ?>/wp-login.php?redirect_to=<?php the_permalink(); ?>">logged in</a> to post a comment.</p>
<?php else : ?>

<form action="<?php echo get_option('siteurl'); ?>/wp-comments-post.php" method="post" id="commentform">

<?php if ( $user_ID ) : ?>

<p>Logged in as <a href="<?php echo get_option('siteurl'); ?>/wp-admin/profile.php"><?php echo $user_identity; ?></a>. <a href="<?php echo get_option('siteurl'); ?>/wp-login.php?action=logout" title="Log out of this account">Logout &raquo;</a></p>

<?php else : ?>

<p><input type="text" name="author" id="author" value="<?php echo $comment_author; ?>" tabindex="1" />
<label for="author"><small>Name (req)</small></label></p>

<p><input type="text" name="email" id="email" value="<?php echo $comment_author_email; ?>" tabindex="2" />
<label for="email"><small>Mail (req)</small></label></p>

<p><input type="text" name="url" id="url" value="<?php echo $comment_author_url; ?>" tabindex="3" />
<label for="url"><small>Website (opt)</small></label></p>

<?php endif; ?>

<!--<p><small><strong>XHTML:</strong> You can use these tags: <?php echo allowed_tags(); ?></small></p>-->

<p><textarea name="comment" id="comment" tabindex="4" cols="40" rows="10"><?php if (function_exists('quoter_comment_server')) { quoter_comment_server(); } ?></textarea></p>

<p><input name="submit" type="submit" id="submit" tabindex="5" value="Submit" />
<input type="hidden" name="comment_post_ID" value="<?php echo $id; ?>" />
</p>
<?php do_action('comment_form', $post->ID); ?>

</form>
</div>

<div class="clear"></div>

<?php endif; // If registration required and not logged in ?>

<?php endif; // if you delete this the sky will fall on your head ?>


