from PyQt5.Qt import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import locale
from controller.ProdutoCTR import ProdutoCTR

class Ui_FormCadastrarProduto(object):

    def click_btn_cadastrar(self):
        descricao = self.editDescricao.text()
        tipo = self.comboBox.currentText()
        preco = self.precoDoubleSpinBox.text()
        preco = float(preco.replace(",","."))
        Preco = float(preco)
        print("{}, {}, {}".format(descricao, tipo, Preco))



    def setupUi(self, FormCadastrarProduto):
        FormCadastrarProduto.setObjectName("FormCadastrarProduto")
        FormCadastrarProduto.resize(489, 205)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../img/listar produtos.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.labelPreco.setGeometry(QtCore.QRect(50, 80, 31, 16))
        self.labelPreco.setObjectName("labelPreco")
        self.precoDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.precoDoubleSpinBox.setGeometry(QtCore.QRect(90, 80, 71, 20))
        self.precoDoubleSpinBox.setSuffix("")
        self.precoDoubleSpinBox.setMaximum(99.99)
        self.precoDoubleSpinBox.setObjectName("precoDoubleSpinBox")
        self.labelDescricao = QtWidgets.QLabel(self.centralwidget)
        self.labelDescricao.setGeometry(QtCore.QRect(30, 53, 50, 16))
        self.labelDescricao.setObjectName("labelDescricao")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(140, 120, 168, 35))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnCadastrar = QtWidgets.QPushButton(self.widget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:\dev\pdv-kairos\img\salvar produtos.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCadastrar.setIcon(icon1)
        self.btnCadastrar.setIconSize(QtCore.QSize(25, 25))
        self.btnCadastrar.setObjectName("btnCadastrar")
        self.horizontalLayout.addWidget(self.btnCadastrar)
        self.btnLimpar = QtWidgets.QPushButton(self.widget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(r"C:\dev\pdv-kairos\img\borracha.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnLimpar.setIcon(icon2)
        self.btnLimpar.setIconSize(QtCore.QSize(25, 25))
        self.btnLimpar.setObjectName("btnLimpar")
        self.horizontalLayout.addWidget(self.btnLimpar)
        self.editDescricao = QtWidgets.QLineEdit(self.centralwidget)
        self.editDescricao.setGeometry(QtCore.QRect(90, 54, 181, 20))
        self.editDescricao.setInputMask("")
        self.editDescricao.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.editDescricao.setObjectName("editDescricao")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(280, 54, 100, 20))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        FormCadastrarProduto.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(FormCadastrarProduto)
        self.statusbar.setObjectName("statusbar")
        FormCadastrarProduto.setStatusBar(self.statusbar)

        self.retranslateUi(FormCadastrarProduto)
        self.btnLimpar.clicked.connect(self.editDescricao.clear)
        self.btnLimpar.clicked.connect(self.precoDoubleSpinBox.clear)
        self.btnCadastrar.clicked.connect(self.click_btn_cadastrar)



        QtCore.QMetaObject.connectSlotsByName(FormCadastrarProduto)
        FormCadastrarProduto.setTabOrder(self.editDescricao, self.btnCadastrar)

    def retranslateUi(self, FormCadastrarProduto):
        _translate = QtCore.QCoreApplication.translate
        FormCadastrarProduto.setWindowTitle(_translate("FormCadastrarProduto", "Cadastrar Produto"))
        self.label.setText(_translate("FormCadastrarProduto", "Cadastrar Produto"))
        self.labelPreco.setText(_translate("FormCadastrarProduto", "Preço:"))
        self.precoDoubleSpinBox.setPrefix(_translate("FormCadastrarProduto", "R$ "))
        self.labelDescricao.setText(_translate("FormCadastrarProduto", "Descrição:"))
        self.btnCadastrar.setText(_translate("FormCadastrarProduto", "Cadastrar"))
        self.btnLimpar.setText(_translate("FormCadastrarProduto", "Limpar"))
        self.comboBox.setItemText(0, _translate("FormCadastrarProduto", "COMIDA"))
        self.comboBox.setItemText(1, _translate("FormCadastrarProduto", "BEBIDA"))
        self.comboBox.setItemText(2, _translate("FormCadastrarProduto", "SORVETE/AÇAI"))

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_FormCadastrarProduto()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())