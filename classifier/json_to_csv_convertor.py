import pandas as pd

df = pd.DataFrame()

data = {
        'id': '1234',
        'created_at': '21321',
        'text': 'test_tweet'
}

df = df.append(data, ignore_index=True)



df.to_csv(r'./test.csv')