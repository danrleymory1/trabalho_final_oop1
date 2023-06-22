from Pessoa import PessoaFisica, PessoaJuridica, Funcionario
from Compra import NotaFiscal
from Produto import Produto


class Dados:
    def __init__(self):
        self.produtos = []
        self.clientes = []
        self.vendas = []

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
            print("\n=================\nProduto cadastrado com sucesso.")
        else:
            print("\n=================\nProduto já cadastrado no sistema.")

        input("\nAperte qualquer tecla para continuar.")

    def alterar_produto(self):
        codigo = int(input("Digite o código do produto que deseja alterar: "))

        for produto in self.produtos:
            if produto.codigo == codigo:
                novo_produto = Produto.criar(alterar=True)

                produto.set_nome(novo_produto.get_nome())
                produto.set_preco(novo_produto.get_preco())
                produto.set_quantidade(novo_produto.get_quantidade())

                print("Produto alterado com sucesso.")
                return

        print("Produto não encontrado.")

    def adicionar_ao_estoque(self):
        codigo = int(
            input("Digite o código do produto que deseja adicionar ao estoque: ")
        )

        for produto in self.produtos:
            if produto.codigo == codigo:
                quantidade = input("Digite a quantidade a ser adicionada ao estoque: ")

                while not quantidade.isnumeric():
                    quantidade = input(
                        "Valor inválido. Digite novamente a quantidade a ser adicionada ao estoque: "
                    )

                produto.set_quantidade(produto.get_quantidade() + quantidade)

                print("Produto adicionado ao estoque com sucesso.")
                return

        print("Produto não encontrado.")

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
                print("Produto removido com sucesso.")
                return

        print("Produto não encontrado.")

    def cadastrar_cliente(self):
        tipo = input(
            "Digite o tipo de cliente (1 - Pessoa Física, 2 - Pessoa Jurídica): "
        )

        if tipo == "1":
            cpf = str(input("Digite o CPF do cliente: "))
            nome = input("Digite o nome do cliente: ")
            endereco = input("Digite o endereço do cliente: ")

            cliente = PessoaFisica(nome, cpf, endereco)
            self.clientes.append(cliente)

            print("Cliente cadastrado com sucesso.")
        elif tipo == "2":
            cnpj = str(input("Digite o CNPJ do cliente: "))
            nome = input("Digite o nome do cliente: ")
            endereco = input("Digite o endereço do cliente: ")

            cliente = PessoaJuridica(nome, cnpj, endereco)
            self.clientes.append(cliente)

            print("Cliente cadastrado com sucesso.")
        else:
            print("Opção inválida.")

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)

    def exibir_clientes(self):
        print("==== Clientes ====")
        for cliente in self.clientes:
            if isinstance(cliente, PessoaFisica):
                print(f"Nome: {cliente.nome} - CPF: {cliente.cpf or 'Não informado'}")
            else:
                print(f"Nome: {cliente.nome} - CNPJ: {cliente.cnpj or 'Não informado'}")
        print("===================")

    def alterar_cliente(self):
        cpf_cnpj = str(input("Digite o CPF/CNPJ do cliente para alterar: "))
        for cliente in self.clientes:
            if isinstance(cliente, PessoaFisica) and cliente.cpf == cpf_cnpj:
                nome = input("Digite o novo nome do cliente: ")
                cpf = str(input("Digite o novo CPF do cliente: "))
                endereco = input("Digite o novo endereço do cliente: ")
                cliente.nome = nome
                cliente.cpf = cpf
                cliente.endereco = endereco
                print("Cliente atualizado com sucesso.")
                return
            elif isinstance(cliente, PessoaJuridica) and cliente.cnpj == cpf_cnpj:
                nome = input("Digite o novo nome do cliente: ")
                cnpj = str(input("Digite o novo cnpj do cliente: "))
                endereco = input("Digite o novo endereço do cliente: ")
                cliente.nome = nome
                cliente.cnpj = cnpj
                cliente.endereco = endereco

                print("Cliente alterado com sucesso.")
                return
        print("Cliente não encontrado.")

    def remover_cliente(self):
        cpf_cnpj = str(input("Digite o CPF/CNPJ do cliente para remover: "))
        for cliente in self.clientes:
            if isinstance(cliente, PessoaJuridica) and cliente.cnpj == cpf_cnpj:
                self.clientes.remove(cliente)
                print("Cliente removido com sucesso.")
                return
            elif isinstance(cliente, PessoaFisica) and cliente.cpf == cpf_cnpj:
                self.clientes.remove(cliente)
                print("Cliente removido com sucesso.")
                return
        print("Cliente não encontrado.")

    def cadastrar_funcionario(self):
        cpf = str(input("Digite o CPF do funcionário: "))
        nome = input("Digite o nome do funcionário: ")
        endereco = input("Digite o endereço do funcionário: ")

        funcionario = Funcionario(nome, cpf, endereco)
        self.clientes.append(funcionario)

        print("Funcionário cadastrado com sucesso.")

    def adicionar_funcionario(self, funcionario):
        self.clientes.append(funcionario)

    def exibir_funcionarios(self):
        print("==== Funcionários ====")
        for funcionario in self.clientes:
            print(
                f"Nome: {funcionario.nome} - CPF: {funcionario.cpf or 'Não informado'}"
            )
        print("===================")

    def alterar_funcionario(self):
        cpf = str(input("Digite o CPF do funcionário para alterar: "))
        for funcionario in self.clientes:
            if isinstance(funcionario, Funcionario) and funcionario.cpf == cpf:
                nome = str(input("Digite o novo nome do Funcionário: "))
                cpf = input("Digite o novo CPF do Funcionário: ")
                endereco = input("Digite o novo endereço do funcionário: ")
                funcionario.nome = nome
                funcionario.cpf = cpf
                funcionario.endereco = endereco
                print("Funcionário atualizado com sucesso.")
                return
        print("Funcionário não encontrado.")

    def remover_funcionario(self):
        cpf = str(input("Digite o CPF do funcionário para remover: "))
        for funcionario in self.clientes:
            if isinstance(funcionario, Funcionario) and funcionario.cpf == cpf:
                self.clientes.remove(funcionario)
                print("Funcionário removido com sucesso.")
                return
        print("Funcionário não encontrado.")

    def realizar_venda(self):
        cpf_cnpj = int(input("Digite o CPF/CNPJ do cliente: "))
        cliente = self.buscar_cliente(cpf_cnpj)

        if cliente is None:
            print("Cliente não encontrado.")
            return

        produtos_venda = {}
        continuar = True

        while continuar:
            codigo = int(input("Digite o código do produto: "))
            quantidade = int(input("Digite a quantidade: "))

            produto = self.buscar_produto(codigo)

            if produto is None:
                print("Produto não encontrado.")
                continue

            if quantidade > produto.quantidade:
                print("Quantidade em estoque insuficiente.")
                continue

            produtos_venda[produto] = quantidade

            continuar = input("Deseja adicionar mais produtos? (S/N)").upper() == "S"

        valor_total = self.calcular_valor_total(produtos_venda)

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

        self.vendas.append(nota_fiscal)

        print("Venda realizada com sucesso.")
        nota_fiscal.exibir_dados()

    def calcular_valor_total(self, produtos):
        valor_total = 0.0
        for produto, quantidade in produtos.items():
            valor_total += produto.preco * quantidade
        return valor_total

    def exibir_total_vendas(self):
        total_vendas = sum(nota_fiscal.valor_total for nota_fiscal in self.vendas)
        print(f"Numero de vendas realizadas: {len(self.vendas)}")
        print(f"Total de Vendas: R$ {total_vendas:.2f}")

    def buscar_produto(self, codigo):
        for produto in self.produtos:
            if produto.codigo == codigo:
                return produto
        return None

    def buscar_cliente(self, cpf_cnpj):
        for cliente in self.clientes:
            if isinstance(cliente, PessoaJuridica) and cliente.cnpj == cpf_cnpj:
                return cliente
            elif isinstance(cliente, PessoaFisica) and cliente.cpf == cpf_cnpj:
                return cliente
        return None
