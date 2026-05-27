#Será criado um sistema para armazenar temperaturas, listar, imprimir e calcular a média das temperaturas 

import os
import sys

def main():
    while True:
        print("="*50)
        print ("Sistemas de Notas")
        print("="*50)
        print ("MENU")
        print("1- Salvar notas: ")
        print("2- Imprimir notas: ")
        print("3- Imprimir média das notas: ")
        print("9 - Sair ")
        opcao = input("Digite a opção desejada: ")
        if opcao == "1":
            salvar_notas() 
        elif opcao == "2":
            imprimir_notas()
        elif opcao == "3":
            imprimir_media_notas()
        elif opcao == "9":
            break
        else:
            print ("Opção inválida do menu.")
            
    print ("="*50)
    print("Obrigado por usar nosso sistema!!!")

#Cadastrar temperaturas em um arquivo texto 
def salvar_notas():
    nome_arquivo = input("Digite o nome do arquivo: ")
    try: 
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            print("Digite as notas e pressione [ENTER]")
            print("Pressione [ENTER] para encerrar")
            while True:
                nota = input()
                if nota == "":
                    break
                arquivo.write(nota + "\n")
        print(f"Notas salvas no arquivo {nome_arquivo} com sucesso.")
    except Exception as e:
        print(f"Erro durante a gravação: {e}")

#Função para listar as temperaturas de um arquivo
def  imprimir_notas():
    nome_arquivo = input("Digite o nome do arquivo das notas: ")
    try:
       with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        nota = arquivo.read()
        print(nota)
        input ("Pressione enter para voltar ao menu principal...")
    except FileNotFoundError as e:
        print(f"Erro durante a leitura do arquivo {e}")

    except Exception as e:
        print(f"Erro durante a leitura do arquivo: {e}")

#Função para calcular 

def imprimir_media_notas():
    nome_arquivo = input("Digite o nome do arquivo para calcular a média: ")
    nota = []
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            while True:
                leitura = arquivo.readline()
                if leitura == "":
                    break
                nota.append(float(leitura))
        media_nota = sum(nota) / len(nota)
        print(f"A nota média é: {media_nota:.2f}")
        input("Pressione [ENTER] para voltar ao menu principal...")
    except FileNotFoundError:
        print(f"Erro: arquivo {nome_arquivo} não encontrado")
    except Expetion as e:
        print (f"Erro durante a leitura de arquvio {e}")




if __name__ == "__main__":
    main()