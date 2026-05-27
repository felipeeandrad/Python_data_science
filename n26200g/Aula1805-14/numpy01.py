#Nesse programa será apresentado a introdução da biblioteca numpy

import numpy as np

dados_1d = np.array([13, 29, 33, 38, 69, 74])
print (dados_1d)

dados_2d = np.array( 
   [ [1, 3, 5], 
    [2, 4, 6],
    [5, 10, 15] ]
)
print (dados_2d)


#cria uma lista com cinco zeros (0,0,0,0,0)
dados_zeros = np.zeros(5)
print (dados_zeros)

#Cria uma tabela com 2 linhas e 6 colunas 
dados_uns = np.ones((2,6))
print (dados_uns)

dados_sequencia = np.arange(2,20,2)
print (dados_sequencia)

dados_espacados = np.linspace (0,1,5)
print(dados_espacados)



