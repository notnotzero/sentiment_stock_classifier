from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from nltk import word_tokenize
import pandas as pd
import numpy as np
import re
from sklearn.model_selection import train_test_split
from collections import defaultdict
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report
import json

with open('train.json') as f:
    raw_train = json.load(f)
with open('test.json') as f:
    raw_test = json.load(f)

def ru_token(string):
    """russian tokenize based on nltk.word_tokenize. only russian letter remaind."""
    return [i for i in word_tokenize(string) if re.match(r'[\u0400-\u04ffа́]+$', i)]

print(ru_token('Привет, Ваня! Я хочу тебе сказать что-то приятное'))
params = {}
params['tokenizer'] = ru_token
params['stop_words'] = stopwords.words('russian')
params['ngram_range'] = (1, 3)
params['min_df'] = 3

tfidf  = TfidfVectorizer(**params)

tfidf.fit([i['text'] for i in raw_train + raw_test])    
print(tfidf)
train = {}
val = {}
tmp = defaultdict(list)
for e in raw_train:
    tmp[e['sentiment']].append(e['text'])
for l in tmp:
    train[l], val[l] = train_test_split(tmp[l], test_size=0.2, random_state=2018)

def upsampling_align(some_dict, random_state=2018):
    rand = np.random.RandomState(random_state)
    upper = max([len(some_dict[l]) for l in some_dict])
    print('upper bound: {}'.format(upper))
    tmp = {}
    for l in some_dict:
        if len(some_dict[l]) < upper:
            repeat_time = int(upper/len(some_dict[l]))
            remainder = upper % len(some_dict[l])
            _tmp = some_dict[l].copy()
            rand.shuffle(_tmp)
            tmp[l] = some_dict[l] * repeat_time + _tmp[:remainder]
            rand.shuffle(tmp[l])
        else:
            tmp[l] = some_dict[l]
    return tmp    

btrain = upsampling_align(train)

m_params = {}
m_params['solver'] = 'lbfgs'
m_params['multi_class'] = 'multinomial'

softmax = LogisticRegression(**m_params)
train_x = [j for i in sorted(btrain.keys()) for j in btrain[i]]
train_y = [i for i in sorted(btrain.keys()) for j in btrain[i]]
softmax.fit(tfidf.transform(train_x), train_y)
print(train_x,tfidf.transform(train_x))

test_x = [j for i in sorted(val.keys()) for j in val[i]]
true = [i for i in sorted(val.keys()) for j in val[i]]

pred = softmax.predict(tfidf.transform(test_x))

accuracy_score(true, pred)

lab = LabelEncoder()
c_true = lab.fit_transform(true)
c_pred = lab.transform(pred)
print(classification_report(c_true, c_pred, target_names=lab.classes_, digits=5))


tickers = ['YNDX', 'LKOH', 'MAIL', 'AFLT', 'QIWI', 'VTBR', 'DSKY', 'LNTA', 'MSFT', 'TSLA', 'SBUX','OZON']
for ticker in tickers:
    df = pd.read_csv(f'./newsdata/formatted_news_data/{ticker}.csv', sep=',')

    sub_pred = softmax.predict(tfidf.transform([i for i in df['post']]))
    sub_df = pd.DataFrame()
    sub_df['sentiment'] = sub_pred
    sub_df['post'] = df['post']
    sub_df['time'] = df['time']

    sub_df.to_csv(f'./newsdata/news_data_with_sentiment/{ticker}.csv',index=False)
