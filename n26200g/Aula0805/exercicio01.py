lado_1 = int(input("Insira o valor de um lado do triangulo: "))
lado_2 = int(input("Insira o valor de outro lado do triangulo: "))
lado_3 = int(input("Insira o valor do ultimo lado do triangulo: "))

if (lado_1 == lado_2) and (lado_2 == lado_3):
    print ("Triangulo equilatero")

elif (lado_1 == lado_2) or (lado_2 == lado_3) or (lado_3 == lado_1):
    print ("Triangulo isóceles")

else: 
 print ("Triangulo escaleno")
  