from view.FormPrincipal import *
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    FormPrincipal = QMainWindow()
    ui = Ui_FormPrincipal()
    ui.setupUi(FormPrincipal)
    FormPrincipal.show()
    sys.exit(app.exec_())