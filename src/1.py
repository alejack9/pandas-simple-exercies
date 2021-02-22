import pandas as pd

df = pd.DataFrame({
    'Anno': [2018, 2014, 2010, 2006, 2002],
    'Sede': ['Russia', 'Brasile', 'Sudafrica', 'Germania', 'Corea del Sud'],
    'Vincitore': ['Francia', 'Germania', 'Spagna', 'Italia', 'Brasile'],
    'Numero Goal': [169, 171, 145, 147, 161],
    'Pubblico': [47371, 53592, 49670, 52401, 42268],
})


def exec():
    print(df)


if __name__ == '__main__':
    exec()
