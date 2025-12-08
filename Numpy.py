import numpy as np

# arr = [1, 3, 4, 3, 2, 2]

# x = np.array(arr)
# print(x *2)


# arr1 = np.arange(1_000_000)#este guion bajo nos ayuda a hacre la division de los valores y reconocer mas rapido que canidad hay en este valor
# lista = list(range(1_000_000))
# arr2 = arr1 * 2
# print(arr2)
array_ = [[1, 2, 3, 4, 5], [5, 3, 2, 1, 4]]
arrdims = np.array(array_)

# print(arrdims.ndim)
# print(arrdims.shape)

matarray3 = np.array([[[1, 2, 3], 
                       [1, 2, 4]], 
                      [[2, 4, 2], 
                       [8, 5, 6]]], dtype= np.float64)

# print(matarray3.shape)
# print(matarray3)

# print("cambiandole el tipo de dato al array ", matarray3)
array_cambiado = arrdims.astype(np.float64)

# print('cambiandole el valor al data set con astype', array_cambiado.ndim)


#indexado y slicing
arrautomatico = np.array(range(1, 15))
#Obtener el quinto elemento del array
# print(arrautomatico,"\n", arrautomatico[5])

#Obtener los últimos tres elementos del array
# print(arrautomatico[-3:])

#Obtener un slice (segmento) que incluya los números desde el 4 hasta el 9 (ambos incluidos).
# print(arrautomatico[3:9])

#Obtener todos los elementos del array, pero solo los que están en posiciones pares 
# (es decir, el elemento en el índice 0, 2, 4, etc.).
# print(arrautomatico[1::2])

#Obtener un nuevo array que contenga solo los números mayores que 10
lista = list(filter(lambda x : x > 10, arrautomatico))
# print(np.array(lista))

#Usar slicing para seleccionar los elementos del índice 5 al 8 
# (es decir, los números 5, 6, 7 y 8) y cambiar su valor a 99.
lista = arrautomatico[4:8]
# print(lista)
lista[:] = 99
# print(lista)


#Indexing con arreglos de vaias dimenciones
# print(matarray3)
# print(matarray3[0,1,2])
# print(matarray3[0][1][2])
# print("resultado",matarray3[0, 1, 2:])
# print(int(matarray3[0][1][2]))

texto = np.array(['cero', 'uno', 'cero', 'dos', 'cero'])
numero = np.array([[1, 2], [4, 3], [4, 5], [6, 7], [8, 9]])

# print(texto == 'cero')
# print(numero[texto == 'cero',::-2])

#cambiando el shape del arreglo

arregloshape = np.array(range(32)).reshape(4, 8)
# print(arregloshape.T) # a esto se le conoce como transposicion del arreglo

# print(np.dot(arregloshape.T, arregloshape)) # operaciones con matriccces
transpuestos = arregloshape.T @ arregloshape
# print(transpuestos) # operaciones con matrices

#retornar todos los valores que sean mayores a 500
# print(np.where(transpuestos > 950, 1, 0))

#para obtener el promedio de numeros del array
# print(np.mean(transpuestos))
# #para sacar el promedio en cada fila
# print(np.mean(transpuestos, axis=0)) # esto da el primedio de las colunas

# #Tambien podemos obtener la suma acumulatica
# print(np.cumsum(transpuestos, axis=0))

#tambien podemos obtener valores ramdom
ramdom = np.random.standard_normal((8, 4))
print(ramdom)

print(np.mean(ramdom, axis=0))

#podemos tambien ordenar los valores
# print(np.sort(ramdom))