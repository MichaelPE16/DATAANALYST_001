import pandas as pd
import numpy as np

data = pd.Series(['hola', 1, None, 'h1'])

# print(data.notna())
##################################################################
#aprendemos a filtrar datos nulos y eliminarlos o limpiarlos

numeros = pd.Series([1, 5, 3, 8, None, 6.5, 7.4, None, 0])

# print(numeros)
# print(numeros.dropna())
# print(numeros)
# print(numeros[numeros.notna()])


df = pd.DataFrame([
    [1, 6, 4] ,
    [7, 8, None],
    [None, 5, 7], 
    ['h', None, 'o', 'l']
])


print(df)