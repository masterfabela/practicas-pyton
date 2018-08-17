# Ejercicio 1
# Devuleve el mayor numero de 2 introducidos

# ------------- EXERCICIO 1 ----------


def devuelve_max(num1, num2):
    if num2 > num1:
        return num2
    else:
        return num1


def ejercicio1():
    devuelve_max(
        int(input("Inserta numero 1")),
        int(input("Inserta numero 1"))
    )


# ---------- EXERCICIO 2 -----------


def guardar_en_lista_mostrar(nombre, direccion, telefono):
    lista_contacto = [nombre, direccion, telefono]
    print("Los datos personales son: " +
          lista_contacto[0] + " " + lista_contacto[2])


def ejercicio2():
    guardar_en_lista_mostrar(
        input("Inserta tu Nombre: "),
        input("Inserta direccion: "),
        input("Numero de telefono: ")
    )


# -------- EXERCICIO 3 -----------


def calcular_media_mostrar(num1, num2, num3):
    media = (num1 + num2 + num3) / 3
    print("La media aritmetica es: " + str(media))


def ejercicio3():
    calcular_media_mostrar(
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


def comprobar_contrasinal(contrasinal):
    lonxitude_valida = False
    conten_espacio = False
    if len(contrasinal) > 7:
        lonxitude_valida = True
        for indice in range(len(contrasinal)):
            if contrasinal[indice] == " ":
                conten_espacio = True
    if lonxitude_valida and not conten_espacio:
        print("Contrasinal OK")
    else:
        print("Contrasinal erronea")


def ejercicio5():
    comprobar_contrasinal(input("Introduza unha contrasinal valida: "))


# ------------ EXERCICIO 6 --------------
# Crea un programa que evalue si unha direccion de correo electronica e valida
# ou non en funcion de se posue @ ou . Hay que ter en conta que a direccion
# considerase correcta si solo ten un @ e se ten un ou mais .
def comprobar_email(email):
    conten_punto = False
    numero_arrobas = 0
    for caracter in email:
        if caracter == ".":
            conten_punto = True
        if caracter == "@":
            numero_arrobas = +1
    if conten_punto and 0 < numero_arrobas < 2:
        print("O email e valido")
    else:
        print("O email non e valido")


def ejercicio6():
    comprobar_email(input("Introduzca o seu email: "))


# ---------------- EXERCICIO 7 ----------------------
# Crea un programa que pida numeros indefinidamente. Os numeros introducidos
# deben ser cada vez maiores, o programa finalizara no caso contrario


def exercicio7():
    numero = input("Inserta un numero: ")
    numero_mayor = input("Inserta un numero mayor: ")
    while numero_mayor > numero:
        print("O numero introducido e maior")
        numero = numero_mayor
        numero_mayor = input("Inserte un numero maior: ")
    else:
        print("O numero non e maior o programa finalizara")


# ------------ EXERCICIO 8 -----------
# Crea un programa que pida numeros positivos indefinidamente. O programa
# termina cando se introduce un numero negativo, finalmente o programa mostra a
# suma de todos os numero introducidos

def exercicio8():
    numero_positivo = True
    numero_sumado = 0
    while numero_positivo:
        numero = int(input("Inserta un numero positivo para sumar, negativo para terminar: "))
        if numero >= 0:
            numero_sumado = numero_sumado + numero
        else:
            print('La suma de todos los numeros es: ' + str(numero_sumado))
            numero_positivo = False


# ------------ EXERCICIO 9 -----------
# Crea un programa que pida introducir a dirreceion de mail por teclado
# o programa debe decirnos se e correcta en base a se ten @, que non teña mais
# de unha a direcion tamen sera erronea de este caracter esta ao princio ou final

def exercicio9():
    if es_email_valido(input("Introduzca o seu email: ")):
        print("El email es valido")
    else:
        print("El email es incorrecto")


def es_email_valido(email):
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
