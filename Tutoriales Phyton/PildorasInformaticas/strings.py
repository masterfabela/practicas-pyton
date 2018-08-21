nombre_usuario = input("Introduce tu nombre de usuario")
nombre_usuario_mayus = nombre_usuario.upper()
nombre_usuario_minus = nombre_usuario.lower()
nombre_usuario_primera_mayus = nombre_usuario.capitalize()
print("El nombre es: ", nombre_usuario)

edad = input("Introduce la edad")
while not edad.isdigit():
    print("No se ha introducido un numero")
    edad = input("Vuelve a introducir la edad")

if int(edad) < 18:
    print("No puede pasar")
else:
    print("Puede pasar")
