def suma(num1, num2):
    return num1 + num2


def resta(num1, num2):
    return num1 - num2


def multiplica(num1, num2):
    return num1 * num2


def divide(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("No puedes dividir entre 0")
        return "Operacion erronea"


def introducir_valores():
    entrada_vacia = dict()
    entrada_vacia['numero1'] = int(input("Introduce el primer número: "))
    entrada_vacia['numero2'] = int(input("Introduce en segundo número: "))
    entrada_vacia['operacion'] = input("Introduce la operación \n suma \n resta \n multiplica \n divide \n\n> ")
    return entrada_vacia


def realiza_operacion(num1, num2, operacion):
    if operacion == 'suma':
        suma(num1, num2)
    elif operacion == 'resta':
        resta(num1, num2)
    elif operacion == 'multiplica':
        multiplica(num1, num2)
    elif operacion == 'divide':
        divide(num1, num2)
    else:
        print("No hai definido un metodo para esa operacion")


try:
    entrada = introducir_valores()
    realiza_operacion(
        entrada['numero1'],
        entrada['numero2'],
        entrada['operacion']
    )
except ValueError:
    print("El tipo de valor introducido no es adecuado")

print(
    "Operacion ejecutada. Continuacion de ejecucion del programa"
)
