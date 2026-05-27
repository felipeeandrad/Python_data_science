#será estudado a estrutura for para receber a nota de um aluno e calcular a sua media 

soma_notas = 0 

for i in range (4):
    nota = float(input("Digite a nota do aluno: "))
    soma_notas += nota 

media = soma_notas / 4 

print (f"A média do aluno foi: {media:.1f}")

#quantidade ilimitada de notas 

soma_notas = 0
numero_notas = 0

for i in range (9999):
    nota = float (input("Digite a nota do aluno: "))
    soma_notas += nota
    numero_notas +=1
    reposta = input ("Deseja lançar outra nota s/n? ")
    if reposta.lower() == "n":
        break 

media = soma_notas / numero_notas 
print (f"A média do aluno foi: {media:.1f}")
