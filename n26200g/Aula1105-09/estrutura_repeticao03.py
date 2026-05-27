#sera usado o comando while para criar uma tabela de tabuada

print("Gerador de tabuada")
print("==="*20)

numero = int(input("Digite um número para gerar a tabuada: "))

print("==="*20)
print(f"Tabuada do {numero}:")
contador = 1
while contador <= 10:
    resultado = numero * contador
    print(f"{numero} x {contador} = {resultado}")
    contador = contador + 1

print("==="*20)
print("Tabuada gerada com sucesso!")