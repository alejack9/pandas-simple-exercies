import pandas as pd
df = __import__('1').df


def exec():
    vincitoriRecenti = df.head(3).loc[:, 'Vincitore']

    print(vincitoriRecenti)


if __name__ == '__main__':
    exec()
