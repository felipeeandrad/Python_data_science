# Continuando com o operador lógico and

salario = float(input("Digite o salário do funcionário: "))

if salario <= 1621:
    inss = salario * 0.075

elif salario > 1621 and salario <= 2904.84:
    inss = salario * 0.09 - 24.32

elif salario > 2904.84 and salario <= 4354.27:
    inss = salario * 0.12 - 111.4 

elif salario > 4354.27 and salario <= 8475.55:
    inss = salario * 0.14 - 198.49 

else:
    inss = salario * 0.14 - 198.49

salario_liquido = salario - inss 

print (f"Salário bruto: {salario:.2f}")
print (f"Desconto INSS: R$ {inss:.2f}")
print (f"Salário liquido: R$ {salario_liquido:.2f}")