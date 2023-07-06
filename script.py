#SOY DALTO CURSO DE YOUTUBE

# nombre = True 
# bienvenida = f"Hola {nombre}" # concatenando con f strings
# del nombre # Estoy borrando la variable nombre
# print("Hol" in bienvenida)
# Si quiero crear un comentario de multiples lineas usar """ 
#python es case sensitive

#En js se usa mas camel cale, en python es mas usado el snake case

#a diferencia de los arreglos, las tuplas no se pueden modificar
#para acceder a un set utilizamos un loop, no almacena datos duplicados 

# print(type(nombre)) # nos muestra el tipo de dato

#con funcion dir podemos ver los metodos de los distintos tipos de datos
#los metodos son funciones especificas de objetos

#Metodos de lista como len, append, insert, extend, pop, remove, clear, sort, reverse
#Metodos de string como len, upper, lower, capitilize, find, index, isnumeric,, isalpha, count, replace, split, endswith, startswith
#Metodos de diccionario como Keys que devuelve las llaves, get devuelve el valor de una llave, clear, pop, items para iterar el dict

#desempaquetado, asignamos los valores de la tupla a las variables creadas de esta forma, siguiendo un orden
# datos = ("Jose", "De Anda", 999)
# nombre, apellido, nivel = datos
# print(nombre)
#Funciona con Tuplas, Listas, Sets

#Podemos crear tuplas con un solo dato 
# nuevaTupla = "SoyUnaTupla", #Agregamos una coma para que sea tupla
# print(type(nuevaTupla))
#Es mejor crear tuplas cuando son datos de lectura

#Con la funcion zip() podemos recorrer dos listas al mismo tiempo del mismo tamano 

#Funciones en Python 
# def crear_contrasena(num):
#     chars = "abcdefghij"
#     num_entero = str(num)
#     num = int(num_entero[0])
#     c1 = num - 2
#     c2 = num 
#     c3 = num - 5 
#     contrasena = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
#     return contrasena #Esta funcion da un valor que podemos utilizar en otras cosas 

# password = crear_contrasena(5)
# print(f"Tu nueva contrasena es {password}")

#Parametro args, me permite poner parametros ilimitados, si queremos agregar otros parametros van antes y args al final
# def suma(nombre, *numeros):
#     return f"{nombre}, la suma de tus numeros es: {sum(numeros)}"

# resultado = suma("Jose", 5,5,9,9,9,9,9)
# print(resultado)

#Funciones Lambda - crear funciones anonimas 
#Retornan automaticamente, no son tan aptas para mas de una instruccion 
# numeros = [3,5,7,8,8,8,6]

# multiplicar_por_dos = lambda x : x*2

# numeros_pares = filter(lambda numero:numero%2==0, numeros)
# print(list(numeros_pares))