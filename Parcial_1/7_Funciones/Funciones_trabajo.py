#Ejemplo 6 Crear un programa que solicite a traves de una funcion la siguiente informacion: Nombre del paciente, Edad, Estatura, tipo de sangre, Utilizar los 4 tipos de funciones 
def solicitarNumeros():
    global n1,n2
    n1=int(input("Numero # 1:"))
    n2=int(input("Numero # 2:"))

def calculadora(n1,n2,opcion):
    if opcion=="1" or opcion=="+" or opcion=="SUMA":
        
        return f"{n1}+{n2}={n1+n2}"
    elif opcion=="2" or opcion=="-" or opcion=="RESTA":
        
        return f"{n1}-{n2}={n1-n2}"
    elif opcion=="3" or opcion=="*" or opcion=="MULTIPLICACION":
       
        return f"{n1}*{n2}={n1*n2}"
    elif opcion=="4" or opcion=="/" or opcion=="DIVISION":
        
        return f"{n1}/{n2}={n1/n2}"
    else:
        opcion=False
        return "Gracias por utilizar el sistema ..."
            

opcion=True
