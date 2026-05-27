#será criado um gráfico de linhas usando a biblioteca matplotlib e prefixo 'ax'
#  esse prefixo é o indicado para gráficos profissionais e com grande volume de dados.abs

import matplotlib.pyplot as plt 

#Dados de exemplo 
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai','Jun']
vendas = [120, 150,180,160,200,230]

#Criar a área do gráfico com a figure(fig) e o Axes (ax)

fig, ax = plt.subplots()

#Plotar os dados usando os metodos de objeto 'ax' 
# marker - marcados de ponto nos valroes do grafico
#linestyle = estilo da linha do grafico
#color - cor da linha do grafico

ax.plot(meses,vendas, marker='v', linestyle = "-", color='#ff7700')

#Definir os titulos do grafico
ax.set_title('Vendas Mensais')
ax.set_xlabel('Meses')
ax.set_ylabel('Quantidade Vendida')
ax.set_facecolor( '#ffffff')

#Adicionar uma grade
ax.grid(True)

#Exibir o gráfico 
plt.show()

