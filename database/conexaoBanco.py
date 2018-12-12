import sqlite3

class ConexaoBanco:
    def get_conexao():
        conn = sqlite3.connect(r"C:\dev\pdv-kairos\view\pdvkairosBD.db")
        return conn