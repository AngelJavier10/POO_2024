class Coches:

    #Atributos o propiedades (variables)
    #Caracteristicas del coche
    #valores iniciales es posible declarar al principio de una clase
    color="rojo"
    marca="Ferrari"
    modelo="2010"
    velocidad=300
    caballaje=500
    plazas=2
    # El encapsulamiento o visibilidad es importante que a traves de el es posibleque python sepa como va a utilizar los atributos y metodos de la clase
    #Atributos Publicos
    atributo_publico="Soy un Atributo Publico"
    # atributo privado
    __atributo_privado="Soy un Atributo Pribado"

    #Nota.1, para utilizar un atributo privado es necesario usarlo dentro de un metodo publico

    def MetodoPublico(self):
       return self.__atributo_privado
    
    #Metodo Privado
    def __MetodoPrivado(self):
       print("Soy un Metodo Privado")

    #Nota. 2, para utilizar un metodo privado es necesario usarlo dentro de un metodo publico
       
    #Metodos o acciones o funciones que hace el objeto 

    def acelerar(self):
        self.velocidad+=1

    def frenar(self):
        self.velocidad-=1


    #Crear los metodos setters y getters .- estos metodos son importantes y necesarios en todos clases para que el programador interactue con los valores de los atributos a traves de estos metodos ... digamos que es la manera mas adecuada y recomendada para solicitar un valor (get) y/o para ingresar o cambiar un valor (set) a un atributo en particular de la clase a traves de un objeto. 
    # En teoria se deberia de crear un metodo Getters y Setters por cada atributo que contenga la clase
    #   Los metodos get siempre regresan valor es decir el valor de la propiedad a traves del return
    #Por otro lado el metodo set siempre recibe parametros para cambiar o modificar el valor del atributo o propiedad en cuestion

    def getColor(self):
      return self.color

    def setColor(self,color):
      self.color=color 

    def getMarca(self):
      return self.marca

    def setMarca(self,marca):
      self.marca=marca 

    def getModelo(self):
      return self.modelo

    def setModelo(self,modelo):
      self.modelo=modelo        

    def getVelocidad(self):
       return self.velocidad

    def setVelocidad(self,velocidad):
      self.velocidad=velocidad 

    def getCaballaje(self):
       return self.caballaje

    def setCaballaje(self,caballaje):
      self.caballaje=caballaje  

    def getPlazas(self):
       return self.plazas

    def setPlazas(self,plazas):
      self.plazas=plazas   
      print(f"Marca:{self.getMarca()}")

#Fin definir clase

#Crear un objetos o instanciar la clase

coche1=Coches()

#Mostrar los valores inicales del objeto o instancia de la clase
print(f"Marca: {coche1.marca} {coche1.color}, numeros de plazas: {coche1.plazas} \nModelo: {coche1.modelo} con una velocidad de {coche1.velocidad} Km/h y un potencia de {coche1.caballaje} hp")

#Utilizar los metodos set para cambiar o modificar los valores de los atributos aun cuando tengan un valor o no ... aunque los valores solo cambiaran para el objeto o instancia en cuestion en el momento que otro objeto se crea si se tienen valores iniciales se crea con los valores de los atributos de clase 

#actualizar todas las propiedades de objeto
coche1.setColor("Amarillo")
coche1.setModelo("2020")
coche1.setMarca("Porsche")
coche1.setVelocidad(250)
coche1.setCaballaje(450)
coche1.setPlazas(2)


#Aunque con los atributos se puede mostrar un valor se recomienda que sea a traves de los getters
print(f"Marca: {coche1.getMarca()} {coche1.getColor()}, numeros de plazas: {coche1.getPlazas()} \nModelo: {coche1.getModelo()} con una velocidad de {coche1.getVelocidad()} Km/h y un potencia de {coche1.getCaballaje()} hp")


#Crear otro objeto e imprimir los valores

coche2=Coches()

#Imprimir los valores del otro objeto
print(f"Marca: {coche2.getMarca()} {coche2.getColor()}, numeros de plazas: {coche2.getPlazas()} \nModelo: {coche2.getModelo()} con una velocidad de {coche2.getVelocidad()} Km/h y un potencia de {coche2.getCaballaje()} hp")
