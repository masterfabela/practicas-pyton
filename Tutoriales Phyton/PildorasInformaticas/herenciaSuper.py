class Persona:
    def __init__(self, nombre, edad, lugar_residencia):
        self.nombre = nombre
        self.edad = edad
        self.lugar_residencia = lugar_residencia

    def descripcion(self):
        print("Nombre: ", self.nombre, " Edad: ", self.edad, " Residencia: ",
              self.lugar_residencia)


class Empleado(Persona):

    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado,
                 residencia):
        super().__init__(nombre_empleado, edad_empleado, residencia)
        self.salario = salario
        self.antiguedad = antiguedad

    def descripcion(self):
        super().descripcion()
        print("Salario: ", self.salario, "Antiguedad: ", self.antiguedad,
              " anos")


antonio = Persona("Manuel", 55, "Colombia")
antonio.descripcion()
print(isinstance(antonio, Empleado))
print(isinstance(antonio, Persona))
