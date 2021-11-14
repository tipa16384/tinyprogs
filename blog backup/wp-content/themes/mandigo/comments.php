<?php
	global $mandigo_options, $dirs;

	/* do not delete these lines */
	if ('comments.php' == basename($_SERVER['SCRIPT_FILENAME']))
		die ('Please do not load this page directly. Thanks!');

	// if there's a password
	if (!empty($post->post_password)) { 
		// and it doesn't match the cookie
		if ($_COOKIE['wp-postpass_' . COOKIEHASH] != $post->post_password) {
?>
			<p class="nocomments">This post is password protected. Enter the password to view comments.<p>
<?php
			return;
		}
	}
	
	if (!function_exists('wp_list_comments')) {
		include 'comments_pre27.php';
		return;
	}



	// if there's at least one comment
	if ($comments) {
?>
	<div id="comments">
<?php
		comments_number(
			__('No Responses to ', 'mandigo'),
			__('One Response to ', 'mandigo'),
			__('% Responses to ',  'mandigo')
		);
?>
		&#8220;<?php the_title();?>&#8221;
	</div> 
	
<?php
		// in case you're wondering why there are hidden empty list item (<li style="display: none;"></li>)
		// they're here so the <ol> tags are never empty and the pages still validate

		// if we chose to display them ABOVE comments
		if ($mandigo_options['trackbacks_position'] == 'above') {
?>
	<div id="trackbacks"><?php _e('Trackbacks', 'mandigo'); ?></div> 
	<ol class="commentlist" id="trackbacklist">
	<?php wp_list_comments(array('type' => 'trackback')); ?>
		<li style="display: none;">&nbsp;</li>
	</ol>
	
	<div id="comments"><?php _e('Comments', 'mandigo'); ?></div> 
	<ol class="commentlist" id="commentlist">
	<?php wp_list_comments(array('type' => 'comment')); ?>
		<li style="display: none;">&nbsp;</li>
	</ol>
	<div class="navigation">
		<div class="alignleft"><?php previous_comments_link('&laquo; '. __('Older Comments', 'mandigo')) ?></div>
		<div class="alignright"><?php next_comments_link(__('Newer Comments', 'mandigo') .' &raquo;') ?></div>
	</div>
	
<?php
		}



		// if we chose to display them ALONG with comments
		elseif ($mandigo_options['trackbacks_position'] == 'along') {
?>
	<ol class="commentlist" id="commentlist">
	<?php wp_list_comments(array('type' => 'all')); ?>
		<li style="display: none;">&nbsp;</li>
	</ol>
	<div class="navigation">
		<div class="alignleft"><?php previous_comments_link('&laquo; '. __('Older Comments', 'mandigo')) ?></div>
		<div class="alignright"><?php next_comments_link(__('Newer Comments', 'mandigo') .' &raquo;') ?></div>
	</div>

<?php
		}



		// if we chose to display them BELOW comments
		elseif ($mandigo_options['trackbacks_position'] == 'below') {
?>
	<ol class="commentlist" id="commentlist">
	<?php wp_list_comments(array('type' => 'comment')); ?>
		<li style="display: none;">&nbsp;</li>
	</ol>
	<div class="navigation">
		<div class="alignleft"><?php previous_comments_link('&laquo; '. __('Older Comments', 'mandigo')) ?></div>
		<div class="alignright"><?php next_comments_link(__('Newer Comments', 'mandigo') .' &raquo;') ?></div>
	</div>
	
	<div id="trackbacks"><?php _e('Trackbacks', 'mandigo'); ?></div> 
	<ol class="commentlist" id="trackbacklist">
	<?php wp_list_comments(array('type' => 'trackback')); ?>
		<li style="display: none;">&nbsp;</li>
	</ol>
<?php
		}
		
		
		
		// if we chose to not display them at all
		else {
?>
	<ol class="commentlist" id="commentlist">
	<?php wp_list_comments(array('type' => 'comment')); ?>
		<li style="display: none;">&nbsp;</li>
	</ol>
	<div class="navigation">
		<div class="alignleft"><?php previous_comments_link('&laquo; '. __('Older Comments', 'mandigo')) ?></div>
		<div class="alignright"><?php next_comments_link(__('Newer Comments', 'mandigo') .' &raquo;') ?></div>
	</div>
<?php
		}
	}
	

	
	
	
	// this is displayed when there are no comments
	else {

		// if comments are open (but there are no comments)
		if ($post->comment_status == 'open') {
		}
		
		// if comments are closed
		else {
?>
		<p class="nocomments"><?php _e('Comments are closed.', 'mandigo'); ?></p>

<?php
		}
	} // end of 'whether there are comments or not' condition





	// if comments are open
	if ($post->comment_status == 'open') {
?>

	<div id="respond">
		<div class="title"><?php _e('Leave a Reply', 'mandigo'); ?></div>

<?php
	// if only registered users can comment, and the current user is not logged in
	if (get_option('comment_registration') && !$user_ID) {
?>
	<p><?php _e('You must be logged in to post a comment.', 'mandigo'); ?> <a href="<?php echo get_option('siteurl'); ?>/wp-login.php?redirect_to=<?php the_permalink(); ?>"><?php _e('Login', 'mandigo'); ?> &raquo;</a></p>
<?php
	}





	// if user can leave a comment
	else {
?>

<div class="cancel-comment-reply">
	<small><?php cancel_comment_reply_link(__('Click here to cancel reply', 'mandigo')); ?></small>
</div>
	<form action="<?php echo get_option('siteurl'); ?>/wp-comments-post.php" method="post" id="commentform">
	<?php comment_id_fields(); ?>
<?php
		// if the user is logged in
		if ($user_ID) {
?>

	<p><?php printf(__('Logged in as %s', 'mandigo'),'<a href="'. get_option('siteurl') .'/wp-admin/profile.php">'. $user_identity .'</a>'); ?>. <a href="<?php echo get_option('siteurl'); ?>/wp-login.php?action=logout" title="<?php _e('Log out of this account', 'mandigo'); ?>"><?php _e('Logout', 'mandigo'); ?> &raquo;</a></p>

<?php
		}

		// if the user is not logged in
		else {
?>

	<p><input type="text" name="author" id="author" value="<?php echo $comment_author; ?>" size="22" tabindex="1" />
	<label for="author"><small><?php _e('Name', 'mandigo'); ?> <?php if ($req) echo "(". __('required', 'mandigo') .")"; ?></small></label></p>

	<p><input type="text" name="email" id="email" value="<?php echo $comment_author_email; ?>" size="22" tabindex="2" />
	<label for="email"><small><?php _e('E-mail', 'mandigo'); ?> (<?php _e('will not be published', 'mandigo'); ?>) <?php if ($req) echo "(". __('required', 'mandigo') .")"; ?></small></label></p>

	<p><input type="text" name="url" id="url" value="<?php echo $comment_author_url; ?>" size="22" tabindex="3" />
	<label for="url"><small><?php _e('Website', 'mandigo'); ?></small></label></p>

<?php
		}





		// if HTML tags are allowed in comments
		if ($mandigo_options['comments_allow_markup']) {
?>
	<p><small><strong>XHTML:</strong> <?php _e('You can use these tags:', 'mandigo'); ?> <?php echo allowed_tags(); ?></small></p>
<?php
		}
?>

	<p><textarea name="comment" id="comment" cols="100%" rows="10" tabindex="4"></textarea></p>

	<p>
		<input name="submit" type="submit" id="submit" tabindex="5" value="<?php _e('Submit Comment', 'mandigo'); ?>" />
		<input type="hidden" name="comment_post_ID" value="<?php echo $post->ID; ?>" />
	</p>
<?php
	do_action('comment_form', $post->ID);
?>
	<br class="clear" />
</form>

<?php
		} // end of 'whether the user is logged in or not' condition
?>
	</div>
<?php
	} // end of 'if comments are open' condition



?>

<script type="text/javascript">
<!-- // <![CDATA[

		jQuery(document).ready(function() {
			if (jQuery('#trackbacklist li').length == 1)
				jQuery('#trackbacks, #trackbacklist').hide();
<?php
	if (!$mandigo_options['disable_animations']) { // if animations are not disabled
?>
			jQuery('li.comment>div>*').filter(':not(.comment-author, .comment-meta)').wrap('<div class="comment"><\/div>');
			
			jQuery('.comment-author').before('<span class="switch-post"><a href="#"><img src="<?php echo $dirs['www']['icons']; ?>bullet_toggle_minus.png" alt="" class="png" /><\/a><\/span>');
<?php
	}
?>
		});

// ]]> -->
</script>