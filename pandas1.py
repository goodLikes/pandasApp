import pandas as pd
import random

lst = ['robot'] * 10 + ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

unique_values = data['whoAmI'].unique()

# Создаем пустой DataFrame для one hot encoding
one_hot_df = pd.DataFrame()

for value in unique_values:
		one_hot_df[value] = (data['whoAmI'] == value).astype(int)

print(one_hot_df.head())