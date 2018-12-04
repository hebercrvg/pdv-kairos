from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from controller.ProdutoCTR import ProdutoCTR

class Ui_FormAlterarProduto(object):

    def preencher_campos(self, codprod, descricao, tipo, preco):
        self.Codprod = codprod
        self.editDescricao.setText(descricao)
        self.tipoComboBox.setCurrentText(tipo)

        self.precoSpinBox.setValue(preco)

    def click_btn_salvar(self):
        descricao = self.editDescricao.text()
        tipo = self.tipoComboBox.currentText()
        preco = self.precoSpinBox.value()
        Codprod = self.Codprod
        produtoCTR = ProdutoCTR
        produtoCTR.Alterar_Produto(Codprod, descricao, tipo, preco)

    def setupUi(self, FormAlterarProduto):
        FormAlterarProduto.setObjectName("FormAlterarProduto")
        FormAlterarProduto.resize(476, 184)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("listar produtos.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FormAlterarProduto.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(FormAlterarProduto)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 10, 151, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.labelPreco = QtWidgets.QLabel(self.centralwidget)
        self.labelPreco.setGeometry(QtCore.QRect(60, 80, 16, 21))
        self.labelPreco.setObjectName("labelPreco")
        self.precoSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.precoSpinBox.setGeometry(QtCore.QRect(80, 80, 81, 20))
        self.precoSpinBox.setPrefix("")
        self.precoSpinBox.setSuffix("")
        self.precoSpinBox.setMaximum(99.99)
        self.precoSpinBox.setObjectName("precoSpinBox")
        self.labelDescricao = QtWidgets.QLabel(self.centralwidget)
        self.labelDescricao.setGeometry(QtCore.QRect(30, 53, 51, 20))
        self.labelDescricao.setObjectName("labelDescricao")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(140, 120, 168, 35))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnCadastrar = QtWidgets.QPushButton(self.layoutWidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("salvar produtos.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCadastrar.setIcon(icon1)
        self.btnCadastrar.setIconSize(QtCore.QSize(25, 25))
        self.btnCadastrar.setObjectName("btnCadastrar")
        self.horizontalLayout.addWidget(self.btnCadastrar)
        self.btnLimpar = QtWidgets.QPushButton(self.layoutWidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("borracha.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnLimpar.setIcon(icon2)
        self.btnLimpar.setIconSize(QtCore.QSize(25, 25))
        self.btnLimpar.setObjectName("btnLimpar")
        self.horizontalLayout.addWidget(self.btnLimpar)
        self.editDescricao = QtWidgets.QLineEdit(self.centralwidget)
        self.editDescricao.setGeometry(QtCore.QRect(80, 54, 191, 20))
        self.editDescricao.setInputMask("")
        self.editDescricao.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.editDescricao.setObjectName("editDescricao")
        self.tipoComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.tipoComboBox.setGeometry(QtCore.QRect(280, 54, 100, 20))
        self.tipoComboBox.setObjectName("tipoComboBox")
        self.tipoComboBox.addItem("")
        self.tipoComboBox.addItem("")
        self.tipoComboBox.addItem("")
        FormAlterarProduto.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(FormAlterarProduto)
        self.statusbar.setObjectName("statusbar")
        FormAlterarProduto.setStatusBar(self.statusbar)

        self.retranslateUi(FormAlterarProduto)
        self.btnLimpar.clicked.connect(self.editDescricao.clear)
        self.btnLimpar.clicked.connect(self.precoSpinBox.clear)
        #SO FUNCIONA SAINDO DO FORM PRODUTOS...
        self.btnCadastrar.clicked.connect(self.click_btn_salvar)

        QtCore.QMetaObject.connectSlotsByName(FormAlterarProduto)
        FormAlterarProduto.setTabOrder(self.editDescricao, self.tipoComboBox)
        FormAlterarProduto.setTabOrder(self.tipoComboBox, self.precoSpinBox)
        FormAlterarProduto.setTabOrder(self.precoSpinBox, self.btnCadastrar)
        FormAlterarProduto.setTabOrder(self.btnCadastrar, self.btnLimpar)

    def retranslateUi(self, FormAlterarProduto):
        _translate = QtCore.QCoreApplication.translate
        FormAlterarProduto.setWindowTitle(_translate("FormAlterarProduto", "Cadastrar Produto"))
        self.label.setText(_translate("FormAlterarProduto", "Alterar Produto"))
        self.labelPreco.setText(_translate("FormAlterarProduto", "R$:"))
        self.labelDescricao.setText(_translate("FormAlterarProduto", "Descrição:"))
        self.btnCadastrar.setText(_translate("FormAlterarProduto", "Salvar"))
        self.btnLimpar.setText(_translate("FormAlterarProduto", "Limpar"))
        self.tipoComboBox.setItemText(0, _translate("FormAlterarProduto", "COMIDA"))
        self.tipoComboBox.setItemText(1, _translate("FormAlterarProduto", "BEBIDA"))
        self.tipoComboBox.setItemText(2, _translate("FormAlterarProduto", "SORVETE/AÇAI"))

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_FormAlterarProduto()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())