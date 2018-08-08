def eliminarH(palabra):
  for letra in palabra:
    if letra == "h":
      continue
    print(letra)

def contarSoloLetras(palabra):
  contador = 0
  for caracter in palabra:
    if caracter == " ":
      continue
    contador+=1
  print(f("{palabra} tiene {contador} letras"))

def tieneArroba(email):
  for letra in email:
    if letra == "@":
      arroba = true
      break
  else:
    arroba = False
  print(arroba)
