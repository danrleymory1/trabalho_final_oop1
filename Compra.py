class NotaFiscal:
    def __init__(self, tipo, cliente, produtos, valor_total):
        self.tipo = tipo
        self.cliente = cliente
        self.produtos = produtos
        self.valor_total = valor_total

    def exibir_dados(self):
        print("=== Nota Fiscal ===")
        print(f"Tipo: {self.tipo}")
        print(f"Cliente: {self.cliente.nome}")
        print("Produtos:")
        for produto, quantidade in self.produtos.items():
            print(f"Nome: {produto.nome}, Quantidade: {quantidade}, Preço: R$ {produto.preco:.2f}")
        print(f"Valor Total: R$ {self.valor_total:.2f}")