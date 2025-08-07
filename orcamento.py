class OrcamentoPessoal:
    def __init__(self):
        self.receita = []
        self.despesa = []

    def adicionar_receita(self, descricao, valor):  # Removi o 's'
        """Adiciona uma receita ao orçamento"""
        self.receita.append({'descricao': descricao, 'valor': valor})

    def adicionar_despesa(self, descricao, valor):  # Removi o 's'
        """Adiciona uma despesa ao orçamento"""
        self.despesa.append({'descricao': descricao, 'valor': valor})

    def calcular_saldo(self):
        """Calcula o saldo total (receitas - despesas)"""
        total_receita = sum(item['valor'] for item in self.receita)
        total_despesa = sum(item['valor'] for item in self.despesa)
        return total_receita - total_despesa

    def obter_resumo(self):
        """Retorna um resumo das finanças"""
        return {
            'total_receita': sum(item['valor'] for item in self.receita),
            'total_despesa': sum(item['valor'] for item in self.despesa),
            'saldo': self.calcular_saldo()
        }