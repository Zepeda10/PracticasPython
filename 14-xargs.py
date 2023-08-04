def suma(*numeros):  # xargs
    r = 0
    for numero in numeros:
        r += numero
    print(f"resultado: {r}")


suma(1, 2)
suma(5, 98, 5, 3, 6)
suma(8, 6, 8)
