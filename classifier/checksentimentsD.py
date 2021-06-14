from dostoevsky.tokenization import RegexTokenizer
from dostoevsky.models import FastTextSocialNetworkModel
import pandas as pd


posts = pd.read_csv(r'newsdata/MAIL.csv', sep=',')['post']



tokenizer = RegexTokenizer()
model = FastTextSocialNetworkModel(tokenizer=tokenizer)

results= model.predict(posts, k = 1)

for message, sentiment in zip(posts, results):
    if 'negative' in sentiment or 'positive' in sentiment:
        print(message, '->', sentiment)
        print('\n\n')