from model.DTO.UsuarioDTO import UsuarioDTO
from model.DAO.UsuarioDAO import UsuarioDAO
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon

class UsuarioCTR:
    def Inserir_usuario(usuario, senha):
        usuarioDAO = UsuarioDAO
        usuarioDTO = UsuarioDTO
        usuarioDTO.usuario = usuario
        usuarioDTO.senha = senha
        usuarioDAO.inserir_usuario(usuarioDTO.usuario, usuarioDTO.senha)

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

