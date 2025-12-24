import pandas as pd
import numpy as np

data = pd.read_csv(r'D:\Last\1.DATAENGINEER\PYSPTS\csv\Dataset_Empresa_Fabricante_de_Algodón.csv', encoding='latin-1')

df = pd.DataFrame(data)
# data1 = df[['Beneficio_USD', 'Margen_Beneficio']].head().Margen_Beneficio.std().__round__()
# print(df.head()[['Fecha_Pedido']])
# print(df.head())
# --- 2. EJERCICIOS DE ANÁLISIS AVANZADO DE MANUFACTURA Y RENTABILIDAD ---

# -----------------------------------------------------------------------------------
# EJERCICIO 1: Feature Engineering y Eficiencia de CO2
# Título: Cálculo de la Intensidad de Carbono por Unidad.
# Descripción: Crea una nueva columna llamada 'Intensidad_CO2_x_Unidad' que calcule la
# emisión de CO2 por unidad vendida (Emision_CO2_Kg / Unidades_Vendidas). 
# Luego, calcula la media y la desviación estándar de esta nueva métrica, 
# agrupando por el 'Metodo_Produccion'.
# -----------------------------------------------------------------------------------
print("Cálculo de la Intensidad de Carbono por Unidad.")
dataframe = df
dataframe['Intensidad_CO2_x_Unidad'] = (df['Emision_CO2_Kg'] / df['Unidades_Vendidas']).round(2)
print(dataframe.head()[['Unidades_Vendidas', 'Costo_Produccion_Unitario_USD', 'Emision_CO2_Kg','Intensidad_CO2_x_Unidad']])
co2_sumary = dataframe.groupby('Metodo_Produccion')['Intensidad_CO2_x_Unidad'].agg(['mean', 'std']).round(2)
print(co2_sumary.head())

# -----------------------------------------------------------------------------------
# EJERCICIO 2: Advanced Aggregation: Rentabilidad por Método y Calidad
# Título: Análisis Bi-variado de Rentabilidad.
# Descripción: Utiliza pivot_table (o doble groupby) para mostrar el Margen de Beneficio
# promedio y la Cantidad Total de CO2 Emitida por cada combinación de 
# 'Metodo_Produccion' y 'Calidad_Algodon'. Ordena el resultado por el margen de beneficio.
# -----------------------------------------------------------------------------------
print('\nAnálisis Bi-variado de Rentabilidad.')
data_element = pd.pivot_table(dataframe,index=['Metodo_Produccion','Calidad_Algodon' ], 
                              values=['Margen_Beneficio', 'Emision_CO2_Kg'], 
                               aggfunc={'Emision_CO2_Kg': 'sum','Margen_Beneficio':'mean' }).sort_values('Margen_Beneficio', ascending= False).round(2)

print(data_element)

# -----------------------------------------------------------------------------------
# EJERCICIO 3: Time Series Analysis: Tendencia Mensual de CO2
# Título: Tendencia Mensual de Emisiones y Ventas.
# Descripción: Agrupa los datos por mes y año (usando .dt.to_period('M') en la columna
# de fecha) y calcula el total de Emision_CO2_Kg y la suma de Ventas_Totales_USD para 
# cada mes. Calcula la variación porcentual de CO2 mes a mes.
# -----------------------------------------------------------------------------------
print('\n Tendencia Mensual de Emisiones y Ventas.')
dataframe['Fecha_Pedido'] = pd.to_datetime(dataframe['Fecha_Pedido']).dt.to_period('M')
# print(dataframe[['Fecha_Pedido']].head())
Monthly_Trend = dataframe.groupby(dataframe['Fecha_Pedido']).agg({
    'Emision_CO2_Kg':'sum' , 'Ventas_Totales_USD': 'sum'
}).reset_index()
Monthly_Trend['Fecha_Pedido'] = Monthly_Trend['Fecha_Pedido']
Monthly_Trend['Variación_%_CO2_M'] = (Monthly_Trend['Emision_CO2_Kg'].pct_change() * 100).round(2)
Monthly_Trend = Monthly_Trend.fillna(0.0)
print(Monthly_Trend, '\n')

print('PIVOT TABLE', '\n')
######################################
data_month = pd.pivot_table(dataframe, index= dataframe['Fecha_Pedido'], 
                            values=['Emision_CO2_Kg', 'Ventas_Totales_USD'],
                            aggfunc={'Emision_CO2_Kg': 'sum','Ventas_Totales_USD': 'sum'})
