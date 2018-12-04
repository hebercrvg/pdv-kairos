from controller.ClienteCTR import ClienteCTR
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog

class Ui_FormAlterarCliente(object):

    def click_btn_salvar(self):
        Codcli = self.Codcli
        nome = self.editNome.text()
        telefone = self.editTelefone.text()
        ClienteCTR.alterar_cliente(Codcli, nome, telefone)

    def preencher_campos(self, codcli, nome, telefone):
        self.Codcli = codcli
        self.editNome.setText(nome)
        self.editTelefone.setText(telefone)

    def setupUi(self, FormCadastrarCliente):

        FormCadastrarCliente.setObjectName("FormCadastrarCliente")
        FormCadastrarCliente.resize(489, 205)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("cadastrar usuario 2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FormCadastrarCliente.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(FormCadastrarCliente)
        self.centralwidget.setObjectName("centralwidget")
        self.labelNome = QtWidgets.QLabel(self.centralwidget)
        self.labelNome.setGeometry(QtCore.QRect(75, 79, 31, 16))
        self.labelNome.setObjectName("labelNome")
        self.labelTelefone = QtWidgets.QLabel(self.centralwidget)
        self.labelTelefone.setGeometry(QtCore.QRect(75, 105, 46, 16))
        self.labelTelefone.setObjectName("labelTelefone")
        self.editTelefone = QtWidgets.QLineEdit(self.centralwidget)
        self.editTelefone.setGeometry(QtCore.QRect(127, 105, 91, 20))
        self.editTelefone.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.editTelefone.setObjectName("editTelefone")
        self.editNome = QtWidgets.QLineEdit(self.centralwidget)
        self.editNome.setGeometry(QtCore.QRect(127, 79, 291, 20))
        self.editNome.setInputMask("")
        self.editNome.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.editNome.setObjectName("editNome")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 20, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(154, 138, 168, 35))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.btnCadastrar = QtWidgets.QPushButton(self.layoutWidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("salvar usuario.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCadastrar.setIcon(icon1)
        self.btnCadastrar.setIconSize(QtCore.QSize(25, 25))
        self.btnCadastrar.setObjectName("btnCadastrar")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.btnCadastrar)
        self.btnLimpar = QtWidgets.QPushButton(self.layoutWidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("borracha.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnLimpar.setIcon(icon2)
        self.btnLimpar.setIconSize(QtCore.QSize(25, 25))
        self.btnLimpar.setObjectName("btnLimpar")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.btnLimpar)
        FormCadastrarCliente.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(FormCadastrarCliente)
        self.statusbar.setObjectName("statusbar")
        FormCadastrarCliente.setStatusBar(self.statusbar)

        self.retranslateUi(FormCadastrarCliente)
        self.btnLimpar.clicked.connect(self.editNome.clear)
        self.btnLimpar.clicked.connect(self.editTelefone.clear)
        self.btnCadastrar.clicked.connect(self.click_btn_salvar)

        QtCore.QMetaObject.connectSlotsByName(FormCadastrarCliente)
        FormCadastrarCliente.setTabOrder(self.editNome, self.editTelefone)
        FormCadastrarCliente.setTabOrder(self.editTelefone, self.btnCadastrar)
        FormCadastrarCliente.setTabOrder(self.btnCadastrar, self.btnLimpar)

    def retranslateUi(self, FormCadastrarCliente):
        _translate = QtCore.QCoreApplication.translate
        FormCadastrarCliente.setWindowTitle(_translate("FormCadastrarCliente", "Cadastrar Cliente"))
        self.labelNome.setText(_translate("FormCadastrarCliente", "Nome:"))
        self.labelTelefone.setText(_translate("FormCadastrarCliente", "Telefone:"))
        self.editTelefone.setInputMask(_translate("FormCadastrarCliente", "(00)00000-0000"))
        self.label.setText(_translate("FormCadastrarCliente", "Alterar Cliente"))
        self.btnCadastrar.setText(_translate("FormCadastrarCliente", "Salvar"))
        self.btnLimpar.setText(_translate("FormCadastrarCliente", "Limpar"))


#NAO VAI EXECUTAR DIRETO NO MODULO POIS NECESSITA DE PARAMETROS ORIUNDOS DO MODULO FORMCLIENTES PARA EXECUTAR
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_FormAlterarCliente()
    ui.setupUi(MainWindow, 0, 'nome', 'telefone')
    MainWindow.show()
    sys.exit(app.exec_())
