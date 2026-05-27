#será estudado a função sem argumento e com argumento, ambas sem retorno

#função sem argumento:
def tracar():
    print("="*40)

#função com argumentos (num1, num2):

def somar_imprimir (num1,num2):
    soma = num1 + num2
    print (f"A soma de {num1} + {num2} é: {soma}")


tracar()

print("***Calculador de dois números")
tracar()
numero1 = int(input("Digite um número inteiro: "))
numero2 = int(input("Digite outro número inteiro: "))
somar_imprimir(numero1, numero2)
tracar()

valor1 = float(input("Digite um número decimal: "))
valor2 = float(input("Digite outro número decimal: "))
somar_imprimir(valor1,valor2)