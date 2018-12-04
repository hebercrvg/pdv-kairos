from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QAbstractItemView
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets

from model.DAO.ProdutoDAO import ProdutoDAO
from model.DAO.ClienteDAO import ClienteDAO
from controller.ProdutoCTR import ProdutoCTR
from controller.ClienteCTR import ClienteCTR


class Ui_FormVenda(object):

    def click_btn_incluir(self):
        cliente = self.clienteComboBox.currentText()
        produto = self.produtoComboBox.currentText()
        codprod = ProdutoCTR.Get_codprod_por_descricao(produto)
        valorunit = ProdutoCTR.Get_preco_produto(codprod)
        qtde = self.qtdeSpinBox.value()
        valortotalprod = (valorunit*qtde)
        item = QTableWidgetItem
        self.tableVenda.insertRow(0)
        self.tableVenda.setItem(0, 0, item(str(codprod)))
        self.tableVenda.setItem(0, 1, item(str(produto)))
        self.tableVenda.setItem(0, 2, item(str(qtde)))
        self.tableVenda.setItem(0, 3, item(str(valorunit)))
        self.tableVenda.setItem(0, 4, item(str(valortotalprod)))
        self.totalvenda += valortotalprod
        self.editTotal.setText(str(self.totalvenda))

    def click_btn_remover(self):
        linha = self.tableVenda.currentRow()
        valortotalprod = float(self.tableVenda.item(linha, 4).text())
        self.totalvenda = (self.totalvenda - valortotalprod)
        self.editTotal.setText(str(self.totalvenda))
        self.tableVenda.removeRow(linha)


    def preencher_comboBox_produto(self):
        produtoDAO = ProdutoDAO
        produtos = produtoDAO.pesquisar_descricao_todos_produtos_lista()
        return produtos
    def preencher_comboBox_cliente(self):
        clienteDAO = ClienteDAO
        clientes = clienteDAO.pesquisar_nomecliente_todos_lista()
        return clientes

    def setupUi(self, FormVenda):
        self.totalvenda = 0.0
        FormVenda.setObjectName("FormVenda")
        FormVenda.resize(814, 600)
        self.centralwidget = QtWidgets.QWidget(FormVenda)
        self.centralwidget.setObjectName("centralwidget")
        self.produtoComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.produtoComboBox.setGeometry(QtCore.QRect(100, 50, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.produtoComboBox.setFont(font)
        self.produtoComboBox.setObjectName("produtoComboBox")
        self.labelProduto = QtWidgets.QLabel(self.centralwidget)
        self.labelProduto.setGeometry(QtCore.QRect(40, 60, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelProduto.setFont(font)
        self.labelProduto.setObjectName("labelProduto")
        self.qtdeSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.qtdeSpinBox.setGeometry(QtCore.QRect(310, 50, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.qtdeSpinBox.setFont(font)
        self.qtdeSpinBox.setObjectName("qtdeSpinBox")
        self.tableVenda = QtWidgets.QTableWidget(self.centralwidget)
        self.tableVenda.setGeometry(QtCore.QRect(40, 130, 601, 192))
        self.tableVenda.setObjectName("tableVenda")
        self.tableVenda.setColumnCount(5)
        self.tableVenda.setRowCount(0)
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
        self.btnIncluir.setGeometry(QtCore.QRect(380, 50, 91, 31))
        self.btnIncluir.setObjectName("btnIncluir")
        self.labelTotal = QtWidgets.QLabel(self.centralwidget)
        self.labelTotal.setGeometry(QtCore.QRect(270, 330, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelTotal.setFont(font)
        self.labelTotal.setObjectName("labelTotal")
        self.editTotal = QtWidgets.QLineEdit(self.centralwidget)
        self.editTotal.setGeometry(QtCore.QRect(320, 330, 113, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.editTotal.setFont(font)
        self.editTotal.setReadOnly(True)
        self.editTotal.setObjectName("editTotal")
        self.labelPagto = QtWidgets.QLabel(self.centralwidget)
        self.labelPagto.setGeometry(QtCore.QRect(40, 400, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelPagto.setFont(font)
        self.labelPagto.setObjectName("labelPagto")
        self.formapgtComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.formapgtComboBox.setGeometry(QtCore.QRect(190, 400, 111, 22))
        self.formapgtComboBox.setObjectName("formapgtComboBox")
        self.formapgtComboBox.addItem("")
        self.formapgtComboBox.addItem("")
        self.btnRemover = QtWidgets.QPushButton(self.centralwidget)
        self.btnRemover.setGeometry(QtCore.QRect(660, 200, 71, 31))
        self.btnRemover.setObjectName("btnRemover")
        self.btnFinalizarVenda = QtWidgets.QPushButton(self.centralwidget)
        self.btnFinalizarVenda.setGeometry(QtCore.QRect(340, 480, 91, 51))
        self.btnFinalizarVenda.setObjectName("btnFinalizarVenda")
        self.labelValorPago = QtWidgets.QLabel(self.centralwidget)
        self.labelValorPago.setGeometry(QtCore.QRect(110, 430, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelValorPago.setFont(font)
        self.labelValorPago.setObjectName("labelValorPago")
        self.valorPagodoubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.valorPagodoubleSpinBox.setGeometry(QtCore.QRect(190, 430, 62, 22))
        self.valorPagodoubleSpinBox.setObjectName("valorPagodoubleSpinBox")
        self.labelCliente = QtWidgets.QLabel(self.centralwidget)
        self.labelCliente.setGeometry(QtCore.QRect(40, 20, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelCliente.setFont(font)
        self.labelCliente.setObjectName("labelCliente")
        self.clienteComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.clienteComboBox.setGeometry(QtCore.QRect(100, 10, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.clienteComboBox.setFont(font)
        self.clienteComboBox.setObjectName("clienteComboBox")
        FormVenda.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(FormVenda)
        self.statusbar.setObjectName("statusbar")
        FormVenda.setStatusBar(self.statusbar)

        self.tableVenda.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableVenda.setTextElideMode(Qt.ElideRight)
        self.tableVenda.setWordWrap(False)
        self.tableVenda.setSortingEnabled(False)
        self.tableVenda.horizontalHeader().setDefaultAlignment(Qt.AlignHCenter | Qt.AlignVCenter |
                                                                 Qt.AlignCenter)
        self.tableVenda.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableVenda.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableVenda.horizontalHeader().setStretchLastSection(True)
        self.clienteComboBox.addItems(self.preencher_comboBox_cliente())
        self.produtoComboBox.addItems(self.preencher_comboBox_produto())
        self.btnIncluir.clicked.connect(self.click_btn_incluir)
        self.btnRemover.clicked.connect(self.click_btn_remover)



        self.retranslateUi(FormVenda)
        QtCore.QMetaObject.connectSlotsByName(FormVenda)

    def retranslateUi(self, FormVenda):
        _translate = QtCore.QCoreApplication.translate
        FormVenda.setWindowTitle(_translate("FormVenda", "MainWindow"))
        self.labelProduto.setText(_translate("FormVenda", "Produto:"))
        item = self.tableVenda.horizontalHeaderItem(0)
        item.setText(_translate("FormVenda", "CODPROD"))
        item = self.tableVenda.horizontalHeaderItem(1)
        item.setText(_translate("FormVenda", "DESCRICAO"))
        item = self.tableVenda.horizontalHeaderItem(2)
        item.setText(_translate("FormVenda", "QUANTIDADE"))
        item = self.tableVenda.horizontalHeaderItem(3)
        item.setText(_translate("FormVenda", "VALOR UNIT."))
        item = self.tableVenda.horizontalHeaderItem(4)
        item.setText(_translate("FormVenda", "VALOR TOTAL"))
        self.btnIncluir.setText(_translate("FormVenda", "Incluir"))
        self.labelTotal.setText(_translate("FormVenda", "Total:"))
        self.labelPagto.setText(_translate("FormVenda", "Forma de Pagamento:"))
        self.formapgtComboBox.setItemText(0, _translate("FormVenda", "A VISTA"))
        self.formapgtComboBox.setItemText(1, _translate("FormVenda", "A PRAZO"))
        self.btnRemover.setText(_translate("FormVenda", "Remover"))
        self.btnFinalizarVenda.setText(_translate("FormVenda", "Finalizar Venda"))
        self.labelValorPago.setText(_translate("FormVenda", "Valor Pago:"))
        self.labelCliente.setText(_translate("FormVenda", "Cliente:"))

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    teste = QMainWindow()
    ui = Ui_FormVenda()
    ui.setupUi(teste)
    teste.show()
    sys.exit(app.exec_())