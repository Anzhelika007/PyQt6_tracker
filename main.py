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
from PyQt5.QtCore import QDate
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
    # print(form.calendarWidget.selectedDate().toString('dd-MM-yyyy'))
    # date = QDate(2022, 9, 17)
    # form.calendarWidget.setSelectedDate(date)


def on_click_calendar():
    # меняем дату в dateEdit на дату выбранную в календаре
    print(form.calendarWidget.selectedDate().toString('dd-MM-yyyy'))
    form.dateEdit.setDate(form.calendarWidget.selectedDate())

def on_dateedit_changer():
    # меняем дату в календаре на дату в dateEdit
    print(form.dateEdit.dateTime().toString('dd-MM-yyyy'))
    form.calendarWidget.setSelectedDate(form.dateEdit.date())

form.pushButton.clicked.connect(on_click)
form.calendarWidget.clicked.connect(on_click_calendar)
form.dateEdit.dateChanged.connect(on_dateedit_changer)

#form.label.setText('erthtzrjnsymzgs')


app.exec_()


