# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FormLogin.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FormLogin(object):
    def setupUi(self, FormLogin):
        FormLogin.setObjectName("FormLogin")
        FormLogin.resize(432, 148)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../img/login.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.label_3.setStyleSheet("image: url(:/newPrefix/key.png);")
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

        self.retranslateUi(FormLogin)
        self.pushButton.clicked.connect(FormLogin.accept)
        QtCore.QMetaObject.connectSlotsByName(FormLogin)

    def retranslateUi(self, FormLogin):
        _translate = QtCore.QCoreApplication.translate
        FormLogin.setWindowTitle(_translate("FormLogin", "Entrar"))
        self.pushButton.setText(_translate("FormLogin", "Entrar"))
        self.pushButton_2.setText(_translate("FormLogin", "Sair"))
        self.label.setText(_translate("FormLogin", "Usuário:"))
        self.label_2.setText(_translate("FormLogin", "Senha:"))

import ket_rc
