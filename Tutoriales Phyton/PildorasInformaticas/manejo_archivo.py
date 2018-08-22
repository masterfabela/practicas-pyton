from io import open


def get_archivo_escritura():
    return open("archivo.txt", "w")


def get_archivo_lectura():
    return open("archivo.txt", "r")


def obtener_texto_archivo(archivo):
    return archivo.read()


def escribir_en_archivo(archivo, texto):
    archivo.write(texto)


def cerrar_archivo(archivo):
    archivo.close()


def obtener_lineas_archivo(archivo):
    return archivo.readlines()


archivo_app = get_archivo_escritura()
frase = "Estupendo dia para estudia python \n el miercoles"
escribir_en_archivo(archivo_app, frase)
cerrar_archivo(archivo_app)
archivo_app = get_archivo_lectura()
obtener_texto_archivo()

