def saludo(nombre, apellido="default"):
    print("Curso Python")
    print(f"Hola {nombre} {apellido}")


saludo("hilda", "zepeda")
saludo("rocio")

saludo(apellido="prieto", nombre="rocio")  # argumentos nombrados


def suma(n1, n2):
    return n1 + n2


n = suma(3, 2)
print(n)
