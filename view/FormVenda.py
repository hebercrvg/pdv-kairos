from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QAbstractItemView, QMessageBox
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from controller.ProdutoCTR import ProdutoCTR
from controller.VendaCTR import VendaCTR
from model.DAO.ProdutoDAO import ProdutoDAO
from model.DAO.ClienteDAO import ClienteDAO

class Ui_FormVenda(object):
    def click_btn_finalizar_venda(self):
        clienteDAO = ClienteDAO
        index = self.formapgtoComboBox.currentIndex()
        if (index == 0):
            nomecliente = self.clienteComboBox.currentText()
            codcli = int(clienteDAO.get_codcli_por_nome(nomecliente))
            valorvenda = self.totalvenda
            valorpago = self.valorPagodoubleSpinBox.value()
            if (valorpago < valorvenda):
                msg = QMessageBox(None)
                msg.setWindowIcon(QIcon("error.png"))
                msg.setWindowTitle("Erro")
                msg.setIcon(QMessageBox.Critical)
                text = ("Erro: O valor pago é menor que o valor da venda. \n"
                        "Para um pagamento parcial, selecione a forma de pagamento A PRAZO.")
                font = QFont()
                font.setFamily("Arial")
                font.setPointSize(15)
                msg.setFont(font)
                msg.setText(text)
                msg.exec_()
            else:
                troco = (valorpago-valorvenda)
                valorpago = valorpago-troco
                VendaCTR.Cadastrar_Venda_Avista(codcli, valorvenda, valorpago, troco)

        if (index == 1):
            nomecliente = self.clienteComboBox.currentText()
            codcli = int(clienteDAO.get_codcli_por_nome(nomecliente))
            valorvenda = self.totalvenda
            valorpago = self.valorPagodoubleSpinBox.value()
            VendaCTR.Cadastrar_Venda_Aprazo(codcli, valorvenda, valorpago)



    def click_btn_incluir(self):
        produto = self.produtoComboBox.currentText()
        qtde = self.qtdeSpinBox.value()
        codprod = ProdutoCTR.Get_codprod_por_descricao(produto)
        valorunit = ProdutoCTR.Get_preco_produto(codprod)

        item = QTableWidgetItem
        if (qtde == 0):
            msg = QMessageBox(None)
            msg.setWindowIcon(QIcon("error.png"))
            msg.setWindowTitle("Erro")
            msg.setIcon(QMessageBox.Critical)
            font = QFont()
            font.setFamily("Arial")
            font.setPointSize(15)
            msg.setFont(font)
            text = ("Erro: A quantidade mínima deve ser 1(um).")
            msg.setText(text)
            msg.exec_()

        elif (qtde > 0):
            valortotal = (valorunit * qtde)
            self.tableVenda.insertRow(0)
            self.tableVenda.setItem(0, 0, item(str(codprod)))
            self.tableVenda.setItem(0, 1, item(str(produto)))
            self.tableVenda.setItem(0, 2, item(str(qtde)))
            self.tableVenda.setItem(0, 3, item(str(valorunit)))
            self.tableVenda.setItem(0, 4, item(str(valortotal)))
            self.totalvenda += valortotal
            self.editTotal.setText(str(self.totalvenda))

    def click_btn_remover(self):
        linha = self.tableVenda.currentRow()
        valortotal = float(self.tableVenda.item(linha, 4).text())
        self.totalvenda = (self.totalvenda - valortotal)
        self.editTotal.setText(str(self.totalvenda))
        self.tableVenda.removeRow(linha)

    def preencher_produtos(self):
        produtoDAO = ProdutoDAO
        produtos = produtoDAO.pesquisar_descricao_todos_produtos_lista()
        return produtos

    def preencher_clientes(self):
        clienteDAO = ClienteDAO
        clientes = clienteDAO.pesquisar_nomecliente_todos_lista()
        return clientes

    def setupUi(self, FormVenda):
        self.totalvenda = 0.0
        FormVenda.setObjectName("FormVenda")
        FormVenda.resize(814, 600)
        font = QtGui.QFont()
        font.setPointSize(9)
        FormVenda.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("loja.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FormVenda.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(FormVenda)
        self.centralwidget.setObjectName("centralwidget")
        self.produtoComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.produtoComboBox.setGeometry(QtCore.QRect(100, 30, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.produtoComboBox.setFont(font)
        self.produtoComboBox.setObjectName("produtoComboBox")
        self.labelProduto = QtWidgets.QLabel(self.centralwidget)
        self.labelProduto.setGeometry(QtCore.QRect(40, 40, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelProduto.setFont(font)
        self.labelProduto.setObjectName("labelProduto")
        self.qtdeSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.qtdeSpinBox.setGeometry(QtCore.QRect(350, 30, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.qtdeSpinBox.setFont(font)
        self.qtdeSpinBox.setObjectName("qtdeSpinBox")
        self.tableVenda = QtWidgets.QTableWidget(self.centralwidget)
        self.tableVenda.setGeometry(QtCore.QRect(40, 90, 601, 192))
        self.tableVenda.setObjectName("tableVenda")
        self.tableVenda.setColumnCount(5)
        self.tableVenda.setRowCount(0)
        self.tableVenda.setColumnWidth(1, 150)
        self.tableVenda.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableVenda.setTextElideMode(Qt.ElideRight)
        self.tableVenda.setWordWrap(False)
        self.tableVenda.setSortingEnabled(False)
        self.tableVenda.horizontalHeader().setDefaultAlignment(Qt.AlignHCenter | Qt.AlignVCenter |
                                                               Qt.AlignCenter)
        self.tableVenda.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableVenda.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableVenda.horizontalHeader().setStretchLastSection(True)
        item = QtWidgets.QTableWidgetItem()
        self.tableVenda.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableVenda.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableVenda.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableVenda.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableVenda.setHorizontalHeaderItem(4, item)
        self.btnIncluir = QtWidgets.QPushButton(self.centralwidget)
        self.btnIncluir.setGeometry(QtCore.QRect(420, 30, 91, 31))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnIncluir.setIcon(icon1)
        self.btnIncluir.setObjectName("btnIncluir")
        self.labelTotal = QtWidgets.QLabel(self.centralwidget)
        self.labelTotal.setGeometry(QtCore.QRect(270, 290, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelTotal.setFont(font)
        self.labelTotal.setObjectName("labelTotal")
        self.editTotal = QtWidgets.QLineEdit(self.centralwidget)
        self.editTotal.setGeometry(QtCore.QRect(320, 290, 113, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.editTotal.setFont(font)
        self.editTotal.setReadOnly(True)
        self.editTotal.setObjectName("editTotal")
        self.labelPagto = QtWidgets.QLabel(self.centralwidget)
        self.labelPagto.setGeometry(QtCore.QRect(30, 390, 147, 18))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelPagto.setFont(font)
        self.labelPagto.setObjectName("labelPagto")
        self.btnRemover = QtWidgets.QPushButton(self.centralwidget)
        self.btnRemover.setGeometry(QtCore.QRect(660, 160, 85, 34))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnRemover.setIcon(icon2)
        self.btnRemover.setObjectName("btnRemover")
        self.btnFinalizarVenda = QtWidgets.QPushButton(self.centralwidget)
        self.btnFinalizarVenda.setGeometry(QtCore.QRect(340, 470, 131, 51))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("greencheck.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnFinalizarVenda.setIcon(icon3)
        self.btnFinalizarVenda.setIconSize(QtCore.QSize(30, 30))
        self.btnFinalizarVenda.setObjectName("btnFinalizarVenda")
        self.labelValorPago = QtWidgets.QLabel(self.centralwidget)
        self.labelValorPago.setGeometry(QtCore.QRect(100, 420, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelValorPago.setFont(font)
        self.labelValorPago.setObjectName("labelValorPago")
        self.valorPagodoubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.valorPagodoubleSpinBox.setGeometry(QtCore.QRect(180, 420, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.valorPagodoubleSpinBox.setFont(font)
        self.valorPagodoubleSpinBox.setObjectName("valorPagodoubleSpinBox")
        self.labelCliente = QtWidgets.QLabel(self.centralwidget)
        self.labelCliente.setGeometry(QtCore.QRect(130, 360, 47, 18))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelCliente.setFont(font)
        self.labelCliente.setObjectName("labelCliente")
        self.clienteComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.clienteComboBox.setGeometry(QtCore.QRect(180, 360, 241, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.clienteComboBox.setFont(font)
        self.clienteComboBox.setObjectName("clienteComboBox")
        self.formapgtoComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.formapgtoComboBox.setGeometry(QtCore.QRect(180, 390, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.formapgtoComboBox.setFont(font)
        self.formapgtoComboBox.setObjectName("formapgtoComboBox")
        self.formapgtoComboBox.addItem("")
        self.formapgtoComboBox.addItem("")
        FormVenda.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(FormVenda)
        self.statusbar.setObjectName("statusbar")
        FormVenda.setStatusBar(self.statusbar)

        self.retranslateUi(FormVenda)
        QtCore.QMetaObject.connectSlotsByName(FormVenda)
        FormVenda.setTabOrder(self.produtoComboBox, self.qtdeSpinBox)
        FormVenda.setTabOrder(self.qtdeSpinBox, self.btnIncluir)
        FormVenda.setTabOrder(self.btnIncluir, self.tableVenda)
        FormVenda.setTabOrder(self.tableVenda, self.btnRemover)
        FormVenda.setTabOrder(self.btnRemover, self.editTotal)
        FormVenda.setTabOrder(self.editTotal, self.clienteComboBox)
        FormVenda.setTabOrder(self.clienteComboBox, self.formapgtoComboBox)
        FormVenda.setTabOrder(self.formapgtoComboBox, self.valorPagodoubleSpinBox)
        FormVenda.setTabOrder(self.valorPagodoubleSpinBox, self.btnFinalizarVenda)

        self.produtoComboBox.addItems(self.preencher_produtos())
        self.clienteComboBox.addItems(self.preencher_clientes())
        self.btnIncluir.clicked.connect(self.click_btn_incluir)
        self.btnRemover.clicked.connect(self.click_btn_remover)
        self.btnFinalizarVenda.clicked.connect(self.click_btn_finalizar_venda)


    def retranslateUi(self, FormVenda):
        _translate = QtCore.QCoreApplication.translate
        FormVenda.setWindowTitle(_translate("FormVenda", "Iniciar Venda"))
        self.labelProduto.setText(_translate("FormVenda", "Produto:"))
        item = self.tableVenda.horizontalHeaderItem(0)
        item.setText(_translate("FormVenda", "CÓD. PROD." ))
        item = self.tableVenda.horizontalHeaderItem(1)
        item.setText(_translate("FormVenda", "DESCRICÃO"))
        item = self.tableVenda.horizontalHeaderItem(2)
        item.setText(_translate("FormVenda", "QUANTIDADE"))
        item = self.tableVenda.horizontalHeaderItem(3)
        item.setText(_translate("FormVenda", "VALOR UNIT."))
        item = self.tableVenda.horizontalHeaderItem(4)
        item.setText(_translate("FormVenda", "VALOR TOTAL"))
        self.btnIncluir.setText(_translate("FormVenda", "Incluir"))
        self.labelTotal.setText(_translate("FormVenda", "Total:"))
        self.labelPagto.setText(_translate("FormVenda", "Forma de Pagamento:"))
        self.btnRemover.setText(_translate("FormVenda", "Remover"))
        self.btnFinalizarVenda.setText(_translate("FormVenda", "Finalizar Venda"))
        self.labelValorPago.setText(_translate("FormVenda", "Valor Pago:"))
        self.labelCliente.setText(_translate("FormVenda", "Cliente:"))
        self.formapgtoComboBox.setItemText(0, _translate("FormVenda", "À VISTA"))
        self.formapgtoComboBox.setItemText(1, _translate("FormVenda", "A PRAZO"))

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    teste = QMainWindow()
    ui = Ui_FormVenda()
    ui.setupUi(teste)
    teste.show()
    sys.exit(app.exec_())