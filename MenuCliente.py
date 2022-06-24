
import verificarcpf


class Usuario:

    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf




class InterfaceU:
    usuarios = []


    def cadastrar_usuarios(self):
        nome = input('Nome do Usuário:\n')
        for x in nome:
            if x.isalpha() or x == ' ':
                continue
            else:
                print("Erro! Por favor, tente novamente.")
            nome = input('Nome do Usuário:\n')

        cpf = input ('CPF (Apenas números):\n')
        while True:
            cpfs = cpf
            cpf = verificarcpf.cpf_valido(cpf)
            if cpf == True:
                cpf = cpfs
                break
            else:
                print('CPF Inválido!')
                cpf = input('CPF:')
        self.usuarios.append(Usuario(nome, cpf))




        print('Usuário adicionado com sucesso!')


    def listar_usuarios(self):
        for i, usuario in enumerate(self.usuarios):
            print("Lista de Usuários:")
            print(i, '[', usuario.nome, '-',usuario.cpf, ']')


    def loop(self):
        global response
        while True:
            cmd = input('''
                   [1] Cadastrar Usuário
                   [2] Listar Usuários
                   [4] Voltar.
                   O que deseja fazer?:
''')
            if cmd == '2':
                self.listar_usuarios()
            elif cmd == '1':
                self.cadastrar_usuarios()
            elif cmd == '4':
                break
            else:
                print('Inválido!')
                continue





if __name__ == '__main__':
    interfaceu = InterfaceU()
    interfaceu.loop()