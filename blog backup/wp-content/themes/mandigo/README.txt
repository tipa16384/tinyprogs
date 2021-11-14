
     WWWWWW    +WWWWW                                 WWWW WWWW                          
     WWWWWW    WWWWWW                                 WWWW WWWW                          
     WWWWWW    WWWWWW                                ,WWWW WWWW                          
     WWWWWW.  WWWWWWW                                WWWW                                
    ,WWW#WW+  WWWWWWW  ,WWWWWWW   WWWW WWWWW    WWWW:WWWW  WWWW  #WWWW WWWW   +WWWWW#    
    WWWW+WWW WWW,WWW+ WWWWWWWWWW  WWWWWWWWWW:  WWWWWWWWWW @WWW  WWWWWWWWWWW  WWWWWWWWW   
    WWWW WWW WWW WWW  WWWW  WWWW. WWWWWWWWWWW WWWWWWWWWWW WWWW #WWWWWWWWWW+ WWWWWWWWWW.  
    WWWW WWW*WW*.WWW    ,   .WWW. WWWW  WWWWW#WWWW  WWWWW WWWW WWWW   WWWW WWWW.  ,WWWW  
    WWW+ WWWWWW WWWW     WWWWWWW #WWW*  @WWW,WWWW   +WWW* WWWW WWWW   WWWW WWWW    WWWW  
    WWW  WWWWWW WWWW  WWWWWWWWWW WWWW   WWWW WWWW   WWWW  WWWW.WWW*   WWWW WWWW    WWWW  
   :WWW  WWWWW  WWWW WWWW   WWWW WWWW   WWWW WWWW   WWWW .WWW*.WWWW  :WWWW WWWW   WWWW   
   WWWW  WWWWW  WWW.WWWW   .WWWW WWWW   WWWW WWWW  WWWWW WWWW  WWWWWWWWWWW WWWW  ,WWWW   
   WWWW  WWWW   WWW WWWWW:WWWWW@ WWWW   WWWW WWWWWWWWWWW WWWW  WWWWWWWWWW. WWWWWWWWWW    
   WWWW  WWWW  *WWW .WWWWWW.WWW+,WWW#  .WWW#  WWWWW:WWWW WWWW   WWWW WWWW   WWWWWWWW     
   +++,  +++:  ++++   WWW:  ++++++++   ++++    WWW  +++. ++++        WWWW    ,WWW#       
                                                              WWWW   WWWW                
   Designed by t0mmmmmmm, Dec 2006                            WWWWWWWWWW                 
   http://www.onehertz.com/portfolio/wordpress/                WWWWWWWWW                  
                                                                #WWWW                    


=== LICENSE ============================================================================

Mandigo is released under the GPL license terms.

Customize the theme at will, but please do not modify the credits in the footer.



=== INSTALLING =========================================================================

To add Mandigo to your WordPress installation, follow these basic steps:

   1. Extract the files from the archive, preserving the directory structure.
   2. Using an FTP client to access your host web server, create a directory to contain 
      your theme in the wp-content/themes directory provided by WordPress 
      (ie wp-content/themes/mandigo).
   3. Upload the theme files to the new directory on your host server.
   4. Log in to the WordPress Administration Panels.
   5. Select the Presentation subpanel and click on the Mandigo screenshot.



=== UPGRADING ==========================================================================

Upgrading Mandigo is generally only a matter of uploading the new files, overwriting the
existing ones.

If you haven't made any modification to the PHP files, and if you haven't overwritten 
any of the standard images, all you have to do is upload the new files. The settings 
made on the Theme Options page will remain untouched.

For more information, check out the Upgrade Notes on the Mandigo wiki:
http://wiki.onehertz.com/WordPress/Mandigo/Upgrading



=== SHOW YOUR SUPPORT ==================================================================

If you enjoy this theme, please consider doing some (all) of the following things:

- let me know and send an email to tom@onehertz.com

