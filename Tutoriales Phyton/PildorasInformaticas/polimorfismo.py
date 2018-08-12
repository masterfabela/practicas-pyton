class Coche():
  
  def desplazamiento(self):
    print("Me desplazo utilizando cuatro ruedas")

class Moto():

  def desplazamiento(self):
    print("Me desplazo utilizando 2 ruedas")

class Camion():

  def desplazamiento(self):
    print("Me desplazo utilizando 6 ruedas")

#Esta funcion sabe de que objeto se trata y puede ejecutar la
# funcion que sea mas comv eniente
def desplazamientoVehiculo(vehiculo):
  vehiculo.desplazamiento()

miVehiculo = Moto()
miVehiculo.desplazamiento()
miVehiculo2 = Coche()
miVehiculo2.desplazamiento()
miVehiculo3 = Camion()
desplazamientoVehiculo(miVehiculo3)

