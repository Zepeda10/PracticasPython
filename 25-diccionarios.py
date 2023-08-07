# Diccionarios: conjunto de datos agrupados poer una llave y un valor
punto = {"x": 25, "y": 14}
print(punto)
print(punto["x"])
print(punto["y"])

punto["z"] = 20
print(punto)

if "w" in punto:
    print("sí se encuentra")
else:
    print("no se encuentra")

print(punto.get("y"))
print(punto.get("w", 97))  # valor por defecto si no se encuentra

del punto["x"]
del (punto["y"])
print(punto)

punto["x"] = 25
punto["y"] = 14

for llave in punto:
    print(llave, punto[llave])

for valor in punto.items():
    print(valor)

for llave, valor in punto.items():
    print(llave, valor)

usuarios = [
    {"id": 1, "nombre": "hilda"},
    {"id": 2, "nombre": "andrés"},
    {"id": 3, "nombre": "claudia"}
]

for usuario in usuarios:
    print(usuario["nombre"])
