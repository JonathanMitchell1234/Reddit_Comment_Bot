# Reddit_Comment_Bot

This is a simple Python script that monitors a chosen subreddit and replies to any comments containing specific keywords with a randomly chosen reply from a list of possible replies.

# Getting Started
Clone this repository to your local machine.

Create a virtual environment and activate it.

Install the required packages using pip:

````pip install -r requirements.txt````


Create a Reddit account if you don't have one already.

Create a new Reddit app and get your client_id and client_secret. Follow these instructions to create a new app and obtain your credentials.

Create a .env file in the root directory of the project and add your credentials as environment variables:

```CLIENT_ID=your_client_id_here
CLIENT_SECRET=your_client_secret_here
USERNAME=your_reddit_username_here
PASSWORD=your_reddit_password_here
USER_AGENT=your_user_agent_here
```
Make sure to replace the values with your own credentials.

Choose the subreddit you want to monitor by modifying the subreddit variable in the script.

Set the keywords you want to search for by modifying the keywords list in the script.

Set the possible replies by modifying the replies list in the script.

Usage
To start the bot, activate your virtual environment and run the script.

The script will run indefinitely, monitoring the chosen subreddit for new comments and replying to any comments containing the specified keywords with a randomly chosen reply from the list of possible replies.

# Disclaimer
This script is for educational purposes only. Use at your own risk. Unapproved bots can result in suspensions and/or bans from Reddit. 