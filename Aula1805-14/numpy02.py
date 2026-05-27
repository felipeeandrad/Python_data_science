#Será estudado 

import numpy as np

dados_01 = np.array([10, 20, 30, 40, 50])

dados_02 = np.array([
    [10, 11, 12],
    [20, 21, 22],
    [30, 31, 32]
])

print(f"primeiro elemento de dados 1: {dados_01[0]}")
print(f"elemento na linha, 1 coluna 2 de dados 2: {dados_02[1,2]}")
print(f"coluna 2 inteira de dados 2: {dados_02[:,2]}")
print(f"Linha 1 inteira de dados 2: {dados_02[1]}")

submatriz = dados_02[0:2, 1:3]
print(f"Submatriz 2x2:\n {submatriz}")

print(f"dados 1 {dados_01}")
dados_01[0] = 15
print(f"dados 1 alterada: {dados_01}")

submatriz[1,1] = 44
print(f"submatriz alterada:\n {submatriz}")