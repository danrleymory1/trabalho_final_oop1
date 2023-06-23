from RepositorioProdutos import RepositorioProdutos
from RepositorioPessoas import RepositorioPessoas
from RepositorioVendas import RepositorioVendas


class Dados:
    def __init__(self):
        self.produtos = RepositorioProdutos()
        self.pessoas = RepositorioPessoas()
        self.vendas = RepositorioVendas(self.produtos, self.pessoas)
