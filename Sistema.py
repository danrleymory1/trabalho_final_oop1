from Dados import Dados
from Menu import Menu
from Produto import Produto
from Pessoa import PessoaFisica, PessoaJuridica, Funcionario


banco_dados = Dados()
menu = Menu(banco_dados)

# Adicionar produtos iniciais
produto1 = Produto("Arroz", 4.5, 10)
produto2 = Produto("Feijão", 5.0, 10)
produto3 = Produto("Macarrão", 3.5, 10)
produto4 = Produto("Oleo", 9, 10)
produto5 = Produto("Tomate", 5, 20)
produto6 = Produto("Batata", 3, 50)
banco_dados.produtos.inserir_produto(produto1)
banco_dados.produtos.inserir_produto(produto2)
banco_dados.produtos.inserir_produto(produto3)
banco_dados.produtos.inserir_produto(produto4)
banco_dados.produtos.inserir_produto(produto5)
banco_dados.produtos.inserir_produto(produto6)
# Adicionar clientes iniciais
cliente1 = PessoaFisica("João", "842.497.200-71", "Rua das Rosas 75")
cliente2 = PessoaFisica("Maria", "689.423.780-80", "Servidão dos Deuses 25")
cliente3 = PessoaJuridica("Empresa XYZ", "80.618.215/0001-00", "Servidão das Deusas 50")
banco_dados.pessoas.inserir_cliente(cliente1)
banco_dados.pessoas.inserir_cliente(cliente2)
banco_dados.pessoas.inserir_cliente(cliente3)
# Adicionar funcionários iniciais
funcionario1 = Funcionario("Danrley", "133.696.890-73", "Servidão dos Anjos 100")
funcionario2 = Funcionario("Vinicius", "727.524.910-34", "Servidão dos Arcanjos 125")
banco_dados.pessoas.inserir_funcionario(funcionario1)
banco_dados.pessoas.inserir_funcionario(funcionario2)

menu.executar()
