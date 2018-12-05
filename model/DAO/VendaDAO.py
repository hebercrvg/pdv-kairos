from model.DTO.VendaDTO import VendaDTO
from database.conexaoBanco import ConexaoBanco

class VendaDAO:
    def cadastrar_venda_avista(codcli, valorvenda, valorpago):
        conn = ConexaoBanco.get_conexao()
        query = ("INSERT INTO VENDA(CODCLI, VALORVENDA, VALORPAGO) VALUES({}, {}, {})".format(codcli, valorvenda, valorpago))
        conn.execute(query)
        conn.commit()
        conn.close()

    def cadastrar_venda_aprazo(codcli, valorvenda, valorpago):
        conn = ConexaoBanco.get_conexao()
        query = ("INSERT INTO VENDA(CODCLI, VALORVENDA, VALORPAGO) VALUES({}, {}, {})".format(codcli, valorvenda, valorpago))
        conn.execute(query)
        conn.commit()
        conn.close()

    def pesquisar_todos_devedores():
        conn = ConexaoBanco.get_conexao()
        query = ("""SELECT V.CODVENDA, C.CODCLI, C.NOME, strftime('%d/%m/%Y', V.dtvenda) AS 'DATA VENDA',
                 V.VALORVENDA, V.VALORPAGO, SUM(V.VALORVENDA-V.VALORPAGO) AS 'DIVIDA'
                 FROM CLIENTE C
                 INNER JOIN VENDA V
                 ON C.CODCLI = V.CODCLI
                 WHERE V.VALORPAGO < V.VALORVENDA 
                 GROUP BY V.CODCLI
                 ORDER BY C.NOME ASC""")
        result = conn.execute(query)
        return result

    def pesquisar_devedor(nome):
        conn = ConexaoBanco.get_conexao()
        query = ("SELECT V.CODVENDA, C.CODCLI, C.NOME, strftime('%d/%m/%Y', V.dtvenda),"
                 "V.VALORVENDA, V.VALORPAGO, SUM(V.VALORVENDA-V.VALORPAGO) AS 'DIVIDA' \n"
                 "FROM CLIENTE C \n"
                 "INNER JOIN VENDA V \n"
                 "ON C.CODCLI = V.CODCLI \n"
                 "WHERE V.VALORPAGO < V.VALORVENDA \n"
                 "AND NOME LIKE '%{}%' \n"
                 "AND C.CODCLI = V.CODCLI \n"
                 "GROUP BY V.CODCLI".format(nome))
        result = conn.execute(query)
        return result

    def lancar_credito_divida(codvenda, credito):
        conn = ConexaoBanco.get_conexao()
        query = ("UPDATE VENDA SET VALORPAGO = {} WHERE CODVENDA = {}".format(credito, codvenda))
        conn.execute(query)
        conn.commit()
        conn.close()

