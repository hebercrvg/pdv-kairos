from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from view.FormClientes import Ui_FormClientes
from view.FormProdutos import Ui_FormProdutos
from view.FormVenda import Ui_FormVenda
from view.FormDevedores import Ui_FormDevedores
from view.FormTitulos import Ui_FormTitulos
from view.FormUsuarios import Ui_FormUsuarios


class Ui_FormMenuPrincipal(object):

    def click_btn_usuarios(self):
        self.usuarios = QMainWindow()
        self.ui = Ui_FormUsuarios()
        self.ui.setupUi(self.usuarios)
        self.usuarios.show()

    def click_btn_clientes(self):
        self.formclientes = QMainWindow()
        self.ui = Ui_FormClientes()
        self.ui.setupUi(self.formclientes)
        self.formclientes.show()

    def click_btn_produtos(self):
        self.formprodutos = QMainWindow()
        self.ui = Ui_FormProdutos()
        self.ui.setupUi(self.formprodutos)
        self.formprodutos.show()

    def click_btn_venda(self):
        self.formvenda = QMainWindow()
        self.ui = Ui_FormVenda()
        self.ui.setupUi(self.formvenda)
        self.formvenda.show()
    def click_btn_contasreceber(self):
        self.devedores = QMainWindow()
        self.ui = Ui_FormDevedores()
        self.ui.setupUi(self.devedores)
        self.devedores.show()
    def click_btn_lancarcredito(self):
        self.lancarcredito = QMainWindow()
        self.ui = Ui_FormTitulos()
        self.ui.setupUi(self.lancarcredito)
        self.lancarcredito.show()

    def setupUi(self, FormMenuPrincipal):
        FormMenuPrincipal.setObjectName("FormMenuPrincipal")
        FormMenuPrincipal.setWindowModality(QtCore.Qt.NonModal)
        FormMenuPrincipal.resize(1360, 720)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("PGKairos1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FormMenuPrincipal.setWindowIcon(icon)
        FormMenuPrincipal.setStyleSheet("background-image: url(fundo.png);")
        self.centralwidget = QtWidgets.QWidget(FormMenuPrincipal)
        self.centralwidget.setObjectName("centralwidget")
        FormMenuPrincipal.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FormMenuPrincipal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1360, 21))
        self.menubar.setStyleSheet("")
        self.menubar.setObjectName("menubar")
        self.menuCadastros = QtWidgets.QMenu(self.menubar)
        self.menuCadastros.setObjectName("menuCadastros")
        self.menuVendas = QtWidgets.QMenu(self.menubar)
        self.menuVendas.setObjectName("menuVendas")
        self.menuFinanceiro = QtWidgets.QMenu(self.menubar)
        self.menuFinanceiro.setObjectName("menuFinanceiro")
        self.menuAdministracao = QtWidgets.QMenu(self.menubar)
        self.menuAdministracao.setObjectName("menuAdministracao")
        FormMenuPrincipal.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FormMenuPrincipal)
        self.statusbar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.statusbar.setObjectName("statusbar")
        FormMenuPrincipal.setStatusBar(self.statusbar)
        self.actionClientes = QtWidgets.QAction(FormMenuPrincipal)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("cadastrar usuario.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClientes.setIcon(icon1)
        self.actionClientes.setObjectName("actionClientes")
        self.actionProdutos = QtWidgets.QAction(FormMenuPrincipal)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("cadastrar produtos 2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionProdutos.setIcon(icon2)
        self.actionProdutos.setObjectName("actionProdutos")
        self.actionUsuarios = QtWidgets.QAction(FormMenuPrincipal)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("cliente.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUsuarios.setIcon(icon3)
        self.actionUsuarios.setObjectName("actionUsuarios")
        self.actionIniciarVenda = QtWidgets.QAction(FormMenuPrincipal)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("loja.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionIniciarVenda.setIcon(icon4)
        self.actionIniciarVenda.setObjectName("actionIniciarVenda")
        self.actionContasAReceber = QtWidgets.QAction(FormMenuPrincipal)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("contas a receber.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionContasAReceber.setIcon(icon5)
        self.actionContasAReceber.setObjectName("actionContasAReceber")
        self.actionLancarCreditoaoCliente = QtWidgets.QAction(FormMenuPrincipal)
        self.actionLancarCreditoaoCliente.setObjectName("actionLancarCreditoaoCliente")
        self.actionLancarCredito = QtWidgets.QAction(FormMenuPrincipal)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("devedor.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLancarCredito.setIcon(icon6)
        self.actionLancarCredito.setObjectName("actionLancarCredito")
        self.menuCadastros.addAction(self.actionClientes)
        self.menuCadastros.addAction(self.actionProdutos)
        self.menuVendas.addAction(self.actionIniciarVenda)
        self.menuFinanceiro.addAction(self.actionContasAReceber)
        self.menuFinanceiro.addAction(self.actionLancarCredito)
        self.menuAdministracao.addAction(self.actionUsuarios)
        self.menubar.addAction(self.menuCadastros.menuAction())
        self.menubar.addAction(self.menuVendas.menuAction())
        self.menubar.addAction(self.menuFinanceiro.menuAction())
        self.menubar.addAction(self.menuAdministracao.menuAction())
        #clicks
        self.actionClientes.triggered.connect(self.click_btn_clientes)
        self.actionProdutos.triggered.connect(self.click_btn_produtos)
        self.actionIniciarVenda.triggered.connect(self.click_btn_venda)
        self.actionContasAReceber.triggered.connect(self.click_btn_contasreceber)
        self.actionLancarCredito.triggered.connect(self.click_btn_lancarcredito)
        self.actionUsuarios.triggered.connect(self.click_btn_usuarios)
        self.retranslateUi(FormMenuPrincipal)
        QtCore.QMetaObject.connectSlotsByName(FormMenuPrincipal)

    def retranslateUi(self, FormMenuPrincipal):
        _translate = QtCore.QCoreApplication.translate
        FormMenuPrincipal.setWindowTitle(_translate("FormMenuPrincipal", "PDV - Kairós v1.0"))
        self.menuCadastros.setTitle(_translate("FormMenuPrincipal", "Cadastros"))
        self.menuVendas.setTitle(_translate("FormMenuPrincipal", "Vendas"))
        self.menuFinanceiro.setTitle(_translate("FormMenuPrincipal", "Financeiro"))
        self.menuAdministracao.setTitle(_translate("FormMenuPrincipal", "Administração"))
        self.actionClientes.setText(_translate("FormMenuPrincipal", "Clientes"))
        self.actionProdutos.setText(_translate("FormMenuPrincipal", "Produtos"))
        self.actionUsuarios.setText(_translate("FormMenuPrincipal", "Usuários"))
        self.actionIniciarVenda.setText(_translate("FormMenuPrincipal", "Iniciar Venda"))
        self.actionContasAReceber.setText(_translate("FormMenuPrincipal", "Contas a Receber"))
        self.actionLancarCreditoaoCliente.setText(_translate("FormMenuPrincipal", "Lançar Crédto ao Cliente"))
        self.actionLancarCredito.setText(_translate("FormMenuPrincipal", "Lançar Crédito ao Cliente"))

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_FormMenuPrincipal()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    sys.exit(app.exec_())
