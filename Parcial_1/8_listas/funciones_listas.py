paises=["Mexico","[Usa","Brasil","China"]
numeros=[100,80,3.1416,75]
varios=["UTD",True,100,0.100]

#ordenar las listas
print(paises)
paises.sort()
print(paises)

print(numeros)
numeros.sort()
print(numeros)

#Agregar

print(numeros)
numeros.append(100)
print(numeros)
numeros.insert(len(numeros),200)
print(numeros)

#Remove

print(numeros)
numeros.remove(100)
print(numeros)
numeros.pop(2)
print(numeros)


# Dar la vuelta a los elementos de una lista

print(varios)
varios.reverse()

#Buscar un valor dentro de una lisata
encontro="Brasil" in paises
print(encontro)

# Vasiar una lista

print(paises)
paises.clear()
print(paises)

# Unir listas

print(varios)
varios.extend(numeros)
print(varios)
