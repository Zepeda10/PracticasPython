numeros = [34, 7, 6, 8, 9]

# numeros.sort()
sorted(numeros)  # La dif entre sorted y .sort es que sorted devuelve una nueva lista
print(numeros)

numeros.sort(reverse=True)
print(numeros)

usuarios = [
    [5, "hilda"],
    [12, "roberto"],
    [13, "grecia"],
    [6, "alberto"]
]

usuarios.sort()  # ordena solo si el primer elemento es ordenable
print(usuarios)

usuarios2 = [
    ["hilda", 5],
    ["roberto", 12],
    ["grecia", 13],
    ["zalberto", 6]
]


def ordenar(elemento):
    return elemento[1]


# ordena solo si el primer elemento es ordenable
# sort se encarga de pasarle el argumento a la funcióm
# usuarios2.sort(key=ordenar, reverse=True)
usuarios2.sort(key=lambda parametros: parametros[1], reverse=True)
print(usuarios2)
