from PyQt5.QtWidgets import QMainWindow, QApplication, QAbstractItemView, QTableWidgetItem, QDialog
from PyQt5.QtCore import Qt
from controller.VendaCTR import VendaCTR
from PyQt5 import QtCore, QtGui, QtWidgets, QtPrintSupport
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter, QPrintPreviewDialog

class Ui_FormDevedores(object):

    def handlePrint(self):
        dialog = QtPrintSupport.QPrintDialog()
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.handlePaintRequest(dialog.printer())

    def handlePreview(self):
        dialog = QtPrintSupport.QPrintPreviewDialog()
        dialog.paintRequested.connect(self.handlePaintRequest)
        dialog.exec_()

    def handlePaintRequest(self, printer):
        document = QtGui.QTextDocument()
         # documento = QtWidgets.QTextEdit()
        # cursor2 = QtGui.QTextCursor(documento)
        cursor = QtGui.QTextCursor(document)

        """table1 = cursor.insertTable(1, self.tableDevedores.columnCount())
                cursor.insertText('CÓD.VENDA')
                cursor.movePosition(QtGui.QTextCursor.NextCell)
                cursor.insertText('CÓD. CLIENTE')
                cursor.movePosition(QtGui.QTextCursor.NextCell)
                cursor.insertText('CLIENTE')
                cursor.movePosition(QtGui.QTextCursor.NextCell)
                cursor.insertText('A PAGAR')
                cursor.movePosition(QtGui.QTextCursor.NextCell) """
        table = cursor.insertTable(self.tableDevedores.rowCount(), self.tableDevedores.columnCount())
        for row in range(table.rows()):
            for col in range(table.columns()):
                item = self.tableDevedores.item(row, col).text()
                cursor.insertText(item)
                cursor.movePosition(QtGui.QTextCursor.NextCell)


        document.print_(printer)

    def click_btn_pesquisar_cliente(self):
        nome = self.editPesquisaCliente.text()
        item = QTableWidgetItem
        if (nome == ''):
            self.tableDevedores.setRowCount(0)
            result = VendaCTR.pesquisar_todos_devedores()
            for num_linha, linha_conteudo in enumerate(result):
                self.tableDevedores.insertRow(num_linha)
                for num_coluna, coluna_conteudo in enumerate(linha_conteudo):
                    self.tableDevedores.setItem(num_linha, num_coluna, item(str(coluna_conteudo)))

        elif (nome != ''):
            result = VendaCTR.pesquisar_devedor(nome)
            self.tableDevedores.setRowCount(0)
            for num_linha, linha_conteudo in enumerate(result):
                self.tableDevedores.insertRow(num_linha)
                for num_coluna, coluna_conteudo in enumerate(linha_conteudo):
                    self.tableDevedores.setItem(num_linha, num_coluna, item(str(coluna_conteudo)))

    def setupUi(self, FormDevedores):
        FormDevedores.setObjectName("FormDevedores")
        FormDevedores.resize(601, 471)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("contas a receber.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FormDevedores.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(FormDevedores)
        self.centralwidget.setObjectName("centralwidget")
        self.labelCliente = QtWidgets.QLabel(self.centralwidget)
        self.labelCliente.setGeometry(QtCore.QRect(20, 20, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelCliente.setFont(font)
        self.labelCliente.setObjectName("labelCliente")
        self.editPesquisaCliente = QtWidgets.QLineEdit(self.centralwidget)
        self.editPesquisaCliente.setGeometry(QtCore.QRect(70, 20, 331, 21))
        self.editPesquisaCliente.setText("")
        self.editPesquisaCliente.setObjectName("editPesquisaCliente")
        self.tableDevedores = QtWidgets.QTableWidget(self.centralwidget)
        self.tableDevedores.setGeometry(QtCore.QRect(10, 70, 581, 301))
        self.tableDevedores.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableDevedores.setAutoFillBackground(False)
        self.tableDevedores.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableDevedores.setGridStyle(QtCore.Qt.SolidLine)
        self.tableDevedores.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableDevedores.setTextElideMode(Qt.ElideRight)
        self.tableDevedores.setWordWrap(False)
        self.tableDevedores.setSortingEnabled(False)
        self.tableDevedores.horizontalHeader().setDefaultAlignment(Qt.AlignHCenter | Qt.AlignVCenter |
                                                                   Qt.AlignCenter)
        self.tableDevedores.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableDevedores.horizontalHeader().setStretchLastSection(True)
        self.tableDevedores.setGridStyle(QtCore.Qt.SolidLine)
        self.tableDevedores.setRowCount(0)
        self.tableDevedores.setObjectName("tableDevedores")
        self.tableDevedores.setColumnCount(4)
        self.tableDevedores.setColumnWidth(0, 80)
        self.tableDevedores.setColumnWidth(1, 100)
        self.tableDevedores.setColumnWidth(2, 250)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableDevedores.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableDevedores.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableDevedores.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableDevedores.setHorizontalHeaderItem(3, item)
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(420, 15, 166, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnPesquisarCliente = QtWidgets.QPushButton(self.layoutWidget)
        self.btnPesquisarCliente.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnPesquisarCliente.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("lupa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPesquisarCliente.setIcon(icon1)
        self.btnPesquisarCliente.setIconSize(QtCore.QSize(16, 16))
        self.btnPesquisarCliente.setObjectName("btnPesquisarCliente")
        self.horizontalLayout.addWidget(self.btnPesquisarCliente)
        self.btnLimpar = QtWidgets.QPushButton(self.layoutWidget)
        self.btnLimpar.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnLimpar.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("borracha.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnLimpar.setIcon(icon2)
        self.btnLimpar.setIconSize(QtCore.QSize(16, 16))
        self.btnLimpar.setObjectName("btnLimpar")
        self.horizontalLayout.addWidget(self.btnLimpar)
        self.btnExportar = QtWidgets.QPushButton(self.centralwidget)
        self.btnExportar.setGeometry(QtCore.QRect(160, 390, 269, 38))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnExportar.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("pdf.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnExportar.setIcon(icon3)
        self.btnExportar.setIconSize(QtCore.QSize(30, 30))
        self.btnExportar.setObjectName("btnExportar")
        FormDevedores.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(FormDevedores)
        self.statusbar.setObjectName("statusbar")
        FormDevedores.setStatusBar(self.statusbar)

        self.retranslateUi(FormDevedores)
        self.btnLimpar.clicked.connect(self.editPesquisaCliente.clear)
        self.btnPesquisarCliente.clicked.connect(self.click_btn_pesquisar_cliente)
        self.btnExportar.clicked.connect(self.handlePreview)

        QtCore.QMetaObject.connectSlotsByName(FormDevedores)
        FormDevedores.setTabOrder(self.editPesquisaCliente, self.btnPesquisarCliente)
        FormDevedores.setTabOrder(self.btnPesquisarCliente, self.btnLimpar)
        FormDevedores.setTabOrder(self.btnLimpar, self.tableDevedores)

    def retranslateUi(self, FormDevedores):
        _translate = QtCore.QCoreApplication.translate
        FormDevedores.setWindowTitle(_translate("FormDevedores", "Devedores"))
        self.labelCliente.setText(_translate("FormDevedores", "Cliente:"))
        item = self.tableDevedores.horizontalHeaderItem(0)
        item.setText(_translate("FormDevedores", "CÓD. VENDA"))
        item = self.tableDevedores.horizontalHeaderItem(1)
        item.setText(_translate("FormDevedores", "CÓD. CLIENTE"))
        item = self.tableDevedores.horizontalHeaderItem(2)
        item.setText(_translate("FormDevedores", "CLIENTE"))
        item = self.tableDevedores.horizontalHeaderItem(3)
        item.setText(_translate("FormDevedores", "A PAGAR"))
        self.btnPesquisarCliente.setText(_translate("FormDevedores", "Pesquisar"))
        self.btnLimpar.setText(_translate("FormDevedores", "Limpar"))
        self.btnExportar.setText(_translate("FormDevedores", "Exportar"))

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    teste = QMainWindow()
    ui = Ui_FormDevedores()
    ui.setupUi(teste)
    teste.show()
    sys.exit(app.exec_())