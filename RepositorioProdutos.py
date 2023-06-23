from Produto import Produto
from Utilidades import print_e_esperar


class RepositorioProdutos:
    def __init__(self):
        self.produtos = []

    def inserir_produto(self, produto):
        for p in self.produtos:
            if p.get_nome().upper() == produto.get_nome().upper():
                return False

        self.produtos.append(produto)
        return True

    def cadastrar_produto(self):
        produto = Produto.criar()

        res = self.inserir_produto(produto)

        if res:
            print_e_esperar("\n=================\nProduto cadastrado com sucesso.")
        else:
            print_e_esperar("\n=================\nProduto já cadastrado no sistema.")

    def alterar_produto(self):
        codigo = int(input("Digite o código do produto que deseja alterar: "))

        for produto in self.produtos:
            if produto.codigo == codigo:
                novo_produto = Produto.criar(alterar=True)

                produto.set_nome(novo_produto.get_nome())
                produto.set_preco(novo_produto.get_preco())
                produto.set_quantidade(novo_produto.get_quantidade())

                print_e_esperar("\n=================\nProduto alterado com sucesso.")
                return

        print_e_esperar("\n=================\nProduto não encontrado.")

    def alterar_estoque(self):
        codigo = input("Digite o código do produto que deseja alterar no estoque: ")
        while not codigo.isnumeric():
            codigo = input("Código inválido. Digite o código novamente")

        codigo = int(codigo)

        for produto in self.produtos:
            if produto.codigo == codigo:
                quantidade = input("Digite a quantidade a ser do produto em estoque: ")

                while not quantidade.isnumeric():
                    quantidade = input(
                        "Valor inválido. Digite novamente a quantidade do produto em estoque: "
                    )

                produto.set_quantidade(int(quantidade))

                print_e_esperar("\n=================\nEstoque corrigido com sucesso.")
                return

        print_e_esperar("\n=================\nProduto não encontrado no sistema.")

    def exibir_estoque(self):
        print("=== Estoque ===")
        for produto in self.produtos:
            produto.exibir_informacoes()
            print()  # Linha em branco para separar os produtos

    def remover_produto(self):
        codigo = int(input("Digite o código do produto que deseja remover: "))

        for produto in self.produtos:
            if produto.codigo == codigo:
                self.produtos.remove(produto)
                print_e_esperar("\n=================\nProduto removido com sucesso.")
                return

        print_e_esperar("\n=================\nProduto não encontrado no sistema.")

    def buscar_produto(self, codigo):
        for produto in self.produtos:
            if produto.codigo == codigo:
                return produto
        return None
