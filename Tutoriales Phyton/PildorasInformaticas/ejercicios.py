# Ejercicio 1
# Devuleve el mayor numero de 2 introducidos

# ------------- EXERCICIO 1 ----------


def devuelveMax(num1, num2):
    if num2 > num1:
        return num2
    else:
        return num1


def ejercicio1():
    devuelveMax(
        int(input("Inserta numero 1")),
        int(input("Inserta numero 1"))
    )

# ---------- EXERCICIO 2 -----------


def guardarEnListaYMostrar(nombre, direccion, telefono):
    listaContacto = [nombre, direccion, telefono]
    print("Los datos personales son: " +
          listaContacto[0] + " " + listaContacto[2])


def ejercicio2():
    guardarEnListaYMostrar(
        input("Inserta tu Nombre: "),
        input("Inserta direccion: "),
        input("Numero de telefono: ")
    )

# -------- EXERCICIO 3 -----------


def calcularMediaYMostrar(num1, num2, num3):
    media = (num1+num2+num3)/3
    print("La media aritmetica es: " + str(media))


def ejercicio3():
    calcularMediaYMostrar(
        float(input("Inserta numero 1: ")),
        float(input("Inserta numero 2: ")),
        float(input("Inserta numero 3: "))
    )

# --------- EXERCICIO 4 ---------
# Mostra os numeros impares do 1 ao 100


def ejercicio4():
    for numero in range(1, 100, 2):
        print(numero)

# --------- EXERCICIO 5 ---------
# Programa que pide ao usuario unha contrasinal, a contraseña non pode ter menos
# de 8 caracteres nin espacios en branco, se a contrasinal e correcta o programa
# imprime "Contraseña ok" en caso contrario imprime, contraseña erronea


def comprobarContrasinal(contrasinal):
    lonxitudeValida = False
    contenEspacio = False
    if len(contrasinal) > 7:
        lonxitudeValida = True
        for indice in range(len(contrasinal)):
            if contrasinal[indice] == " ":
                contenEspacio = True
    if lonxitudeValida and not contenEspacio:
        print("Contrasinal OK")
    else:
        print("Contrasinal erronea")


def ejercicio5():
    comprobarContrasinal(input("Introduza unha contrasinal valida: "))


# ------------ EXERCICIO 6 --------------
# Crea un programa que evalue si unha direccion de correo electronica e valida
# ou non en funcion de se posue @ ou . Hay que ter en conta que a direccion
# considerase correcta si solo ten un @ e se ten un ou mais .
def comprobarEmail(email):
    contenPunto = False
    numeroArrobas = 0
    for caracter in email:
        if caracter == ".":
            contenPunto = True
        if caracter == "@":
            numeroArrobas = +1
    if contenPunto and 0 < numeroArrobas < 2:
        print("O email e valido")
    else:
        print("O email non e valido")


def ejercicio6():
    comprobarEmail(input("Introduzca o seu email: "))

# ---------------- EXERCICIO 7 ----------------------
# Crea un programa que pida numeros indefinidamente. Os numeros introducidos
# deben ser cada vez maiores, o programa finalizara no caso contrario


def exercicio7():
  numero = input("Inserta un numero: ")
  numeroMayor = input("Inserta un numero mayor: ")
  while numeroMayor > numero:
    print("O numero introducido e maior")
    numero = numeroMayor
    numeroMayor = input("Inserte un numero maior: ")
  else:
    print("O numero non e maior o programa finalizara")


#------------ EXERCICIO 8 -----------
# Crea un programa que pida numeros positivos indefinidamente. O programa
# termina cando se introduce un numero negativo, finalmente o programa mostra a
# suma de todos os numero introducidos

def exercicio8():
  numeroPositivo = True
  numeroSumado = 0
  while numeroPositivo:
    numero = int(input("Inserta un numero positivo para sumar, negativo para terminar: "))
    if numero >= 0:
      numeroSumado = numeroSumado + numero
    else:
      print('La suma de todos los numeros es: '+str(numeroSumado))
      numeroPositivo = False

#------------ EXERCICIO 9 -----------
# Crea un programa que pida introducir a dirreceion de mail por teclado
# o programa debe decirnos se e correcta en base a se ten @, que non teña mais
# de unha a direcion tamen sera erronea de este caracter esta ao princio ou final

def exercicio9():
    if esEmailValido(input("Introduzca o seu email: ")):
        print("El email es valido")
    else:
        print("El email es incorrecto")

def esEmailValido(email):
    if email.count('@') == 1:
        if email.endswith('@'):
            return False
        elif email.startswith('@'):
            return False
        else:
            return True
    else:
        return False

exercicio9()
