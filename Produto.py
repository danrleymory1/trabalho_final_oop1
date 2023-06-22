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
            return False

    def get_quantidade(self):
        return self.quantidade

    def set_quantidade(self, nova_quantidade):
        try:
            nova_quantidade = int(nova_quantidade)
            self.quantidade = nova_quantidade
        except:
            return False

    def exibir_informacoes(self):
        print(f"Código: {self.codigo}")
        print(f"Nome: {self.nome}")
        print(f"Preço: R$ {self.preco:.2f}")
        print(f"Quantidade: {self.quantidade}")

    def criar(alterar=False):
        produto = Produto(None, None, None)

        if alterar:
            Produto.codigo_sequencial -= 1

        produto.set_nome(input("Digite o nome do produto: "))
        while produto.get_nome() == None or len(produto.get_nome()) == 0:
            produto.set_nome(
                input("Nome inválido. Digite novamente o nome do produto: ")
            )

        produto.set_preco(input("Digite o preço do produto: "))
        while produto.get_preco() == None:
            produto.set_preco(
                input("Preço inválido. Digite novamente o preço do produto: ")
            )

        produto.set_quantidade(input("Digite a quantidade do produto: "))
        while produto.get_quantidade() == None:
            produto.set_quantidade(
                input("Quantidade inválida. Digite novamente a quantidade do produto: ")
            )

        return produto
