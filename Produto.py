class Produto:
    codigo_sequencial = 1

    def __init__(self, nome, preco, quantidade=0):
        self.codigo = Produto.codigo_sequencial
        Produto.codigo_sequencial += 1
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def get_codigo(self):
        return self.codigo

    def get_nome(self):
        return self.nome

    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def get_preco(self):
        return self.preco

    def set_preco(self, novo_preco):
        try:
            novo_preco = float(novo_preco)
            self.preco = novo_preco
        except:
            print("Valor inválido")

    def get_quantidade(self):
        return self.quantidade

    def set_quantidade(self, nova_quantidade):
        try:
            nova_quantidade = int(nova_quantidade)
            self.quantidade = nova_quantidade
        except:
            print("Valor inválido")

    def exibir_informacoes(self):
        print(f"Código: {self.codigo}")
        print(f"Nome: {self.nome}")
        print(f"Preço: R$ {self.preco:.2f}")
        print(f"Quantidade: {self.quantidade}")
