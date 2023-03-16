import random
import praw
import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# Access variables from .env file
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
user_agent = os.getenv('USER_AGENT')


# Authenticate your bot account
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    username=username,
    password=password,
    user_agent=user_agent
)

# Choose the subreddit to monitor
subreddit = reddit.subreddit("WGU")

# Set the keywords to search for
keywords = ["ball", "green", "banana", "cat", "dog", "boy", "girl"]

# List of possible replies
replies = [
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum",
    "llo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni",
    "Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? "
    ]


# Monitor new posts and comments and reply if the keywords are found
for comment in subreddit.stream.comments(skip_existing=True):
    for keyword in keywords:
        if keyword in comment.body.lower():
            print(f"Found a comment with keyword '{keyword}':")
            print(comment.body)
            comment.reply(random.choice(replies) + "\n\n *I'm a bot, this action was completed automatically.*")
