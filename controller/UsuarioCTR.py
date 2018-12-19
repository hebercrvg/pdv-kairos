from model.DTO.UsuarioDTO import UsuarioDTO
from model.DAO.UsuarioDAO import UsuarioDAO
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon

class UsuarioCTR:
    def inserir_usuario(usuario, senha):
        usuarioDAO = UsuarioDAO
        usuarioDTO = UsuarioDTO
        usuarioDTO.usuario = usuario
        usuarioDTO.senha = senha
        dlg = QMessageBox(None)
        dlg.setWindowIcon(QIcon("question.png"))
        dlg.setIcon(QMessageBox.Question)
        dlg.setWindowTitle("Confirmação")
        dlg.setText("Deseja cadastrar o usuário?")
        dlg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        op = dlg.exec_()
        if op == QMessageBox.Ok:
            usuarioDAO.inserir_usuario(usuarioDTO.usuario, usuarioDTO.senha)
            dlg = QMessageBox(None)
            dlg.setWindowIcon(QIcon("greencheck.png"))
            dlg.setIcon(QMessageBox.Information)
            dlg.setWindowTitle("Sucesso")
            dlg.setText("Usuário cadastrado com sucesso.")
            dlg.exec_()
        if op == QMessageBox.Cancel:
            dlg = QMessageBox(None)
            dlg.setWindowIcon(QIcon("error.png"))
            dlg.setIcon(QMessageBox.Information)
            dlg.setWindowTitle("Cancelado")
            dlg.setText("Cadastro cancelado!")
            dlg.exec_()


    def autentica_usuario(usuario, senha):
        try:
            usuarioDAO = UsuarioDAO
            senhabanco = usuarioDAO.get_senha(usuario)
            if (senha == senhabanco):
                return True

            elif (senha != senhabanco):
                return False
        except:
            msg = QMessageBox(None)
            msg.setWindowTitle("Erro")
            msg.setWindowIcon(QIcon("key.png"))
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Usuário inexistente.")
            msg.exec_()

    def pesquisa_todos_usuarios():
        result = UsuarioDAO.pesquisar_todos_usuario()
        return result

    def pesquisa_usuario(usuario):
        usuarioDAO = UsuarioDAO
        result = usuarioDAO.pesquisar_usuario(usuario)
        return result

    def alterar_usuario(codusuario, usuario, senha):

        usuarioDAO = UsuarioDAO
        usuarioDTO = UsuarioDTO
        usuarioDTO.usuario = usuario
        usuarioDTO.senha = senha
        if ((usuarioDTO.usuario != '') and (usuarioDTO.senha != '')):
            dlg = QMessageBox(None)
            dlg.setWindowIcon(QIcon("question.png"))
            dlg.setIcon(QMessageBox.Question)
            dlg.setWindowTitle("Confirmação")
            dlg.setText("Deseja alterar o usuário?")
            dlg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            op = dlg.exec_()
            if op == QMessageBox.Ok:
                usuarioDAO.alterar_usuario(codusuario, usuarioDTO.usuario, usuarioDTO.senha)
                dlg = QMessageBox(None)
                dlg.setWindowIcon(QIcon("greencheck.png"))
                dlg.setIcon(QMessageBox.Information)
                dlg.setWindowTitle("Sucesso")
                dlg.setText("Usuário alterado com sucesso.")
                dlg.exec_()
            if op == QMessageBox.Cancel:
                dlg = QMessageBox(None)
                dlg.setWindowIcon(QIcon("error.png"))
                dlg.setIcon(QMessageBox.Information)
                dlg.setWindowTitle("Cancelado")
                dlg.setText("Alteração cancelada!")
                dlg.exec_()

    def excluir_usuario(codusuario, usuario):
        usuarioDAO = UsuarioDAO
        dlg = QMessageBox(None)
        dlg.setWindowTitle("Confirmação")
        dlg.setWindowIcon(QIcon("question.png"))
        dlg.setIcon(QMessageBox.Question)
        dlg.setText("Deseja excluir o usuário {} ?".format(usuario))
        dlg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        op = dlg.exec_()
        if (op == QMessageBox.Ok):
            usuarioDAO.excluir_usuario(codusuario)
            dlg = QMessageBox(None)
            dlg.setWindowIcon(QIcon("greencheck.png"))
            dlg.setIcon(QMessageBox.Information)
            dlg.setWindowTitle("Sucesso")
            dlg.setText("Usuário excluído com sucesso.")
            dlg.exec_()
        elif (op == QMessageBox.Cancel):
            dlg = QMessageBox(None)
            dlg.setWindowIcon(QIcon("error.png"))
            dlg.setIcon(QMessageBox.Information)
            dlg.setWindowTitle("Cancelado")
            dlg.setText("Exclusão cancelada!")
            dlg.exec_()