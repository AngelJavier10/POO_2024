
edad = 20
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")




# Iterar sobre una lista
numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    print(numero)

# Iterar sobre un rango de números
for i in range(5):
    print(i)





contador = 0
while contador < 5:
    print(contador)
    contador += 1




cadena1 = "Hola"
cadena2 = "Mundo"
cadena3 = cadena1 + " " + cadena2
print(cadena3)  # Salida: Hola Mundo






# Longitud de una cadena
cadena = "Hola Mundo"
print(len(cadena))  # Salida: 10

# Convertir a mayúsculas
print(cadena.upper())  # Salida: HOLA MUNDO

# Convertir a minúsculas
print(cadena.lower())  # Salida: hola mundo

# Reemplazar parte de la cadena
print(cadena.replace("Mundo", "Python"))  # Salida: Hola Python

# Dividir una cadena
print(cadena.split())  # Salida: ['Hola', 'Mundo']







# De cadena a entero
numero_str = "123"
numero_int = int(numero_str)
print(numero_int)  # Salida: 123

# De entero a cadena
numero = 123
numero_str = str(numero)
print(numero_str)  # Salida: "123"

# De cadena a flotante
flotante_str = "123.45"
flotante = float(flotante_str)
print(flotante)  # Salida: 123.45

# De flotante a cadena
flotante = 123.45
flotante_str = str(flotante)
print(flotante_str)  # Salida: "123.45"
