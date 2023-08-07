mascotas = ["Kiara", "Dama", "Loki", "Nami", "Dama"]

print(mascotas.index("Dama"))
# print(mascotas.index("otra")) # devuelve un error

if "otra" in mascotas:
    print(mascotas.index("otra"))
else:
    print("no está")

print(mascotas.count("Dama"))
