def generaPares(limite):
  num = 1
  miLista=[]
  while num < limite:
    miLista.append(num*2)
    num+=1
  return miLista

print(generaPares(10))


def generadorPares(limite):
  num = 1
  while num < limite:
    yield num*2
    num+=1

def pedirTodosLosPares():
  for numeroPar in generadorPares(10):
    print(numeroPar)

print(next(generadorPares(10)))

print(next(generadorPares(10)))

