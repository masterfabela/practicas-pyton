def primer_ejemplo():
    edad = -7
    if 0 < edad < 100:
        print("La edad es correcta")
    else:
        print("Edad incorrecta")


def ejemplo_salarios_empresa():
    salario_presidente = int(input("Introduce salario del presidente: "))
    print("Salario presidente: " + str(salario_presidente))

    salario_director = int(input("Introduce salario del director: "))
    print("Salario director: " + str(salario_director))

    salario_jefe_area = int(input("Introduce salario del Jefe de area: "))
    print("Salario Jefe de area: " + str(salario_jefe_area))

    salario_administrativo = int(
        input("Introduce salario del administrativo: "))
    print("Salario administrativo: " + str(salario_administrativo))

    if salario_administrativo < salario_jefe_area < salario_director < salario_presidente:
        print("Los salarios son correctos")
    else:
        print("Algo falla en esta empresa")


def asignador_de_becas():
    print("Programa de becas año 2017: ")
    distancia_escuela = int(input("Introduce la distancia en KMs: "))
    numero_hermanos = int(input("Introduce numero de hermanos en el centro: "))
    salario_familiar = float(input("Introduce salario anual bruto: "))
    if tiene_derecho_beca(distancia_escuela, numero_hermanos, salario_familiar):
        print("Tiene derecho a beca")
    else:
        print("No tiene derecho a beca")


def tiene_derecho_beca(distancia_escuela, numero_hermanos, salario_familiar):
    if distancia_escuela > 40 and numero_hermanos > 2 or salario_familiar <= 20000:
        return True
    else:
        return False


def ejemplo_asignaturas():
    lista_asignaturas = (
        "informatica grafica",
        "pruebas de software",
        "usabilidad y accesibilidad"
    )
    print("Asignaturas a escojer: " + str(lista_asignaturas))

    if esta_asignatura(
            input("Que asignatura desea?: "),
            list(lista_asignaturas)
    ):
        print("Asignatura Asignada: ")
    else:
        print("La asignatura no existe en la lista")


def esta_asignatura(asignatura, asignaturas):
    asignatura = asignatura.lower()
    return asignatura in asignaturas


ejemplo_asignaturas()
