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
        try:
            opcaoSelecionada = int(opcaoSelecionada)
        except ValueError:
            print("A opção escolhida não é válida!")
            print("Tente novamente.")
            return self.selecionarOpcao(opcoesValidas)
        
        # Confere se o que o usuário digitou é uma das opções válidas.
        if opcaoSelecionada not in opcoesValidas:
            print("A opção escolhida não é válida!")
            print("Tente novamente.")
            return self.selecionarOpcao(opcoesValidas)
        
        return opcaoSelecionada
    
    # Exibe as opções do menu.
    def menuPrincipal(self):
        print("1 - Mostrar fichas de personagem já cadastradas.")
        print("2 - Cadastrar a ficha de um novo personagem.")
        print("3 - Fechar.")
        print("_________________________________")
        print("")

    def listaPersonagens(self):
        print("__________________________________")
        print("|                                |")
        print("|   PERSONAGENS JÁ CADASTRADOS   |")
        print("|________________________________|")
        print("")

        fichas = self.banco.buscarDadosCadastrados('fichas')
        for fichas in fichas:
            id, nome, classe, nivel, raca, antecedente, alinhamento, experiencia, jogador, forca, destreza, constituicao, inteligencia, sabedoria, carisma = fichas
            print(f"Ficha {id} | {nome}")
            print("______________________________")
            print("")
            print("Aperte ENTER para prosseguir.")


    def solicitarDados(self, legenda, tipo = 'texto', permiteNulo = False):
        valor = input(legenda)

        if valor == "" and not permiteNulo:
            print("Insira um valor válido.")
            return self.solicitarDados(legenda, tipo, permiteNulo)
        
        elif valor == "" and permiteNulo:
            return valor
        
        if tipo == 'numero':
            try:
                valor = int(valor)
            except ValueError:
                print("O valor inserido não é válido!")
                return self.solicitarDados(legenda, tipo, permiteNulo)
        return valor


    def cadastrarPersonagem(self):
        print("____________________________________________________")
        print("|                                                  |")
        print("|             Insira os dados do personagem.       |")
        print("| (Campos com * são de preenchimento OBRIGATÓRIO.) |")
        print("|__________________________________________________|")
        print("")

        nome = self.solicitarDados("| Nome do personagem*: ", 'texto', False)
        classe = self.solicitarDados("| Classe*: ", 'texto', False)
        nivel = self.solicitarDados("| Nível*: ", 'numero', False)
        raca = self.solicitarDados("| Raça*: ", 'texto', False)
        antecedente = self.solicitarDados("| Antecedente*: ", 'texto', False)
        alinhamento = self.solicitarDados("| Alinhamento: ", 'texto', True)
        experiencia = self.solicitarDados("| Pontos de Experiência: ", 'numero', True)
        jogador = self.solicitarDados("| Nome do Jogador*: ", 'texto', False)
        print("|_________________________________________________________________________|")
        print("")
        print("_____________________")
        print("|                   |")
        print("|     ATRIBUTOS     |")
        print("|___________________|")
        print("")
        forca = self.solicitarDados("| Força: ", 'numero', True)
        destreza = self.solicitarDados("| Destreza: ", 'numero', True)
        constituicao = self.solicitarDados("| Constituição: ", 'numero', True)
        inteligencia = self.solicitarDados("| Inteligência: ", 'numero', True)
        sabedoria = self.solicitarDados("| Sabedoria: ", 'numero', True)
        carisma = self.solicitarDados("| Carisma: ", 'numero', True)
        print("")

        valores = {
            "nome": nome,
            "classe": classe,
            "nivel": nivel,
            "raca": raca,
            "antecedente": antecedente,
            "alinhamento": alinhamento,
            "experiencia": experiencia,
            "jogador": jogador,
            "forca": forca,
            "destreza": destreza,
            "constituicao": constituicao,
            "inteligencia": inteligencia,
            "sabedoria": sabedoria,
            "carisma": carisma
        }

        self.banco.inserirDados('fichas', 'valores')


