def gerar_relatorio_detalhado(orcamento):
    """Gera um relatório detalhado de receitas e despesas"""
    print("\n=== Relatório Detalhado ===")
    
    print("\nreceita:")
    for receita in orcamento.receitas:
        print(f"- {receita['descricao']}: R$ {receita['valor']:.2f}")
    
    print("\ndespesa:")
    for despesa in orcamento.despesa:
        print(f"- {despesa['descricao']}: R$ {despesa['valor']:.2f}")
    
    resumo = orcamento.obter_resumo()
    print(f"\nSaldo Final: R$ {resumo['saldo']:.2f}")