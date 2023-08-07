mascotas = [
    "Kiara",
    "Dama",
    "Loki",
    "Nami"
]

mascotas.insert(1, "Michi")
mascotas.append("Rambo")
print(mascotas)

mascotas.remove("Dama")
print(mascotas)

mascotas.pop()  # elimina último elemento
print(mascotas)

mascotas.pop(1)  # elimina elemento dado
print(mascotas)

del mascotas[0]  # elimina el elemento dado
print(mascotas)

mascotas.clear()
print(mascotas)
