#será estudado alguns comandos par alterar o calor de uma lista (vetor)

frutas = ["banana", "Pera", "maçã","Uva"] #precisa ser colchetes para ser um vetor (lista)
print (frutas)

frutas[2] = "Melão" # altera o valor do 3 elemento da lista 
print(frutas)

#adicionando um elemento ao final da lista

frutas.append("Melancia")
print(frutas)

#adicionando um elemento em uma posição especifica

frutas.insert(1,"abacaxi") # numero representa onde sera inserido a fruta na lista
print (frutas)

#removendo o ultimo elemento da lista (deixa sem numero no pop)
frutas.pop(0) #número representa o elemento que vai ser removido
print(frutas)

#remove um elemento pelo nome
frutas.remove("Melão")
print(frutas)