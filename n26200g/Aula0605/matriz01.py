#será estudado as listas bidimensional (matriz)

matriz_numeros = [
    [13, 25, 29, 32], 
    [28, 5, 18, 24],
    [131, 152, 505, 439]
]
print(matriz_numeros)
print (f"Linha 1 coluna 3 : {matriz_numeros[0][2]}")
print (f"linha 2 inteira: {matriz_numeros[1]}") #somente linhas inteiras

#média de cada linha 
media_1 = sum(matriz_numeros[0]) / len(matriz_numeros[0])
media_2 = sum(matriz_numeros[1]) / len(matriz_numeros[1])
media_3 = sum(matriz_numeros[2]) / len(matriz_numeros[2])
print(f"Média da linha 1: {media_1}")
print(f"Média da linha 2: {media_2}")
print(f"Média da linha 3: {media_3}")
