# PyQt6_tracker
**Урок 1**
1. Устанавливаем PyQt6 терминал
pip install PyQt6
2. Cоздали файл в Qt Designer
3. Вызвали утилиту конвертации файла pyuic6
pyuic6 ui_imagedialod.ui -o  ui_imagedialod.py
4. Берем название класса из сформированного .ру файла и вставляем в импорт и переменную

from ui_imagedialog import Ui_Dialog
ui = Ui_Dialog()

Или при создании в Qt Designer 


**Урок 2**

1. Создадим QMessageBox (paзновидности встроенных:information(), question(), warning(), and critical())
https://doc.qt.io/qt-6/qmessagebox.html

int ret = QMessageBox::warning(this, tr("My Application"),
                               tr("The document has been modified.\n"
                                  "Do you want to save your changes?"),
                               QMessageBox::Save | QMessageBox::Discard
                               | QMessageBox::Cancel,
                               QMessageBox::Save);

Есть баг - кнопки Save/Discard/Cancel - относятся к StandardButton - смотри файл кода урока

**Урок 3**

1. Создадим трекер в Qt Designer
2. Из документации копируем код запуска (загрузка без конвертации)

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

- указали файл ui без конвертации
Form, Window = uic.loadUiType("tracker.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()
app.exec_()


**Урок 4**

Coздали файл обмена bat 
create_py_file_from_ui.bat который содержит одну команду обмена
pyuic6.exe -x D:\Python\Project\PyQt6_tracker\tracker.ui  -o D:\Python\Project\PyQt6_tracker\tracker.py


На практике посмотрели в чем разница между двумя подходами:
-как обновляются (для варианта, когда мы получаем объект как клас - обновление через bat фаил)


**Урок 5**

Cпособы обращения к элементам(фаил main - без конвертации, фаил tracker - с конвертацией и открытым классом):
1. Фаил main (через form.)
form.label.setText('erthtzrjnsymzgs') > посмотреть нужный элемент можно в файле tracker
2. Фаил tracker НЕ РЕКОМЕНДУЕТСЯ
просто наращивать функциями вниз 
3. В фаил main импортировать фаил tracker как модуль (через ui.):

from tracker import *

import sys

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

ui.label.setText('erthtzrjnsymzgs')

sys.exit(app.exec())

В данном уроке мы считали дату, текстовое поле, вывели нажатие на кнопку

**Урок 6**

Документация по календарю (см методы)
https://doc.qt.io/qtforpython-5/PySide2/QtCore/QDate.html#PySide2.QtCore.PySide2.QtCore.QDate
Работа с датой и календарем
вызов функций при наступлении событий:

form.pushButton.clicked.connect(on_click)
form.calendarWidget.clicked.connect(on_click_calendar)
form.dateEdit.dateChanged.connect(on_dateedit_changer)

**Урок 7**

Меняем стартовую дату в dateEdit при помощи функции перед зыпуском приложения
Добавили функционал подсчета различных дат методом daysTo()

**Урок 8**

1. Импортируем модуль для сохранения и импорта данных в файл/из файла
import pickle
2. Создадим 2 функции(одна записывает в файл / другая считывает из файла)