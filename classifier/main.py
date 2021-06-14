import pandas as pd
import flair
import re
import yfinance as yf 
from datetime import datetime, date, time
from get_all_tickers import get_tickers as gt

date_column = 'Mon Apr 06 22:19:45 PDT 2009'
text_column = "@switchfoot http://twitpic.com/2y1zl - Awww, that's a bummer.  You shoulda got David Carr of Third Day to do it. ;D"
id_column = '1467810369'
# print(datetime(2005, 7, 14, 12, 30))

# tsla = yf.Ticker("TSLA")
# tsla_stock= tsla.history(period='max')

# print(tsla_stock)
def clean(row):
    with_out_dogs = re.sub(r"@\w*",'',row)
    return " ".join(with_out_dogs.split())


sentiment_model = flair.models.TextClassifier.load('en-sentiment')
data = pd.read_csv('./datasets/tweets_kaggle_1600000.csv',encoding="ISO-8859-1")
tickers = pd.read_csv('./datasets/tickers.csv')
tickers_list = tickers[tickers.columns[0]]



list_of_tickers = gt.get_tickers()
print(list_of_tickers)

# data.head()
for row in range(100):    
    id = data[id_column][row]
    date = data[date_column][row]
    text = data[text_column][row]
    clean_text = clean(data[text_column][row])
    sentense = flair.data.Sentence(clean_text)
    sentiment_model.predict(sentense)
    result = sentense.labels[0].value + ' ' + str(sentense.labels[0].score)
    print(id,date,clean_text, result)