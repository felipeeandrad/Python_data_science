# Será criado um arquivo texto usando o python 
import os
import sys

nome_arquivo = "arquivo01.txt"

with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
    arquivo.write("hoje é quinta feira ")
    arquivo.write("\nAmanhã é sexta feira ")

    print("Arquivo criado com sucesso!")

