
contador=1

for contador in range(1,6):
    print("@")
    print("Hola")


#ejemplo 2 Crear un programa que inmorima los numeros del 1 al 5 y los seme y al final imprima la suma

contador=1
suma=0
for contador in range(1,6):
    print(contador)
    suma+=contador

    print(f"La suma es: {suma}")

    #Ejemplo 3 Crar un progrma que imprima la tabla de multiplicar que el usuario desee
    tabla=input("ingresa un numero para calcular su tabla de multiplicar: ")
    
    i=1
    multi=0

multi=i+tabla

for i in range(1,11):
    print(f"{tabla} X {multi}")
    
