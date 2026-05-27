contador = 0
numero = 0 
lista =  []

numero = int(input("Digite um número: "))

while contador < 10:
    numero = int(input("Digite um número: "))
    lista.append(numero)
    contador += 1 

print (f"O total da lista é: {sum(lista)}")
