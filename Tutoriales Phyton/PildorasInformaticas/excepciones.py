def suma(num1, num2):
  return num1 + num2

def resta(num1, num2):
  return num1-num2

def multiplica(num1, num2):
  return num1 * num2

def divide(num1, num2):
  try:
    return num1/num2
  except ZeroDivisionError:
    print("No puedes dividir entre 0")
    return("Operacion erronea")

def introducirValores():
  entrada = dict()
  entrada['numero1'] = int(input("Introduce el primer numero: ")) 
  entrada['numero2'] = int(input("Introduce en segundo numero: "))
  entrada['operacion'] = input("Introduce la operacion \n suma \n resta \n multiplica \n divide \n\n> ")
  return entrada

def realizaOperacion(num1, num2, operacion):
  if operacion == 'suma':
    suma(num1, num2)
  elif operacion == 'resta':
    resta(num1, num2)
  elif operacion == 'multiplica':
    multiplica(num1, num2)
  elif operacion == 'divide':
    divide(num1, num2)
  else:
    print("No hai definido un metodo para esa operacion");

try:
  entrada = introducirValores()
  realizaOperacion(
    entrada['numero1'],
    entrada['numero2'],
    entrada['operacion']
  )
except ValueError:
  print ("El tipo de valor introducido no es adecuado")

print(
  "Operacion ejecutada. Continuacion de ejecucion del programa"
) 

