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