data_month.reset_index(inplace=True)
data_month['Emision_%_mensual'] = (data_month['Emision_CO2_Kg'].pct_change() * 100).round(2)
data_month.fillna(0.0, inplace=True)
print(data_month)

# -----------------------------------------------------------------------------------
# EJERCICIO 4: Conditional Feature Engineering con NumPy
# Título: Clasificación de Eficiencia Hídrica.
# Descripción: Utiliza np.select para crear una nueva columna 'Uso_Agua_Clase' 
# clasificando el consumo de Agua_Utilizada_L en 'Eficiente' (debajo Q25), 
# 'Alto Consumo' (encima Q75) y 'Estándar' (en el medio). Muestra el recuento final de cada clase.
# -----------------------------------------------------------------------------------
# dataframe = np.select(dataframe['Uso_Agua_Clase'])
## FIX=---------------------------------------------------------------------------------------------------
print('\n Clasificación de Eficiencia Hídrica. \n')
print(dataframe['Agua_Utilizada_L'].head().min())
dataframe['Uso_Agua_Clase'] = pd.cut(dataframe['Agua_Utilizada_L'], 
                                     bins =[0, 250_000,750_000, np.inf], 
                                     labels=['Eficiente', 'Estándar', 'Alto Consumo'])
consumo_agua = df[["ID_Pedido", 'Pais', "Region","Agua_Utilizada_L", 'Uso_Agua_Clase']].head()
print(consumo_agua)
# print('\n EFICIENCIA DE CONSUMODE AGUA POR PAIS\n')
# print(consumo_agua.groupby('Uso_Agua_Clase')['Agua_Utilizada_L'].sum())



# -----------------------------------------------------------------------------------
# EJERCICIO 5: Window Functions: Control de Calidad
# Título: Identificación de Desempeño Atípico en Defectos.
# Descripción: Ordena el DF por 'ID_Pedido'. Calcula el promedio móvil (rolling mean) 
# de 'Defectos_Unidad' con una ventana de 5. Luego, identifica qué pedidos tienen 
# defectos al menos 2 veces por encima de ese promedio móvil.
# -----------------------------------------------------------------------------------



# -----------------------------------------------------------------------------------
# EJERCICIO 6: Data Quality: Imputación Condicional
# Título: Imputación Inteligente de Satisfacción.
# Descripción: Imputa los valores faltantes (NaN) en 'Satisfaccion_Cliente' con la 
# media de Satisfaccion_Cliente específica para los pedidos donde 'Estado_Pedido' es 'Entregado'.
# Verifica que no queden nulos después de la imputación.
# -----------------------------------------------------------------------------------



# -----------------------------------------------------------------------------------
# EJERCICIO 7: Advanced Aggregation: Costo por Unidad de Materia Prima
# Título: Costo Promedio Ponderado de Materia Prima.
# Descripción: Calcula la media PONDERADA del Costo_Produccion_Unitario_USD utilizando 
# Materia_Prima_Kg como pesos. Haz este cálculo agrupado por 'Categoria_Producto'.
# -----------------------------------------------------------------------------------



# -----------------------------------------------------------------------------------
# EJERCICIO 8: Efficiency Metric: Rendimiento de Materia Prima
# Título: Análisis de Rendimiento de Conversión de Materia Prima.
# Descripción: Crea una columna 'Rendimiento_Materia' (Unidades_Vendidas / Materia_Prima_Kg). 
# Calcula el rendimiento promedio agrupado por 'Turno_Produccion' y 'Metodo_Produccion'.
# -----------------------------------------------------------------------------------



# -----------------------------------------------------------------------------------
# EJERCICIO 9: Logistical Analysis: Retraso en la Entrega
# Título: Impacto del Retraso en la Satisfacción.
# Descripción: Crea una columna booleana 'Retraso' (True si Fecha_Produccion - Fecha_Pedido > Plazo_Entrega_Dias). 
# Calcula la satisfacción promedio (ignora nulos) para pedidos con Retraso=True vs. Retraso=False.
# -----------------------------------------------------------------------------------



# -----------------------------------------------------------------------------------
# EJERCICIO 10: Outlier Detection: Detección de Margen Atípico
# Título: Identificación de Margen de Beneficio Anormalmente Bajo.
# Descripción: Usa el rango intercuartílico (IQR) para identificar y listar ID_Pedido 
# que tienen un 'Margen_Beneficio' que se clasifica como outlier por debajo de Q1 - 1.5 * IQR.
# -----------------------------------------------------------------------------------


