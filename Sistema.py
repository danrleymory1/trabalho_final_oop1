"""
Falta corrigir o problema do CPF/CNPJ em que se inicia com '0', não consegue depois fazer a referencia
Falta adicionar tratamento de erros para o programa não dar erro durante a execução de int em str, etc
Melhorar o Menu para limpar a tela
Também vai faltar mais itens iniciais para vender.
Verificar se realmente o programa utiliza os conceitos que a professora trabalhou em sala
Além disso(duvida), não entendi o porque de aparecer para função dever ser tipo 'static'
Também verificar se é preciso o uso de set e get, pois não utilizei no programa
Depois das correções, eu faço o diagrama, só realmente não sei se utilizei: 
Agregação, Composição, Herança e/ou polimorfismo

Mas verifica aí, acredito que tem como deixar mais limpo o código kkk
"""""
# Menu Estoque Ok
# Menu Clientes Ok
# Menu Funcionário Ok
# Menu Vendas Ok
# Menu Relatório Ok

from BancodeDados import BancoDados
from Menu import Menu
from Produto import Produto
from Pessoa import PessoaFisica, PessoaJuridica, Funcionario


banco_dados = BancoDados()
menu = Menu(banco_dados)

# Adicionar produtos iniciais
produto1 = Produto("Arroz", 4.5, 10)
produto2 = Produto("Feijão", 5.0, 10)
produto3 = Produto("Macarrão", 3.5, 10)
produto4 = Produto("Oleo", 9, 10)
produto5 = Produto("Tomate", 5, 20)
produto6 = Produto("Batata", 3, 50)
banco_dados.adicionar_produto(produto1)
banco_dados.adicionar_produto(produto2)
banco_dados.adicionar_produto(produto3)
banco_dados.adicionar_produto(produto4)
banco_dados.adicionar_produto(produto5)
banco_dados.adicionar_produto(produto6)
# Adicionar clientes iniciais
cliente1 = PessoaFisica("João", 12345678944, "Rua das Rosas 75")
cliente2 = PessoaFisica("Maria", 12345678900, "Servidão dos Deuses 25")
cliente3 = PessoaJuridica("Empresa XYZ", 12345678900001, "Servidão das Deusas 50")
banco_dados.adicionar_cliente(cliente1)
banco_dados.adicionar_cliente(cliente2)
banco_dados.adicionar_cliente(cliente3)
# Adicionar funcionários iniciais
funcionario1 = Funcionario("Danrley", 98765432100, "Servidão dos Anjos 100")
funcionario2 = Funcionario("Vinicius", 87654321000, "Servidão dos Arcanjos 125")
banco_dados.adicionar_funcionario(funcionario1)
banco_dados.adicionar_funcionario(funcionario2)

menu.executar()
