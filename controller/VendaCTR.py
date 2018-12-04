from model.DAO.VendaDAO import VendaDAO
from model.DTO.VendaDTO import VendaDTO
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon, QFont

class VendaCTR:
    def Cadastrar_Venda_Avista(codcli, valorvenda, valorpago, troco):

        vendaDTO = VendaDTO
        vendaDTO.codcli = codcli
        vendaDTO.valorvenda = valorvenda
        vendaDTO.valorpago = valorpago
        vendaDAO = VendaDAO
        if (troco > 0):

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Question)
            msg.setWindowIcon(QIcon("question.png"))
            text = ("Deseja finalizar esta venda? \n"
                    "Valor da Venda: R$ {}".format(vendaDTO.valorvenda))
            msg.setText(text)
            font = QFont()
            font.setFamily("Arial")
            font.setPointSize(15)
            msg.setFont(font)
            msg.setWindowTitle("Confirmação")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            op = msg.exec_()
            if op == QMessageBox.Ok:
                vendaDAO.cadastrar_venda_avista(vendaDTO.codcli, vendaDTO.valorvenda, vendaDTO.valorpago)
                msg = QMessageBox(None)
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Sucesso!")
                msg.setWindowIcon(QIcon("greencheck.png"))
                font = QFont()
                font.setFamily("Arial")
                font.setPointSize(15)
                msg.setFont(font)
                text = ("Venda finalizada!\n"
                        "Valor Total da Venda: R$ {}\n"
                        "Valor Pago: R$ {}\n"
                        "Troco: R$ {:.2f}".format(vendaDTO.valorvenda, vendaDTO.valorpago, troco))
                msg.setText(text)

                msg.exec_()


            elif op == QMessageBox.Cancel:
                msg = QMessageBox(None)
                msg.setWindowIcon(QIcon("error.png"))
                msg.setWindowTitle("Cancelado")
                msg.setText("Venda cancelada.")
                font = QFont()
                font.setFamily("Arial")
                font.setPointSize(15)
                msg.setFont(font)
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Question)
            msg.setWindowIcon(QIcon("question.png"))
            text = ("Deseja finalizar esta venda? \n"
                        "Valor da Venda: R$ {}".format(vendaDTO.valorvenda))
            msg.setText(text)
            font = QFont()
            font.setFamily("Arial")
            font.setPointSize(15)
            msg.setFont(font)
            msg.setWindowTitle("Confirmação")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            op = msg.exec_()
            if op == QMessageBox.Ok:
                vendaDAO.cadastrar_venda_avista(vendaDTO.codcli, vendaDTO.valorvenda, vendaDTO.valorpago)
                msg = QMessageBox(None)
                msg.setWindowIcon(QIcon("greencheck.png"))
                msg.setWindowTitle("Sucesso!")
                msg.setIcon(QMessageBox.Information)
                font = QFont()
                font.setFamily("Arial")
                font.setPointSize(15)
                msg.setFont(font)
                text = ("Venda finalizada!")
                msg.setText(text)
                msg.exec_()


            elif op == QMessageBox.Cancel:
                msg = QMessageBox(None)
                msg.setWindowIcon(QIcon("error.png"))
                msg.setWindowTitle("Cancelado")
                msg.setText("Venda cancelada.")
                font = QFont()
                font.setFamily("Arial")
                font.setPointSize(15)
                msg.setFont(font)
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()

    def Cadastrar_Venda_Aprazo(codcli, valorvenda, valorpago):
        vendaDTO = VendaDTO
        vendaDAO = VendaDAO
        vendaDTO.codcli = codcli
        vendaDTO.valorvenda = valorvenda
        vendaDTO.valorpago = valorpago

        if (vendaDTO.valorpago == 0):
            msg = QMessageBox(None)
            msg.setWindowIcon(QIcon("question.png"))
            msg.setWindowTitle("Confirmação")
            font = QFont()
            font.setFamily("Arial")
            font.setPointSize(15)
            msg.setFont(font)
            text = ("Deseja finalizar a venda? \n"
                    "Valor Total da Venda: R$ {}".format(vendaDTO.valorvenda))
            msg.setText(text)
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            op = msg.exec_()

            if (op == QMessageBox.Ok):
                vendaDAO.cadastrar_venda_aprazo(vendaDTO.codcli, vendaDTO.valorvenda, vendaDTO.valorpago)
                msg = QMessageBox(None)
                msg.setWindowIcon(QIcon("greencheck.png"))
                msg.setWindowTitle("Sucesso!")
                msg.setIcon(QMessageBox.Information)
                text = ("Venda finalizada! \n"
                        "Total a pagar a prazo: R$ {}".format(vendaDTO.valorvenda))
                font = QFont()
                font.setFamily("Arial")
                font.setPointSize(15)
                msg.setFont(font)
                msg.setText(text)
                msg.exec_()


            elif (op == QMessageBox.Cancel):
                msg = QMessageBox(None)
                msg.setWindowIcon(QIcon("error.png"))
                msg.setWindowTitle("Cancelado")
                msg.setText("Venda cancelada.")
                font = QFont()
                font.setFamily("Arial")
                font.setPointSize(15)
                msg.setFont(font)
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()

        elif (vendaDTO.valorpago > 0):
            if (vendaDTO.valorpago >= vendaDTO.valorvenda):
                msg = QMessageBox(None)
                msg.setWindowIcon(QIcon("error.png"))
                msg.setWindowTitle("Erro")
                msg.setText("Na venda A PRAZO o valor pago não pode ser maior ou igual o valor da venda. Selecione venda À VISTA.")
                font = QFont()
                font.setFamily("Arial")
                font.setPointSize(15)
                msg.setFont(font)
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()

            else:
                restante = (vendaDTO.valorvenda - vendaDTO.valorpago)
                msg = QMessageBox(None)
                msg.setWindowIcon(QIcon("question.png"))
                msg.setWindowTitle("Confirmação")
                text = ("Deseja finalizar a venda? \n"
                        "Valor Total da Venda: R$ {} \n"
                        "Valor Total Pago: R$ {}".format(vendaDTO.valorvenda, vendaDTO.valorpago))
                msg.setText(text)
                font = QFont()
                font.setFamily("Arial")
                font.setPointSize(15)
                msg.setFont(font)
                msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                op = msg.exec_()

                if op == QMessageBox.Ok:
                    vendaDAO.cadastrar_venda_aprazo(vendaDTO.codcli, vendaDTO.valorvenda, vendaDTO.valorpago)
                    msg = QMessageBox(None)
                    msg.setWindowIcon(QIcon("greencheck.png"))
                    msg.setWindowTitle("Sucesso!")
                    msg.setIcon(QMessageBox.Information)
                    text = ("Venda finalizada! \n"
                            "Total a pagar a prazo: R$ {}".format(restante))
                    font = QFont()
                    font.setFamily("Arial")
                    font.setPointSize(15)
                    msg.setFont(font)
                    msg.setText(text)
                    msg.exec_()

                elif op == QMessageBox.Cancel:
                    msg = QMessageBox(None)
                    font = QFont()
                    font.setFamily("Arial")
                    font.setPointSize(15)
                    msg.setFont(font)
                    msg.setWindowIcon(QIcon("error.png"))
                    msg.setWindowTitle("Cancelado")
                    msg.setText("Venda cancelada.")
                    msg.setIcon(QMessageBox.Critical)
                    msg.exec_()

    def pesquisar_todos_devedores():
        vendaDAO = VendaDAO
        result = vendaDAO.pesquisar_todos_devedores()
        return result

    def pesquisar_devedor(nome):
        vendaDAO = VendaDAO
        result = vendaDAO.pesquisar_devedor(nome)
        return result

    def lancar_credito(codvenda, valorvenda, valorpago, credito):
        vendaDAO = VendaDAO

        dividarestante = (credito+valorpago)-valorvenda

        msg = QMessageBox(None)
        msg.setWindowIcon(QIcon("question.png"))
        msg.setWindowTitle("Confirmação")
        text = ("Deseja lancar o crédito? \n"
                "Valor Total da Venda: R$ {} \n"
                "Valor Total Pago: R$ {} \n"
                "Crédito a ser lançado: R$ {} ".format(valorvenda, valorpago, credito))
        msg.setText(text)
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        msg.setFont(font)
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        op = msg.exec_()

        if (op == QMessageBox.Ok):
            if (valorpago == 0 ):
                vendaDAO.lancar_credito_divida(codvenda, credito)
                msg = QMessageBox(None)
                msg.setWindowIcon(QIcon("greencheck.png"))
                msg.setWindowTitle("Sucesso!")
                msg.setIcon(QMessageBox.Information)
                text = ("Crédito lançado! \n"
                        "Dívida restante: R$ {:.2f}".format(dividarestante))
                font = QFont()
                font.setFamily("Arial")
                font.setPointSize(15)
                msg.setFont(font)
                msg.setText(text)
                msg.exec_()
            elif (valorpago != 0):
                creditofinal = valorpago+credito
                vendaDAO.lancar_credito_divida(codvenda, creditofinal)
                msg = QMessageBox(None)
                msg.setWindowIcon(QIcon("greencheck.png"))
                msg.setWindowTitle("Sucesso!")
                msg.setIcon(QMessageBox.Information)
                text = ("Crédito lançado! \n"
                        "Dívida restante: R$ {:.2f}".format(dividarestante))
                font = QFont()
                font.setFamily("Arial")
                font.setPointSize(15)
                msg.setFont(font)
                msg.setText(text)
                msg.exec_()


        elif (op == QMessageBox.Cancel):
            msg = QMessageBox(None)
            font = QFont()
            font.setFamily("Arial")
            font.setPointSize(15)
            msg.setFont(font)
            msg.setWindowIcon(QIcon("error.png"))
            msg.setWindowTitle("Cancelado")
            msg.setText("Lançamento cancelado.")
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()