peso = float(input("Insira seu peso: "))
altura = float(input("insira sua altura: "))

imc = peso / altura**2

if imc >= 40:
    print ("Seu imc é {imc:.1f}, você esta com obesidade grave")

elif imc >=25:
    print (f"Seu imc é {imc:.1f}, Voçê esta acima do peso")

elif imc >=18.5:
    print (f"Seu imc é {imc:.1f}, Voçê esta com peso normal")

elif imc <=18.4:
    print (f"Seu imc é {imc:.1f}, Voçê esta abaixo do peso")