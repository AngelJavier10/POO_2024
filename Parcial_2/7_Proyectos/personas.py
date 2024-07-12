
class personas:
    def __init__(self,nombre,edad,tel):
        self.nombre=nombre
        self.edad=edad
        self.tel=tel
# Nombre
    def getnombre(self):
      return self.nombre

    def setColor(self,nombre):
      self.nombre=nombre

# edad
    def getedad(self):
       return self.edad
    

    def setedad(self,edad):
       self.edad=edad

# Telefono
    def gettel(self):
       return self.tel


    def settel(self,tel):
       self.tel=tel



class Estudiantes (personas):
    def __init__(self,carrera,matricula,informar_carrera,info_persona):
       super().__int__(informar_carrera,info_persona)
       self.matricula=matricula
       self.carrera=carrera


    def getcarrera(self):
      return self.carrera

    def setColor(self,carrera):
      self.carrera=carrera


    def getmatricula(self):
       return self.matricula
    
    def setmatricula(self,matricula):
       self.matricula=matricula
    def getInfo(self):
      print(f"Carrera: {self.getMarca()} {self.getColor()}, matricula: {self.getPlazas()} \ncarrera: {self.getModelo()} info: {self.getVelocidad()}  info personal: {self.getEje()}")       




class Docentes (personas):
    def __init__(self,modalidad,num_empleado,informar_modalidad,info_personal):
       super().__int__(informar_modalidad,info_personal)
       self.modalidad=modalidad
       self.num_empleado=num_empleado

    def getmodalidad(self):
       return self.modalidad
    
    def setmodalidad(self,modalidad):
       self.modalidad=modalidad

    def getnum_empleado(self):
       return self.num_empleado
    
    def setnum_empleado(self,num_empleado):
       self.num_empleado=num_empleado

    
       