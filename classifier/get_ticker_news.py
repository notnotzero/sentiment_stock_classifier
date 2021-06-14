# Import libraries
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import os
import pandas as pd
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer
# import flair
import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib
from datetime import datetime

# sentiment_model = flair.models.TextClassifier.load('en-sentiment')
# finwiz_url = 'https://finviz.com/quote.ashx?t='
# news_tables = {}
# tickers = ['MSFT']





# msft_stock = msft.history(
#     start=(data['created_at'].min()).strftime('%Y-%m-%d'),
#     'Mar-29-21'.strftime('%Y-%m-%d'),
#     interval='60m'
# ).reset_index()

# for ticker in tickers:
#     url = finwiz_url + ticker
#     req = Request(url=url,headers={'user-agent': 'my-app/0.0.1'}) 
#     response = urlopen(req)    
#     # Read the contents of the file into 'html'
#     html = BeautifulSoup(response, 'html.parser')
#     # Find 'news-table' in the Soup and load it into 'news_table'
#     news_table = html.find(id='news-table')
#     # Add the table to our dictionary
#     news_tables[ticker] = news_table

# parsed_news = []

# # Iterate through the news
# for file_name, news_table in news_tables.items():
#     # Iterate through all tr tags in 'news_table'
#     for x in news_table.findAll('tr'):
#         # read the text from each tr tag into text
#         # get text from a only
#         text = x.a.get_text() 
#         # splite text in the td tag into a list 
#         date_scrape = x.td.text.split()
#         # if the length of 'date_scrape' is 1, load 'time' as the only element

#         if len(date_scrape) == 1:
#             time = date_scrape[0]
            
#         # else load 'date' as the 1st element and 'time' as the second    
#         else:
#             date = date_scrape[0]
#             time = date_scrape[1]
#         # Extract the ticker from the file name, get the string up to the 1st '_'  
#         ticker = file_name.split('_')[0]
        
#         # Append ticker, date, time and headline as a list to the 'parsed_news' list
#         parsed_news.append([ticker, date, time, text])

# columns = ['ticker', 'date', 'time', 'headline']
# parsed_news_frame = pd.DataFrame(parsed_news, columns=columns)
# parsed_news_frame.to_csv(r'./news_mock.csv')

def make_flair_scores(headlines):
    scores = []
    for headline in headlines:
        sentense = flair.data.Sentence(headline)
        sentiment_model.predict(sentense)
        result = ''
        if sentense.labels[0].value == 'POSITIVE':
            result = sentense.labels[0].score
        else : result = -1 * sentense.labels[0].score
        scores.append(result)
    return scores


# for article in parsed_news[:5]: 
#     text = article[3]
#     sentense = flair.data.Sentence(text)
#     sentiment_model.predict(sentense)
    
#     result = sentense.labels[0].value + ' ' + str(sentense.labels[0].score)
#     print(text,result)



# vader = SentimentIntensityAnalyzer()
# parsed_and_scored_news = pd.read_csv(r'./news_mock.csv', sep=',')
# nltk_scores = parsed_and_scored_news['headline'].apply(vader.polarity_scores).tolist()
# flair_scores = make_flair_scores(parsed_and_scored_news['headline'])

# nltk_scores_df = pd.DataFrame(nltk_scores)
# flair_scores_df = pd.DataFrame(flair_scores, columns=['flair_score'])

# parsed_and_scored_news = parsed_and_scored_news.join(nltk_scores_df, rsuffix='_right')
# parsed_and_scored_news = parsed_and_scored_news.join(flair_scores_df)
# parsed_and_scored_news.to_csv(r'./news_mock_with_flair.csv')
# parsed_and_scored_news['date'] = pd.to_datetime(parsed_and_scored_news.date).dt.date
# for result in parsed_and_scored_news['0']:

news_mock = pd.read_csv(r'./news_mock_with_flair.csv', sep=',')
# stock = pd.read_csv(r'./msft_stock.csv', sep=',')
# stock_dates = matplotlib.dates.date2num(stock['Datetime'])
# matplotlib.pyplot.plot_date(stock_dates, stock['Open'])
# plt.show()
news_date = matplotlib.dates.date2num(news_mock['date'])

print(datetime.strptime(news_date[0], '%m-%d-%y'))


# plt.plot(news_date, flair_scores)
# plt.show()