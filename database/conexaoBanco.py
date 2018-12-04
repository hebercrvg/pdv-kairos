import sqlite3

class ConexaoBanco:
    def get_conexao():
        conn = sqlite3.connect("pdvkairosBD.db")
        return conn