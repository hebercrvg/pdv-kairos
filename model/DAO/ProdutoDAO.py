from database.conexaoBanco import ConexaoBanco

class ProdutoDAO:

    def cadastrar_produto(descricao, tipo, preco):
        conn = ConexaoBanco.get_conexao()
        query = ("INSERT INTO PRODUTO(DESCRICAO, TIPO, PRECO) VALUES('{}', '{}', {})".format(descricao, tipo, preco))
        conn.execute(query)
        conn.commit()
        conn.close()

    def alterar_produto(codprod, descricao, tipo, preco):
        conn = ConexaoBanco.get_conexao()
        query = ("UPDATE PRODUTO SET DESCRICAO = '{}' WHERE CODPROD = {}".format(descricao, codprod))
        query2 = ("UPDATE PRODUTO SET TIPO = '{}' WHERE CODPROD = {}".format(tipo, codprod))
        query3 = ("UPDATE PRODUTO SET PRECO = {} WHERE CODPROD = {}".format(preco, codprod))
        conn.execute(query)
        conn.commit()
        conn.execute(query2)
        conn.commit()
        conn.execute(query3)
        conn.commit()
        conn.close()

    def excluir_produto(codprod):
        conn = ConexaoBanco.get_conexao()
        query = ("DELETE FROM PRODUTO WHERE CODPROD = {}".format(codprod))
        conn.execute(query)
        conn.commit()
        conn.close()

    def pesquisar_todos_produtos():
        conn = ConexaoBanco.get_conexao()
        query = ("SELECT * FROM PRODUTO")
        result = conn.execute(query)
        return result

    def pesquisar_descricao_todos_produtos_lista():
        conn = ConexaoBanco.get_conexao()
        conn.row_factory = lambda cursor, row: row[0]
        query = ('SELECT DESCRICAO FROM PRODUTO ORDER BY DESCRICAO ASC')
        result = conn.execute(query).fetchall()
        return result


    def pesquisar_produto(descricao):
        conn = ConexaoBanco.get_conexao()
        query = ("SELECT * FROM PRODUTO WHERE DESCRICAO LIKE '%{}%'".format(descricao))
        result = conn.execute(query)
        return result

    def get_cod_produto_por_descricao(descricao):
        conn = ConexaoBanco.get_conexao()
        conn.row_factory = lambda cursor, row: row[0]
        query = ("SELECT CODPROD FROM PRODUTO WHERE DESCRICAO = '{}'".format(descricao))
        result = conn.execute(query).fetchall()
        return result[0]

    def get_preco_produto(codprod):
        conn = ConexaoBanco.get_conexao()
        conn.row_factory = lambda cursor, row: row[0]
        query = ('SELECT PRECO FROM PRODUTO WHERE CODPROD = {}'.format(codprod))
        result = conn.execute(query).fetchall()
        return result[0]