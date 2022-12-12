import twint
from datetime import date
import pandas as pd
# Configure
c = twint.Config()
# c.Username = "now"
c.Search = "#anxiety"
c.Limit = 10,000
c.Pandas = True
c.Lang = 'en'
c.Store_csv = True
c.Output = "new_file.csv"
twint.run.Search(c)
c.Until = (date.today()).strftime('2022-09-20')
# c.Since = (date.today() - timedelta(days=30)).strftime('2021-01-01')
# Run

Tweets_df = twint.storage.panda.Tweets_df
# print(len(Tweets_df))
Tweets_df.to_csv("new_file.csv")
