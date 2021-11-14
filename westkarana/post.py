#!/usr/bin/Python

# ID,post_author,post_date,post_date_gmt,post_content,post_title,post_category,post_excerpt,post_status,comment_status,ping_status,post_password,
# # post_name,to_ping,pinged,post_modified,post_modified_gmt,post_content_filtered,post_parent,guid,menu_order,post_type,post_mime_type,comment_count

import os
from markdownify import markdownify
import re
from utils import filename, mangle

postfolder = './posts'
post_key = 'INSERT INTO `wp_posts` VALUES ('
post_columns = 'ID,post_author,post_date,post_date_gmt,post_content,post_title,post_category,post_excerpt,post_status,comment_status,ping_status,post_password,post_name,to_ping,pinged,post_modified,post_modified_gmt,post_content_filtered,post_parent,guid,menu_order,post_type,post_mime_type,comment_count'.split(
    ',')
wk_post_key = 'INSERT INTO `wk_posts` VALUES('
wk_post_columns = 'ID,post_author,post_date,post_date_gmt,post_content,post_title,post_excerpt,post_status,comment_status,ping_status,post_password,post_name,to_ping,pinged,post_modified,post_modified_gmt,post_content_filtered,post_parent,guid,menu_order,post_type,post_mime_type,comment_count'.split(
    ',')

month_names = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']


class Post:
    def __init__(self, row):
        self.ID = row['ID']
        self.post_author = row['post_author']
        self.post_date = row['post_date']
        self.post_date_gmt = row['post_date_gmt']
        self.post_content = row['post_content']
        self.post_title = row['post_title']
        self.post_category = row['post_category'] if 'post_category' in row else None
        self.post_excerpt = row['post_excerpt']
        self.post_status = row['post_status']
        self.comment_status = row['comment_status']
        self.ping_status = row['ping_status']
        self.post_password = row['post_password']
        self.post_name = row['post_name']
        self.to_ping = row['to_ping']
        self.pinged = row['pinged']
        self.post_modified = row['post_modified']
        self.post_modified_gmt = row['post_modified_gmt']
        self.post_content_filtered = row['post_content_filtered']
        self.post_parent = row['post_parent']
        self.guid = row['guid']
        self.menu_order = row['menu_order']
        self.post_type = row['post_type']
        self.post_mime_type = row['post_mime_type']
        self.comment_count = row['comment_count']
        self.post_author_name = None
        m = re.match(u'(\d+)-(\d+)-(\d+)', self.post_date)
        self.post_year = int(m.group(1)) if m else 0
        self.post_month = month_names[int(m.group(2))-1] if m else 'Octember'
        self.post_day = int(m.group(3)) if m else 0
        self.comments = None
        self.category = None

    def setPostAuthorUser(self, user_dict):
        if self.post_author and self.post_author in user_dict:
            self.post_author_name = user_dict[self.post_author].display_name

    def save(self):
        postpath = postfolder

        postpath = os.path.join(postpath, str(self.post_year), self.post_month)
        os.makedirs(postpath, exist_ok=True)
        postpath = os.path.join(postpath, str(self.ID) + ".md")

        with open(postpath, 'w', encoding="utf8") as f:
            print("Back to: [West Karana](/posts/{}) > [{}](/posts/{}/{}) > [{}](./{})".format(
                filename, self.post_year, self.post_year, filename, self.post_month, filename), file=f)
            print("# {}\n".format(self.post_title), file=f)

            if self.post_author_name:
                print(
                    "*Posted by {} on {}*\n".format(self.post_author_name, self.post_date), file=f)

            md = mangle(markdownify(self.post_content))
            print("{}".format(md), file=f)

            if self.comments:
                print("## Comments!\n", file=f)
                for comment in self.comments:
                    author = comment.comment_author if not comment.comment_author_url else "[{}]({})".format(
                        comment.comment_author, comment.comment_author_url)
                    print("**{}** writes: {}\n".format(mangle(author),
                                                       mangle(markdownify(comment.comment_content))), file=f)
                    print("---\n", file=f)
