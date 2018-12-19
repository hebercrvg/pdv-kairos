# -*- encoding:utf-8 -*-
from database.conexaoBanco import ConexaoBanco
from PyQt5.QtWidgets import QMessageBox
from PyQt5.Qt import QIcon

class UsuarioDAO:
    def inserir_usuario(usuario, senha):
        try:
            conn = ConexaoBanco.get_conexao()
            query = (""" INSERT INTO USUARIO(USUARIO, SENHA) VALUES("{}", "{}")
                    """.format(usuario, senha))
            conn.execute(query)
            conn.commit()
            conn.close()
        except:
            dlg = QMessageBox(None)
            dlg.setWindowIcon(QIcon("error.png"))
            dlg.setIcon(QMessageBox.Information)
            dlg.setWindowTitle("Cancelado")
            dlg.setText("Usuário já existente!")
            dlg.exec_()

    def get_senha(usuario):

        conn = ConexaoBanco.get_conexao()
        query = ("SELECT SENHA FROM USUARIO WHERE USUARIO = '{}'".format(usuario))
        senha = conn.execute(query).fetchone()
        return senha[0]

    def excluir_usuario(codusuario):
        conn = ConexaoBanco.get_conexao()
        query = ("DELETE FROM USUARIO WHERE CODUSUARIO = {}".format(codusuario))
        conn.execute(query)
        conn.commit()
        conn.close()

    def pesquisar_usuario(usuario):
        conn = ConexaoBanco.get_conexao()
        query = ("SELECT CODUSUARIO, USUARIO FROM USUARIO WHERE USUARIO LIKE '%{}%'".format(usuario))
        result = conn.execute(query)
        return result

    def pesquisar_todos_usuario():
        conn = ConexaoBanco.get_conexao()
        query = ("SELECT CODUSUARIO, USUARIO FROM USUARIO")
        result = conn.execute(query)
        return result

    def alterar_usuario(coduser, usuario, senha):
        conn = ConexaoBanco.get_conexao()
        query = ("UPDATE USUARIO SET USUARIO = '{}' WHERE CODUSUARIO = {};".format(usuario, coduser))
        query2 = ("UPDATE USUARIO SET SENHA = '{}' WHERE CODUSUARIO = {};".format(senha, coduser))
        conn.execute(query)
        conn.execute(query2)
        conn.commit()
        conn.close()

