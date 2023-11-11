# Interface do usuário.
from bancodados import BancoDados
import os

class Interface:
    def __init__(self):
        self.banco = BancoDados("CadastroPersonagens.db")


    # Criando o título principal.
    def titulo(self):
        print("_________________________________")
        print("|                               |")
        print("|      FICHA DE PERSONAGENS     |")
        print("|_______________________________|")
        print(" CAMPANHA: Início")
        print(" SISTEMA: D&D 5E")
        print("_________________________________")
        print("")


    # Criando a função do limpa tela.
    def limpaTela(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    # Opções do menu: cadastrar personagem e exibir lista de personagens.
    def selecionarOpcao(self, opcoesValidas = []):

        # O usuário precisa digitar alguma coisa para verificar se o que ele digitou é uma opção válida.
        opcaoSelecionada = input("Escolha uma opção: ")

        # Faz a verificação se algo foi digitado pelo usuário.
        if opcaoSelecionada == "":
            return self.selecionarOpcao(opcoesValidas)
        
        # Conversão da opção em números.