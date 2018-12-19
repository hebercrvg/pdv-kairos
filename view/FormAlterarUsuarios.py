from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from controller.UsuarioCTR import UsuarioCTR

class Ui_FormAlterarUsuario(object):

    def preencher_campos(self, codusuario, usuario):
        self.codusuario = codusuario

        self.editUsuario.setText(usuario)
    def click_btn_salvar(self):
        codusuario = self.codusuario
        usuario = self.editUsuario.text()
        senha = self.editSenha.text()
        UsuarioCTR.alterar_usuario(codusuario, usuario, senha)

    def setupUi(self, FormAlterarUsuario):

        FormAlterarUsuario.setObjectName("FormAlterarUsuario")
        FormAlterarUsuario.resize(489, 260)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("cadastrar usuario 2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FormAlterarUsuario.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(FormAlterarUsuario)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 20, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(140, 170, 168, 35))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.btnSalvar = QtWidgets.QPushButton(self.layoutWidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("salvar usuario.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSalvar.setIcon(icon1)
        self.btnSalvar.setIconSize(QtCore.QSize(25, 25))
        self.btnSalvar.setObjectName("btnSalvar")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.btnSalvar)
        self.btnLimpar = QtWidgets.QPushButton(self.layoutWidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("borracha.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnLimpar.setIcon(icon2)
        self.btnLimpar.setIconSize(QtCore.QSize(25, 25))
        self.btnLimpar.setObjectName("btnLimpar")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.btnLimpar)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(90, 70, 311, 86))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelUsuario = QtWidgets.QLabel(self.layoutWidget1)
        self.labelUsuario.setObjectName("labelUsuario")
        self.verticalLayout.addWidget(self.labelUsuario)
        self.editUsuario = QtWidgets.QLineEdit(self.layoutWidget1)
        self.editUsuario.setInputMask("")
        self.editUsuario.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.editUsuario.setObjectName("editUsuario")
        self.verticalLayout.addWidget(self.editUsuario)
        self.labelSenha = QtWidgets.QLabel(self.layoutWidget1)
        self.labelSenha.setObjectName("labelSenha")
        self.verticalLayout.addWidget(self.labelSenha)
        self.editSenha = QtWidgets.QLineEdit(self.layoutWidget1)
        self.editSenha.setInputMask("")
        self.editSenha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.editSenha.setObjectName("editSenha")
        self.verticalLayout.addWidget(self.editSenha)
        FormAlterarUsuario.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(FormAlterarUsuario)
        self.statusbar.setObjectName("statusbar")
        FormAlterarUsuario.setStatusBar(self.statusbar)

        self.retranslateUi(FormAlterarUsuario)
        self.btnLimpar.clicked.connect(self.editUsuario.clear)
        self.btnSalvar.clicked.connect(self.click_btn_salvar)
        QtCore.QMetaObject.connectSlotsByName(FormAlterarUsuario)
        FormAlterarUsuario.setTabOrder(self.editUsuario, self.btnSalvar)
        FormAlterarUsuario.setTabOrder(self.btnSalvar, self.btnLimpar)

    def retranslateUi(self, FormAlterarUsuario):
        _translate = QtCore.QCoreApplication.translate
        FormAlterarUsuario.setWindowTitle(_translate("FormAlterarUsuario", "Alterar Usuário"))
        self.label.setText(_translate("FormAlterarUsuario", "Alterar Usuário"))
        self.btnSalvar.setText(_translate("FormAlterarUsuario", "Cadastrar"))
        self.btnLimpar.setText(_translate("FormAlterarUsuario", "Limpar"))
        self.labelUsuario.setText(_translate("FormAlterarUsuario", "Usuário:"))
        self.labelSenha.setText(_translate("FormAlterarUsuario", "Senha:"))


