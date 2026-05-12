#será estudado o comando while para receber notas de um professor e calcular a média.Nesse caso o professor poderá imprir quantas notas quiser


notas_inseridas = 0 
soma_notas = 0
 
while True:
    nota = float(input("Digite a nota do aluno: "))
    soma_notas += nota
    notas_inseridas += 1
    resposta = input("Deseja inserir outra nota? (s/n): ")
    if resposta.lower() == 'n':
        break

media = soma_notas / notas_inseridas
print(f"A média do aluno é: {media:.2f}")  