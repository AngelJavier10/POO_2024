import random

miLista=['Manzana','Pera','Limon','Kiwi']

print(random.choices(miLista,weights=[1,1,1,1],k=3))