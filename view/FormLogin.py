from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from view.FormPrincipal import Ui_FormPrincipal
from view.FormMenuPrincipal import Ui_FormMenuPrincipal
from controller.UsuarioCTR import UsuarioCTR

class Ui_FormLogin(object):
    def click_btn_login(self):
        usuario = self.editUsuario.text()
        senha = self.editSenha.text()
        aux = UsuarioCTR.autentica_usuario(usuario, senha)
        if (aux == True):
            self.formprincipal = QMainWindow()
            self.ui = Ui_FormMenuPrincipal()
            self.ui.setupUi(self.formprincipal)
            self.formprincipal.showMaximized()
            FormLogin.close()


        elif(aux == False):
            msg = QMessageBox(None)
            msg.setWindowTitle("Erro")
            msg.setWindowIcon(QtGui.QIcon("key.png"))
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Senha incorreta.")
            msg.exec_()
            self.editUsuario.clear()
            self.editSenha.clear()


    def setupUi(self, formLogin):
        global FormLogin
        FormLogin = formLogin
        FormLogin.setObjectName("FormLogin")
        FormLogin.resize(432, 148)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("login.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FormLogin.setWindowIcon(icon)
        FormLogin.setStyleSheet("background-color: rgb(13, 42, 172);")
        self.btnEntrar = QtWidgets.QPushButton(FormLogin)
        self.btnEntrar.setGeometry(QtCore.QRect(350, 60, 75, 23))
        self.btnEntrar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btnEntrar.setObjectName("btnEntrar")
        self.btnSair = QtWidgets.QPushButton(FormLogin)
        self.btnSair.setGeometry(QtCore.QRect(350, 90, 75, 23))
        self.btnSair.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btnSair.setObjectName("btnSair")
        self.labelKey = QtWidgets.QLabel(FormLogin)
        self.labelKey.setGeometry(QtCore.QRect(10, 30, 91, 101))
        self.labelKey.setStyleSheet("image: url(key.png);")
        self.labelKey.setText("")
        self.labelKey.setObjectName("labelKey")
        self.layoutWidget = QtWidgets.QWidget(FormLogin)
        self.layoutWidget.setGeometry(QtCore.QRect(120, 20, 191, 96))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelUsuario = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelUsuario.setFont(font)
        self.labelUsuario.setStyleSheet("color: rgb(255, 255, 255);")
        self.labelUsuario.setObjectName("labelUsuario")
        self.verticalLayout.addWidget(self.labelUsuario)
        self.editUsuario = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.editUsuario.setFont(font)
        self.editUsuario.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.editUsuario.setObjectName("editUsuario")
        self.verticalLayout.addWidget(self.editUsuario)
        self.labelSenha = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelSenha.setFont(font)
        self.labelSenha.setStyleSheet("color: rgb(255, 255, 255);")
        self.labelSenha.setObjectName("labelSenha")
        self.verticalLayout.addWidget(self.labelSenha)
        self.editSenha = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.editSenha.setFont(font)
        self.editSenha.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.editSenha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.editSenha.setObjectName("editSenha")
        self.verticalLayout.addWidget(self.editSenha)

        self.retranslateUi(FormLogin)
        self.btnEntrar.clicked.connect(self.click_btn_login)
        self.btnSair.clicked.connect(FormLogin.close)
        QtCore.QMetaObject.connectSlotsByName(FormLogin)

    def retranslateUi(self, FormLogin):
        _translate = QtCore.QCoreApplication.translate
        FormLogin.setWindowTitle(_translate("FormLogin", "Entrar"))
        self.btnEntrar.setText(_translate("FormLogin", "Entrar"))
        self.btnSair.setText(_translate("FormLogin", "Sair"))
        self.labelUsuario.setText(_translate("FormLogin", "Usuário:"))
        self.labelSenha.setText(_translate("FormLogin", "Senha:"))

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    tela = QDialog()
    ui = Ui_FormLogin()
    ui.setupUi(tela)
    tela.show()
    sys.exit(app.exec_())