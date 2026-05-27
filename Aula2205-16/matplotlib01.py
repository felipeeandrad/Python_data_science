#Nesse programa vamos criar um gráfico simples usando o Matplotlib e o prefixo plt, para gráfico simples

import matplotlib.pyplot as plt 

#Plotar alguns dados no axes  ativo

plt.plot([10,20,30,40], [10,40,20,30])

#Configurando os titulos do gráfico 
plt.title('Gráfico de Vendas')
plt.xlabel('Vendas')
plt.ylabel('Valores em R$')

#Exibir o gráfico 
plt.show()