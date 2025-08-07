def mostrar_menu():
    """Exibe o menu principal"""
    print("\n=== Calculadora de Orçamento Pessoal ===")
    print("1. Adicionar Receita")
    print("2. Adicionar Despesa")
    print("3. Ver Resumo")
    print("4. Sair")
    return input("Escolha uma opção: ")

def obter_valor(descricao):
    """Obtém um valor numérico válido do usuário"""
    while True:
        try:
            valor = float(input(f"Digite o valor da {descricao}: "))
            if valor >= 0:
                return valor
            print("O valor deve ser positivo.")
        except ValueError:
            print("Por favor, digite um valor numérico válido.")

def mostrar_resumo(resumo):
    """Exibe o resumo financeiro"""
    print("\n=== Resumo Financeiro ===")
    print(f"Total de Receita: R$ {resumo['total_receita']:.2f}")
    print(f"Total de Despesa: R$ {resumo['total_despesa']:.2f}")
    print(f"Saldo Disponível: R$ {resumo['saldo']:.2f}")
    
    if resumo['saldo'] > 0:
        print("Situação: Positiva (você está gastando menos do que ganha)")
    elif resumo['saldo'] < 0:
        print("Situação: Negativa (atenção! você está gastando mais do que ganha)")
    else:
        print("Situação: Equilibrada (seus gastos igualam seus ganhos)")