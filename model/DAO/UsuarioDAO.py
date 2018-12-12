# -*- encoding:utf-8 -*-
from database.conexaoBanco import ConexaoBanco
import bcrypt

class UsuarioDAO:
    def inserir_usuario(usuario, senha):
        conn = ConexaoBanco.get_conexao()
        query = (""" INSERT INTO USUARIO(USUARIO, SENHA) VALUES("{}", "{}")
                """.format(usuario, senha))
        conn.execute(query)
        conn.commit()
        conn.close()

    def get_senha(usuario):

        conn = ConexaoBanco.get_conexao()
        query = ("SELECT SENHA FROM USUARIO WHERE USUARIO = '{}'".format(usuario))
        senha = conn.execute(query).fetchone()
        return senha[0]




