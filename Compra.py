class NotaFiscal:
    def __init__(self, tipo, cliente, produtos, valor_total):
        self.tipo = tipo
        self.cliente = cliente
        self.produtos = produtos
        self.valor_total = valor_total

    def get_tipo(self):
        return self.tipo

    def get_cliente(self):
        return self.cliente

    def get_produtos(self):
        return self.produtos

    def get_valor_total(self):
        return self.valor_total

    def exibir_dados(self):
        print("=== Nota Fiscal ===")
        print(f"Tipo: {self.tipo}")
        print(f"Cliente: {self.cliente.nome}")
        print("Produtos:")
        for produto, quantidade in self.produtos.items():
            print(
                f"Nome: {produto.nome}, Quantidade: {quantidade}, Preço: R$ {produto.preco:.2f}"
            )
        print(f"Valor Total: R$ {self.valor_total:.2f}")

    def calcular_valor_total(produtos):
        valor_total = 0.0
        for produto, quantidade in produtos.items():
            valor_total += produto.preco * quantidade
        return valor_total
