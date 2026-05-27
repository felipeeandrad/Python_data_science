#Nesse Programa vamos usar a biblioteca pandas para analisar uma serie de dados

import pandas as pd

#Criando uma serie a partir de listas

faturamento = [1200, 1500, 900,2000, 1800]
dias = ["segunda", "terça", "quarta", "quinta", "sexta"]

serie_vendas = pd.Series(faturamento, index=dias)

print("série vendas")
print(serie_vendas)

#Operações matemáticas

print(f"faturamento total: R$ {serie_vendas.sum()}")
print(f"Média de vendas: R$ {serie_vendas.mean():.2f}")

#filtrando valores

dias_bons = serie_vendas[serie_vendas > 1400]
print(f"Dias com faturamento acima de R$: 1400:")
print (dias_bons)

#Acessando um valor pelo indice 
print (f"Vendas da quarta-feira: RS: {serie_vendas["quarta"]}")
