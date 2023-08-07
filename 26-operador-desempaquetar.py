def f1(n1, n2, n3, n4, n5):
    print(n1)


lista = [1, 2, 3, 4, 5]
print(*lista)  # Es como pasarle directamente los valores 1 2 3 4 5  al print

f1(*lista)  # ejemplo de uso

lista2 = [6, 7, 8]
combinada = ["hola", *lista, "mundo", *lista2]
print(combinada)

# en diccionarios solamente hay que usar dos * en lugar de uno
punto1 = {"x": 14}
punto2 = {"y": 18}
nuevoPunto = {**punto1, "w": 55.4, **punto2, "z": "hola"}
print(nuevoPunto)
