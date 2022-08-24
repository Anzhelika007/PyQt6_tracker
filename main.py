# from tracker import *
#
# import sys
#
# app = QtWidgets.QApplication(sys.argv)
# MainWindow = QtWidgets.QMainWindow()
# ui = Ui_MainWindow()
# ui.setupUi(MainWindow)
# MainWindow.show()
#
# ui.label.setText('erthtzrjnsymzgs')
#
# sys.exit(app.exec())


from PyQt5 import uic
from PyQt5.QtWidgets import QApplication


Form, Window = uic.loadUiType('tracker.ui')


app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

def on_click():
    print(form.plainTextEdit.toPlainText())
    print(form.dateEdit.dateTime().toString('dd-MM-yyyy'))
    print('Cliked!!!')

form.pushButton.clicked.connect(on_click)


#form.label.setText('erthtzrjnsymzgs')


app.exec_()


