from io import open


def get_archivo_escritura():
    return open("archivo.txt", "w")


def get_archivo_lectura():
    return open("archivo.txt", "r")


def get_archivo_agregar():
    return open("archivo.txt", "a")


def obtener_texto_archivo(archivo):
    return archivo.read()


def escribir_en_archivo(archivo, texto):
    archivo.write(texto)


def cerrar_archivo(archivo):
    archivo.close()


def obtener_lineas_archivo(archivo):
    return archivo.readlines()


archivo_app = get_archivo_escritura()
frase = "Estupendo dia para estudiar python \n el miercoles"
escribir_en_archivo(archivo_app, frase)
cerrar_archivo(archivo_app)
archivo_app = get_archivo_lectura()
print(obtener_lineas_archivo(archivo_app)[0])
cerrar_archivo(archivo_app)
archivo_app = get_archivo_agregar()
escribir_en_archivo(archivo_app, " siempre es una buena ocasion para estudia "
                                 "python")
archivo_app.close()
archivo_app = get_archivo_lectura()
print(obtener_texto_archivo(archivo_app))
archivo_app.close()

