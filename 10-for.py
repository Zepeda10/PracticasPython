buscar = 13

for numero in range(5):
    print(numero, numero * "hola ")
    if numero == buscar:
        print("encontrado")
        break
    else:
        print("no encontrado")


print("\n\n")

# for else
for numero in range(5):
    print(numero, numero * "hola ")
    if numero == buscar:
        print("encontrado")
        break
else:
    print("no encontrado")


print("\n\n")

for char in "hola mundo":
    print(char, " - ")