- show your support by making a donation:
  http://www.onehertz.com/portfolio/wordpress/donate/

- leave a comment on the Appreciation Thread:
  http://www.onehertz.com/portfolio/wordpress/mandigo/testrun/appreciation-thread/

Thank you for choosing Mandigo!



=== WIDGETS SUPPORT ====================================================================

Mandigo supports up to five widgets bars: two on the sides, one at the top and one at 
the bottom, plus a fifth one that spans the two sidebars when they're aligned on the 
right. The sidebars can be displayed on either side of the reading area. The top/bottom 
bars are most useful to display some kind of static content (using text widgets), or 
recent posts/comments.

If you're still not using widgets (you should!), you can find more information about 
them here: http://automattic.com/code/widgets/



=== HEADER IMAGES ======================================================================

Header images management will eventually be better explained on the Mandigo wiki:
http://wiki.onehertz.com/WordPress/Mandigo

** Replacing Default Header Images
If none of the headers satisfy your needs, create a new scheme by copying one of the
existing ones and just replace the head.jpg file in the newly created images/ subfolder.
If you are using the wide layout, save your image as head-1024.jpg instead.

You DO NOT have to modify the PNG files, as the JPG files are displayed ON TOP of them.

For best results, resize your header image to the dimensions below:

                      +-----------------------+
                      |      Layout Width     |
                      +-----------+-----------+
                      | standard  |   wide    |
                      |   800px   |  1024px   |
  +--------+----------+-----------+-----------+
  |        |          |           |           |
  |        | standard | 737 x 226 | 961 x 226 |
  | Header |          |           |           |
  |        +----------+-----------+-----------+
  | Height |          |           |           |
  |        |   slim   | 737 x 126 | 961 x 126 |
  |        |          |           |           |
  +--------+----------+-----------+-----------+

** Per-Page Header Images:
If you wish to have a different header image on a page, all you have to do is name it 
after the ID (not slug) of the page on which it should be displayed, and upload it to 
the images/headers/ folder, eg 'images/headers/412.jpg' if you want a custom image for 
post/page #412.

Images should be saved as JPG and use the dimensions mentionned above. You can retrieve 
a page's ID from the administration interface, under Manage, Posts/Page. If the script 
can't find a custom header image, the default one is used instead. If there is more than
one post on a page (default view, archives, search, ...), the ID of the first post to 
appear on the page will be used.

** Per-Category Header Images:
Same as above, you only need to prefix the filename with "cat_", eg cat_9.jpg for
category ID 9.

** Random Header Images:
If the "Use random header images" option is enabled in the Theme Options page, AND a
per-page header could not be found, Mandigo will use a random file from the 
images/headers/ folder. Valid file types are JPG, GIF, PNG and BMP.

** Detection Order:
As of version 1.34, Mandigo will first look for headers in the user's uploaded files,
THEN in images/headers/ as this allows for people in a WPMU environment to still benefit
from this functionality.

For images to be detected from the user's uploaded files (the WordPress Media library),
the files have to be named according to the following pattern PRIOR to uploading:
- "mandigo_header.jpg" in the case of a image to use site-wide
- "mandigo_header_cat_ID.jpg" where ID is the category ID
- "mandigo_header_ID.jpg" where ID is the post ID (see per-page headers section above)



=== IMAGES IN POSTS ====================================================================

Image management will eventually be better explained on the Mandigo wiki:
http://wiki.onehertz.com/WordPress/Mandigo

** Alignment:
Most of the time Mandigo will follow the alignment options you set in the rich editor,
but in some cases, depending on how you want the pictures to be arranged and which set 
of options you enabled, things may get a little trickier. This section should help you 
solve most alignment problems.

Text is set to wrap around images by default, however if you want to override this 
behaviour, there is an option ("Do not wrap text around images") to disable it.

