# La tutpla es lo mismo que la lista, con la diferencia de que esta no puede ser modificada
# no puedes agregar, eliminar, modificar elementos

numeros = (1, 2, 3) + (4, 5, 6)
print(numeros)

numerosLista = [1, 2, 3, 4]
numerosTupla = tuple(numerosLista)
otraListaNumeros = list(numeros)  # convirtiendo tupla a lista

print(otraListaNumeros)
