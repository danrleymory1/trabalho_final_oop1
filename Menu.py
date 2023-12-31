class Menu:
    def __init__(self, banco_dados):
        self.banco_dados = banco_dados

    def limpar_tela(self):
        print("\033c\033[3J", end="")

    def exibir_menu_principal(self):
        print("---- Menu Principal ----")
        print("1 - Estoque")
        print("2 - Clientes")
        print("3 - Funcionários")
        print("4 - Vendas")
        print("5 - Relatório de Vendas")
        print("0 - Sair")

    def exibir_menu_estoque(self):
        print("---- Menu Estoque ----")
        print("1 - Cadastrar Produto")
        print("2 - Alterar Produto")
        print("3 - Alterar Quantidade")
        print("4 - Excluir Produto")
        print("5 - Exibir Estoque")
        print("0 - Voltar")

    def exibir_menu_clientes(self):
        print("---- Menu Clientes ----")
        print("1 - Exibir Clientes")
        print("2 - Consultar Cliente")
        print("3 - Cadastrar Cliente")
        print("4 - Alterar Cliente")
        print("5 - Excluir Cliente")
        print("0 - Voltar")

    def exibir_menu_funcionarios(self):
        print("---- Menu Funcionários ----")
        print("1 - Exibir Funcionários")
        print("2 - Consultar funcionário")
        print("3 - Cadastrar Funcionário")
        print("4 - Alterar Funcionário")
        print("5 - Excluir Funcionário")
        print("0 - Voltar")

    def exibir_menu_vendas(self):
        print("---- Menu Vendas ----")
        print("1 - Realizar Venda")
        print("0 - Voltar")

    def executar(self):
        while True:
            self.limpar_tela()
            self.exibir_menu_principal()
            opcao = input("Digite a opção desejada: ")

            if opcao == "1":
                self.executar_menu_estoque()
            elif opcao == "2":
                self.executar_menu_clientes()
            elif opcao == "3":
                self.executar_menu_funcionarios()
            elif opcao == "4":
                self.executar_menu_vendas()
            elif opcao == "5":
                self.banco_dados.vendas.exibir_total_vendas()
            elif opcao == "0":
                break
            else:
                print("Opção inválida.")

    def executar_menu_estoque(self):
        while True:
            self.limpar_tela()
            self.exibir_menu_estoque()
            opcao = input("Digite a opção desejada: ")

            if opcao == "1":
                self.banco_dados.produtos.cadastrar_produto()
            elif opcao == "2":
                self.banco_dados.produtos.alterar_produto()
            elif opcao == "3":
                self.banco_dados.produtos.alterar_estoque()
            elif opcao == "4":
                self.banco_dados.produtos.remover_produto()
            elif opcao == "5":
                self.limpar_tela()
                self.banco_dados.produtos.exibir_estoque()
                input("Pressione qualquer tecla para continuar.")
            elif opcao == "0":
                break
            else:
                print("Opção inválida.")

    def executar_menu_clientes(self):
        while True:
            self.limpar_tela()
            self.exibir_menu_clientes()
            opcao = input("Digite a opção desejada: ")

            if opcao == "1":
                self.banco_dados.pessoas.exibir_clientes()
            elif opcao == "2":
                self.banco_dados.pessoas.consultar_cliente()
            elif opcao == "3":
                self.banco_dados.pessoas.cadastrar_cliente()
            elif opcao == "4":
                self.banco_dados.pessoas.alterar_cliente()
            elif opcao == "5":
                self.banco_dados.pessoas.remover_cliente()
            elif opcao == "0":
                break
            else:
                print("Opção inválida.")

    def executar_menu_funcionarios(self):
        while True:
            self.limpar_tela()
            self.exibir_menu_funcionarios()
            opcao = input("Digite a opção desejada: ")

            if opcao == "1":
                self.banco_dados.pessoas.exibir_funcionarios()
            elif opcao == "2":
                self.banco_dados.pessoas.consultar_funcionario()
            elif opcao == "3":
                self.banco_dados.pessoas.cadastrar_funcionario()
            elif opcao == "4":
                self.banco_dados.pessoas.alterar_funcionario()
            elif opcao == "5":
                self.banco_dados.pessoas.remover_funcionario()
            elif opcao == "0":
                break
            else:
                print("Opção inválida.")

    def executar_menu_vendas(self):
        while True:
            self.limpar_tela()
            self.exibir_menu_vendas()
            opcao = input("Digite a opção desejada: ")

            if opcao == "1":
                self.banco_dados.vendas.realizar_venda()
            elif opcao == "0":
                break
            else:
                print("Opção inválida.")
