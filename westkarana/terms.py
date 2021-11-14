#  `term_id` bigint(20) unsigned NOT NULL auto_increment,
#   `name` varchar(200) NOT NULL default '',
#   `slug` varchar(200) NOT NULL default '',
#   `term_group` bigint(10) NOT NULL default '0',

term_cols = ['term_id', 'name', 'slug', 'term_group']
term_key = 'INSERT INTO `wp_terms` VALUES ('

class Term:
    def __init__(self, row):
        self.term_id = row['term_id']
        self.name = row['name']
        self.slug = row['slug']
        self.term_group = row['term_group']
