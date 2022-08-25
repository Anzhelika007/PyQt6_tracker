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
    global start_date, calc_date

    # меняем дату в dateEdit на дату выбранную в календаре
    #print(form.calendarWidget.selectedDate().toString('dd-MM-yyyy'))
    form.dateEdit.setDate(form.calendarWidget.selectedDate())

    # расчет количества оставшихся дней до события метод daysTo
    calc_date = form.calendarWidget.selectedDate()
    delta_days = start_date.daysTo(calc_date)
    print(delta_days)
    # меняем значение поля
    form.label_3.setText("До наступления события осталось: %s дней" % delta_days)


def on_dateedit_changer():
    global start_date, calc_date
    # меняем дату в календаре на дату в dateEdit
    #print(form.dateEdit.dateTime().toString('dd-MM-yyyy'))
    form.calendarWidget.setSelectedDate(form.dateEdit.date())

    # расчет количества оставшихся дней до события метод daysTo / изменили значение calc_date
    calc_date = form.dateEdit.date()
    delta_days = start_date.daysTo(calc_date)
    print(delta_days)
    # меняем значение поля
    form.label_3.setText("До наступления события осталось: %s дней" % delta_days)




# при наступлении указанного события (clicked, dateChanged) вызываем ранее описанные функции (on_click, on_click_calendar, on_dateedit_changer)
form.pushButton.clicked.connect(on_click)
form.calendarWidget.clicked.connect(on_click_calendar)
form.dateEdit.dateChanged.connect(on_dateedit_changer)

# создадим 2 переменные для отображения сколько дней нам осталось до наступления события
start_date = form.calendarWidget.selectedDate()
calc_date = form.calendarWidget.selectedDate()


# вставим метку от какой даты считаем
form.label.setText("Трекер события от %s" % start_date.toString('dd-MM-yyyy'))


# перед запуском вызвали функцию для отображения со старта в dateEdit текущей даты(календарь открывается сразу на текущей дате)
on_click_calendar()


# запуск приложения
app.exec_()


