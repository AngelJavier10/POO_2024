# Manejo de errores es la forma en l que tienen los lenguajes de programacion
# para evitar que sucedan errores en tiempo de ejecucion

# Ejemplo 1 Error cuando una variable no se jenera

# # try:
# #  nombre=input("DAme el nombre: ")

# #  if len(nombre)>1:
# #     nombre_Usuario="El nombre es: "+nombre

# #  print(nombre_Usuario)
# # except:
# #   print("Es necesario introducir un nombre de usuario. . .")

# Ejemplo 2 Cuando se solicita un numero y se introduce una letra
try:
 numero=int(input("Dame un numero: "))
 if numero>0:
  print("..::Soy un numero entero positivo::..")
 else:
  print("..::Soy un numero entero negativo::..")
except:
 print("---no se puede convertir un caracter no numerico a numero. . .---")
else:
 print("---Todo se ejecuto sin errores---")

#  Ejemplo 3 cuando se generan multiples exepciones

try:
 numero=int(input("Dame un numero: "))

 print("El cuadraddo es:"+str(numero*numero))
except ValueError:
 print("Debes introducir un numero no se puede convertir un caracter que no sea numerico")
except TypeError:
 print("No es posible convertir el numero a entero")
else:
 print("Finalizo correctamente")
finally:
 print("listo se termino")




