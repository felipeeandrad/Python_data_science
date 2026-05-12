#sera estudado algumas funções aritméticas para lista

notas = {5.5, 8.2, 10, 7.5}
print(notas)

nota_maxima = max(notas)
print (f"Maior nota: {nota_maxima}")

nota_minima = min(notas)
print(f"Menor nota: {nota_minima}")

amplitude = nota_maxima - nota_minima
print (f"Amplitude das notas: {amplitude}")

soma_notas = sum(notas)
print (f"soma das notas: {soma_notas}")

numero_de_notas = len(notas)
print(f"Numero de notas: {numero_de_notas}")

#Media das notas

media_notas = sum(notas) / len(notas)
print(f"A media é {media_notas}")