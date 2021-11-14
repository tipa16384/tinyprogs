comment_key = 'INSERT INTO `wp_comments` VALUES ('

#  `comment_ID` bigint(20) unsigned NOT NULL auto_increment,
#   `comment_post_ID` bigint(20) unsigned NOT NULL default '0',
#   `comment_author` tinytext NOT NULL,
#   `comment_author_email` varchar(100) NOT NULL default '',
#   `comment_author_url` varchar(200) NOT NULL default '',
#   `comment_author_IP` varchar(100) NOT NULL default '',
#   `comment_date` datetime NOT NULL default '0000-00-00 00:00:00',
#   `comment_date_gmt` datetime NOT NULL default '0000-00-00 00:00:00',
#   `comment_content` text NOT NULL,
#   `comment_karma` int(11) NOT NULL default '0',
#   `comment_approved` varchar(20) NOT NULL default '1',
#   `comment_agent` varchar(255) NOT NULL default '',
#   `comment_type` varchar(20) NOT NULL default '',
#   `comment_parent` bigint(20) unsigned NOT NULL default '0',
#   `user_id` bigint(20) unsigned NOT NULL default '0',

comment_cols = ['comment_ID', 'comment_post_ID', 'comment_author', 'comment_author_email', 'comment_author_url', 'comment_author_IP', 'comment_date', 'comment_date_gmt',
                'comment_content', 'comment_karma', 'comment_approved', 'comment_agent', 'comment_type', 'comment_parent', 'user_id']


class Comment:
    def __init__(self, row):
        self.comment_ID = row['comment_ID']
        self.comment_post_ID = row['comment_post_ID']
        self.comment_author = row['comment_author'] if row['comment_author'] else 'Unknown'
        self.comment_author_email = row['comment_author_email']
        self.comment_author_url = row['comment_author_url']
        self.comment_author_IP = row['comment_author_IP']
        self.comment_date = row['comment_date']
        self.comment_date_gmt = row['comment_date_gmt']
        self.comment_content = row['comment_content']
        self.comment_karma = row['comment_karma']
        self.comment_approved = True if row['comment_approved'] == '1' else False
        self.comment_agent = row['comment_agent']
        self.comment_type = row['comment_type']
        self.comment_parent = row['comment_parent']
        self.user_id = row['user_id']
