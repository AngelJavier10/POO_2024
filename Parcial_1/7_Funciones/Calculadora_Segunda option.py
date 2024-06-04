print("\n\t..::CALCULADORA BASICA::..\n1.-Suma\n2.-Resta\n3.-Multiplicacion\n4.-Divicion")
option=input("\t Elige una option:").upper()

n1=int(input("Numero #1:"))
n2=int(input("Numero #2:"))

if option=="1" or option=="+" or option=="SUMA":
    print(f"{n1}+{n2}={n1+n2}")
elif option=="2" or option=="-" or option=="RESTA":
    print(f"{n1}-{n2}={n1-n2}")
elif option=="3" or option=="*" or option=="MULTIPLICACION":
    print(f"{n1}*{n2}={n1*n2}")
elif option=="4"or option=="/" or option=="DIVICION":
    print(f"{n1}/{n2}={n1/n2}")
else:
    print("Gracias por utilizar el sistema...")