import pandas as pd
import numpy as np

df = pd.read_csv(r'D:\Last\1.DATAENGINEER\PYSPTS\csv\estudiantes_secundaria.csv')

# print(df.head())
data = pd.DataFrame(df, columns=['gender', 'race', 'parentalLevelEducation', 'lunch', 'testPreparationCourse', 'math_score', 'reading_score', 'writing_score', 'promd'])
data['promd'] = data[['math_score', 'reading_score', 'writing_score']].mean(axis=1).round(2)
print('Conoce tu data frame =>', np.shape(df))
print('Conoce la info de tu csv =>', df.info())
print('Resumen estadistico de los datos\n', df.describe())
print('Estudiantes con mayor calificacion en matematicas\n'
      ,data.loc[data.math_score > 90, ['gender', 'math_score']].sort_index(ascending=False))


print('Datos de los estudiantes con promedio total de Materias \n', data.head(10))


print('Suma de datos nulos =>\n ', data.isna().sum())

print(df.tail(15))
promedios = df[['math_score', 'writing_score', 'reading_score']].agg(['mean', 'std', 'min', 'median', 'max'])
print(promedios)


# investiga cuantos hombres y cuantasmujeres hay en esta escuela
hombres = df['gender'] == 'male'
mujeres = df['gender'] == 'female'
print('Cantidad de Hombres ',hombres.sum())
print('Cantidad de Mujeres ', mujeres.sum())

print(df['gender'].value_counts())

print('Cantidades de padres con dregrees or not \n', df['parentalLevelEducation'].value_counts())

print('Lunche de los estudiantes\n',df['lunch'].value_counts())
print(df[['gender', 'parentalLevelEducation', 'lunch']].value_counts())

print('Estudiantes destacados\n', data[data['promd'] >=85].sort_values(['promd']
, ascending=True).head(15), f"\nCantidad total de registros " , data.head(15).index.size)


#crear una funcion que agregue en el promedio de los estudianes si estos sacaron A, B, C, D, F


def categoria_notas(promedio): 
    if promedio >= 90.0: 
        return 'A'
    elif promedio >=80.0: 
        return 'B'
    elif promedio >=70.0: 
        return 'C'
    elif promedio >= 60.0: 
        return 'D'
    else: 
        return 'F'
    
data['category'] = data['promd'].apply(categoria_notas)
print(data.head(15).sort_values(['category'], ascending=True))

print(data['category'].value_counts())   

print("Datos de correlacion de materias \n", data[['math_score', 'reading_score', 'writing_score']].corr())
#epezamos a agrupar los datos
print(data.groupby('gender')[['math_score', 'reading_score', 'writing_score']].mean()) 
# aqui estamos agrupando por genero los estudiantes cuyas calificaciones son mejores o peores segun el genero

print(data.groupby('parentalLevelEducation')[['math_score', 'reading_score', 'writing_score']].mean())
#este categoriza los estudiantes segun el nivel academico de sus padres

print(data.groupby('lunch')[['math_score', 'reading_score', 'writing_score']].mean())
#estudianes cuyas materias les va mejor o peros segun su lunch
