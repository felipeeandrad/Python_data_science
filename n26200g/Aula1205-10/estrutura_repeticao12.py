#nesse programa vamos sortear os numeros da megasena

import random
numero_sorteado = 0 
megasena = []
for i in range (9999):
    numero = random.randint(1,60)
    if numero in megasena:
        continue
    megasena.append(numero)
    numero_sorteado += 1 
    if numero_sorteado >=6:
        break
megasena.sort()  
print(megasena)