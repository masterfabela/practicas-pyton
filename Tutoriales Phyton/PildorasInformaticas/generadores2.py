def devuelve_ciudades(*ciudades):
  for ciudad in ciudades:
    #for letra in ciudad:
    yield from ciudad

ciudades_devueltas= devuelve_ciudades(
  "Madrid",
  "Barcelona",
  "Bilbao",
  "Valencia"
)

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))