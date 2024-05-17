#El ciclo while es una Estructura iteractiva que se ejecuta X veces



for contador in range(1,6):
    print("@")

suma=0
contador=1
while contador<=5:
    suma+=contador
    contador+=1
    print("@")
print(f"Se termino de cilclar: {suma}")

tabla=int(input("Ingresa un nuevo numero para calcular su tabla de multiplicar: "))
i=1
multi=0

while i<=10:
    multi=i*tabla
    i+1
    print(f"{tabla} X {i} = {multi}")
    i+=1