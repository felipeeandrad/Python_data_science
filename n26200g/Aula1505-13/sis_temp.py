#Será criado um sistema para armazenar temperaturas, listar, imprimir e calcular a média das temperaturas 

import os
import sys

def main():
    while True:
        print("="*50)
        print ("Sistemas de temperaturas")
        print("="*50)
        print ("MENU")
        print("1- Cadastrar temperaturas: ")
        print("2- Listar temperaturas: ")
        print("3- Calcular a média das temperaturas: ")
        print("9 - Sair ")
        opcao = input("Digite a opção desejada: ")
        if opcao == "1":
            cadastrar_temp() 
        elif opcao == "2":
            listar_temp()
        elif opcao == "3":
            calcular_media_temp()
        elif opcao == "4":
            break
        else:
            print ("Opção inválida do menu.")
            
    print ("="*50)
    print("Obrigado por usar nosso sistema!!!")

#Cadastrar temperaturas em um arquivo texto 
def cadastrar_temp():
    nome_arquivo = input("Digite o nome do arquivo: ")
    try: 
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            print("Digite as temperaturas e pressione [ENTER]")
            print("Pressione [ENTER] para encerrar")
            while True:
                temp = input()
                if temp == "":
                    break
                arquivo.write(temp + "\n")
        print(f"Temperaturas gravadas no arquivo:{nome_arquivo}")
    except Exception as e:
        print(f"Erro durante a gravação: {e}")

#Função para listar as temperaturas de um arquivo
def listar_temp():
    nome_arquivo = input("Digite o nome do arquivo das temperaturas: ")
    try:
       with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        temperaturas = arquivo.read()
        print(temperaturas)
        input ("Pressione enter para voltar ao menu principal...")
    except FileNotFoundError as e:
        print(f"Erro durante a leitura do arquivo {e}")

    except Exception as e:
        print(f"Erro durante a leitura do arquivo: {e}")

#Função para calcular 

def calcular_media_temp():
    nome_arquivo = input("Digite o nome do arquivo para calcular a média: ")
    temp = []
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            while True:
                leitura = arquivo.readline()
                if leitura == "":
                    break
                temp.append(float(leitura))
        media_temp = sum(temp) / len(temp)
        print(f"A temperatura média é: {media_temp:.2f}")
        input("Pressione [ENTER] para voltar ao menu principal...")
    except FileNotFoundError:
        print(f"Erro: arquivo {nome_arquivo} não encontrado")
    except Expetion as e:
        print (f"Erro durante a leitura de arquvio {e}")




if __name__ == "__main__":
    main()