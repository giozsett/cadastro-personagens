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
                raça TEXT NOT NULL,
                alinhamento TEXT NULL,
                experiencia INTEGER NULL,
                jogador TEXT NOT NULL,
            )
        """)
