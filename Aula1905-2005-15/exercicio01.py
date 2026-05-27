#Crie um DataFrame com o pandas
#imprima o DataFrama completo 
#imprima as 5 ultimas linhas
#imprima as 5 primeiras linhas
#imprima as informações do dataframe
#imprima a descriação estatisticas
#imprima os dados da coluna estado
#Crie a coluna "Total da devolução" multiplicando "quantidade devolvida" * "Preço unitario"
#imprima um total por estado
#imprima as devoluções de janeira de 2018.

import pandas as pd
import io
def traco():
    print("="*50)

df_devolucoes = pd.read_csv("Devolucoes2018.csv", sep=";",decimal =",", parse_dates = ['Data'] )

print("DataFrame completo")
print(df_devolucoes)
traco()

print ("Primeiras 5 linhas")
print(df_devolucoes.head())
print()
traco()

print ("Ultimas 5 linhas")
print(df_devolucoes.tail())
print()
traco()

print("Informações do DataFrame")
print(df_devolucoes.info())
print()
traco()

print("Estatistica descritiva")
print(df_devolucoes.describe())
print()
traco()

print("Coluna Estado")
print(df_devolucoes['Estado'])
print()
traco()

df_devolucoes["TotalDevolução"] = df_devolucoes["Quantidade Devolvida"] * df_devolucoes["Preço Unitário"]
print("DataFrame alterado")
print(df_devolucoes)
print()
traco()

print("Total por estado")
total_estado = df_devolucoes.groupby('Estado')['TotalDevolução'].sum()
print(total_estado)
print()

print("Devoluções Janeiro 2018")
dev_jan_2018 = df_devolucoes[(df_devolucoes['Data']>='01-01-2018') & (df_devolucoes['Data'] <= '-01-31-2018')]
print (dev_jan_2018)
print()
traco()