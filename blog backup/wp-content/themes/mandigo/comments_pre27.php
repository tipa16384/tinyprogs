<?php
	// this is the legacy comments.php file
	// it'll be used instead of comments.php if you're running a pre-2.7 WordPress version
	
	global $mandigo_options, $dirs;

	// the post/page author
	$the_author       = get_the_author();
	$the_author_email = get_the_author_email();

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
		// loop through comments
		// what we do here is process each comment, build <li> items, and separate real comments from trackbacks
		// we will display them later according to the chosen options
		foreach ($comments as $comment) {
			// the comment id
			$id = get_comment_ID();
			
			// a BIG sprintf, not for the faint of heart
			$comment_list_item = sprintf('
				<li class="clear%s" id="comment-%s">
					<div class="commenter%s"%s>
					%s
						<cite>%s</cite>
						%s
						<small class="commentmetadata"><a href="#comment-%s">%s</a> %s</small>
					</div>
					<div class="comment">
						%s
					</div>
				</li>
				',

				( // first %s, highlight author comment class
					(
						$mandigo_options['comments_highlight_author']
						&& get_comment_author() == $the_author
						&& get_comment_author_email() == $the_author_email
					)
					? ' bypostauthor'
					: ''
				),
				
				$id, // second %s, the comment id
				
				( // 3rd %s, gravatar class
					(
						!$comment->comment_type == 'trackback'
						&& !$mandigo_options['comments_no_gravatars']
						&& function_exists('get_avatar')
						&& function_exists('get_comment_author_email')
					)
					? ' avatar'
					: ''
				),
				
				( // 4th %s, gravatar
					!$mandigo_options['comments_no_gravatars'] && $comment->comment_type != 'trackback'
					? (
						function_exists('get_avatar') && function_exists('get_comment_author_email')
						? sprintf(
							' style="background: url(%s) no-repeat top left;"',
							preg_replace(
								'/.+src=[\'"]([^\'"]+)[\'"].+/',
								'\1',
								get_avatar(get_comment_author_email(), '36')
							)
 						)
						: ''
					)
					: ''
				),
				
				( // 5th %s, animation link
					!$mandigo_options['disable_animations'] // if animations are not disabled
					? '<span class="switch-post"><a href="javascript:toggleComment();"><img src="'. $dirs['www']['icons'] .'bullet_toggle_minus.png" alt="" class="png" /></a></span>'
					: ''
				),
				
				sprintf( // 6th %s, the user name
					__('%s says:', 'mandigo'),
					get_comment_author_link()
				),
				
				( // 7th %s, whether the comment is pending moderation or not
					$comment->comment_approved == '0'
					? '<em>'. __('Your comment is awaiting moderation.', 'mandigo') .'</em><br />'
					: ''
				),
				
				$id, // 8th %s, the comment id again
				
				sprintf( // 9th %s, "which date at what time"
					__('%s at %s', 'mandigo'),
					get_comment_date(__('F jS, Y', 'mandigo')),
					get_comment_time()
				),
				
				( // 10th %s, the edit comment link, if appropriate
					function_exists('get_edit_comment_link') && current_user_can('edit_post', $post->ID)
					? ' - '. apply_filters(
						'edit_comment_link',
						'<a href="'. get_edit_comment_link($id) .'">'. __('Edit', 'mandigo') .'</a>',
						$comment->comment_ID
					)
					: ''
				),
				
				// 11th %s, the comment itself
				apply_filters('comment_text', get_comment_text())
				
			); // end of big sprintf, phew!

		
			// if this is a trackback
			if ($comment->comment_type == 'trackback') {
			
				// and we chose to display them either above or below regular comments
				if ($mandigo_options['trackbacks_position'] == 'above' || $mandigo_options['trackbacks_position'] == 'below') {
					// put them in a separate list
					$trackback_list[] = $comment_list_item;
				}
				
				// if we chose to display them along other comments
				elseif ($mandigo_options['trackbacks_position'] == 'along') {
					$comment_list[] = $comment_list_item;
				}
			}
			
			else {
				$comment_list[] = $comment_list_item;
			}

		} // end of foreach loop

		// if we have trackbacks and we chose to display them ABOVE comments
		if ($mandigo_options['trackbacks_position'] == 'above' && $trackback_list) {
?>
	<br />
	<div id="trackbacks"><?php _e('Trackbacks', 'mandigo'); ?></div> 
	<ol class="commentlist pre27">
<?php
			echo implode("\n", $trackback_list);
?>
	</ol>
	<div id="trackbacks"><?php _e('Comments', 'mandigo'); ?></div> 
<?php
		}



		// the comments
?>

	<ol class="commentlist pre27">
<?php
			echo implode("\n", $comment_list);
?>
	</ol>

<?php



		// if we have trackbacks and we chose to display them BELOW comments
		if ($mandigo_options['trackbacks_position'] == 'below' && $trackback_list) {
?>
	<div id="trackbacks"><?php _e('Trackbacks', 'mandigo'); ?></div> 
	<ol class="commentlist pre27">
<?php
			echo implode("\n", $trackback_list);
?>
	</ol>
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

	<div id="respond" class="pre27"><?php _e('Leave a Reply', 'mandigo'); ?></div>

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

	<form action="<?php echo get_option('siteurl'); ?>/wp-comments-post.php" method="post" id="commentform">

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
</form>

<?php
		} // end of 'whether the user is logged in or not' condition
	} // end of 'if comments are open' condition
?>
