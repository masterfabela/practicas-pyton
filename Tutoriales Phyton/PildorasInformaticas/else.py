print("Verificacion de acceso")


def comprobacion_edad(edad):
    if edad < 18:
        print("No puedes pasar")
    elif edad > 100:
        print("Edad incorrecta")
    else:
        print("Puedes pasar")
    print("El programa ha finalizado")


def comprobar_nota(nota):
    if nota < 5:
        return "Insuficiente"
    elif nota < 6:
        return "Suficiente"
    elif nota < 7:
        return "Bien"
    elif nota < 9:
        return "notable"
    else:
        return "sobresaliente"


print(comprobar_nota(int(input("Inserta nota de alumno: "))))
