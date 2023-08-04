def es_palindromo(texto):
    texto = str(texto)

    # print(texto.lower()[::-1]) # invierte el texto

    if texto.lower() == texto.lower()[::-1]:
        return True
    else:
        return False


def no_space(texto):
    nuevo_texto = ""
    for char in texto:
        if char != " ":
            nuevo_texto += char
    return nuevo_texto


def reverse(texto):
    texto_reves = ""
    for char in texto:
        texto_reves = char + texto_reves
    return texto_reves


def es_palindromo2(texto):
    texto = no_space(texto)
    al_reves = reverse(texto)

    return texto.lower() == al_reves.lower()


#print(es_palindromo("hola mundo"))
# print(es_palindromo("Abba"))
print(es_palindromo2("hola mundo"))
print(es_palindromo2("Amo la paloma"))
