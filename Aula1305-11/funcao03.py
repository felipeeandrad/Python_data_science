#Nesse programa será estudado funções sem argumento e com retorno

import random

def gerar_num_aleatorio ():
    numero = random.randint(1,100)
    return numero

print ("gerador de numero secreto")

resposta = "S"
while resposta.upper() == "S":
    numero_aleatorio = gerar_num_aleatorio()
    print (numero_aleatorio)
    resposta = input ("Deseja gerar outro número S/N? ")
   
print (f"Gerando mais um número: {gerar_num_aleatorio()}")