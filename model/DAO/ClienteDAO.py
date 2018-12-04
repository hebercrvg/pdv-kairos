from database.conexaoBanco import ConexaoBanco
import sqlite3

class ClienteDAO:
    def cadastrar_cliente(nome, telefone):
        conn = ConexaoBanco.get_conexao()
        query = "INSERT INTO CLIENTE(NOME, TELEFONE) VALUES ('{}','{}')".format(nome, telefone)
        conn.execute(query)
        conn.commit()
        conn.close()

    def alterar_cliente(codcli, nome, telefone):
        conn = ConexaoBanco.get_conexao()
        query = ("UPDATE CLIENTE SET NOME = '{}' WHERE CODCLI = {}".format(nome, codcli))
        query2 = (" UPDATE CLIENTE SET TELEFONE = '{}' WHERE CODCLI = {}".format(telefone, codcli))
        conn.execute(query)
        conn.execute(query2)
        conn.commit()
        conn.close()

    def excluir_cliente(codcli):
        conn = ConexaoBanco.get_conexao()
        query = ("DELETE FROM CLIENTE WHERE CODCLI = {}".format(codcli))
        conn.execute(query)
        conn.commit()
        conn.close()

    def pesquisar_cliente(nome):
        conn = ConexaoBanco.get_conexao()
        query = ("SELECT * FROM CLIENTE WHERE NOME LIKE '%{}%' ".format(nome))
        result = conn.execute(query)
        return result

    def pesquisar_todos_clientes():
        conn = ConexaoBanco.get_conexao()
        query = "SELECT * FROM CLIENTE"
        result = conn.execute(query)
        return result

    def pesquisar_nomecliente_todos_lista():
        conn = ConexaoBanco.get_conexao()
        conn.row_factory = lambda cursor, row: row[0]
        query = ('SELECT NOME FROM CLIENTE ORDER BY NOME ASC')
        result = conn.execute(query).fetchall()
        return result

    def get_codcli_por_nome(nome):
        conn = ConexaoBanco.get_conexao()
        conn.row_factory = lambda cursor, row: row[0]
        query = ("SELECT CODCLI FROM CLIENTE WHERE NOME = '{}'".format(nome))
        result = conn.execute(query).fetchall()
        return result[0]


