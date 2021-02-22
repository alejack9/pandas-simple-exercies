import pandas as pd
df1 = __import__('1').df

df2 = pd.DataFrame({
    'Anno': [2016, 2012, 2008, 2004, 2000],
    'Sede': ['Francia', 'Polonia', 'Austria', 'Portogallo', 'Belgio'],
    'Vincitore': ['Portogallo', 'Spagna', 'Spagna', 'Grecia', 'Francia', ],
    'Numero Goal': [108, 76, 71, 77, 85],
    'Pubblico': [47594, 46479, 36383, 37306, 35220],
})


def exec():
    # Il set e` usato per togliere le ripetizioni
    vincitori = set(pd.merge(df1, df2, on='Vincitore')['Vincitore'])

    print(vincitori)


if __name__ == '__main__':
    exec()
