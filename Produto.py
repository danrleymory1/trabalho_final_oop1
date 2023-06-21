class Produto:
    codigo_sequencial = 1

    def __init__(self, nome, preco, quantidade=0):
        self.codigo = Produto.codigo_sequencial
        Produto.codigo_sequencial += 1
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def exibir_informacoes(self):
        print(f"Código: {self.codigo}")
        print(f"Nome: {self.nome}")
        print(f"Preço: R$ {self.preco:.2f}")
        print(f"Quantidade: {self.quantidade}")
