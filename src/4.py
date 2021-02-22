import pandas as pd
df = __import__('1').df


def exec():
    df['Numero Goal'] = df.loc[:, 'Numero Goal'].map(lambda x: x/64)

    print(df)


if __name__ == '__main__':
    exec()
