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
            print("Nome inválido. Tente novamente")

    def get_endereco(self):
        return self.endereco

    def set_endereco(self, novo_endereco):
        if len(novo_endereco) > 0:
            self.endereco = novo_endereco
        else:
            print("Endereço inválido. Tente novamente")


class PessoaFisica(Pessoa):
    def __init__(self, nome, cpf, endereco):
        self.cpf = cpf
        self.super().__init__(nome, endereco)

    def get_cpf(self):
        return self.cpf

    def set_cpf(self, novo_cpf):
        if validar_cpf(novo_cpf):
            self.cpf = novo_cpf
        else:
            print("CPF inválido. Tente novamente")

    def get_nome(self):
        return self.nome

    def set_nome(self, novo_nome):
        if len(novo_nome) > 0:
            self.nome = novo_nome
        else:
            print("Nome inválido. Tente novamente")


class PessoaJuridica(Pessoa):
    def __init__(self, nome, cnpj, endereco):
        self.cnpj = cnpj
        self.super().__init__(nome, endereco)

    def get_cnpj(self):
        return self.cnpj

    def set_cnpj(self, novo_cnpj):
        if validar_cnpj(novo_cnpj):
            self.cnpj = novo_cnpj
        else:
            print("CNPJ inválido. Tente novamente")

    def aplicar_desconto(self, valor_total):
        desconto = valor_total * 0.05  # 5% de desconto
        valor_com_desconto = valor_total - desconto
        return valor_com_desconto


class Funcionario(PessoaFisica):
    def __init__(self, nome, cpf, endereco):
        super().__init__(nome, cpf, endereco)

    def aplicar_desconto(self, valor_total):
        desconto = valor_total * 0.1  # 10% de desconto
        valor_com_desconto = valor_total - desconto
        return valor_com_desconto
