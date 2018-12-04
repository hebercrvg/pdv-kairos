from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QAbstractItemView
from view.FormCadastrarCliente import Ui_FormCadastrarCliente
from view.FormAlterarCliente import Ui_FormAlterarCliente
from PyQt5.QtCore import Qt

from controller.ClienteCTR import ClienteCTR

class Ui_FormClientes(object):

    def click_btn_cadastrar_cliente(self):
        self.formcadastrarcliente = QMainWindow()
        self.ui = Ui_FormCadastrarCliente()
        self.ui.setupUi(self.formcadastrarcliente)
        self.formcadastrarcliente.show()

    def click_btn_excluir_cliente(self):
        linha = self.tableCliente.currentItem().row()
        codcli = (int(self.tableCliente.item(linha, 0).text()))
        nome = self.tableCliente.item(linha, 1).text()
        ClienteCTR.Excluir_Cliente(codcli, nome)


    def click_btn_alterar_cliente(self):

        linha = self.tableCliente.currentItem().row()
        codcli = self.tableCliente.item(linha, 0).text()
        nome = self.tableCliente.item(linha, 1).text()
        telefone = self.tableCliente.item(linha, 2).text()
        self.formalterarcliente = QMainWindow()
        self.ui = Ui_FormAlterarCliente()
        self.ui.setupUi(self.formalterarcliente)
        self.formalterarcliente.show()
        self.ui.preencher_campos(codcli, nome, telefone)

    def click_btn_pesquisar(self):

        aux = self.editPesquisaCliente.text()

        if (aux == ''):
            result = ClienteCTR.Pesquisar_Todos_Clientes()
            self.tableCliente.setRowCount(0)
            for num_linha, linha_conteudo in enumerate(result):
                self.tableCliente.insertRow(num_linha)
                for num_coluna, coluna_conteudo in enumerate(linha_conteudo):
                    self.tableCliente.setItem(num_linha, num_coluna, QtWidgets.QTableWidgetItem(str(coluna_conteudo)))

        elif (aux != ''):
            nome = self.editPesquisaCliente.text()
            result = ClienteCTR.Pesquisar_Cliente(nome)
            self.tableCliente.setRowCount(0)
            for num_linha, linha_conteudo in enumerate(result):
                self.tableCliente.insertRow(num_linha)
                for num_coluna, coluna_conteudo in enumerate(linha_conteudo):
                    self.tableCliente.setItem(num_linha, num_coluna, QtWidgets.QTableWidgetItem(str(coluna_conteudo)))


    def setupUi(self, FormClientes):
        FormClientes.setObjectName("FormClientes")
        FormClientes.resize(661, 471)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("cadastrar usuario.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FormClientes.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(FormClientes)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.editPesquisaCliente = QtWidgets.QLineEdit(self.centralwidget)
        self.editPesquisaCliente.setGeometry(QtCore.QRect(90, 20, 371, 21))
        self.editPesquisaCliente.setText("")
        self.editPesquisaCliente.setObjectName("editPesquisaCliente")
        self.tableCliente = QtWidgets.QTableWidget(self.centralwidget)
        #CONFIGURACOES QUE ACHEI NO YOUTUBE
        self.tableCliente.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableCliente.setTextElideMode(Qt.ElideRight)
        self.tableCliente.setWordWrap(False)
        self.tableCliente.setSortingEnabled(False)
        self.tableCliente.horizontalHeader().setDefaultAlignment(Qt.AlignHCenter | Qt.AlignVCenter |
                                                          Qt.AlignCenter)
        self.tableCliente.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableCliente.horizontalHeader().setStretchLastSection(True)

        #FIM
        self.tableCliente.setGeometry(QtCore.QRect(10, 60, 641, 301))
        self.tableCliente.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableCliente.setAutoFillBackground(False)

        self.tableCliente.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableCliente.setGridStyle(QtCore.Qt.SolidLine)
        self.tableCliente.setRowCount(0)
        self.tableCliente.setObjectName("tableCliente")
        self.tableCliente.setColumnCount(3)
        self.tableCliente.setColumnWidth(1, 300)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableCliente.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableCliente.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableCliente.setHorizontalHeaderItem(2, item)
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(470, 15, 166, 31))
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
        self.widget.setGeometry(QtCore.QRect(120, 370, 403, 42))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnExcluirCliente = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnExcluirCliente.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("excluircliente.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnExcluirCliente.setIcon(icon3)
        self.btnExcluirCliente.setIconSize(QtCore.QSize(30, 30))
        self.btnExcluirCliente.setObjectName("btnExcluirCliente")
        self.horizontalLayout_2.addWidget(self.btnExcluirCliente)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.btnAlterarCliente = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnAlterarCliente.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("editar usuario.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAlterarCliente.setIcon(icon4)
        self.btnAlterarCliente.setIconSize(QtCore.QSize(30, 30))
        self.btnAlterarCliente.setObjectName("btnExcluirCliente")
        self.gridLayout.addWidget(self.btnAlterarCliente, 0, 0, 1, 1)
        self.btnCadastrarCliente = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnCadastrarCliente.setFont(font)
        self.btnCadastrarCliente.setIcon(icon)
        self.btnCadastrarCliente.setIconSize(QtCore.QSize(30, 30))
        self.btnCadastrarCliente.setObjectName("btnCadastrarCliente")
        self.gridLayout.addWidget(self.btnCadastrarCliente, 0, 1, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        FormClientes.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(FormClientes)
        self.statusbar.setObjectName("statusbar")
        FormClientes.setStatusBar(self.statusbar)

        self.retranslateUi(FormClientes)
        self.btnLimpar.clicked.connect(self.editPesquisaCliente.clear)
        self.btnPesquisarCliente.clicked.connect(self.click_btn_pesquisar)
        self.btnCadastrarCliente.clicked.connect(self.click_btn_cadastrar_cliente)
        self.btnAlterarCliente.clicked.connect(self.click_btn_alterar_cliente)
        self.btnExcluirCliente.clicked.connect(self.click_btn_excluir_cliente)


        QtCore.QMetaObject.connectSlotsByName(FormClientes)
        FormClientes.setTabOrder(self.editPesquisaCliente, self.btnPesquisarCliente)
        FormClientes.setTabOrder(self.btnPesquisarCliente, self.btnLimpar)
        FormClientes.setTabOrder(self.btnLimpar, self.tableCliente)
        FormClientes.setTabOrder(self.tableCliente, self.btnAlterarCliente)
        FormClientes.setTabOrder(self.btnAlterarCliente, self.btnCadastrarCliente)

    def retranslateUi(self, FormClientes):
        _translate = QtCore.QCoreApplication.translate
        FormClientes.setWindowTitle(_translate("FormClientes", "Clientes"))
        self.label.setText(_translate("FormClientes", "Nome:"))
        item = self.tableCliente.horizontalHeaderItem(0)
        item.setText(_translate("FormClientes", "Cód. Cliente"))
        item = self.tableCliente.horizontalHeaderItem(1)
        item.setText(_translate("FormClientes", "Nome"))
        item = self.tableCliente.horizontalHeaderItem(2)
        item.setText(_translate("FormClientes", "Telefone"))
        self.btnPesquisarCliente.setText(_translate("FormClientes", "Pesquisar"))
        self.btnLimpar.setText(_translate("FormClientes", "Limpar"))
        self.btnExcluirCliente.setText(_translate("FormClientes", "Excluir Cliente"))
        self.btnAlterarCliente.setText(_translate("FormClientes", "Alterar Cliente"))
        self.btnCadastrarCliente.setText(_translate("FormClientes", "Cadastrar Cliente"))

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_FormClientes()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())