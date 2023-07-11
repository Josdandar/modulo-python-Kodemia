#Un diccionario es ordenado
#Tambien existe un Dictionary Comprehension - obtener un diccionario a partir de un diccionario preexistente

#Una cadena de caracteres tambien se puede considerar iterable.

# perro = "winter"
# print(perro[:2])
#El inicio es incluyente y el final exluyente el primer indice lo incluye y el ultimo no lo va a incluir 

#Los metodos de string devuelven nuevos valores, no modifican el elemento original

#Hay un metodo que nos permite eliminar white space - o sea los espacios vacios 
#.strip() es el metodo de string 

#.replace() recibe dos argumentos 1: secuencia de caracteres a remplazar 2: caracteeres que remplazara
#Remplaza todos los caracteres que coincidan 

#Metodo split - Separa los strings dependiendo de lo que se especifique

# message = (
#     "Hello Koders, Hola Koders, Bye Koders"
# )
# mensaje_modificado = [msg.strip() for msg in message.split(",")]
# print(mensaje_modificado)

#metodo format, agrega valor en donde se coloquen las llaves y se los pasas como parametro llamando al metodo
# message = "Hello {} Koders. estoy equivocado somos {}"
# print(message.format(500, 777))

koders = [
    "Luis",
    "Benjamin",
    "Juan",
    "Julio",
    "Irving",
    "Miren",
    "Martin",
    "Miguel",
    "Enrique",
    "Francisco",
    "Rodrigo",
    "Francisco2",
    "Jose",
    "Jesus",
]

edades = [25, 32, 56, 65, 34, 22, 55, 22 , 10, 22, 15, 100, 2, 59]
koderInfo = ()

#unir las dos listas y imprimir
    