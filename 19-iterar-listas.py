mascotas = ["Kiara", "Dama", "Loki", "Nami"]

for m in mascotas:
    print(m)

for m in enumerate(mascotas):
    print(m)  # tupla
    print(m[0])
    print(m[1])


for indice, mascota in enumerate(mascotas):
    print(indice, mascota)
