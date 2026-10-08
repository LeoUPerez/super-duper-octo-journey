def sustituir_repetidos(vector):
    encontrados = []
    modificados = 0

    for i in range(len(vector)):
        numero = vector[i]

        if numero in encontrados:
            vector[i] = -5
            modificados += 1
        else:
            encontrados.append(numero)

    return vector, modificados


numeros = [4, 2, 4, 7, 2, 4, 9]
vector_modificado, cantidad = sustituir_repetidos(numeros)

print("Vector modificado:", vector_modificado)