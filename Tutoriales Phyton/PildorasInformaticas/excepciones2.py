import math

def evaluaEdad(edad):
  if edad < 0:
    raise TypeError(
      "No se permiten edades negativas"
    )
  if edad < 20:
    return "Eres muy joven"
  elif edad < 40:
    return "Eres joven"
  elif edad < 65:
    return "Eres Maduro"
  elif edad <100:
    return "Cuidate..."

def calcularRaizCuadrada(numero):
  if numero < 0:
    raise ValueError("El numero no puede ser negativo")
  else:
    return math.sqrt(numero)

try:
  print(
    calcularRaizCuadrada(
      int(input("Introduce un numero: "))
    )
  )
except ValueError as ErrorDeNumeroNegativo:
  print(ErrorDeNumeroNegativo)

print("Programa terminado")