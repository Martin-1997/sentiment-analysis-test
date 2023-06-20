import snscrape.modules.twitter as sntwitter
import pandas as pd

# query = "monero"
query = "monero min_replies:20 min_faves:100 min_retweets:18 since:2023-06-10"
tweets = []
limit = 100

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    
    # print(vars(tweet))
    # break
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.user.username , tweet.rawContent])
        
df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])
print(df)

