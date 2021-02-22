import pandas as pd
df1 = __import__('6').df1
df2 = __import__('6').df2

dfConcat = pd.concat([df1, df2])
dfConcat['Tipologia'] = ['MONDIALE' if x < len(
    df1) else 'EUROPEO' for x in range(0, len(dfConcat))]


def exec():
    print(dfConcat)


if __name__ == '__main__':
    exec()
