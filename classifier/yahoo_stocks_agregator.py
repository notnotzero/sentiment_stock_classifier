import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import datetime

tickers = ['YNDX', 'LKOH', 'MAIL', 'AFLT', 'QIWI', 'VTBR', 'DSKY', 'LNTA', 'MSFT', 'TSLA', 'SBUX','OZON']

# # def format_time(time):
# #     splited = time.split(' ')
# #     return f'{splited[2]}-{month_number[splited[1]]}-{splited[0]}'

# month_number = {
#     'января': '01',
#     'февраля': '02',
#     'марта': '03',
#     'апреля': '04',
#     'мая': '05',
#     'июня': '06',
#     'июля': '07',
#     'августа' : '08',
#     'сентября' : '09',
#     'октября': '10',
#     'ноября': '11',
#     'декабря': '12',
# }

df = pd.read_csv(f'newsdata/{ticker}.csv')
stocks_frame = pd.DataFrame()
stocks_array = []
for date in df['time'][:200]:
    year, month,day = [int(i) for i in date.split('-')]

    start = datetime.datetime(year,month,day)
    end = datetime.datetime(year,month,day) + datetime.timedelta(days=1)
    day_info = yahoo.history(
    start=start,
    end=end,
    ).reset_index()
    stocks_frame = pd.concat([stocks_frame, day_info], axis=0)

stocks_frame.to_csv('./test_stcok_yndx.csv',index=False)


# result['time'] = stock['Date']
# result['']

# print(stock)









# df = pd.read_csv('yandex_sent_full_predict.csv', sep=',')
# df_with_format_time = pd.read_csv('newsdata/YNDX.csv', sep=',')
# df['time'] = df_with_format_time['time']

# df.to_csv('yandex_sent_news.csv',index=False)