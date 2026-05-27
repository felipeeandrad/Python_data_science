#Será estudado a biblioteca pandas usando dataframe com arquivo csv

import pandas as pd
import io
def traco():
    print("="*50)

df_vendas = pd.read_csv('vendas.csv', sep=";", decimal = ',', parse_dates = ['DataVenda'])

print ("DataFrame Original")
print(df_vendas)
print()
traco()
# Vizualizando as 5 primeiras linhas
print ("Primeiras 5 linhas")
print(df_vendas.head())
print()
traco()
# Vizualizando as 5 ultimas linhas
print ("Ultimas 5 linhas")
print(df_vendas.tail())
print()
traco()
# Visualizando informações do dataFrame
print("Informações do DataFrame")
print(df_vendas.info())
print()
traco()
#Vizualizando a descrição estatisca dos dados
print("Estatistica descritiva")
print(df_vendas.describe())
print()
traco()
#Visualizando uma coluna especifica
print("Coluna produto")
print(df_vendas['Produto'])
print()
traco()

#Filtrando dados: vendas de produtos da categoria "eletronicos"
print("vendas de Celular")
celular = df_vendas [df_vendas['Categoria']== 'Celular']
print(celular)
print()
traco()

#Visualizando a descrição estatística dos celular
print("Estatística descritiva dos celulares")
print (celular.describe())
print()
traco() 

#Criando uma nova coluna: Valor total
#Valor total = Preço * quantidade
df_vendas["ValorTotal"] = df_vendas["Preco"] * df_vendas["Quantidade"]
print("DataFrame alterado")
print(df_vendas)
print()
traco()

#Agrupando dados: vendas totais por categoria
print("Vendas totais por categoria")
vendas_por_categoria = df_vendas.groupby('Categoria')['ValorTotal'].sum()
print(vendas_por_categoria)
print()
vendas_formatada = vendas_por_categoria.map('R${:,.2f}'.format).str.replace(',','x').str.replace('.',',').str.replace('x','.')
print(vendas_formatada)
traco()

#convertendo a coluna DataVenda para tipo cliente
#print(df_vendas.info())
#df_vendas['DataVenda'] = pd.to_datetime(df_vendas['DataVenda'])
#print(df_vendas.info())
#Convertido na criação do DataFrame no inicio do códido line 8 'parsa_date'

#Filtrando dados pro data: Vendas realizadas em 2016-01-01
print('Vendas em 01-01-2016')
vendas_01_01_16 = df_vendas[df_vendas['DataVenda'] == '2016-01-01']
print(vendas_01_01_16)
print()
traco()
print("Vendas totais por categoria em 01-01-2016")
vendas_categoria_01_01_16 = vendas_01_01_16.groupby('Categoria') ['ValorTotal'].sum()
print (vendas_categoria_01_01_16)
print()
traco()

#Filtrando dados por data: Vendas realizadas em 2016

print("Vendas em 2016")
vendas_2016 = df_vendas[(df_vendas['DataVenda']>='2016-01-01') & (df_vendas['DataVenda'] <= '2016-12-31')]
print (vendas_2016)
print()
traco()