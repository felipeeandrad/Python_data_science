#Será estudado a estrutura de repetição while para receber 4 notas e calcular a média.abs

contador = 1
soma_notas = 0

while contador <= 4:
    nota = float(input(f"Digite a {contador}ª nota: "))
    soma_notas = soma_notas + nota
    contador += 1
media = soma_notas / (contador - 1)

if media >= 7:
  conceito = "Aprovado"

else:
  conceito = "Reprovado"

print(f"O aluno está: {conceito} com a média: {media}")