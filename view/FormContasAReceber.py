from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from view.FormDevedores import Ui_FormDevedores
from view.FormTitulos import Ui_FormTitulos

class Ui_FormContasReceber(object):

    def click_btn_devedores(self):
        self.formdevedores = QMainWindow()
        self.ui = Ui_FormDevedores()
        self.ui.setupUi(self.formdevedores)
        self.formdevedores.show()

    def click_btn_lancar_Credito(self):
        self.formlancar = QMainWindow()
        self.ui = Ui_FormTitulos()
        self.ui.setupUi(self.formlancar)
        self.formlancar.show()

    def setupUi(self, FormContasReceber):
        FormContasReceber.setObjectName("FormContasReceber")
        FormContasReceber.resize(379, 239)
        self.label = QtWidgets.QLabel(FormContasReceber)
        self.label.setGeometry(QtCore.QRect(120, 20, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btnDevedores = QtWidgets.QPushButton(FormContasReceber)
        self.btnDevedores.setGeometry(QtCore.QRect(50, 110, 121, 41))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("devedor.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnDevedores.setIcon(icon)
        self.btnDevedores.setIconSize(QtCore.QSize(30, 30))
        self.btnDevedores.setObjectName("btnDevedores")
        self.btnLancarCredito = QtWidgets.QPushButton(FormContasReceber)
        self.btnLancarCredito.setGeometry(QtCore.QRect(210, 110, 121, 41))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("credit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnLancarCredito.setIcon(icon1)
        self.btnLancarCredito.setIconSize(QtCore.QSize(30, 30))
        self.btnLancarCredito.setObjectName("btnLancarCredito")


        self.btnDevedores.clicked.connect(self.click_btn_devedores)
        self.btnLancarCredito.clicked.connect(self.click_btn_lancar_Credito)

        self.retranslateUi(FormContasReceber)
        QtCore.QMetaObject.connectSlotsByName(FormContasReceber)

    def retranslateUi(self, FormContasReceber):
        _translate = QtCore.QCoreApplication.translate
        FormContasReceber.setWindowTitle(_translate("FormContasReceber", "Contas a Receber"))
        self.label.setText(_translate("FormContasReceber", "Contas a Receber"))
        self.btnDevedores.setText(_translate("FormContasReceber", "Devedores"))
        self.btnLancarCredito.setText(_translate("FormContasReceber", "Lançar Crédito"))

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    dialog = QMainWindow()
    ui = Ui_FormContasReceber()
    ui.setupUi(dialog)
    dialog.show()
    sys.exit(app.exec_())