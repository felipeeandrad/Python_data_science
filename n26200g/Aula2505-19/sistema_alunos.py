import os
import sys

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    limpar_tela()
    print("="*50)
    print("          SISTEMA DE GERENCIAMENTO DE ALUNOS")
    print("="*50)
    print()
    print("1. Incluir Aluno")
    print("2. Alterar Aluno")
    print("3. Consultar Aluno")
    print("4. Excluir Aluno")
    print("5. Sair")
    print()
    print("="*50)

def executar_modulo(modulo):
    """Executa o módulo desejado e aguarda o usuário pressionar Enter"""
    try:
        if modulo == "incluir_alunos":
            import incluir_alunos
            if hasattr(incluir_alunos, 'main'):
                incluir_alunos.main()
            else:
                print("Módulo incluído sem função main(). Executando como script...")
                exec(open("incluir_aluno.py", encoding="utf-8").read())
                
        elif modulo == "alterar_alunos":
            import alterar_alunos
            if hasattr(alterar_alunos, 'main'):
                alterar_alunos.main()
            else:
                exec(open("alterar_alunos.py", encoding="utf-8").read())
                
        elif modulo == "consultar_alunos":
            import consultar_alunos
            if hasattr(consultar_alunos, 'main'):
                consultar_alunos.main()
            else:
                exec(open("consultar_alunos.py", encoding="utf-8").read())
                
        elif modulo == "excluir_alunos":
            import biblio_sqlite.excluir_alunos as excluir_alunos
            if hasattr(excluir_alunos, 'main'):
                excluir_alunos.main()
            else:
                exec(open("excluir_alunos.py", encoding="utf-8").read())
                
    except ImportError:
        print(f"\nErro: Arquivo {modulo}.py não encontrado!")
    except Exception as e:
        print(f"\nErro ao executar o módulo: {e}")
    
    input("\nPressione Enter para voltar ao menu...")

def main():
    while True:
        mostrar_menu()
        
        opcao = input("Escolha uma opção (1-5): ").strip()
        
        if opcao == "1":
            executar_modulo("incluir_alunos")
        elif opcao == "2":
            executar_modulo("alterar_alunos")
        elif opcao == "3":
            executar_modulo("consultar_alunos")
        elif opcao == "4":
            executar_modulo("excluir_alunos")
        elif opcao == "5":
            print("\nEncerrando o sistema. Até logo!")
            break
        else:
            print("\nOpção inválida! Tente novamente.")
            input("Pressione Enter para continuar...")

if __name__ == "__main__":
    main()