salir = ""

while salir.lower() != "salir":
    salir = input(">> ")

    if salir == "salir":
        break

    n1 = input("Ingrese n1: ")
    op = input("ingrese operación: ")
    n2 = input("ingrese n2: ")

    n1 = int(n1)
    n2 = int(n2)
    r = 0

    if op.lower() == "suma":
        r = n1 + n2
    elif op.lower() == "resta":
        r = n1 - n2
    else:
        print("solo \"suma\" o \"resta\" ")

    print(f"Resultado: {r}")
