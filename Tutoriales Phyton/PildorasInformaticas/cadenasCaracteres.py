nombreUsuario = input("Introduce un nombre de usuario: ")

print("El nombre es: ", nombreUsuario.capitalize())

edad = input("Introduce la edad: ")
while not edad.isdigit():
    edad = input("Vuelve a introducir la edad: ")
else:
    if int(edad) < 18:
        print("No puede pasar")
    else:
        print("Puede pasar")
