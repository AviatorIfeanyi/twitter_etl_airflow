import pandas as pd

def transform_data(data):
  tweets_df = pd.read_csv(data)
  print(tweets_df.info() )
	### Transformation happens here	
  return



