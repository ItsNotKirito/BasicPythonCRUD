

class Produto:

    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo

    def mudar_codigo(self, codigo_antigo, codigo_novo):
        if self.codigo == codigo_antigo:
            self.codigo = codigo_novo
            return True  # Sucesso
        else:
            return False  # Código de produto n confere

class Interface:

    produtos = []

    def cadastrar_produtos(self):
        nome = input('Nome do Produto?\n')
        codigo = input('Código de Produto\n')

        self.produtos.append(Produto(nome, codigo))
        print('Produto adicionado com sucesso!')

    def listar_produtos(self):
        for i, produto in enumerate(self.produtos):
            print("Lista de Produtos:")
            print(i, '[',produto.nome,']')


    def mudar_codigo(self):
        numero_produto = input('Qual é o número de listagem do produto?')
        numero_produto = int(numero_produto)

        codigo_antigo = input('Qual é o código Atual?\n')
        codigo_novo = input('Digite o novo código de produto.\n')
        sucesso = self.produtos[numero_produto].mudar_codigo(codigo_antigo, codigo_novo)

        if sucesso:
            print('Alteração realizada com sucesso.')
        else:
            print('Erro')


    def loop(self):
        global response
        while True:
            cmd = input('''
                   [1] Listar Produtos
                   [2] Cadastrar Produto
                   [3] Mudar Codigo de Produto
                   [4] Voltar.
                   O que deseja fazer?:
''')
            if cmd == '1':
                self.listar_produtos()
            elif cmd == '2':
                self.cadastrar_produtos()
            elif cmd == '3':
                self.mudar_codigo()
            elif cmd == '4':
                break
            else:
                print('Inválido')
                continue


if __name__ == '__main__':
    interface = Interface()
    interface.loop()