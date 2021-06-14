import datetime
import pandas as pd
import yfinance as yf

tickers = ['MSFT','TSLA']
#  'LKOH', 'MAIL', 'AFLT', 'QIWI', 'VTBR', 'DSKY', 'LNTA', 'MSFT', 'TSLA', 'SBUX','OZON']


history = {}
df = pd.DataFrame()
for ticker in tickers:
    yahoo =  yf.Ticker(ticker)
    time_column = pd.read_csv(f'../newsdata/news_data_with_sentiment/{ticker}.csv', sep=',')['time']
    for time in time_column:
        
        if not(time in history) : 
            year, month,day = [int(i) for i in time.split('-')]
            start = datetime.datetime(year,month,day)
            end = datetime.datetime(year,month,day) + datetime.timedelta(days=1)
            day_info = yahoo.history(
            start=start,
            end=end,
            ).reset_index()    
            if not(day_info.empty):
                history[time] = day_info
                df = pd.concat([df,day_info])
            # print(time,day_info)
            
    df.to_csv(f'../tickersdata/{ticker}.csv',index=False)