# PyQt6_tracker
Урок 1
1. Устанавливаем PyQt6 терминал
pip install PyQt6
2. Cоздали файл в Qt Designer
3. Вызвали утилиту конвертации файла pyuic6
pyuic6 ui_imagedialod.ui -o  ui_imagedialod.py
4. Берем название класса из сформированного .ру файла и вставляем в импорт и переменную

from ui_imagedialog import Ui_Dialog
ui = Ui_Dialog()

Или при создании в Qt Designer 


Урок 2
1. Создадим QMessageBox (paзновидности встроенных:information(), question(), warning(), and critical())
https://doc.qt.io/qt-6/qmessagebox.html

int ret = QMessageBox::warning(this, tr("My Application"),
                               tr("The document has been modified.\n"
                                  "Do you want to save your changes?"),
                               QMessageBox::Save | QMessageBox::Discard
                               | QMessageBox::Cancel,
                               QMessageBox::Save);

Есть баг - кнопки Save/Discard/Cancel - относятся к StandardButton - смотри файл кода урока