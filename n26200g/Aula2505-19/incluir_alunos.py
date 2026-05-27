#Nesse programa vamos cadastrar alunos no banco de dados SQLite (curso.db) na tabela alunos

import sqlite3

def main():

    conn = sqlite3.connect('curso.db')
    cursor = conn.cursor()

    #Coleta de dados via console

    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    curso = input("Digite o curso do aluno: ")
    cpf = input("Digite o CPF do aluno: ")

    #Gravando dados na tabela usando '?' para evitar SQL Injection (Segurança de dados)
    cursor.execute(''' 
    INSERT INTO alunos (nome, idade, curso, cpf)
    VALUES (?, ?, ?, ?)
    ''', (nome, idade, curso, cpf))

    conn.commit() #Salva definitivamente na tabela
    conn.close()
    print("Aluno cadastrado com sucesso.")

if __name__ == "__main__":
    main()