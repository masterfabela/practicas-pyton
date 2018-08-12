class Coche():

  def __init__(self):
    self.__largoChasis = 250
    self.__anchoChasis = 120
    self.__ruedas = 4
    self.__enMarcha = False

  def arrancar(self, arrancamos):
    self.__enMarcha = arrancamos
    return self.estado()

  def estado(self):
    chequeo = self.__chequeoInterno()
    if self.__enMarcha and chequeo:
      return "El coche esta en marcha"
    elif self.__enMarcha and not chequeo:
      return "Algo ha ido mal en el chequeo, no podemos arrancar"
    else:
      return "El coche esta apagado" 

  def getCaracteristicas(self):
    return "El coche tiene ", self.__ruedas, " ruedas. y un ancho de ", self.__anchoChasis, " y un largo de ", self.__largoChasis

  def __chequeoInterno(self):
    print("Realizando chequeo interno")
    self.gasolina = "ok"
    self.aceite = "mal"
    self.puertas = "cerradas"
    return self.gasolina == "ok" and self.aceite=="ok" and self.puertas == "cerradas"

miCoche = Coche()
print(miCoche.arrancar(True))
print(miCoche.getCaracteristicas())

print("-----------A continuacion creamos el segundo objeto--------------")
miCoche2 = Coche()
print(miCoche2.getCaracteristicas())