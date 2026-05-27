#Nesse programa sera arrumado uma base com dados faltantes

import pandas as pd
import io

df=pd.read_csv('base_vendas_02.csv', parse_dates = ['Data_Ultima_Compra'])
print (df)

#Eliminar linhas com valores ausentes
df = df.dropna(how='all')

#Eliminar colunas com valores ausentes
df = df.dropna(axis=1, how='all')
print(df)

print('Verificando valores ausentes')
print(df.isna())

print('Informações do Dataframe')
print(df.info())

#Preenchendo com constantes
df_const = df.fillna({
    'Idade' : 0,
    'Renda' : 0.0,
    'Cidade': 'Desconhecida',
    'Data_Ultima_Compra' : 'Sem Data'
})
print(df_const)
print(df_const.info())

#Preenchendo com a média

df_media = df_media['Idade'].fillna(df_media['Idade'].mean())
df_media = df_media['Renda'].fillna(df_media['Renda'].mean())
print (df_media)
