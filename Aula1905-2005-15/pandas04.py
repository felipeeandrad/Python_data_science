#será criado uma base ficticia e depois exportar para .csv, .xlsx e .json

import pandas as pd
import numpy as np

#criando a base de dados

np.random.seed(42)
nomes = ['Gaspar', 'Jorge', 'anabela', 'Luiza','Bruce']
cidades = ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba', 'Salvador']
dados = {
    'Nome': np.random.choice(nomes, 50),
    'Idade': np.random.randint (18, 60, 50),
    'Salario': np.random.uniform(1500, 8000, 50).round(2),
    'Cidade': np.random.choice(cidades,50),
    'Data_Compra': pd.date_range(start='2015-01-01', periods = 50, freq='D')
}

df = pd.DataFrame(dados)
print(df)

#Criando arquivo CSV
df.to_csv('base_vendas.csv', index=False, sep=';', encoding='utf-8')

#Criando arquivo xlxs (excel)
#instalar a biblioteca openpyxl
df.to_excel('base_vendas.xlsx', index=False)

#Criando arquivo Json 
df.to_json('base_vendas.json', orient='records', force_ascii=False, date_format='iso')