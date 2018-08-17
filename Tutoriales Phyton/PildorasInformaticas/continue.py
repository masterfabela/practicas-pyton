def eliminar_h(palabra):
    for letra in palabra:
        if letra == "h":
            continue
        print(letra)


def contar_solo_letras(palabra):
    contador = 0
    for caracter in palabra:
        if caracter == " ":
            continue
        contador += 1
    print(f'{palabra} tiene {contador} letras')


def tiene_arroba(email):
    for letra in email:
        if letra == "@":
            arroba = True
            break
    else:
        arroba = False
    print(arroba)
