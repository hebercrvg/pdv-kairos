from PyQt5.QtWidgets import QDialog
from view.FormLogin import *
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = QDialog()
    ui = Ui_FormLogin()
    ui.setupUi(dialog)
    dialog.show()
    sys.exit(app.exec_())