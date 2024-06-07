
import listas
#list(Array)
#son collecione o conjunto de datos/valores bajo un mismo nombre, para acceder a los valores se hace con un indice numerico

#Nota: sus valores si son modificables

#La lista es un coleccion ordenada y modificable. permite miembros diblicados.


# numeros=[23,34]
# print(numeros)

# for i in numeros:
#     print(i)
    

# i=0
# while i<len(numeros):
#   print(numeros[i])
#   i+=1

#Ejemplo 2 Crear una lista de palabras, posteriormente ingresar una palabra para buscar la conincidencia en lista e indicar si   
#la palabra y en que posicion en caso contrario indicar una sola vez si no la encontro

# palabra=["hola","2024","10.23","True"]
# print(palabra)
# palabra_buscar=input("Ingresar la palbra a buscar: ")

# noloencontro=True
# for i in palabra:
#    if palabra_buscar==i:
#       print(f"Encontre la palbra{palabra_buscar}, en la posicion:{palabra.index(i)}")
#       noloencontro=False
 
# while (True):
#  palabra=["hola","2024","10.23","True"]
#  print(palabra)
#  palabra_buscar=input("Ingresar la palbra a buscar: ")

#  noloencontro=True
#  for i in palabra:
#    if palabra_buscar==i:
#       print(f"Encontre la palbra{palabra_buscar}, en la posicion:{palabra.index(i)}")
#       noloencontro=False
#  if noloencontro:


#    print(f"No se encontro la palabra dentro de la lista")

   # ejemplo.3 Listamultilinea o multimensional (matriz)para crear una agenda telefonica

# agenda=[
#     ["Carlos",6181234567]
#     ["Fernando",618346733]
#     ["Matias",6183746372]
#     ["Juan Pablo",6183647223]
# ]
# print(agenda)

# for i in agenda:
#     print("i")
#     print(f"{agenda.index(i)+1.-{i}}")



# Ejemplo.4 Crear un programa que permita Gestionar (Asministrar) 
# peliculas, colocar un menu de opciones para agragar, removerconsultar peliculas 

# 1.- Utilizar funciones y mandar llamar llamar desde otro archivo
# 2.- Utilizar listas para almacenar los nombres de peliculas


def insertarPeliculas():
    pelicula=input("Ingresar la pelicual: ")
    Peliculas.append(pelicula)
    espereTecla()
def eliminarPeliculas():
    pelicula=input("Ingrese la pelicual: ")
    pelicula.removeprefix
    espereTecla()


Peliculas=[]

print("\n\t..::Cine Polito::..\n1.-Agregar\n2.-Remover\n3.-Buscar\n4.-Consultar\n5.-Salir")
option=input("\tElige una opcion: ").upper()

if option=="1" or option=="AGREGAR":
    insertarPeliculas()
elif option=="2" or option=="ELIMINAR":
    eliminarPeliculas()
  




      
