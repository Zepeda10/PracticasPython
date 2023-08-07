# set: colección de datos que no se puede repetir y tampoco está ordenada

numeros = {1, 1, 2, 2, 3, 3, 3}
print(numeros)

numeros.add(6)
numeros.remove(2)
print(numeros)

lista = [3, 4, 5, 6, 7]
setDeLista = set(lista)
print(setDeLista)

print(numeros | setDeLista)  # las une con el operador de unión
print(numeros & setDeLista)  # intersección
print(numeros - setDeLista)  # diferencia
print(setDeLista - numeros)  # diferencia
print(numeros ^ setDeLista)  # diferencia simétrica
