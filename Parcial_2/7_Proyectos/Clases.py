


class figuras:


    def _init_(self,largo,ancho):
        self.largo=largo
        self.ancho=ancho
    
    def getlargo(self):
      return self.largo

    def setlargo(self,largo):
      self.largo=largo
    
    def getancho(self):
      return self.ancho

    def setancho(self,ancho):
      self.ancho=ancho 


class rectangulo (figuras):
   def __init__(self,largo,ancho,CalcularArea):
      super().__init__(largo,ancho)
      self.CalcularArea=CalcularArea

   def getEje(self):
     return self.CalcularArea

   def setEje(self,CalcularArea):
      self.CalcularArea=CalcularArea
   def getInfo(self):   
        print(f"Marca: {self.getlargo()} {self.getancho()}") 

class Circulo (figuras):
   def __init__(self,largo,ancho,radio,CalcularArea):
      super().__init__(largo,ancho)
      self.CalcularArea=CalcularArea
      self.radio=radio

   def getTraccion(self):
    return self.CalcularArea

   def setCerrada(self,CalcularArea):
     self.CalcularArea=CalcularArea
   def getTraccion(self):
    return self.radio

   def setCerrada(self,radio):
     self.radio=radio
   





