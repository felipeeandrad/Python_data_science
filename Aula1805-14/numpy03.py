# Nesse programa vamos fazer alguma operações vetorizadas
# e estatísticas
import numpy as np

vendas = np.array([100, 210, 150, 300])
icms = 0.18

# Operação vetorizada (multiplica todos os elementos)
vendas_com_imposto = vendas * (1 + icms)

print(f"Vendas sem imposto: {vendas}")
print(f"Vendas com imposto: {vendas_com_imposto}")

print (f"Total das vendas sem imposto: R$ {vendas.sum()}")
print (f"Média das vendas sem imposto: R$ {vendas.mean()}")
print (f"Desvio padrão das vendas sem imposto: R$ {vendas.std():.2f}")
