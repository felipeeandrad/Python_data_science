#Nesse programa vamo estudar a exceção da divisão por 0.

print ("Calculadora de divisão")
print ("="*40)

while True:
    try: 
        numerador = int(input("Digite o numerador da divisão: "))
        denominador = int(input("Digite o denominador da divisão: "))
        resultado = numerador/denominador
        print(f"A divisão de {numerador} por {denominador} é {resultado}")
        break
    except ZeroDivisionError: 
        print("ERROR: A divisão por zero não e permitida.")
        print ("Digite um numero diferente de zero no denominador.")
    except ValueError:
        print("ERRO: Digite apenas números para a divisão")   
        print ("Tente novamente")
        
        