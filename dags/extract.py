import snscrape.modules.twitter as sntwitter
import pandas as pd

# Creating list to append tweet data to
def extract_data():
  
  tweets_list = []
    
    # scrape tweets and append to a list
  for i,tweet in enumerate(sntwitter.TwitterSearchScraper('Chatham House since:2023-01-14').get_items()):
    if i>5:
      break
    tweets_list.append([tweet.date, tweet.user.username, tweet.rawContent, 
                          tweet.sourceLabel,tweet.user.location
                          ])
      # convert tweets into a dataframe
  tweets_df = pd.DataFrame(tweets_list, columns=['datetime', 'username', 'text', 'source', 'location'])

      # save tweets as csv file
  tweets_df.to_csv('./tweets_extracted.csv')
