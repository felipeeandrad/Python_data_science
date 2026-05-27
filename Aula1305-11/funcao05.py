#será estudado função com argumentos e retorno usando if dentro da função

salario_base = 2000
def calcular_bonus(salario,porcentagem):
    if salario <= salario_base:
        bonus = salario * porcentagem
    else:
        bonus = 0 

    return bonus 

print("Sistema de RH")
salaro = float(input("Digite o salário do funcionário: "))
porc_bonus = 0.15 
bonus = calcular_bonus(salario,porc_bonus)
salario = salario + bonus 
print (f"Salário com bonus: R$ {salario:.2f}")


