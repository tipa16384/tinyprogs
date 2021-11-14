#!/usr/bin/python

import os
from post import Post, post_key, post_columns, wk_post_key, wk_post_columns
from utils import consume
from user import User, user_key, user_columns
from pages import create_year_page, create_year_month_page, create_year_month_day_page
from comment import comment_key, comment_cols, Comment
from terms import Term, term_cols, term_key

pathbackup = 'E:\\blog backup\\wp-content\\backup-a9adc\\westkara_wp_20131107_981.sql'
newPathBackup = 'chasing.sql'

post_dict = {}
user_dict = {}
by_year = {}
by_year_month = {}
comments_by_post = {}
term_by_term_id = {}


def processComment(l):
    l = l.replace('tipa@westkarana.com', 'brendahol@gmail.com')
    vals = [x for x in consume(l)]
    comment_val_dict = {}
    for i in range(len(comment_cols)):
        comment_val_dict[comment_cols[i]] = vals[i] if i < len(vals) else None
    return Comment(comment_val_dict)


def processPost(l):
    l = l.replace('http://westkarana.com/wp-content', '../../..')
    l = l.replace('http://westkarana.com', '../../..')

    vals = [x for x in consume(l)]
    post_val_dict = {}
    for i in range(len(post_columns)):
        post_val_dict[post_columns[i]] = vals[i] if i < len(vals) else None
    return Post(post_val_dict)


def processWkPost(l):
    vals = [x for x in consume(l)]
    post_val_dict = {}
    for i in range(len(wk_post_columns)):
        post_val_dict[wk_post_columns[i]] = vals[i] if i < len(vals) else None
    return Post(post_val_dict)


def processUser(l):
    vals = [x for x in consume(l)]
    user_val_dict = {}
    for i in range(len(user_columns)):
        user_val_dict[user_columns[i]] = vals[i] if i < len(vals) else None
    return User(user_val_dict)


def processTerm(l):
    vals = [x for x in consume(l)]
    term_val_dict = {}
    for i in range(len(term_cols)):
        term_val_dict[term_cols[i]] = vals[i] if i < len(vals) else None
    return Term(term_val_dict)


def processLine(l):
    if l.startswith(comment_key):
        comment = processComment(l)
        if comment.comment_approved:
            if comment.comment_post_ID in comments_by_post:
                comments_by_post[comment.comment_post_ID].append(comment)
            else:
                comments_by_post[comment.comment_post_ID] = [comment]
    elif l.startswith(post_key):
        post = processPost(l[len(post_key):-4])
        if post.post_status == 'publish':
            post_dict[post.ID] = post
    elif l.startswith(wk_post_key):
        post = processWkPost(l[len(wk_post_key):-4])
        if post.post_status == 'publish':
            post_dict[post.ID] = post
    elif l.startswith(user_key):
        user = processUser(l)
        user_dict[user.ID] = user
    elif l.startswith(term_key):
        term = processTerm(l[len(term_key):])
        term_by_term_id[term.term_id] = term


def post_associate_author():
    for post in post_dict.values():
        post.setPostAuthorUser(user_dict)
#        post.category = term_by_term_id[post.post_category] if post.post_category else term_by_term_id[1]


def addPostToYear(post):
    if post.post_year in by_year:
        by_year[post.post_year] += 1
    else:
        by_year[post.post_year] = 1
    #print ("by_year now {}".format(by_year))


def addPostToMonth(post):
    tups = (post.post_year, post.post_month)

    if tups in by_year_month:
        by_year_month[tups].append(post)
    else:
        by_year_month[tups] = [post]


def post_associate_comment():
    for post_id in comments_by_post:
        if post_id in post_dict:
            post_dict[post_id].comments = comments_by_post[post_id]


if __name__ == "__main__":
    with open(pathbackup, 'r', encoding="utf8") as f:
        print("We found the backup!")
        lineno = 0
        try:
            for l in f:
                lineno += 1
                processLine(l)
        except UnicodeDecodeError as err:
            print("Unicode error in line {}, was {}".format(lineno, err))

    post_associate_author()
    post_associate_comment()

    for post in post_dict.values():
        post.save()
        addPostToYear(post)
        addPostToMonth(post)

    post_dict = {}
    user_dict = {}
    comments_by_post = {}
    term_by_term_id = {}

    with open(newPathBackup, 'r', encoding="utf8") as f:
        print("We found the new backup!")
        lineno = 0
        try:
            for l in f:
                lineno += 1
                processLine(l)
        except UnicodeDecodeError as err:
            print("Unicode error in line {}, was {}".format(lineno, err))

    post_associate_author()
    post_associate_comment()

    for post in post_dict.values():
        post.save()
        addPostToYear(post)
        addPostToMonth(post)

    create_year_page(by_year)
    create_year_month_page(by_year_month)
    for ym in by_year_month:
        create_year_month_day_page(ym, by_year_month[ym])
