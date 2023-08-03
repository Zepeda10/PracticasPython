name = "COMPUTADORA"
description = """"
Una camputadora
Es una herramienta de gran ayuda para
todos los desarrolladores de software.
Equis de.
"""
print(name, description)

length_d = len(description)
length_n = len(name)
print(length_d)
print(length_n)

print(name[4])
print(description[26:30])
print(description[51:])
print(description[:50])
print(description[:])

# concatenando strings
nombre = "hilda"
apellido = "zepeda"
nombre_completo_forma1 = nombre + " " + apellido
print(nombre_completo_forma1)

nombre_completo_forma2 = f"{nombre} {apellido}"
print(nombre_completo_forma2)

nombre_completo_forma3 = f"{nombre[0]} {5 + 9}"
print(nombre_completo_forma3)
