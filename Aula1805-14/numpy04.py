#Será estudado algumas operações vetorizadas e estastisticas com matrizes no numpy

import numpy as np

vendas = np.array([
    [2000, 2500, 3000, 3400],
    [1500, 1200, 1800, 2000],
    [3600, 4500, 4200, 3900]
])

icms = 0.18
vendas_com_imposto = vendas * (1+icms)
print("Matriz de vendas com imposto (18%)")
print (vendas_com_imposto)

#Funções estatisticas com AXIS
#axis=0 - Analisa as colunas
#axis=1 - Analisa as linhas

print(f"Média de vendas por produto: {vendas.mean(axis=1)}")
print(f"Média de vendas por mes: {vendas.mean(axis=0)}")

soma_vendas = vendas.sum(axis=0)
print(f"Total de janeiro: {soma_vendas[0]}")
print(f"Maior venda registrada: {vendas.max()}")
