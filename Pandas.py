import pandas as pd

obj = pd.Series([1, 2, 3])

# print(obj)

# print(obj.array)
# print(obj.index)
objeto= pd.Series([4, 3, 5], index=['Nombre', 'Edad', 'DOB'])

# print(objeto['Nombre'])
objeto['Nombre'] = 1010

# print('Edad'  in objeto)

objeto1 = {'Nombre': "Pedrito", 'Edad': 28, 'Manzana': '23MZT456'}
data = pd.Series(objeto1)
# print(data.to_dict())

#vamos a crear un ejecicio donde tengamos frutas en una lista y a partir de ello
# trabajaremos en lo que se requiere

frutas = ['Mango', 'Pera', 'Manzana']
obj2 = pd.Series(data, index=frutas)

# print(obj2)
#cuando tenemos una seria a la cual le queremos indexar un arreglo mucha veces si 
# los datos no corresponden con los de la serie colocara esos datos como NaN o Null
# Para comprobar esto muchas veces podemos usar isna()

# print(pd.isna(obj2)) #$ esto da True si el calor es Null

# print(pd.notna(obj2)) # este verifica y da True si el objeto no es nulo

# print(pd.isna(obj2).sum()) # este sum() suma los valores que si son nulos

# print(pd.notna(obj2).sum()) # este suma los que no son nulos

###################################################
#DATAFRAMES

datos_geograficos = {
    'estado': [
        'California',
        'Texas',
        'Florida',
        'Nueva York',
        'Pensilvania',
        'Illinois'
    ],
    'anio': [
        2020,
        2020,
        2021,
        2022,
        2021,
        2020
    ],
    'poblacion_millones': [
        39.51,
        29.14, 
        21.78, 
        19.83, 
        13.00, 
        12.81
    ]
}

# print(datos_geograficos)

frame = pd.DataFrame(datos_geograficos)

# print(frame.head())

orden = pd.DataFrame(datos_geograficos, columns=['anio', 'poblacion_millones', 'estado', 'promd'])
orden['promd'] = orden['poblacion_millones'] * 2 / 100
# print(orden)
# print(orden['estado'])

frame2 = orden.copy()
#aqui especificamos los datos qeu no queremos ver del frame
# print(frame2.drop(index=[1, 5]))
# print(frame2.drop(columns=['anio']))
# print('Esta es la copia en crudo')
# print(frame2)


##########################
#Slicing con pandas

# print(orden[:-4:-1])
# print(orden[:-4:-1].sort_index(ascending=True))

###########
#Loc
copia = 4
# print(f"Datos Pertenecientes al Registro #{orden.index[copia]}")
# print(
#     orden.loc[copia]
# )

# print(orden.iloc[[1, 5], [2, 3]]) # asi puedo ver los registos usando incices numericos
print(orden)
# print('\n Aqui mostramos el anio y el primedio de Texas \n')
# print(orden.loc[orden.estado == 'Texas', ['anio', 'promd']])
# print('\n Aqui mostramos el anio y el primedio para los datos de idice mayor o igual 2 \n')
# print(orden.loc[orden.index >= 2, ['anio', 'promd']])

print(orden.describe()) # esta funcion nos da valores estadisticos aplicados al dataframe
