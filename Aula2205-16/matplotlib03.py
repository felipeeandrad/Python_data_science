#Nesse programa vamos criar um gráfico de dispersão usando o plt

import matplotlib.pyplot as plt

#Dados

horas_estudo = [1,2,3,4,5,6,7]
nota_prova = [5.0, 5.5, 6.0, 7.0, 7.5, 5, 9.0]

#Criando um gráfico de dispersão 
plt.scatter (horas_estudo, nota_prova, color ='#EF4600')
plt.title('Relação entre horas de estudo e nota')
plt.xlabel('Horas de Estudo')
plt.ylabel('Nota na prova')

plt.grid(True)
plt.show()
