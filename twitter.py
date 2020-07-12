import tweepy
import time

auth = tweepy.OAuthHandler('API key','API key secret')
auth.set_access_token('Access Token','secret')

api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify=True)

user = api.me()

search = 'Football'
nrTweets = 500

# for follower in tweepy.Cursor(api.followers).items():
#     print(follower.name)

for tweet in tweepy.Cursor(api.search,search).items(nrTweets):
    try:
        print('Tweet Liked')
        #to like the Tweets
        # tweet.favorite()
        #to retweet
        tweet.retweet()
        #sleeping time to net get banned
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
