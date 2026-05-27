# Nesse programa vamos conectar ao banco de dados
# e excluir um registro da tabela alunos
import sqlite3

def main():

    # Conecta ao banco
    conn = sqlite3.connect("curso.db")
    cursor = conn.cursor()

    cpf = input("Digite o CPF para pesquisa e exclusão: ")

    cursor.execute("SELECT * FROM alunos WHERE cpf = ?", (cpf,))
    aluno = cursor.fetchone() # Pega um registro

    if aluno:
        print("Registro encontrado:")
        print(f"Nome: {aluno[1]}")
        print(f"CPF: {aluno[4]}")
        resposta = input("Deseja excluir esse registro S/N: ")
        if resposta.upper() == "S":
            cursor.execute("DELETE FROM alunos WHERE cpf = ?", (cpf,))
            conn.commit()
            print("Registro excluido com sucesso.")
    else:
        print("\nErro: Aluno com este CPF não foi encontrado no sistema.")

    # Fechar a conexão
    conn.close()

