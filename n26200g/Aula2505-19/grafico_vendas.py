import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def gerar_grafico():
    conn = sqlite3.connect('empresa_xpto.db')
    df = pd.read_sql_query("SELECT * FROM vendas", conn)
    conn.close()

    # Agrupa por categoria
    vendas_por_categoria = df.groupby('Categoria')['Preco'].sum().reset_index()

    # ================== CONFIGURAÇÃO DO GRÁFICO ==================
    plt.figure(figsize=(10, 6))

    barras = plt.bar(vendas_por_categoria['Categoria'], 
                     vendas_por_categoria['Preco'], 
                     color='skyblue', 
                     alpha=0.85)

    # Títulos
    plt.title('Total de Vendas por Categoria', fontsize=16, pad=40)
    plt.xlabel('Categoria', fontsize=13)
    plt.ylabel('Valor Total Vendido (R$)', fontsize=13)

    # ================== AJUSTES NO EIXO Y ==================
    plt.ylim(0, vendas_por_categoria['Preco'].max() * 1.15)  # Aumenta o limite superior
    
    # Formata o eixo Y para mostrar valores completos (sem notação científica)
    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'R${x:,.0f}'))

    # ================== AJUSTES NO EIXO X ==================
    plt.xticks(rotation=45, ha='right', fontsize=11)
    plt.subplots_adjust(bottom=0.28)   # ← Aumenta espaço para os rótulos do eixo X

    # Grid
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Valores acima das barras
    for barra in barras:
        altura = barra.get_height()
        plt.text(barra.get_x() + barra.get_width()/2, 
                 altura + (altura * 0.03), 
                 f'R${altura:,.0f}', 
                 ha='center', va='bottom', fontsize=11, fontweight='bold')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    gerar_grafico()