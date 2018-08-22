class Vehiculo:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enMarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enMarcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print(
            "Marca: ", self.marca,
            "\nModelo: ", self.modelo,
            "\nEsta en marcha: ", self.enMarcha,
            "\nEsta acelerando: ", self.acelera,
            "\nEsta frenando: ", self.frena
        )


class Furgoneta(Vehiculo):

    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.cargado = False

    def carga(self):
        if self.cargado:
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta no esta cargada"


class Moto(Vehiculo):
    haciendo_caballito = ""

    def caballito(self):
        self.haciendo_caballito = "Voy haciendo el caballito"

    def estado(self):
        print(
            "Marca: ", self.marca,
            "\nModelo: ", self.modelo,
            "\nEsta en marcha: ", self.enMarcha,
            "\nEsta acelerando: ", self.acelera,
            "\nEsta frenando: ", self.frena, "\n",
            self.haciendo_caballito
        )


class VehiculoElectrico(Vehiculo):

    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.autonomia = 100
        self.cargando = False

    def cargar_energia(self):
        self.cargando = True


class BicicletaElectrica(VehiculoElectrico):
    pass

