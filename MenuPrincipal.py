import csv
import MenuProduto
import MenuCliente
import verificarcpf
import sqlite3
from subprocess import call
from tkinter import *

class UI:
 def loop(self):
        global response
        while True:
            cmd = input('''
                   Central de Cadastros.
                    
                   [1] Menu de Produtos
                   [2] Menu de Clientes
                   [3] Sair.
                   O que deseja fazer?:
''')
            if cmd == '1':
                call(["python", "MenuProduto.py"])
            elif cmd == '2':
                call(["python", "MenuCliente.py"])
            elif cmd == '3':
                break
            else:
                print('Inválido')
                continue

if __name__ == '__main__':
    interface = UI()
    interface.loop()