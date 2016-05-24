#!/usr/bin/env python3

import time
import praw
from pprint import pprint

r = praw.Reddit('Trump name dropz')

r.login('CheckOutThesePythons', 'M%f&nBnK1BmL', disable_warning=True)
already_done = [] #Ignore
nicks = ['Trump', 'Donald', 'The Donald']
mentions = 0



while True:
    Trump_file = open('Trump_comments.txt', 'a')
    Comments_read = open('Comments_read.txt', 'w+')

    subreddit = r.get_subreddit('The_Donald')
    for submission in subreddit.get_hot(limit=25):
        submission.replace_more_comments(limit=16, threshold=1)
        flat_comments = praw.helpers.flatten_tree(submission.comments)
        for comment in flat_comments:
                if comment.id not in Comments_read.readlines() and 'Trump' in comment.body:
                    mentions += 1
                    Trump_file.write(comment.body + '\n')
                    print(comment.id)
                    Comments_read.write(comment.id + '\n')


    print("The above are the flattened comments for the top 25 submissions of The_Donald for: " + str(time.clock()))
    Trump_file.close()
    Comments_read.close()
    time.sleep(600)


