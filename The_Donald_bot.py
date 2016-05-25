#!/usr/bin/env python3

import time
import praw


r = praw.Reddit('Trump name dropz')

r.login('CheckOutThesePythons', 'M%f&nBnK1BmL', disable_warning=True)
already_done = [] #Ignore
current_date = time.strftime("%d\%m\%Y")

while True:
    comments_file_name = "trump_comments " + current_date + ".txt"
    comments_read_file = "trump_comments_read " + current_date + ".txt"
    trump_file = open(comments_file_name, "a+")
    comments_read = open(comments_read_file, "a+")
    subreddit = r.get_subreddit('The_Donald')
    for submission in subreddit.get_hot(limit=25):
        submission.replace_more_comments(limit=16, threshold=1)
        flat_comments = praw.helpers.flatten_tree(submission.comments)
        for comment in flat_comments:
                if comment.id not in comments_read.readlines():
                    trump_file.write(comment.body + '\n' + 'END OF COMMENT' + '\n')
                    print(comment.id)
                    comments_read.write(comment.id + '\n')
    trump_file.close()
    comments_read.close()
    time.sleep(600)
    get_date = time.strftime("%d\%m\%Y")
    if get_date == current_date:
        pass
    else:
        current_date = get_date