If you want text to be wrapped around images but have problems with short paragraphs 
messing up your posts, try adding the "clear" class to your p tag, i.e. 
<p class="clear">. If you don't use <p>s, adding <br class="clear" /> between paragraphs
will do the trick as well.

If you want to center an image, use the "aligncenter" class instead. Note however that
text can't be wrapped around centered images, and that such aligned images occupy a 
full line. This implies that if you want to have more than one picture side by side but
aligned to the center, you will have to apply the "alignnone" class to them, and wrap 
them in a centered container, i.e.
<div style="text-align: center">
	<img class="alignnone" />
	<img class="alignnone" />
</div>

If you want text to wrap around SOME images, let text wrapping enabled, and add 
class="nowrap" to the img tags around which you don't want text to wrap, i.e. 
<img class="nowrap" />. Adding this class to a block container will make all its child 
images inherit this behaviour (useful for galleries).

** Border:
Images in posts are surrounded by a border by default. While it is possible to disable
them throughout the theme using the appropriate option, you can also override this 
behaviour on certain images by adding the "noborder" class to the img tag.



=== COLOR SCHEMES ======================================================================

Mandigo comes with seven different schemes which files can be found in the schemes/
directory: blue, green, orange, pink, purple, red & teal.

The new schemes structure in version 1.26 allows for new schemes to be added.

