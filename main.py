import os
import sys
import tweepy

if not os.getenv('TWITTER_TOKEN'):
    print("TWITTER_TOKEN not set Please Set TWITTER_TOKEN")
    print("Exiting")
    sys.exit(1)

TWITTER_TOKEN = os.getenv('TWITTER_TOKEN')
# Auth2
client = tweepy.Client(bearer_token=TWITTER_TOKEN)

# Replace with your own search query
# query = "nft.pharo.tech"
query = "#covid19"
# query = "#covid19 -is:retweet"
# query = 'from:jabhishek87 -is:r

# search all is forbidden for normal user and can only used by
# for the `Academic Research product track`
# https://developer.twitter.com/en/docs/twitter-api/getting-started/about-twitter-api#v2-access-level
# tweets =  client.search_all_tweets(search_term)

tweets = client.search_recent_tweets(
    query=query, tweet_fields=['context_annotations', 'created_at'],
    user_fields=['profile_image_url'], expansions='author_id', max_results=100
)

# Get users list from the includes object
users = {u["id"]: u for u in tweets.includes['users']}

if tweets.data:
    for tweet in tweets.data:
        tw_url=f"https://twitter.com/{users[tweet.author_id]}/status/{tweet.id}"
        msg = f"text={tweet.text}, Author={users[tweet.author_id]}, tw_url={tw_url}"
        print(msg)
        # if len(tweet.context_annotations) > 0:
        #     print(tweet.context_annotations)