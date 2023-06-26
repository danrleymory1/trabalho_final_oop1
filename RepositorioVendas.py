from bradocs4py import validar_cnpj, validar_cpf
from Pessoa import PessoaFisica, PessoaJuridica, Funcionario
from Utilidades import print_e_esperar
from Compra import NotaFiscal


class RepositorioVendas:
    def __init__(self, repositorio_produtos, repositorio_pessoas):
        self.vendas = []
        self.repositorio_produtos = repositorio_produtos
        self.repositorio_pessoas = repositorio_pessoas

    def realizar_venda(self):
        cpf_cnpj = input("Digite o CPF/CNPJ do cliente: ")

        print(validar_cnpj(cpf_cnpj))
        print(validar_cpf(cpf_cnpj))
        print(validar_cnpj(cpf_cnpj) or validar_cpf(cpf_cnpj))

        while not (validar_cnpj(cpf_cnpj) or validar_cpf(cpf_cnpj)):
            cpf_cnpj = input(
                'CPF/CNPJ inválido. Digite "SAIR" para sair.\nDigite novamente o CPF/CNPJ do cliente: '
            )
            if cpf_cnpj == "SAIR":
                return

        cliente = self.repositorio_pessoas.buscar_cliente(cpf_cnpj)

        if cliente is None:
            print_e_esperar("Cliente não encontrado.")
            return

        produtos_venda = {}

        while True:
            codigo = input("Digite o código do produto: ")
            while not codigo.isnumeric():
                input(
                    'Código inválido. Digite "SAIR" para sair.\nDigite o código novamente: '
                )
                if quantidade == "SAIR":
                    return

            codigo = int(codigo)

            quantidade = input("Digite a quantidade do produto: ")
            while not quantidade.isnumeric():
                quantidade = input(
                    'Quantidade inválida. Digite "SAIR" para sair.\nDigite a quantidade novamente: '
                )
                if quantidade == "SAIR":
                    return

            quantidade = int(quantidade)

            produto = self.repositorio_produtos.buscar_produto(codigo)

            if produto is None:
                print_e_esperar("Produto não encontrado.")
                continue

            if quantidade > produto.quantidade:
                print_e_esperar("Quantidade em estoque insuficiente.")
                continue

            produtos_venda[produto] = quantidade

            if input("Deseja adicionar mais produtos? (S/N)").upper() != "S":
                break

        valor_total = NotaFiscal.calcular_valor_total(produtos_venda)

        if isinstance(cliente, PessoaJuridica):
            valor_total = cliente.aplicar_desconto(valor_total)
        elif isinstance(cliente, Funcionario):
            valor_total = cliente.aplicar_desconto(valor_total)

        nota_fiscal = NotaFiscal(
            "CPF" if isinstance(cliente, PessoaFisica or Funcionario) else "CNPJ",
            cliente,
            produtos_venda,
            valor_total,
        )

        nota_fiscal.exibir_dados()

        self.vendas.append(nota_fiscal)

        print_e_esperar("\n=================\nVenda realizada com sucesso.")
        nota_fiscal.exibir_dados()

    def exibir_total_vendas(self):
        total_vendas = sum(nota_fiscal.valor_total for nota_fiscal in self.vendas)
        print(f"Numero de vendas realizadas: {len(self.vendas)}")
        print_e_esperar(f"Total de Vendas: R$ {total_vendas:.2f}")
