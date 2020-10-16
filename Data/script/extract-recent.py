import pandas as pd

data = pd.read_csv('/Users/mbatakuclinton/HIT SONG PREDICTION/song-popularity-prediction/Data/archive/data.csv')

recent = data['year'] >= 2000
recent_data = data[recent]
print(recent_data.shape)

recent_data.reset_index(inplace=True)

recent_data.drop(['index'], axis= 1, inplace=True)

recent_data.to_csv('/Users/mbatakuclinton/HIT SONG PREDICTION/song-popularity-prediction/Data/archive/recent_data.csv')
