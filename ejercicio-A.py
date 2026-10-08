def contar_letra(vector, letra):
    cantidad = 0

    for caracter in vector:
        if caracter == letra:
            cantidad += 1

    return cantidad


caracteres = ["a", "b", "a", "c", "a", "d"]
resultado = contar_letra(caracteres, "a")

print("Cantidad de apariciones:", resultado)