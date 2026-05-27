#vamos criar um arquivo texto usando o python
import os
import sys

nome_arquivo = "arquivo01.txt"

try:
    with open (nome_arquivo, 'a', encoding="utf-8"  ) as arquivo:
        arquivo.write("AAAA")
        arquivo.write("\nBBBB")

        print ("Conteudo anexado com sucesso")

except Exception as e:
        print(f"Erro ao anexar o arquivo: {e}")