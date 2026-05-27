#Nesse programa vamos estudar a estrutura de repetição for, utilizando a a função para imprimir uma tabuada.

print("=" * 40)
print('Gerador de Tabuada')
print("=" * 40)

numero = int(input('Digite um número para ver sua tabuada: '))
print("-" * 40)

for i in range(1, 11):
    print(f'{numero} x {i} = {numero * i}')
print("-" * 40)

print('Tabuada finalizada. Volte sempre!')
