from polyglot.text import Text
import pandas as pd
import re




sum = 0

posts = pd.read_csv('newsdata/AFLT.csv', sep=',')['post']
for post in posts:
    try:
        print(post,Text(post).polarity, '\n\n\n')
        sum += Text(post).polarity
    except:
        sum += 0
print(sum)