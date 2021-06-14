import pandas as pd


tickers = ['SBER','GAZP']

df = pd.DataFrame() 

# 3	12:06 Вчера · Портал vc.ru

for ticker in tickers:
    tickerDF = pd.read_csv(f'newsdata/{ticker}.csv')
    df = pd.concat([df,tickerDF],ignore_index=True)

df['time'] = [format_time(time) for time in df['time']]
print(df['time'])
# df.to_csv('newsdata/newssummary.csv',index=False)