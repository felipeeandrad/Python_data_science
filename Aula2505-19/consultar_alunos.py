#Nesse programa vamos consultar os alunos da tabela "alunos"

import sqlite3

def main():
    conn = sqlite3.connect("curso.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM alunos")
    alunos = cursor.fetchall() #Tranforma o resultado da consulta lista

    print(f"{'Nome' :<20} {'Idade' :<5} {'Curso':<30} {'CPF'}")
    for aluno in alunos: 
        #Acesso via indice
        print(f"{aluno[1]:<20} {aluno[2]:<5} {aluno[3]:<30} {aluno[4]} ")
        conn.close()

if __name__ == "__main__":
    main()