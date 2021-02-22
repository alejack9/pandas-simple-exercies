import pandas as pd
df = __import__('1').df

df['Numero Goal'] = df.loc[:, 'Numero Goal'].map(lambda x: x/64)

print(df)
