import praw

reddit = praw.Reddit(client_id = "zeaZLi0pfF18GQ", client_secret ="NL8mqsZr2rHX1kbVXQ1OIOilyzI" ,  user_agent ="prawDemo" )
subreddit = reddit.subreddit('Watches')
hot = subreddit.hot()
for submission in hot:
    print (submission.title)