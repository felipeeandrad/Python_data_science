#vamos estudar o tratamento de exceções usando try except

print("calculador de dois numeros")
print ("="*40)

while True:
    try:
        numero = int(input("Digite um número: "))
        numero2 = int(input("Digie outro número: "))
        soma = numero + numero2
        print(f"A soma de {numero} + {numero2} é {soma}")
        break
    except ValueError: 
        print("ERRO: A entrada não pode ser convertida para inteiro.")
        print ("Tente novamente digitando apenas números.")
        

print ("="*40)