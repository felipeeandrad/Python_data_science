#Será estudado a biblioteca pandas usando um dataframe simples

import pandas as pd 

dados = {
    'Produto' : ['Notebook', 'Mouse', 'Teclado', 'Monitor'],
    'Preço' : [3500, 80.50, 150.00, 950.00],
    'Em estoque': [True, True, False, True]
}

df_vendas = pd.DataFrame(dados)

print("Dicionário Python")
print(dados)

print("DataFrame Pandas")
print(df_vendas)