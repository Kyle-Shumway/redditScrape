import praw
import time
import smtplib


reddit = praw.Reddit(client_id="CLIENT ID",
                    client_secret='CLIENT SECRET',
                    user_agent='REDDIT USERNAME')

print(reddit.read_only)

lfu_users = []   #users that are scraped
seen_users = [] #users that have been scrapped already
count = 1
while (count == 1):
    for submission in reddit.subreddit('SUBREDDIT').hot(limit=20): #finds submissions in specific subreddit hot 20 is the latest 20 posts
            if (submission.link_flair_text == "FLAIR"): #specific flair for people looking for a group
                lfu_users.append(submission.author) #appends the user to the users array

    strUser = "";
    for user in lfu_users: #loops through all users and writes it in a file
        strUser = str(user)
        if user in seen_users: #checks if the user is new
            break
        else:
            with open('redditLog', 'a') as out:
                out.write("/u/" + strUser + '\n')
                seen_users.append(user)

    time.sleep(120) # sleep for 2mins
