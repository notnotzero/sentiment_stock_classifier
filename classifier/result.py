import pandas as pd
import datetime
import matplotlib.pyplot as plt

tickers = ['YNDX', 'LKOH', 'MAIL', 'AFLT', 'QIWI', 'VTBR', 'DSKY', 'LNTA', 'MSFT', 'TSLA', 'SBUX','OZON']


def sent_to_number(sentiment):
    if sentiment == 'positive':
        return 1
    if sentiment == 'negative':
        return -1
    if sentiment == 'neutral':
        return 0 


for ticker in tickers:
    news = pd.read_csv(f'./newsdata/news_data_with_sentiment/{ticker}.csv')
    stocks = pd.read_csv(f'./tickersdata/{ticker}.csv')
    news_count = news.shape[0]


    # stock_dict = {}
    result = {}

    for index in range(news_count): # news_count 
        row = news.iloc[[index]]
        time = row['time'].values[0]
        sent = sent_to_number(row['sentiment'].values[0])

        # if not(type(time) is float):
        # year,month,day = [int(i) for i in time.split('-')]
        open_values = stocks.loc[stocks['Date'] == time]['Open'].values
        close_values = stocks.loc[stocks['Date'] == time]['Close'].values 
        if ( len(open_values) > 0):
            open_value = open_values[0]
            close_value = close_values[0]
            diff = open_value - close_value
            
            if (not time in result ):
                result[time] = {
                                'open' : open_value,
                                'close' : close_value,
                                'sent' : sent,
                                'diff' : diff
                                }
            else: result[time]['sent'] += sent 
            # stock_dict[time]= sent_dict.get(time,0) + open_values[0]
            # sent_dict[time] = sent_dict.get(time,0) + sent
    correct = 0 
    missed = 0
    summary = len(result.keys())
    zeros = 0
    for key in result.keys():
        data = result[key]
        if ((data['open'] < data['close'] and data['sent'] > 0) or ( data['sent'] < 0 and data['open'] > data['close'])  ):
            correct += 1
        else:
            if data['sent'] != 0:
                print(data['sent'],data['open'],data['close'])
                missed += 1
        if data['sent'] == 0: 
            zeros += 1
    print(correct,missed,zeros,summary, correct / (correct + missed))
    


    # fig, axs = plt.subplots(2)
    # fig.suptitle('SENTIMENT')
    # axs[0].plot(stock_dict.keys(),stock_dict.values())
    # axs[1].plot(sent_dict.keys(),sent_dict.values())
    # # beautify the x-labels
    # plt.gcf().autofmt_xdate()
    # plt.show()
    # # print(sent_dict,len(),len(sent_dict.values()))
    # for key in sent_dict.keys():
    #     year,month,day = [int(i) for i in time.split('-')]
    #     date = datetime.datetime(year,month,day
    #     if not date in datetimes:
    #         print(key)
    # stock_info = yandex_stocks[yandex_stocks['Date'].str.contains(time)]['Open']
        # print(stock_info)
        # dates = matplotlib.dates.date2num(list_of_datetimes)