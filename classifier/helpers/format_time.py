import pandas as pd
import re

tickers = ['LKOH', 'MAIL', 'QIWI', 'VTBR', 'DSKY', 'LNTA', 'MSFT', 'TSLA', 'SBUX','OZON']
# год-месяц-день
month_number = {
    'января': '01',
    'февраля': '02',
    'марта': '03',
    'апреля': '04',
    'мая': '05',
    'июня': '06',
    'июля': '07',
    'августа' : '08',
    'сентября' : '09',
    'октября': '10',
    'ноября': '11',
    'декабря': '12',
}
def time_formatter (time):
    dot_index = time.index('·')
    with_out_author = time[0:dot_index-1].split(' ')
    return str(with_out_author[2])+'-'+str(month_number[with_out_author[1]]) + '-' + str(with_out_author[0])


for ticker in tickers:
    df = pd.read_csv(f'../newsdata/{ticker}.csv', sep=',')
    time_column = df['time']
       

    formatted_df =  pd.DataFrame()
    formatted_df['post'] = df['post']
    formatted_df['time'] = df['time'].map(time_formatter)

    formatted_df.to_csv(f'../newsdata/formatted_news_data/{ticker}.csv', index=False)