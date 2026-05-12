#Nesse programa sera estudado o uso do comando 'input'
#e a maneira mais moderna de formatar um string em python usando o f-string
print ("Sistema de cadastro de usuários")
print ("=" * 40)
nome_usuario = input ("Digite o nome do usuário: ")
idade = input ("Digite a idade do usuário: ")
cidade = input ("Digite a cidade do usuário: ")
print ("=" * 40)
print (f"Nome do usuário {nome_usuario} cadastrado com sucesso.")
print (f"O usuário tem {idade} anos.")
print (f"O usuário mora na cidade de {cidade}.")