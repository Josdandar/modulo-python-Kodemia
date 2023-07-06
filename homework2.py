# 1. Escribe un script que le pregunte al usuario varios nombres hasta que el usuario especifique que ya no desea ingresar más nombres.
#     Como resultado deberá mostrar al usuario una lista, una tupla y un set con todos los nombres que ingresó el usuario

# respuesta = "si"
# nombresLista = []
# nombresTupla = ()
# nombresSet = set()

# while respuesta != "no":
#     respuesta = input("Desea agregar nombres? si/no ")
#     if respuesta == "no":
#         break
#     nombre = input("Escriba el nombre a agregar: ")
#     nombresLista.append(nombre)
#     nombresTupla += (nombre,)
#     nombresSet.add(nombre)

# print("Lista de nombres:", nombresLista)
# print("Tupla de nombres:", nombresTupla)
# print("Conjunto de nombres:", nombresSet)

#2. Escribe un script que calcule la diferencia entre un número dado y 17 e imprima el resultado.
#Si el número es más grande que 17 deberá imprimir el doble de la diferencia entre ambos números
# number = float(input("Dame un numero"))
# if number < 17:
#     resultado = 17 - number
# else:
#     resultado = (17 - number) * 2
# print("El resultado es", resultado)

# 3. Escribe un script que calcule la suma de 3 números dados por el usuario.
#     Si los valores son iguales deberá imprimir la suma multiplicada por 3
# valor1 = int(input("Dame un valor: "))
# valor2 = int(input("Dame un valor: "))
# valor3 = int(input("Dame un valor: "))

# if valor1 == valor2 and valor2 == valor3:
#     resultado = valor1 * valor2 * valor3
#     print(resultado)
# else:
#     resultado = valor1 + valor2 + valor3
#     print(resultado)

# 4. Escribe un script que calcule cuantas veces se repite un nombre en una lista de nombres determinada por el usuario.
# respuesta = "si"
# nombresLista = []

# while respuesta != "no":
#     respuesta = input("Desea agregar nombres? si/no ")
#     if respuesta == "no":
#         break
#     nombre = input("Escriba el nombre a agregar: ")
#     nombresLista.append(nombre)
    
# print(nombresLista.count("jose"))

