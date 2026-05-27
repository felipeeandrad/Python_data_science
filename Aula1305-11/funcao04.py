#Será estudado funções com argumento e com retorno

def calcular_area_retangulo (base,altura):
    area = base * altura 
    return area

def calcular_dobro (valor):
    return valor *2

valor_base = float(input("Digite a base do retangulo: "))
valor_altura = float(input("Digite a altura do retangulo: "))

area_retangulo = calcular_area_retangulo

print(f"A area do retangulo é: {area_retangulo}")

area_dobrada = calcular_dobro(area_retangulo)
print(f"O dobro da área é {area_dobrada}")


