
print("\n\t..::CALCULADORA BASICA::..\n1.-Suma\n2.-Resta\n3.-Multiplicacion\n4.-Divicion")
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
else:
    print("Gracias por utilizar el sistema...")
    

    opcion=True
    while option:
        print("\n\t..::Calculadora Basica::..\n1.-Suma\n2.-Resta\n3.-Multiplicacion\n4.-Division\5.-Salir")
        opcion=input("\tElige una opcion. ").upper()
    
    





    