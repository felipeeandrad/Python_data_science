#Nesse programa será criado um banco de dados SQLite e uma tabela para receber os dados de aluno

import sqlite3

def main():

    #Criar a conexão(se o arquivo não existir, ele será criado na pasta do arquivo Python) 
    conn = sqlite3.connect('curso.db')
    cursor = conn.cursor()
    #Comando SQL para criar a tabela com os tipo de dados
    cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS alunos (
        id_aluno INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        idade INTEGER,
        curso TEXT,
        cpf TEXT NOT NULL UNIQUE
    )
    ''')



    conn.close()
    print ("Banco de dados e tabela criados com sucesso")
if __name__=="__main__":
    main()




