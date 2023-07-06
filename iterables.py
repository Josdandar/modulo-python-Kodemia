#Iterable, todo tipo de dato que podemos recorrer. 

#Listas - Son ordenadas, pueden cambiaar y permiten valores duplicados. tienen index y pueden modificarse.se accede a valores con corchetes, tambien haciendo referencia al indice del valor que queremos cambiar lo podemos cambiar asignandole un nuevo valor
#Listas - para insertar elementos tenemos metodo insert(agrega elementos en la posicion especificada) y append(agrgea elementos al final de la lista)
#Suma de listas crea una tercer lista
#Remove elimina elementos de una lista pasandole el valor, Pop, eliina por indice o sin parametros elimina el ultimo elemento

# fruits = [
#     "banana",
#     "orange",
#     "Kiwi",
#     "melon",
#     1,
#     20,
#     8.7,
#     "Cherry",
#     "mango",
#     "apple",
# ]


# print(fruits)
# fruits.sort(key=mi_funcion)
# print(fruits)


    
#lIST COMPREHENSION 
#obtener una lista de otra lista

#Diccionario es un tipo de dato ordenado, los elementos ya tienen un orden definido, son modificables y no permiten duplicados

#Escribir un script que permita ordenar la siguiente lista de tuplas por el segundo valor de cada tupla e manera ascendente y descendente
pair_numbers = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]


for pair in pair_numbers:
    segundo_valor = pair[1]
    print(segundo_valor)
