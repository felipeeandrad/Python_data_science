#sera estudado a função round para arrendondar um número

numero = 123.45678
print (f"Numero com duas casas decimais: {numero:.2f}") #aqui só arredonda para visualização
print (f"Numero completo {numero}")

numero = round (numero, 0) # o numero zero representa quantas casas decimais irá arredondar
print (f"Numero arredondado {numero}")