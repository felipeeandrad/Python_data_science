#será estudado a excesão genérica

try:
    numero1 = int(input("Digite um numero: "))
    numero2 = int(input("Digite outro numero: "))
    divisao = numero1 / numero2 
    print (f"A divisão de {numero1} por {numero2} é {divisao}")

except Exception as erro:
    print ("ERRO: informe a mensagem abaixo ao suporte.")
    print (erro)
