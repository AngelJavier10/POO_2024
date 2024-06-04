import random

miLista=["Piedra","Papel","Tijera"]
#print(miLista)
print(random.choices(miLista,weights=[1,1,1],k=2))