from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from view.FormClientes import Ui_FormClientes
from view.FormProdutos import Ui_FormProdutos
from view.FormVenda import Ui_FormVenda
from view.FormContasAReceber import Ui_FormContasReceber


class Ui_FormPrincipal(object):
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
        self.ui = Ui_FormContasReceber()
        self.ui.setupUi(self.devedores)
        self.devedores.show()
    def click_btn_relatorios(self):
        msg = QMessageBox(None)
        msg.setWindowTitle("DESCULPE")
        msg.setIcon(QMessageBox.Information)
        msg.setText("Desculpe, esta função está em desenvolvimento!")
        msg.exec_()


    def setupUi(self, FormPrincipal):
        FormPrincipal.setObjectName("FormPrincipal")
        FormPrincipal.resize(835, 458)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FormPrincipal.sizePolicy().hasHeightForWidth())
        FormPrincipal.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("PGKairos1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FormPrincipal.setWindowIcon(icon)
        FormPrincipal.setToolTip("")
        FormPrincipal.setStyleSheet("")
        FormPrincipal.setIconSize(QtCore.QSize(60, 60))
        self.centralwidget = QtWidgets.QWidget(FormPrincipal)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(9, 83, 1000, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.btnCadastrarCliente = QtWidgets.QPushButton(self.centralwidget)
        self.btnCadastrarCliente.setGeometry(QtCore.QRect(30, 10, 150, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnCadastrarCliente.sizePolicy().hasHeightForWidth())
        self.btnCadastrarCliente.setSizePolicy(sizePolicy)
        self.btnCadastrarCliente.setMaximumSize(QtCore.QSize(150, 100))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.btnCadastrarCliente.setFont(font)
        self.btnCadastrarCliente.setStatusTip("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("cadastrar usuario.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCadastrarCliente.setIcon(icon1)
        self.btnCadastrarCliente.setIconSize(QtCore.QSize(60, 60))
        self.btnCadastrarCliente.setObjectName("btnCadastrarCliente")
        self.btnCadastrarProduto = QtWidgets.QPushButton(self.centralwidget)
        self.btnCadastrarProduto.setGeometry(QtCore.QRect(190, 10, 150, 71))
        self.btnCadastrarProduto.setMaximumSize(QtCore.QSize(150, 100))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.btnCadastrarProduto.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("cadastrar produtos 2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCadastrarProduto.setIcon(icon2)
        self.btnCadastrarProduto.setIconSize(QtCore.QSize(60, 60))
        self.btnCadastrarProduto.setObjectName("btnCadastrarProduto")
        self.imgPrincipal = QtWidgets.QLabel(self.centralwidget)
        self.imgPrincipal.setGeometry(QtCore.QRect(-100, 100, 941, 341))
        self.imgPrincipal.setText("")
        self.imgPrincipal.setPixmap(QtGui.QPixmap("PGKairosIcone.png"))
        self.imgPrincipal.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.imgPrincipal.setObjectName("imgPrincipal")
        self.btnVenda = QtWidgets.QPushButton(self.centralwidget)
        self.btnVenda.setGeometry(QtCore.QRect(350, 10, 150, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnVenda.sizePolicy().hasHeightForWidth())
        self.btnVenda.setSizePolicy(sizePolicy)
        self.btnVenda.setMaximumSize(QtCore.QSize(150, 100))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.btnVenda.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("loja.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnVenda.setIcon(icon3)
        self.btnVenda.setIconSize(QtCore.QSize(60, 60))
        self.btnVenda.setObjectName("btnVenda")
        self.btnContasAReceber = QtWidgets.QPushButton(self.centralwidget)
        self.btnContasAReceber.setGeometry(QtCore.QRect(510, 10, 150, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnContasAReceber.sizePolicy().hasHeightForWidth())
        self.btnContasAReceber.setSizePolicy(sizePolicy)
        self.btnContasAReceber.setMaximumSize(QtCore.QSize(150, 100))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(8)
        self.btnContasAReceber.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("contas a receber.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnContasAReceber.setIcon(icon4)
        self.btnContasAReceber.setIconSize(QtCore.QSize(40, 40))
        self.btnContasAReceber.setObjectName("btnContasAReceber")
        self.btnRelatorios = QtWidgets.QPushButton(self.centralwidget)
        self.btnRelatorios.setGeometry(QtCore.QRect(670, 10, 141, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnRelatorios.sizePolicy().hasHeightForWidth())
        self.btnRelatorios.setSizePolicy(sizePolicy)
        self.btnRelatorios.setMaximumSize(QtCore.QSize(150, 100))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.btnRelatorios.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("relatorioVenda.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnRelatorios.setIcon(icon5)
        self.btnRelatorios.setIconSize(QtCore.QSize(60, 60))
        self.btnRelatorios.setObjectName("btnRelatorios")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(730, 100, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(247, 247, 247);")
        self.label.setObjectName("label")
        FormPrincipal.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(FormPrincipal)
        self.statusbar.setObjectName("statusbar")
        FormPrincipal.setStatusBar(self.statusbar)

        self.retranslateUi(FormPrincipal)
        QtCore.QMetaObject.connectSlotsByName(FormPrincipal)


        self.btnCadastrarCliente.clicked.connect(self.click_btn_clientes)
        self.btnCadastrarProduto.clicked.connect(self.click_btn_produtos)
        self.btnVenda.clicked.connect(self.click_btn_venda)
        self.btnContasAReceber.clicked.connect(self.click_btn_contasreceber)
        self.btnRelatorios.clicked.connect(self.click_btn_relatorios)

    def retranslateUi(self, FormPrincipal):
        _translate = QtCore.QCoreApplication.translate
        FormPrincipal.setWindowTitle(_translate("FormPrincipal", "Sistema de Vendas - KAIRÓS"))
        self.btnCadastrarCliente.setToolTip(_translate("FormPrincipal", "<html><head/><body><p>Aqui você pode cadastrar e alterar clientes.</p></body></html>"))
        self.btnCadastrarCliente.setText(_translate("FormPrincipal", "Clientes"))
        self.btnCadastrarProduto.setToolTip(_translate("FormPrincipal", "<html><head/><body><p>Aqui você pode cadastrar e alterar produtos..</p></body></html>"))
        self.btnCadastrarProduto.setText(_translate("FormPrincipal", "Produtos"))
        self.btnVenda.setToolTip(_translate("FormPrincipal", "<html><head/><body><p>Aqui você pode realizar uma venda.</p></body></html>"))
        self.btnVenda.setText(_translate("FormPrincipal", "Vendas"))
        self.btnContasAReceber.setToolTip(_translate("FormPrincipal", "<html><head/><body><p>Aqui você pode veficar assuntos financeiros.</p></body></html>"))
        self.btnContasAReceber.setText(_translate("FormPrincipal", "Contas a Receber"))
        self.btnRelatorios.setToolTip(_translate("FormPrincipal", "<html><head/><body><p>Aqui você pode gerar alguns relatórios.</p></body></html>"))
        self.btnRelatorios.setText(_translate("FormPrincipal", "Relatórios"))
        self.label.setText(_translate("FormPrincipal", "Versão: BETA1.1"))

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_FormPrincipal()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
