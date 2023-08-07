numeros = [1, 2, 3]
# print(numeros[0])
# print(numeros[1])
# print(numeros[2])

n1, n2, n3 = numeros  # Otra forma de acceder a c/número
print(n1, n2, n3)

num1, *otros = numeros  # se obtiene el primer número y los demás en un iterable
print(num1)
print(otros)

primero, *otros2, ultimo = numeros
