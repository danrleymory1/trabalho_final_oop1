class PessoaFisica:
    def __init__(self, nome, cpf, endereco):
        self.cpf = cpf
        self.nome = nome
        self.endereco = endereco


class PessoaJuridica:
    def __init__(self, nome, cnpj, endereco):
        self.nome = nome
        self.cnpj = cnpj
        self.endereco = endereco

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