schemes
`-- name                             # scheme name (eg. blue, green, ...)
    |-- images
    |   |-- cal_bg.jpg               # gradient behind date stamps
    |   |-- comments.gif             # comments icon
    |   |-- edit.gif                 # edit icon
    |   |-- head-1024.jpg            # header image for 1024px 
    |   |-- head.jpg                 # header image for 800px
    |   |-- rss_l.gif                # large rss icon
    |   |-- rss_l_hover.gif          # large rss icon for rollover
    |   |-- rss_s.gif                # small rss icon
    |   |-- search.gif               # search icon
    |   |-- search_hover.gif         # search icon for rollover
    |   `-- star.gif                 # widget bullet
    |-- preview.jpg                  # preview for the Theme Options page
    `-- style.css                    # style, colors


If you want to create your own scheme, the easiest way is to make a copy of one of the 
default schemes, give the directory the desired name, and then replace the files with 
your own.

All schemes detected by Mandigo (those for which style.css exists) will automatically 
appear on the Theme Options page, so they will also be included in the pool for the 
random scheme switching feature. This also allows for some schemes to be excluded from 
the random switching (delete the folder in schemes/ or rename its style.css).



=== SEO OPTIONS ========================================================================

** Custom <title> schemes:
The keywords in <title> tags being the most important factor in search engine ranking,
it is important that to make these tags as relevant as possible. Mandigo has a feature 
that lets you customize <title> tags on a per-pagetype basis, which means you can use 
different naming patterns on the index, posts, pages, archives and search results.

The following variables are available:
%blogname% = the blog title
%tagline%  = the blog description
%post%     = the title of the current post or page
%category% = the category for the current archive, or the list of categories for a post
%date%     = the date for the current archive
%search%   = the search terms 

Patterns can be a combination of arbitrary text and these variables, i.e. you could
use "Welcome to %blogname%" for the index or "Archives for %category%" for archives.

** Custom HTML tags
Another important factor to popular search engines is the use of keywords in headings, 
particulary the h1 and h2 elements, so wrapping relevant content in them is a good idea.

Since the title and description of your blog may or may not be relevant to your content,
Mandigo let's you choose which heading level you want to use for these elements. You can 
also do the same thing to the title of posts in single and multiple views, and to the 
title of some pages ('Search results', 'Archives', ..).

Note that using a different kind of tag does not (should not, please report bugs) affect
the look and feel at all.



=== LOCALIZATION =======================================================================

For instructions on how to use WordPress in your language, please read the following:
http://codex.wordpress.org/Installing_WordPress_in_Your_Language

The .mo files which come with Mandigo are complements to the .mo files that are used to 
translate the WordPress interface, as they contain the information needed to translate 
the parts that are specific to the theme.

Once you have the WordPress interface set in your language, the Mandigo .mo file will
be loaded automatically, provided it exists.

If Mandigo has not been translated in your language and you are interested in helping 
with translation, please let me know by sending an email to tom@onehertz.com

.po files are available at http://www.onehertz.com/portfolio/wordpress/mandigo/l10n/



=== CREDITS ============================================================================

** Translation Credits
Arabic:                Maxer
Bahasa Indonesia:      Benny Wu
Basque:                Lurdes Imaz
Bulgarian:             Canko Balkanski
Catalan:               Sergi Barroso
Chinese (Simplified):  Hua Zhou
Chinese (Traditional): Charles Low
Croatian:              Ivana Pavic
Czech:                 Milan Tucek
Danish:                Daniel Noesgaard Rasmussen
Dutch:                 Ramsy de Vos
Finish:                Mika Majakorpi
French:                Michel Bibal, David Sahli
German:                Michael Nickel, Ted Box, Philipp Fischer
Greek:                 Andrew Kontokanis, Thanasis Dais
Hebrew:                Omry Yadan
Hindi:                 Debashish Chakrabarty
Hungarian:             Horvath Zoltan, Farkas Gyozo
Icelandic:             Karl Kristjansson
Italian:               Sebastiano Cannata, Diego Pierotto
Japanese:              Mitsuhiro Kanda, Yamane Shinji
Lithuanian:            Simonas Kiela
Malay:                 Intan Keristina
Maltese:               James Cauchi
Norwegian (Bokmal):    Torbjorn Blystad, Espen Gjelsvik
Norwegian (Nynorsk):   Eivind Odegard
Polish:                Mateusz Baran
Portuguese (PT):       Rodrigo Neves
Portuguese (BR):       Oscar Nogueira Neto, Marcelo Todaro
Romanian:              Victor Butiu
Russian:               Michael Dolgov
Serbian:               Aleksandar Duric
Slovak:                Marek, Marian Trnka
Slovenian:             Xin
Spanish:               Juan Luis Perez Perez
Swedish:               Ulf Wrede, Johan
Turkish:               Mert Yabul
Ukrainian:             Gabriel Korzhos

** Photography Credits
Blue Scheme:   "Abstract Smoke" by Brian Lary:  http://www.sxc.hu/profile/blary54
Red Scheme:    "Energy 2" by Diane Miller:      http://www.sxc.hu/profile/dinny
Green Scheme:  "Horizontal 2" by Lucretious:    http://www.sxc.hu/profile/Lucretious
Pink Scheme:   "Spinning Fan" by Janet Goulden: http://www.sxc.hu/profile/cooljinny
Purple Scheme: "Light Play 8" by Sarah Lee:     http://www.sxc.hu/profile/clashed
Orange Scheme: "ADN" by Frederico Oddone:       http://www.sxc.hu/profile/FedexsnaP
Teal Scheme:   "Green Globe" by Jenny W.:       http://www.sxc.hu/profile/emsago

** Other Credits
"Silk" Iconset by Mark James: http://www.famfamfam.com/lab/icons/silk/
"jQuery" by John Resig: http://www.jquery.com/
"jQuery ifixpng plugin" by khurshid: http://jquery.khurshid.com/ifixpng.php



=== CHANGELOG ==========================================================================

1.42
* WP 3.0 compatibility
* fixed the exclude pages from head nav bug

1.41
+ header submenus can be nested to an arbitrary depth
+ added options to set the animation speed of header submenus
+ added an option to use the legacy fully-dynamic stylesheet (see below)
* grammar fixes: Bulgarian (bg_BG)
* split the stylesheet to make the theme work on all types of setups (even on free,
  ad-polluted GoDaddy accounts). Static rules now reside in style.css and the dynamic
  ones in style.css.php. They're loaded in two different ways depending on whether
  you're using the fully-dynamic stylesheet or not (which will be the default behaviour)
* fixed a minor bug in comments.php

1.40.1
* fixed custom excerpts support
* fixed a php warning in header.php

1.40
+ language: Hindi (hi)
+ custom excerpts support
* grammar fixes: Italian (it_IT)
* grammar fixes: Greek (el)
* fixed shrinking fonts in nested comments
* renamed Ukrainian translation file to uk_UA.mo
* fixed random headers not working when viewing a category archive
* don't put images resized by WP in the custom headers pool
* fixed a class conflict the wp-pagenavi plugin
* fixed the option to not display trackbacks at all

1.39
+ per-category headers
+ paged comments support (WP 2.7+)
+ threaded comments support (WP 2.7+)
+ added an option to display the post date along with author name and categories
+ added an option to make the header clickable
* don't display a gravatar if the comment is a trackback
* fixed custom headers not working on some wpmu setups

1.38
+ added an option to disallow comments on pages
+ added an option to change the font family
* fixed the issue with flash objects being cut down to half-height
* fixed a problem with Google ads making the page go blank when used in the left sidebar

1.37
* grammar fixes: French (fr_FR)
* grammar fixes: Hungarian (hu_HU)
* fixed the heading level for page titles not having a default value
* fixed the datestamps not showing up correctly in japanese
* fixed widgets not collapsing when in a left sidebar
* fixed the "collapse frontpage and archive posts" option being a little too greedy
* fixed the submenus animation queuing
* fixed the submenus not showing up in IE when the translucent stripe is used
* allow overriding and inheritance of list-style-type in content lists
* more image/object resizing fixes for IE
* subpages are now also shown in the list of pages that can be excluded from the header

1.36.2
* fixed the submit button on the HTML Inserts page
* prevent the options page CSS rules from interfering with the rest of the dashboard
* more stylesheet fixes

1.36.1
* fixed a bug that would prevent the stylesheet from being loaded in some (rare) cases

1.36
+ added a new widget container (sidebox) which spans the two sidebars when they are 
  aligned on the right side
+ added a new HTML Inserts field for late code (right before the closing </body> tag)
+ added an option to create drop caps
* silenced a few annoying php warnings
* fixed image/object resizing again
* fixed the upgrade system not retroactively applying updates

1.35
+ added options to set the sidebars width
+ added an option to hide datestamps
* finally fixed the dropdown menu bug in IE (hi Tim)
* fixed the color picker not working on WP nightly builds
* better Windows Live Writer compatibility

1.34
+ the theme now also looks for custom header images in the user's uploaded files. See
  the updated section about headers in the README file
+ added a registration link to the footer for WordPress MU setups
- removed the option to float all images to the right by default
- removed jquery.dimensions.js since it's now part of the jQuery core library
* grammar fixes: German (de_DE)
* MORE code cleanup: the file structure has changed somewhat, but there's now a set of 
  functions to move the files for you. Just make sure the theme directory is writable
  by the web server prior to uploading this version. See the upgrade notes in the README
* updated jQuery to 1.2.6
* fixed comment numbers overlapping gravatars (except in Opera)
* fixed comment alternate coloring for when trackbacks are displayed separately
* fixed author comment highlighting, now also checks the commenter's email address
* fixed the sidebars always showing up in single post view
* fixed the jQuery/prototype conflicts: this should fix broken lightboxes and all other
  prototype-based plugins
* fixed the animation links showing up in comments even when animations are disabled
* fixed adsense units not working in sidebars when placed on the left

1.33.1
+ added an option to wrap one paragraph at most
* moved image control options from misc to posts

1.33
+ language: Slovenian (sl_SI)
+ added an option to disable submenus in header navigation
+ added gravatars support in comments
+ added support for the new image classes in 2.5, no more hair tearing! (well hopefully)
* grammar fixes: Brazilian Portuguese (pt_BR)
* grammar fixes: Norwegian (nb_NO)
* MAJOR code cleanup
* fixed non clickable sidebar links in IE6
* now using the packed version of jQuery
* fixed the "restore default color" links

1.32
+ language: Basque (eu)
+ language: Finish (fi_FI)
+ language: Norwegian Nynorsk (nn_NO)
+ added sub-page navigation to header links
+ added comments on pages
+ added animation buttons to comments
* updated jQuery to 1.2.3 (addresses sidebar bugs in IE)
* fixed transparency of PNG background patterns in IE6
* fixed animation buttons in IE

1.31
+ added an option to automatically collapse posts when viewing archives & categories
+ added the Tag Cloud page template
+ added a gradient background pattern (repeat: horizontally only, position: 0% 0%)
+ added an option to center the top navigation
* fixed comments using wrong post IDs
* fixed the fixes (sic) that split long URLs in comments
* fixed links.php not showing up full width
* fixed a js error with the togglePost() function

1.30
+ language: Romanian (ro)
+ added a color picker to the Options page
+ added support for categories description
+ defined font-size for regular header tags (h1-h6)
+ added options to try and fix issues with columns showing up wider than they should
+ added options to display trackbacks above/below/along with comments or not at all
* grammar fixes: German (de_DE)
* grammar fixes: Polish (pl_PL)
* fixed the image resizing function for IE
* fixed widget titles not showing up as bold when wrapped in divs
* fixed a backward compatiblity issue with "edit comment" links
* only show the link to edit a comment to users who can actually edit comments
* the .noborder class is now inheritable from parent elements
* PNG transparency in IE is now handled by a custom version of jquery.ifixpng

1.29
+ language: Croatian (hr)
+ language: Japanese UTF-8 (ja)
+ added an option to display trackbacks after the comments
+ added header/footer files for the WPG2 plugin
+ automatically load favicon.ico if it exists in the theme directory
* text shadow & stroke are now applied on the fly: this is better for SEO as it removes
  some duplicated content
* sidebars now appear after the content in the HTML code (better SEO)
* fixed the scheme detection function for sites on which glob() is restricted
* fixed a PHP error that occured with older versions of WP (2.1* and earlier)

1.28
+ language: Bulgarian (bg_BG)
* grammar fixes: French (fr_FR)
* localized dates in comments
* fixed empty uls validation errors on the front page (WP2.2+)
* fixed duplicate ids validation errors in archives and search results
* fixed archive pages for WP<2.3 and WPMU (check if is_tag() exists before calling it)
* fixed images sometimes going out of post boundaries
* fixed the Theme Editor which was still not working
* removed the list bullet from the Tag Cloud
* lots of minor changes and bugfixes (hi ArnWald)

1.27.1
* fixed incompatibilities with the prototype library

1.27 "It's moving!"
+ added controls to hide/show posts and sidebars
* smaller PNG files
* PNG transparency in IE is now handled by iepngfix.htc
* more efficient image and object resizing in IE
* restored Theme Editor functionality: schemes stylesheets are now named scheme.css
* fixed some more HTML validation errors
* fixed the label for Tags not displaying correctly
* fixed the "Display tags after the content" option which couldn't be unset

1.26
+ added support for WP 2.3 tags
* color schemes now use a plugin-like structure, which means you can easily create new 
  schemes or remove the ones you don't want to use with the random switcher. See 
  upgrading notes.
* dropped the switch to disable background patterns (select 'none' in menu instead)
* fixed an HTML Insert (the "right before the content" one) not showing up
* fixed the resizing of images and objects AGAIN
* fixed various HTML validation errors
* fixed shadow/stroke of blog description not using the correct font when a H1-H3 tag 
  was used
* fixed the fontsize for the Blogroll (which can't have a custom heading level btw)
* fixed the README page not showing up correctly

1.25
+ added options to select the heading level (h1-h6, div) of some important elements 
  like the blog name & desc, title of posts, ...
* language: switched to formal German, now using 'Sie' instead of 'Du'
* automatically resize <objects> so they don't stretch the reading area
* fixed the resizing of images and objects for the 1-column layout
* .nowrap (previously .nofloat) can now be inherited from parent block elements

1.24
+ language: Portuguese (pt_PT)
+ language: Ukrainian (ua_UA)
+ added an option to not show any sidebar at all (1-column layout)
+ added a field to select the background pattern from a list rather than type its name
+ added options to change the sidebars/posts background & border colors
+ added an option to display allowed XHTML tags above the comment field
+ added an option to align images to the right
+ added an option to disable justify alignment
* finally fixed RSS feed links
* fixed misplaced calendar captions in IE7
* fixed a problem that would cause the content column to shrink when it had too little
  text
* fixed the color & positioning of H1 tags in posts

1.23
+ language: Arabic (ar)
+ language: Catalan (ca_ES)
+ language: Chinese Simplified (zh_CN)
+ language: Hebrew (he_IL)
+ language: Lithuanian (lt_LT)
+ added support for right-to-left scripts (Hebrew & Arabic)
+ added options to customize the <title> tag on a per-pagetype basis
+ added an option to (slightly) highlight comments made by the author of a post
* language: renamed zh_CN to zh_TW
* alignment fixes for the sidebars and previous/next post navigation links
* restored page templates functionnality

1.22
+ language: Bahasa Indonesia (id_ID)
+ added an option to add a drop shadow to the blog name and tagline
+ added an option to display full search results
+ added a new HTML Insert container which displays before the content area
+ the name of the author now links to the author archives
* custom header images would not work if the installation path contained spaces
* columns are now displayed in a table, this should fix a lot of recurrent issues
* the widecolumn class now spans the whole layout
* finally made a decent archives page
* images in attachments view mode are not floated anymore
* Mandigo can now be installed in a directory of arbitrary depth

1.21
+ added an option to number comments
+ added options to hide the blog name and description
+ added options to set the background pattern attachment/repeat/position
+ added an option to reduce the font size for the blog name (useful for looong titles)
+ added an option to disable the border around images
* background patterns now have their own subdirectory, if you are using one, you will 
  have to move it to images/patterns/
* fixed the issue with overlapping images in page view
* fixed list bullets in posts which were displayed off stage in IE
* fixed the overlapping footer bug in IE7 (hi Randy)
* fixed more footer gap issues
* the footer should also be resize-proof now

1.20.1
* fixed the 3-column layout option not being read by the stylesheet's fallback method
* fixed the parsing of boolean options for WPMU
* fixed the footer gap issue for good

1.20
+ added an option to make the header 100px smaller in height
* tested successfully with WordPress 2.2
* donation link now links to our NICE donation page *hint* *hint*
* grammar fixes: Spanish (es_ES)
* grammar fixes: Swedish (sv_SE)
* WPMU friendly
* fixed a javascript error occuring on pages without a sidebar
* fixed a bug that would cause the translation for "Pages" to not show up correctly
* fixed more Event Calendar alignment issues

1.19
+ added an option to use random header images
* fixed an incompatibility with older versions of MySQL
* fixed an incompatibility with WordPress-MU

1.18
+ per-page headers: you can now have a different header image on each page, see README
+ added an option to apply a black stroke to blog title and description for better
  readibility on lighter header images
+ added an option to restore the default background color
* images larger than the reading area are now resized upon loading
* fixed a bug that would cause the reading area background to not be completely shown
* fixed EM tags not being displayed as italics even if the option was enabled
* faster stylesheet serving: style.css.php now directly connects to the database instead
  of relying on WP
* moved all browser-dependent content to style.css.php so that it's never cached

1.17
+ implemented HTML Inserts, a feature that will hopefully make updates easier
* grammar fixes: Slovak (sk)
* fixed an issue that would cause the navigation links in single.php to not work when
  the "previous posts" widget was active
* slightly increased the font size of H3 tags
* restored smileys transparency
* smaller stylesheet

1.16
+ added the .googlemap class for use with Google Maps (restores image transparency)
* grammar fixes: Hungarian (hu_HU)
* reverted php short tags to standard tags (changes were not included in last update)
* fixed the gap between header and reading area
* fixed alignment issues with Opera
* fixed alignment issues with the Event Calendar Plugin

1.15
+ added an option to display EM tags as italics
+ language: Malay (ms)
* reverted php short tags to standard tags
* fixed previous/next navigation links on the home page
* fixed various alignment issues
* fixed some incompatibilities with earlier versions of WordPress

1.14
+ added an option to use background patterns
+ added an option to set header navigation alignment
+ added an option to show sidebars even in single.php
+ language: Greek (el)
+ language: Icelandic (is_IS)
+ language: Maltese (mt_MT)
* fixed the (lastminute) css warning in the header
* pages in sidebar are now sorted according to menu_order

1.13.1
* fixed an issue which caused sidebars to overflow when the second sidebar was too long 
  to fit the main area

1.13
+ added the 3-column layout
+ added options to move the sidebars left/right
+ language: Brazilian Portuguese (pt_BR)
+ language: Polish (pl_PL)
+ language: Russian (ru_RU)
+ language: Serbian (sr_CS)
+ language: Simplified Chinese (zh_CN)

1.12
+ added Top and Bottom widgets bars
+ language: Czech (cs_CZ)
+ language: Danish (da_DK)
+ language: French (fr_FR)
+ language: Hungarian (hu_HU)
+ language: Slovak (sk)
* localized dates
* fixed calendar caption issue in Safari

1.11
+ added an option to prevent images from float'ing
+ added an option to display stats (queries+rendering time) in the footer
+ language: Japanese (ja_EUC)
+ language: Norwegian (nb_NO)
+ language: Spanish (es_ES)
* fixed not translated 'previous/next entries' links in index.php

1.10
+ Mandigo is now fully localizable
+ language: Dutch (nl_NL)
+ language: German (de_DE)
+ language: Italian (it_IT)
+ language: Swedish (sv_SE)
+ language: Turkish (tr_TR)
* fixed the nofloat class
* fixed stylesheet not loading when pretty permalinks are enabled
* fixed a bug that caused to wide version header images to always load

1.9
+ by popular request, the theme is now available in two widths: 800px (default) and 
  1024px, hooray!
+ added an option to change schemes randomly
* fixed non-clickable footer links issue in IE6

1.8
+ added an option to change the body background color
* reworked the pages navigation
- dropped the option to make the black stripe span multiple lines, now done with css
* the theme now uses png files for the main aera decorations
- deleted the extras/ subfolder
* fixed the calendar caption issue
* pages are now sorted according to menu_order rather than alphabeticaly
* fixed some CSS warnings

1.7.1
* changed the color of links in the green and teal schemes
* removed some duplicate files

1.7
+ added the teal color scheme
+ added a .nofloat class to use with images
+ added an option to exclude some pages from header navigation
+ added an option to display all links in bold

1.6
+ added the orange color scheme
+ added an option to make the translucent stripe span multiple lines
* fine-tuned max-width for images in posts

1.5
+ added the purple color scheme
+ added an option to change the date format
+ added an option to display a translucent black stripe over the header image for better
  readability
* fixed some alignment issues in IE7

1.4
+ added the pink color scheme
+ included a blank image header in extras/

1.3
+ added the Version Checker on the Theme Options subpanel
* fixed empty li tags in sidebar issue

1.2
+ added a 'Home' link to the pages (in the wordpress sense)
* empty categories are now displayed as well
* categories are now displayed in a hierarchical way

1.1
+ added the README subpage to the Presentation subpanel
* fixed a few minor glitches on IE7

1.0
* first public release

