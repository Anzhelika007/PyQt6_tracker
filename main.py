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

import pickle
from PyQt5 import uic
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QApplication

Form, Window = uic.loadUiType('tracker.ui')

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()


def save_to_file():
    # сохраняем в файл
    global start_date, calc_date, description
    data_to_save = {'start': start_date, 'end': calc_date, 'desc': description}
    file1 = open('config.txt', 'wb')
    pickle.dump(data_to_save, file1)
    file1.close()


def read_from_file():
    # считываем из файла
    global start_date, calc_date, description, now_date
    # обработка исключений если файла не будет выведет сообщение
    try:
        file1 = open('config.txt', 'rb')
        date_to_load = pickle.load(file1)
        file1.close()
        start_date = date_to_load['start']
        calc_date = date_to_load['end']
        description = date_to_load['desc']
        print(start_date.toString('dd-MM-yyyy'), calc_date.toString('dd-MM-yyyy'), description)
        # отобразим дату события
        form.calendarWidget.setSelectedDate(calc_date)
        form.dateEdit.setDate(calc_date)
        form.plainTextEdit.setPlainText(description)

        delta_days_left = now_date.daysTo(start_date)    # прошло дней
        delta_days_right = now_date.daysTo(calc_date)    # осталось дней
        days_total = start_date.daysTo(calc_date)        # всего дней
        print(delta_days_left,delta_days_right,days_total)
        procent = int(delta_days_left * 100 / days_total)
        print(procent)
        form.progressBar.setProperty("value", procent)
    except:
        print("Не могу прочитать файл... Может его нет")

def on_click():
    global calc_date, description
    # записываем переменные по клику следить    calc_date = form.calendarWidget.selectedDate()
    description = form.plainTextEdit.toPlainText()

    # print(form.plainTextEdit.toPlainText())
    # print(form.dateEdit.dateTime().toString('dd-MM-yyyy'))
    # print('Cliked!!!')
    save_to_file()
    # print(form.calendarWidget.selectedDate().toString('dd-MM-yyyy'))
    # date = QDate(2022, 9, 17)
    # form.calendarWidget.setSelectedDate(date)


def on_click_calendar():
    global start_date, calc_date

    # меняем дату в dateEdit на дату выбранную в календаре
    # print(form.calendarWidget.selectedDate().toString('dd-MM-yyyy'))
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
    # print(form.dateEdit.dateTime().toString('dd-MM-yyyy'))
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
now_date = form.calendarWidget.selectedDate()
calc_date = form.calendarWidget.selectedDate()
description = form.plainTextEdit.toPlainText()


# при старте программы записываем в файл текущую дату
read_from_file()


# вставим метку от какой даты считаем
form.label.setText("Трекер события от %s" % start_date.toString('dd-MM-yyyy'))

# перед запуском вызвали функцию для отображения со старта в dateEdit текущей даты(календарь открывается сразу на текущей дате)
on_click_calendar()

# запуск приложения
app.exec_()
