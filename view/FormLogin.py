from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from view.FormPrincipal import Ui_FormPrincipal
from controller.UsuarioCTR import UsuarioCTR

class Ui_FormLogin(object):

    def click_btn_login(self):
        usuario = self.editUsuario.text()
        senha = self.editSenha.text()
        aux = UsuarioCTR.autentica_usuario(usuario, senha)
        if (aux == True):
            self.formprincipal = QMainWindow()
            self.ui = Ui_FormPrincipal()
            self.ui.setupUi(self.formprincipal)
            self.formprincipal.show()
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
        self.pushButton = QtWidgets.QPushButton(FormLogin)
        self.pushButton.setGeometry(QtCore.QRect(350, 60, 75, 23))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(FormLogin)
        self.pushButton_2.setGeometry(QtCore.QRect(350, 90, 75, 23))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(FormLogin)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 91, 101))
        self.label_3.setStyleSheet("image: url(key.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.widget = QtWidgets.QWidget(FormLogin)
        self.widget.setGeometry(QtCore.QRect(120, 20, 191, 96))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.editUsuario = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.editUsuario.setFont(font)
        self.editUsuario.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.editUsuario.setObjectName("editUsuario")
        self.verticalLayout.addWidget(self.editUsuario)
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.editSenha = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.editSenha.setFont(font)
        self.editSenha.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.editSenha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.editSenha.setObjectName("editSenha")
        self.verticalLayout.addWidget(self.editSenha)

        self.pushButton.clicked.connect(self.click_btn_login)

        self.pushButton_2.clicked.connect(FormLogin.reject)

        self.retranslateUi(FormLogin)
        QtCore.QMetaObject.connectSlotsByName(FormLogin)


    def retranslateUi(self, FormLogin):
        _translate = QtCore.QCoreApplication.translate
        FormLogin.setWindowTitle(_translate("FormLogin", "Entrar"))
        self.pushButton.setText(_translate("FormLogin", "Entrar"))
        self.pushButton_2.setText(_translate("FormLogin", "Sair"))
        self.label.setText(_translate("FormLogin", "Usuário:"))
        self.label_2.setText(_translate("FormLogin", "Senha:"))


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    tela = QDialog()
    ui = Ui_FormLogin()
    ui.setupUi(tela)
    tela.show()
    sys.exit(app.exec_())