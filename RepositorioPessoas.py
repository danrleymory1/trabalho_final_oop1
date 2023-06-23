from Pessoa import PessoaFisica, PessoaJuridica, Funcionario
from bradocs4py import validar_cpf, validar_cnpj
from Utilidades import print_e_esperar


class RepositorioPessoas:
    def __init__(self):
        self.clientes = []
        self.funcionarios = []

    def cadastrar_cliente(self):
        tipo = input(
            "Digite o tipo de cliente (1 - Pessoa Física, 2 - Pessoa Jurídica): "
        )

        while tipo not in ["1", "2"]:
            tipo = input(
                "Opção inválida!\nDigite novamente o tipo de cliente (1 - Pessoa Física, 2 - Pessoa Jurídica): "
            )

        if tipo == "1":
            cliente = PessoaFisica.criar()
            res = self.inserir_cliente(cliente)

            if not res:
                print_e_esperar(
                    "\n=================\nCliente já está cadastrado no sistema."
                )

            print_e_esperar("\n=================\nCliente cadastrado com sucesso.")
        elif tipo == "2":
            cliente = PessoaJuridica.criar()
            res = self.inserir_cliente(cliente)

            if not res:
                print_e_esperar(
                    "\n=================\nCliente já está cadastrado no sistema."
                )

            print_e_esperar("\n=================\nCliente cadastrado com sucesso.")

    def inserir_cliente(self, cliente):
        for p in self.clientes:
            if cliente.get_id() == p.get_id():
                return False

        self.clientes.append(cliente)
        return True

    def exibir_clientes(self):
        print("==== Clientes ====")
        for p in self.clientes:
            if isinstance(p, PessoaFisica):
                print(f"Nome: {p.get_nome()} - CPF: {p.get_cpf() or 'Não informado'}")
            else:
                print(f"Nome: {p.get_nome()} - CNPJ: {p.get_cnpj() or 'Não informado'}")
        print_e_esperar("===================")

    def alterar_cliente(self):
        cpf_cnpj = input("Digite o CPF/CNPJ do cliente para alterar: ")

        while not (validar_cnpj(cpf_cnpj) or validar_cpf(cpf_cnpj)):
            cpf_cnpj = input(
                "CPF/CNPJ inválido.\nDigite o CPF/CNPJ do cliente para alterar: "
            )

        if validar_cpf(cpf_cnpj):
            cliente = PessoaFisica.criar()
        elif validar_cnpj(cpf_cnpj):
            cliente = PessoaJuridica.criar()

        for p in self.clientes:
            if p.get_id() == cliente.get_id():
                if isinstance(cliente, PessoaFisica):
                    p.set_cpf(cliente.get_cpf())
                elif isinstance(cliente, PessoaJuridica):
                    p.set_cnpj(cliente.get_cnpj())

                p.set_nome(cliente.get_nome())
                p.set_endereco(cliente.get_endereco())
                print_e_esperar("\n=================\nCliente alterado com sucesso.")
                return

        print_e_esperar("\n=================\nCadastro não encontrado no sistema.")

    def remover_cliente(self):
        cpf_cnpj = input("Digite o CPF/CNPJ do cliente para remover: ")

        while not (validar_cnpj(cpf_cnpj) or validar_cpf(cpf_cnpj)):
            cpf_cnpj = input(
                "CPF/CNPJ inválido.\nDigite o CPF/CNPJ do cliente para remover: "
            )

        for p in self.clientes:
            if p.get_id() == cpf_cnpj:
                self.clientes.remove(p)
                print_e_esperar("\n=================\nCadastro removido com sucesso.")
                return

        print_e_esperar("\n================\nCadastro não encontrado no sistema.")

    def inserir_funcionario(self, funcionario):
        for f in self.funcionarios:
            if f.get_cpf() == funcionario.get_cpf():
                return False

        self.funcionarios.append(funcionario)
        return True

    def cadastrar_funcionario(self):
        funcionario = Funcionario.criar()

        res = self.inserir_funcionario(funcionario)

        if res:
            print_e_esperar("\n=================\nFuncionário cadastrado com sucesso.")
        else:
            print_e_esperar(
                "\n=================\nFuncionário já cadastrado no sistema."
            )

    def exibir_funcionarios(self):
        print("==== Funcionários ====")
        for f in self.funcionarios:
            print(f"Nome: {f.get_nome()} - CPF: {f.get_cpf() or 'Não informado'}")
        print("===================")

    def alterar_funcionario(self):
        cpf = input("Digite o CPF do funcionário para alterar: ")

        while not validar_cpf(cpf):
            cpf = input(
                "CPF inválido.\nDigite novamente o CPF do funcionário para alterar: "
            )

        for f in self.funcionarios:
            if f.get_cpf() == cpf:
                funcionario = Funcionario.criar()
                f.set_nome(funcionario.get_nome())
                f.set_cpf(funcionario.get_cpf())
                f.set_endereco(funcionario.get_endereco())
                print_e_esperar(
                    "\n=================\nFuncionário alterado com sucesso."
                )
                return
            print_e_esperar(
                "\n=================\nFuncionário não encontrado no sistema."
            )

    def remover_funcionario(self):
        cpf = input("Digite o CPF do funcionário para remover: ")

        while not validar_cpf(cpf):
            cpf = input(
                "CPF inválido.\nDigite novamente o CPF do funcionário para remover: "
            )

        for f in self.funcionarios:
            if f.get_cpf() == cpf:
                self.funcionarios.remove(f)
                print_e_esperar(
                    "\n=================\nFuncionário não encontrado no sistema."
                )
                return
            print_e_esperar(
                "\n=================\nFuncionário não encontrado no sistema."
            )

    def buscar_cliente(self, cpf_cnpj):
        for cliente in self.clientes:
            if isinstance(cliente, PessoaJuridica) and cliente.cnpj == cpf_cnpj:
                return cliente
            elif isinstance(cliente, PessoaFisica) and cliente.cpf == cpf_cnpj:
                return cliente
        return None
