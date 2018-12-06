from model.DAO.ClienteDAO import ClienteDAO
from model.DTO.ClienteDTO import ClienteDTO
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtGui
from PyQt5.QtGui import QFont, QIcon

class ClienteCTR:

    def alterar_cliente(codcli, nome, telefone):


        try:
            clienteDTO = ClienteDTO
            clienteDAO = ClienteDAO
            clienteDTO.nome = nome
            clienteDTO.telefone = telefone
            Codcli = codcli
            aux = 0

            if (clienteDTO.nome == ''):
                aux += 1
                msg = ("Nome inválido. \n"
                       "{}".format(clienteDTO.nome))
                dlg = QMessageBox(None)
                dlg.setWindowTitle("Erro")
                font = QFont()
                font.setFamily("Arial")
                font.setPointSize(15)
                dlg.setFont(font)
                dlg.setIcon(QMessageBox.Critical)
                dlg.setWindowIcon(QtGui.QIcon("error.png"))
                dlg.setText(msg)
                dlg.exec_()

            if (clienteDTO.telefone == '') or ((len(clienteDTO.telefone)) < 13):
                aux += 1
                msg = ("Telefone inválido. \n"
                       "Por favor informe um telefone válido.")
                dlg = QMessageBox(None)
                dlg.setWindowTitle("Erro")
                dlg.setIcon(QMessageBox.Critical)
                font = QFont()
                font.setFamily("Arial")
                font.setPointSize(15)
                dlg.setFont(font)
                dlg.setWindowIcon(QtGui.QIcon("error.png"))
                dlg.setText(msg)
                dlg.exec_()

            if (aux==0):
                clienteDAO.alterar_cliente(Codcli, clienteDTO.nome, clienteDTO.telefone)
                dlg = QMessageBox(None)
                dlg.setWindowTitle("Sucesso")
                dlg.setIcon(QMessageBox.Information)
                font = QFont()
                font.setFamily("Arial")
                font.setPointSize(15)
                dlg.setFont(font)
                dlg.setWindowIcon(QtGui.QIcon("greencheck.png"))
                dlg.setText("Cliente alterado com sucesso.")
                dlg.setStandardButtons(QMessageBox.Ok)
                dlg.exec_()
        except:
            dlg = QMessageBox(None)
            dlg.setWindowTitle("Exclusão")
            dlg.setIcon(QMessageBox.Information)
            dlg.setWindowIcon(QIcon("greencheck.png"))
            font = QFont()
            font.setFamily("Arial")
            font.setPointSize(15)
            dlg.setFont(font)
            dlg.setText("Cliente excluído com sucesso.")
            dlg.exec_()



    def Excluir_Cliente(codcli, nome):
        clienteDAO = ClienteDAO
        Codcli = codcli
        dlg = QMessageBox(None)
        dlg.setWindowIcon(QIcon("question.png"))
        dlg.setWindowTitle("Confirmação")
        dlg.setIcon(QMessageBox.Question)
        font = QFont()
        font.setFamily(("Arial"))
        font.setPointSize(15)
        dlg.setFont(font)
        text = ("Deseja excluir o cliente: \n"
                "{}?".format(nome))
        dlg.setText(text)
        dlg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        op = dlg.exec_()
        if (op == QMessageBox.Ok):
            clienteDAO.excluir_cliente(Codcli)
            dlg = QMessageBox(None)
            dlg.setWindowTitle("Exclusão")
            dlg.setIcon(QMessageBox.Information)
            dlg.setWindowIcon(QIcon("greencheck.png"))
            font = QFont()
            font.setFamily("Arial")
            font.setPointSize(15)
            dlg.setFont(font)
            dlg.setText("Cliente excluído com sucesso.")
            dlg.exec_()
        elif (op == QMessageBox.Cancel):
            dlg = QMessageBox(None)
            dlg.setWindowTitle("Cancelado")
            dlg.setWindowIcon(QIcon("error.png"))
            dlg.setIcon(QMessageBox.Critical)
            font = QFont()
            font.setFamily('Arial')
            font.setPointSize(15)
            dlg.setFont(font)
            text = ("Exclusão cancelada.")
            dlg.setText(text)
            dlg.exec_()



    def Cadastrar_Cliente(nome, telefone):
        clienteDTO = ClienteDTO
        clienteDAO = ClienteDAO
        aux = 0

        clienteDTO.nome = nome
        clienteDTO.telefone = telefone

        if clienteDTO.nome == '':
            aux += 1
            msg = ("Nome inválido. \n "
                   "{}".format(clienteDTO.nome))
            dlg = QMessageBox(None)
            dlg.setWindowTitle("Erro")
            dlg.setIcon(QMessageBox.Critical)
            font = QFont()
            font.setFamily("Arial")
            font.setPointSize(15)
            dlg.setFont(font)
            dlg.setWindowIcon(QtGui.QIcon("error.png"))
            dlg.setText(msg)

            dlg.exec_()

        if (clienteDTO.telefone == '') or ((len(clienteDTO.telefone)) < 13):
            aux += 1
            msg = ("Telefone inválido. \n"
                   "{}".format(clienteDTO.telefone))
            dlg = QMessageBox(None)
            dlg.setWindowTitle("Erro")
            dlg.setIcon(QMessageBox.Critical)
            font = QFont()
            font.setFamily("Arial")
            font.setPointSize(15)
            dlg.setFont(font)
            dlg.setWindowIcon(QtGui.QIcon("error.png"))
            dlg.setText(msg)
            dlg.exec_()

        if (aux==0):
            clienteDAO.cadastrar_cliente(clienteDTO.nome, clienteDTO.telefone)
            dlg = QMessageBox(None)
            dlg.setWindowTitle("Sucesso")
            dlg.setIcon(QMessageBox.Information)
            dlg.setWindowIcon(QtGui.QIcon("greencheck.png"))
            dlg.setText("Cliente cadastrado com sucesso.")
            font = QFont()
            font.setFamily("Arial")
            font.setPointSize(15)
            dlg.setFont(font)
            dlg.exec_()

    def Pesquisar_Cliente(nome):
        result = ClienteDAO.pesquisar_cliente(nome)
        return result

    def Pesquisar_Todos_Clientes():
        result = ClienteDAO.pesquisar_todos_clientes()
        return result

