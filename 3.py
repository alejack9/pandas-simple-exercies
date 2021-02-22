import pandas as pd
df = __import__('1').df

vincitoriRecenti = df.head(3).loc[:, 'Vincitore']

print(vincitoriRecenti)
