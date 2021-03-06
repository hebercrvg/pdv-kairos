from PyQt5.Qt import QApplication, QMainWindow, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
import locale
from controller.ProdutoCTR import ProdutoCTR

class Ui_FormCadastrarProduto(object):

    def click_btn_cadastrar(self):
        descricao = self.editDescricao.text()
        tipo = self.tipoComboBox.currentText()
        preco = self.precoSpinBox.value()
        ProdutoCTR.Cadastrar_Produto(descricao, tipo, preco)

    def setupUi(self, FormCadastrarProduto):
        FormCadastrarProduto.setObjectName("FormCadastrarProduto")
        FormCadastrarProduto.resize(476, 205)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("listar produtos.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FormCadastrarProduto.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(FormCadastrarProduto)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 10, 151, 23))
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
        FormCadastrarProduto.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(FormCadastrarProduto)
        self.statusbar.setObjectName("statusbar")
        FormCadastrarProduto.setStatusBar(self.statusbar)

        self.retranslateUi(FormCadastrarProduto)
        self.btnLimpar.clicked.connect(self.editDescricao.clear)
        self.btnLimpar.clicked.connect(self.precoSpinBox.clear)
        self.btnCadastrar.clicked.connect(self.click_btn_cadastrar)

        QtCore.QMetaObject.connectSlotsByName(FormCadastrarProduto)
        FormCadastrarProduto.setTabOrder(self.editDescricao, self.tipoComboBox)
        FormCadastrarProduto.setTabOrder(self.tipoComboBox, self.precoSpinBox)
        FormCadastrarProduto.setTabOrder(self.precoSpinBox, self.btnCadastrar)
        FormCadastrarProduto.setTabOrder(self.btnCadastrar, self.btnLimpar)

    def retranslateUi(self, FormCadastrarProduto):
        _translate = QtCore.QCoreApplication.translate
        FormCadastrarProduto.setWindowTitle(_translate("FormCadastrarProduto", "Cadastrar Produto"))
        self.label.setText(_translate("FormCadastrarProduto", "Cadastrar Produto"))
        self.labelPreco.setText(_translate("FormCadastrarProduto", "R$:"))
        self.labelDescricao.setText(_translate("FormCadastrarProduto", "Descrição:"))
        self.btnCadastrar.setText(_translate("FormCadastrarProduto", "Cadastrar"))
        self.btnLimpar.setText(_translate("FormCadastrarProduto", "Limpar"))
        self.tipoComboBox.setItemText(0, _translate("FormCadastrarProduto", "COMIDA"))
        self.tipoComboBox.setItemText(1, _translate("FormCadastrarProduto", "BEBIDA"))
        self.tipoComboBox.setItemText(2, _translate("FormCadastrarProduto", "SORVETE/AÇAI"))

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_FormCadastrarProduto()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())