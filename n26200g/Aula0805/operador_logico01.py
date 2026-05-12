#Será estudado operador lógico and

sexo = input(f"Digite seu sexo (M/F): ")
idade = int (input(f"Digite sua idade: "))

if (sexo.upper() == "M") and (idade == 18):
 
    print ("Você está apto ao alistamento militar")
    
# A função pass permite que o programa pule o if quando não souber o que por na condição dele
#   # ''' no começo e no final muda todo o condigo para comentário.

else:
    if sexo.upper() == "F":
        print("Mulheres não são obrigadas ao alistamento militar")
    else:
        print ("Você não esta apto ao alistamento militar")