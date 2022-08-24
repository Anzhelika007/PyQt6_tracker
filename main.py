import sys
from PyQt6.QtWidgets import QApplication, QDialog, QMessageBox
from ui_imagedialog import Ui_ImageDialog

app = QApplication(sys.argv)
window = QDialog()
ui = Ui_ImageDialog()
ui.setupUi(window)

window.show()

#-----------------------------------------------------------------------
# модальное окно
msg = QMessageBox().critical(window, 'Title', 'Some info',
                             QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
# выведем нажатую кнопку
print(msg)

#----------------------------------------------------------------------
# обычное информационное модальное окно
msgBox = QMessageBox()
msgBox.setWindowTitle('Hi this is my title')
msgBox.setText("The document has been modified.")
msgBox.setInformativeText("Do you want to save your changes?")
msgBox.setStandardButtons(
    QMessageBox.StandardButton.Save | QMessageBox.StandardButton.Discard | QMessageBox.StandardButton.Cancel)
msgBox.setDefaultButton(QMessageBox.StandardButton.Save)
ret = msgBox.exec()
print(ret)

sys.exit(app.exec())
