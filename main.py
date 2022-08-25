import pickle
from PyQt5 import uic
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QApplication
import os

# путь программы
#print(os.path.realpath(__file__))
# разбили путь по переменным
dirmame, filename = os.path.split(os.path.realpath(__file__))
Form, Window = uic.loadUiType(dirmame+ '\\tracker.ui')

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()


def save_to_file():
    # сохраняем в файл
    global start_date, calc_date, description, dirmame
    data_to_save = {'start': start_date, 'end': calc_date, 'desc': description}
    file1 = open(dirmame+'\\config.txt', 'wb')
    pickle.dump(data_to_save, file1)
    file1.close()

    task = """schtasks /create /tr "python """ + os.path.realpath(
        __file__) + """" /tn "Трекер события" /sc MINUTE /mo 120 /ed 31/12/2020 /F"""
    task = """schtasks /create /tr "python """ + os.path.realpath(
        __file__) + """" /tn "Трекер события" /sc MINUTE /mo 120 /ed """ + calc_date.toString("dd/MM/yyyy") + """ /F"""
    print(task)
    os.system('chcp 65001')
    os.system(task)


def read_from_file():
    # считываем из файла
    global start_date, calc_date, description, now_date,dirmame
    # обработка исключений если файла не будет выведет сообщение
    try:
        file1 = open(dirmame+'\\config.txt', 'rb')
        date_to_load = pickle.load(file1)
        file1.close()
        start_date = date_to_load['start']
        calc_date = date_to_load['end']
        description = date_to_load['desc']
        # отобразим дату события
        form.calendarWidget.setSelectedDate(calc_date)
        form.dateEdit.setDate(calc_date)
        form.plainTextEdit.setPlainText(description)

        delta_days_left = now_date.daysTo(start_date)    # прошло дней
        delta_days_right = now_date.daysTo(calc_date)    # осталось дней
        days_total = start_date.daysTo(calc_date)        # всего дней
        procent = int(delta_days_left * 100 / days_total)
        form.progressBar.setProperty("value", procent)
    except:
        print("Не могу прочитать файл... Может его нет")

def on_click():
    global calc_date, description
    # записываем переменные по клику следить
    calc_date = form.calendarWidget.selectedDate()
    description = form.plainTextEdit.toPlainText()
    save_to_file()


def on_click_calendar():
    global start_date, calc_date
    # меняем дату в dateEdit на дату выбранную в календаре
    form.dateEdit.setDate(form.calendarWidget.selectedDate())

    # расчет количества оставшихся дней до события метод daysTo
    calc_date = form.calendarWidget.selectedDate()
    delta_days = start_date.daysTo(calc_date)
    # меняем значение поля
    form.label_3.setText("До наступления события осталось: %s дней" % delta_days)


def on_dateedit_changer():
    global start_date, calc_date
    # меняем дату в календаре на дату в dateEdit
    form.calendarWidget.setSelectedDate(form.dateEdit.date())

    # расчет количества оставшихся дней до события метод daysTo / изменили значение calc_date
    calc_date = form.dateEdit.date()
    delta_days = start_date.daysTo(calc_date)
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
