import sqlite3
import pandas as pd


def analisar_vendas():
    conn = sqlite3.connect("empresa_xpto.db")

    # Lê todos os dados da tabela para um DataFrame
    df = pd.read_sql_query("SELECT * FROM vendas", conn)

    conn.close()

    print("=== PRIMEIRAS LINHAS ===")
    print(df.head())
    print("\n" + "=" * 50)

    print("=== INFORMAÇÕES GERAIS ===")
    print(df.info())
    print("\n" + "=" * 50)

    print("=== ESTATÍSTICAS DESCRITIVAS ===")
    print(df.describe())

    # Estatísticas por categoria
    print("\n=== VENDAS POR CATEGORIA ===")
    resumo = df.groupby('Categoria').agg({
        'Preco': 'sum',
        'Quantidade': 'sum',
        'Produto': 'count'
    }).rename(columns={
        'Preco': 'Valor_Total_R$',
        'Quantidade': 'Unidades_Vendidas',
        'Produto': 'Quantidade_de_Vendas'
    })

    print(resumo)


if __name__ == "__main__":
    analisar_vendas()
