from bradocs4py import validar_cpf, validar_cnpj


class Pessoa:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

    def get_nome(self):
        return self.nome

    def set_nome(self, novo_nome):
        if len(novo_nome) > 0:
            self.nome = novo_nome
        else:
            return False

    def get_endereco(self):
        return self.endereco

    def set_endereco(self, novo_endereco):
        if len(novo_endereco) > 0:
            self.endereco = novo_endereco
        else:
            return False


class PessoaFisica(Pessoa):
    def __init__(self, nome, cpf, endereco):
        self.cpf = cpf
        super().__init__(nome, endereco)

    def get_cpf(self):
        return self.cpf

    def set_cpf(self, novo_cpf):
        if validar_cpf(novo_cpf):
            self.cpf = novo_cpf
        else:
            return False

    def criar(self):
        pessoa = PessoaFisica(None, None, None)

        pessoa.set_nome(input("Digite o nome a ser cadastrado: "))
        while pessoa.get_nome() is None or len(pessoa.get_nome()) == 0:
            pessoa.set_nome(input("Nome inválido. Digite novamente: "))

        pessoa.set_cpf(input("Digite o CPF: "))
        while pessoa.get_cpf() is None:
            pessoa.set_cpf(input("CPF inválido. Digite novamente o CPF: "))

        pessoa.set_endereco(input("Digite o endereço: "))
        while pessoa.get_endereco() is None or len(pessoa.get_endereco()) == 0:
            pessoa.set_endereco(input("Endereço inválido. Digite novamente: "))

        return pessoa

    def get_id(self):
        return self.cpf


class PessoaJuridica(Pessoa):
    def __init__(self, nome, cnpj, endereco):
        self.cnpj = cnpj
        super().__init__(nome, endereco)

    def get_cnpj(self):
        return self.cnpj

    def set_cnpj(self, novo_cnpj):
        if validar_cnpj(novo_cnpj):
            self.cnpj = novo_cnpj
        else:
            return False

    def aplicar_desconto(self, valor_total):
        desconto = valor_total * 0.05  # 5% de desconto
        valor_com_desconto = valor_total - desconto
        return valor_com_desconto

    def criar(self):
        pessoa = PessoaJuridica(None, None, None)

        pessoa.set_nome(input("Digite o nome a ser cadastrado: "))
        while pessoa.get_nome() == None or len(pessoa.get_nome()) == 0:
            pessoa.set_nome(input("Nome inválido. Digite novamente: "))

        pessoa.set_cnpj(input("Digite o CNPJ: "))
        while pessoa.get_cnpj() == None:
            pessoa.set_cnpj(input("CNPJ inválido. Digite novamente o CNPJ: "))

        pessoa.set_endereco(input("Digite o endereço: "))
        while pessoa.get_endereco() == None or len(pessoa.get_endereco()) == 0:
            pessoa.set_endereco(input("Endereço inválido. Digite novamente: "))

        return pessoa

    def get_id(self):
        return self.cnpj


class Funcionario(PessoaFisica):
    def __init__(self, nome, cpf, endereco):
        super().__init__(nome, cpf, endereco)

    def aplicar_desconto(self, valor_total):
        desconto = valor_total * 0.1  # 10% de desconto
        valor_com_desconto = valor_total - desconto
        return valor_com_desconto
