from orcamento import OrcamentoPessoal
from interface import mostrar_menu, obter_valor, mostrar_resumo
from relatorio import gerar_relatorio_detalhado

def main():
    orcamento = OrcamentoPessoal()
    
    while True:
        opcao = mostrar_menu()
        
        if opcao == '1':
            descricao = input("Descrição da receita: ")
            valor = obter_valor("receita")
            orcamento.adicionar_receita(descricao, valor)  # CORRETO
            print("Receita adicionada com sucesso!")
        
        elif opcao == '2':
            descricao = input("Descrição da despesa: ")
            valor = obter_valor("despesa")
            orcamento.adicionar_despesa(descricao, valor)
            print("Despesa adicionada com sucesso!")
        
        elif opcao == '3':
            resumo = orcamento.obter_resumo()
            mostrar_resumo(resumo)
            if input("\nDeseja ver o relatório detalhado? (s/n): ").lower() == 's':
                gerar_relatorio_detalhado(orcamento)
        
        elif opcao == '4':
            print("Encerrando o programa...")
            break
        
        else:
            print("Opção inválida. Por favor, escolha uma opção de 1 a 4.")

if __name__ == "__main__":
    main()