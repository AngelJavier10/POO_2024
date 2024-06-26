
print("\n\t..::CALCULADORA BASICA::..\n1.-Suma\n2.-Resta\n3.-Multiplicacion\n4.-Divicion\n5.-Potencia")
option=input("\t Elige una option:").upper()

if option=="1" or option=="+" or option=="SUMA":
    n1=int(input("Numero #1:"))
    n2=int(input("Numero #2:"))
    suma=n1+n2
    print(f"{n1}+{n2}={suma}")
elif option=="2" or option=="-" or option=="RESTA":
    n1=int(input("Numero #1:"))
    n2=int(input("Numero #2:"))
    resta=n1-n2
    print(f"{n1}-{n2}={resta}")
elif option=="3" or option=="*" or option=="MULTIPLICACION":
    n1=int(input("Numero #1:"))
    n2=int(input("Numero #2:"))
    multi=n1*n2
    print(f"{n1}*{n2}={multi}")
elif option=="4"or option=="/" or option=="DIVICION":
    n1=int(input("Numero #1:"))
    n2=int(input("Numero #2:"))
    divicion=n1/n2
    print(f"{n1}/{n2}={divicion}")
elif option=="5" or "POTENCIA":
    n1=int(input("Numero #1: "))
    Ex1=int(input("Exponente: "))
    n2=int(input("Numero #2: "))
    Ex2=int(input("Exponente: "))
    potencia1=n1**Ex1
    potencia2=n2**Ex2
    print(f"{n1}^{Ex1}={potencia1}")
    print(f"{n2}^{Ex2}={potencia2}")
else:
    print("Gracias por utilizar el sistema...")
    

    opcion=True
    while option:
        print("\n\t..::Calculadora Basica::..\n1.-Suma\n2.-Resta\n3.-Multiplicacion\n4.-Division\5.-Salir")
        opcion=input("\tElige una opcion. ").upper()
    
    





    