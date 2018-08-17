def genera_pares(limite):
    num = 1
    mi_lista = []
    while num < limite:
        mi_lista.append(num * 2)
        num += 1
    return mi_lista


print(genera_pares(10))


def generador_pares(limite):
    num = 1
    while num < limite:
        yield num * 2
        num += 1


def pedir_todos_los_pares():
    for numeroPar in generador_pares(10):
        print(numeroPar)


print(next(generador_pares(10)))

print(next(generador_pares(10)))
