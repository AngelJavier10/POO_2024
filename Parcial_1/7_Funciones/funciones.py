#una funcion es un conjuto de instrucciones agrupadas bajo un nombre en particular como un programa mas pequeño que cumpple 
#la funcio se puede reutilizar con el simple hecho de invocarla es decir mandarla llamar

#sintaxis:
#def nombredeMifuncion(Parametros):
#bloque o conjunto de instrucciones 

#Nombre de mi funcion (parametros)

#las funciones pueden ser de 4 tipos 
#1.- funciones que no recibe parametros y no regresa valor
#2.- funciones que no recibe parametos y regresa valor 
#3.- funcio que recibe parametros y no regresa valor
#4.- funcion que recibe y regresa

#1
def SumaNumeros1():
    n1=int(input("Numero # 1:"))
    n2=int(input("Numero # 2:"))
    suma=n1+n2
    print(f"{n1}+{n2}={suma}")


#2
def SumaNumeros2():
    n1=int(input("Numero # 1:"))
    n2=int(input("Numero # 2:"))
    suma=n1+n2
    return f"{n1}+{n2}={suma}"
    return

#4
def SumaNumeros4(n1,n2):
    suma=n1+n2
    return f"{n1}+{n2}={sum}"




n1=int(input("Numero #1:"))
n2=int(input("Numero #2:"))

print(SumaNumeros4(n1,n2))



