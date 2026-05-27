import sqlite3

def main():
    conn = sqlite3.connect('curso.db')
    cursor = conn.cursor()

    #Coleta de dados via console

    cpf_busca = input("Digite o CPF do aluno: ")

    cursor.execute("SELECT * FROM alunos WHERE cpf = ?", (cpf_busca,))
    aluno = cursor.fetchone() #Retorna apenas um resultado
    if aluno:
        print("Registro encontrado")
        print(f"Nome: {aluno[1]}") 
        print(f"Idade: {aluno[2]}") 
        print(f"Curso: {aluno[3]}") 
        print(f"CPF: {aluno[4]}") 
        print("="*40)
        print("Digite os novos dados ou pressione [ENTER] para manter os atuais: ")
        
        novo_nome = input(f"Novo nome [{aluno[1]}]: ") or aluno[1] #Se o usuário não digitar nada, mantém o valor atual
        novo_idade = input(f"Nova idade [{aluno[2]}]: ") or aluno[2] #Se o usuário não digitar nada, mantém o valor atual
        novo_curso = input(f"Novo curso [{aluno[3]}]: ") or aluno[3] #Se o usuário não digitar nada, mantém o valor atual
        nova_idade = int(novo_idade) #Converte para inteiro
        #Executa a atualização
        sql_update = ("UPDATE alunos SET nome = ?, idade = ?, curso = ? WHERE cpf = ?") 
        cursor.execute(sql_update, (novo_nome, nova_idade, novo_curso, cpf_busca))
        conn.commit() #Salva as alterações
        print("Dados alterados com sucesso.")
    else:
        print("CPF não encontrado.")
    conn.close()

if __name__ == "__main__":
    main()
