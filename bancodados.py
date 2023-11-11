# Banco de dados.
import sqlite3

class BancoDados:
    def __init__(self, banco_dados):
        self.conectarBanco(banco_dados)


    # Conecta o arquivo de banco de dados.
    def conectarBanco(self, banco_dados):
        self.banco = sqlite3.connect(banco_dados)
        self.cursor = self.banco.cursor()
        self.criarFichaPersonagem()

    # Dados da ficha.
    def criarFichaPersonagem(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS personagens(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                classe TEXT NOT NULL,
                nivel INTEGER NOT NULL,
                raca TEXT NOT NULL,
                antecedente TEXT NOT NULL,
                alinhamento TEXT NULL,
                experiencia INTEGER NULL,
                jogador TEXT NOT NULL,
                forca INTEGER NULL,
                destreza INTEGER NULL,
                constituicao INTEGER NULL,
                inteligencia INTEGER NULL,
                sabedoria INTEGER NULL,
                carisma INTEGER NULL
            )
        """)


    # Busca as fichas já cadastradas para serem exibidas ao usuário.
    def buscarDadosCadastrados (self, tabela, campos = '*'):
        sql = f"SELECT {campos} FROM {tabela}"
        self.cursor.execute(sql)
        dados = self.cursor.fetchall()
        return dados

    # Inserindo os dados nos campos das fichas.
    def inserirDados(self, valores, tabela):
        colunas = ', '.join(valores.keys())
        placeholders = ', '.join(['?'] * len(valores))
        sql = f"INSERT INTO {tabela} ({colunas}) VALUES ({placeholders})"

        self.cursor.execute(sql, tuple(valores.values()))
        self.banco.commit()

        if self.cursor.lastrowid:
            print(f"Sucesso ao cadastrar {tabela}!")
            return True
        else:
            print("Ocorreu um erro durante o cadastro.")
            return False