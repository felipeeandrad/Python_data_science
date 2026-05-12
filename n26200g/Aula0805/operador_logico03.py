#será estudad o operador lógico or

idade = int (input("Digite sua idade: "))
estudante = input("Você é estudante (S/N)? " )
meia_entrada = (idade <=18) or (estudante) 

if (idade <= 18) or (estudante.upper()):
    print ("Direito a meia entrada garantida")

else:
    print("Pagamento de valor integral")