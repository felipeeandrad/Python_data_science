#Nesse programa vamos usar o for para listas

frutas = ["maçã", "banana", "laranja", "pera", "goiaba"]

for i in frutas: 
    print (f"Eu gosto de {i}")

#imprimindo as letras de uma palavra

palavra = "Senai Celso Charuri"
vogais = "aeiouáéíóú"
numero_vogais = 0 
for letra in palavra: 
    print (letra)
    if letra.lower() in vogais: 
        numero_vogais += 1
print(f"A palavra possui {numero_vogais} vogais.")
