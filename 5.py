import pandas as pd
df = __import__('1').df

# Calcolare la media non influisce sul risultato
sede = df[df['Numero Goal'] == df['Numero Goal'].min()]['Sede']

print(sede)
