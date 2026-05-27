#Nesse programa vamos criar dois gráficos no mesmo figure usando axs

import matplotlib.pyplot as plt

#Criando o figure com 1 linha e 2 colunas
fig, axs = plt.subplots(1,2,figsize=(5,12))

# Definindo o primeiro grafico
axs[0].plot([1,2,3,4], [1,4,2,3], color='green')
axs[0].set_title('Vendas no Semestre')
axs[0].set_xlabel('Vendas')
axs[0].set_ylabel('Em Milhares de R$')

#Definindo o segundo gráfico 
axs[1].bar(['A', 'b', 'C', 'D', 'E'],[5, 9, 15, 7,3], color = 'red')
axs[1].set_title('Relação de notas')
axs[1].set_xlabel('Notas')
axs[1].set_ylabel('Numero de Alunos')

#Ajustar os parâmetros para caber na area da figure

plt.tight_layout()
plt.show()