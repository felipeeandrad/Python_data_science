#Será estudado    estranhos ou seja, nem todos os dados ausentes, porem não atendem as informações das colunas

import pandas as pd
import io

df = pd.read_csv('dados_ausentes_03.csv')
print(df)

#Definindo as strings que devem ser tratadas como naN
valores_ausentes_personalizados = ["","N/A","?","-"]

df_corrigido = pd.read_csv("dados_ausentes_03.csv",na_values=valores_ausentes_personalizados)
print('='*50)
print("Base Corrigida")
print(df_corrigido)

df_corrigido_02 = df_corrigido.fillna({
  'Idade' : 0,
  'Cidade' : 'Desconhecida',
  'Renda' : 0,
  'Comentarios' : 'Sem Comentários'
})
print('='*50)
print("Base corrijida para analise")
print(df_corrigido_02)

