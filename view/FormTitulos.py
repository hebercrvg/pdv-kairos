from PyQt5.QtWidgets import QMainWindow, QApplication, QAbstractItemView, QTableWidgetItem, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from controller.VendaCTR import VendaCTR
from view.FormLancarCredito import Ui_FormLancarCredito
from model.DAO.ClienteDAO import ClienteDAO

class Ui_FormTitulos(object):

    def click_btn_incluir_credito(self):
        try:
            linha = self.tableDevedores.currentRow()
            codvenda = self.tableDevedores.item(linha, 0).text()
            cliente = self.tableDevedores.item(linha, 2).text()
            valorvenda = self.tableDevedores.item(linha, 4).text()
            valorpago = self.tableDevedores.item(linha, 5).text()
            self.formlancarcredito = QMainWindow()
            self.ui = Ui_FormLancarCredito()
            self.ui.setupUi(self.formlancarcredito)
            self.formlancarcredito.show()
            self.ui.preencher_campos(codvenda, valorvenda, valorpago, cliente)
        except:
            msg = QMessageBox(None)
            msg.setWindowTitle("Erro.")
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowIcon(QtGui.QIcon("error.png"))
            msg.setText("Selecione uma venda para lançar o crédito/pagamento.")
            msg.exec_()



    def click_btn_pesquisar_cliente(self):
        nome = self.editPesquisaCliente.text()
        item = QTableWidgetItem
        if (nome == ''):
            self.tableDevedores.setRowCount(0)
            result = VendaCTR.pesquisar_todos_devedores_por_divida()
            for num_linha, linha_conteudo in enumerate(result):
                self.tableDevedores.insertRow(num_linha)
                for num_coluna, coluna_conteudo in enumerate(linha_conteudo):
                    self.tableDevedores.setItem(num_linha, num_coluna, item(str(coluna_conteudo)))

        elif (nome != ''):
            result = VendaCTR.pesquisar_devedor_por_divida(nome)
            self.tableDevedores.setRowCount(0)
            for num_linha, linha_conteudo in enumerate(result):
                self.tableDevedores.insertRow(num_linha)
                for num_coluna, coluna_conteudo in enumerate(linha_conteudo):
                    self.tableDevedores.setItem(num_linha, num_coluna, item(str(coluna_conteudo)))


    def setupUi(self, FormDevedores):
        FormDevedores.setObjectName("FormDevedores")
        FormDevedores.resize(853, 471)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("contas a receber.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FormDevedores.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(FormDevedores)
        self.centralwidget.setObjectName("centralwidget")
        self.labelCliente = QtWidgets.QLabel(self.centralwidget)
        self.labelCliente.setGeometry(QtCore.QRect(90, 20, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelCliente.setFont(font)
        self.labelCliente.setObjectName("labelCliente")
        self.editPesquisaCliente = QtWidgets.QLineEdit(self.centralwidget)
        self.editPesquisaCliente.setGeometry(QtCore.QRect(140, 20, 371, 21))
        self.editPesquisaCliente.setText("")
        self.editPesquisaCliente.setObjectName("editPesquisaCliente")
        self.tableDevedores = QtWidgets.QTableWidget(self.centralwidget)
        self.tableDevedores.setGeometry(QtCore.QRect(10, 60, 831, 301))
        self.tableDevedores.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableDevedores.setAutoFillBackground(False)
        self.tableDevedores.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableDevedores.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableDevedores.setTextElideMode(Qt.ElideRight)
        self.tableDevedores.setWordWrap(False)
        self.tableDevedores.setSortingEnabled(False)
        self.tableDevedores.horizontalHeader().setDefaultAlignment(Qt.AlignHCenter | Qt.AlignVCenter |
                                                                 Qt.AlignCenter)
        self.tableDevedores.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableDevedores.horizontalHeader().setStretchLastSection(True)
        self.tableDevedores.setGridStyle(QtCore.Qt.SolidLine)
        self.tableDevedores.setRowCount(0)
        self.tableDevedores.setObjectName("tableDevedores")
        self.tableDevedores.setColumnCount(7)
        self.tableDevedores.setColumnWidth(2, 200)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableDevedores.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableDevedores.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableDevedores.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableDevedores.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableDevedores.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableDevedores.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableDevedores.setHorizontalHeaderItem(6, item)
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(560, 15, 166, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnPesquisarCliente = QtWidgets.QPushButton(self.layoutWidget)
        self.btnPesquisarCliente.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnPesquisarCliente.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("lupa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPesquisarCliente.setIcon(icon1)
        self.btnPesquisarCliente.setIconSize(QtCore.QSize(16, 16))
        self.btnPesquisarCliente.setObjectName("btnPesquisarCliente")
        self.horizontalLayout.addWidget(self.btnPesquisarCliente)
        self.btnLimpar = QtWidgets.QPushButton(self.layoutWidget)
        self.btnLimpar.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnLimpar.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("borracha.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnLimpar.setIcon(icon2)
        self.btnLimpar.setIconSize(QtCore.QSize(16, 16))
        self.btnLimpar.setObjectName("btnLimpar")
        self.horizontalLayout.addWidget(self.btnLimpar)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(290, 370, 271, 40))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnInserirCredito = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnInserirCredito.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("credit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnInserirCredito.setIcon(icon3)
        self.btnInserirCredito.setIconSize(QtCore.QSize(30, 30))
        self.btnInserirCredito.setObjectName("btnInserirCredito")
        self.horizontalLayout_2.addWidget(self.btnInserirCredito)
        self.btnExportar = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnExportar.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("pdf.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnExportar.setIcon(icon4)
        self.btnExportar.setIconSize(QtCore.QSize(30, 30))
        self.btnExportar.setObjectName("btnExportar")
        self.horizontalLayout_2.addWidget(self.btnExportar)
        FormDevedores.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(FormDevedores)
        self.statusbar.setObjectName("statusbar")
        FormDevedores.setStatusBar(self.statusbar)

        self.retranslateUi(FormDevedores)
        self.btnLimpar.clicked.connect(self.editPesquisaCliente.clear)
        QtCore.QMetaObject.connectSlotsByName(FormDevedores)
        FormDevedores.setTabOrder(self.editPesquisaCliente, self.btnPesquisarCliente)
        FormDevedores.setTabOrder(self.btnPesquisarCliente, self.btnLimpar)
        FormDevedores.setTabOrder(self.btnLimpar, self.tableDevedores)
        FormDevedores.setTabOrder(self.tableDevedores, self.btnInserirCredito)

        self.btnPesquisarCliente.clicked.connect(self.click_btn_pesquisar_cliente)
        self.btnInserirCredito.clicked.connect(self.click_btn_incluir_credito)

    def retranslateUi(self, FormDevedores):
        _translate = QtCore.QCoreApplication.translate
        FormDevedores.setWindowTitle(_translate("FormDevedores", "Devedores por Dívida"))
        self.labelCliente.setText(_translate("FormDevedores", "Cliente:"))
        item = self.tableDevedores.horizontalHeaderItem(0)
        item.setText(_translate("FormDevedores", "CÓD. VENDA"))
        item = self.tableDevedores.horizontalHeaderItem(1)
        item.setText(_translate("FormDevedores", "CÓD. CLIENTE"))
        item = self.tableDevedores.horizontalHeaderItem(2)
        item.setText(_translate("FormDevedores", "CLIENTE"))
        item = self.tableDevedores.horizontalHeaderItem(3)
        item.setText(_translate("FormDevedores", "DATA VENDA"))
        item = self.tableDevedores.horizontalHeaderItem(4)
        item.setText(_translate("FormDevedores", "VALOR VENDA"))
        item = self.tableDevedores.horizontalHeaderItem(5)
        item.setText(_translate("FormDevedores", "VALOR PAGO"))
        item = self.tableDevedores.horizontalHeaderItem(6)
        item.setText(_translate("FormDevedores", "A PAGAR"))
        self.btnPesquisarCliente.setText(_translate("FormDevedores", "Pesquisar"))
        self.btnLimpar.setText(_translate("FormDevedores", "Limpar"))
        self.btnInserirCredito.setText(_translate("FormDevedores", "Inserir Crédito"))
        self.btnExportar.setText(_translate("FormDevedores", "Exportar"))

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    teste = QMainWindow()
    ui = Ui_FormTitulos()
    ui.setupUi(teste)
    teste.show()
    sys.exit(app.exec_())