import random

print("\n\t..::CALCULADORA BASICA::..\n1.-Recorrer Lista\n2.-Devolver un String\n3.-Ordenar\n4.-Mostrar Longitud")

milista=[]
for i in range(8):
    x=random.randrange(1,20)
    milista.append(x)
print("Los Numero Seleccionados son: ",(milista))

option=input("\t Elige una option:").upper()

if option=="1" or option=="RECORRER" or option=="RECORRER LISTA":
    print(milista)
    print("Numeros en Total [5]")
    print("Numero seleccionados Entre [-1 a 20-]")
elif option=="2" or option=="-" or option=="RESTA":
    print("Numeros en Total [5]")
elif option=="3" or option=="*" or option=="MULTIPLICACION":
    milista.sort()
elif option=="4"or option=="/" or option=="DIVICION":
    print("Numeros en Total [5]")
else:
    print("Gracias por utilizar el sistema...")
