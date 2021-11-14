#   `ID` bigint(20) unsigned NOT NULL auto_increment,
#   `user_login` varchar(60) NOT NULL default '',
#   `user_pass` varchar(64) NOT NULL default '',
#   `user_nicename` varchar(50) NOT NULL default '',
#   `user_email` varchar(100) NOT NULL default '',
#   `user_url` varchar(100) NOT NULL default '',
#   `user_registered` datetime NOT NULL default '0000-00-00 00:00:00',
#   `user_activation_key` varchar(60) NOT NULL default '',
#   `user_status` int(11) NOT NULL default '0',
#   `display_name` varchar(250) NOT NULL default '',

user_key = 'INSERT INTO `wp_users` VALUES ('
user_columns = ['ID', 'user_login', 'user_pass', 'user_nicename', 'user_email', 'user_url', 'user_registered', 'user_activation_key', 'user_status', 'display_name']

class User:
    def __init__(self, l):
        self.ID = l['ID']
        self.user_login = l['user_login']
        self.user_pass = l['user_pass']
        self.user_nicename = l['user_nicename']
        self.user_email = l['user_email']
        self.user_url = l['user_url']
        self.user_registered = l['user_registered']
        self.user_activation_key = l['user_activation_key']
        self.user_status = l['user_status']
        self.display_name = l['display_name']
