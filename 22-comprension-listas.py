usuarios = [
    ["hilda", 5],
    ["roberto", 12],
    ["grecia", 1],
    ["zalberto", 6]
]

# nombres = []

# for usuario in usuarios:
#     nombres.append(usuario[0])

# print(nombres)

# obteniendo solo los nombres por medio de esta transformación (map)
nombres = [usuario[0] for usuario in usuarios]
print(nombres)

# filtrar si el id del usuario es mayor a 2 (filter)
nombres2 = [usuario for usuario in usuarios if usuario[1] > 2]
print(nombres2)

# filtrar y transformar
nombres3 = [usuario[0] for usuario in usuarios if usuario[1] > 2]
print(nombres3)

# transformar con la función map
nombres4 = list(map(lambda usuario: usuario[0], usuarios))
print(nombres4)

# filtrar con la función filter
nombres5 = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(nombres5)
