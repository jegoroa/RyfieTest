from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from settings import *

class FirstWin(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Начало теста")
        self.initUI()
        self.show()
        
    def initUI(self):
        start_vertical = QVBoxLayout()
        start_title = QLabel(HELLO_TEXT)
        start_info = QLabel(FIRST_TEXT)
        start_button = QPushButton("НАЧАТЬ")

        start_vertical.addWidget(start_title)
        start_vertical.addWidget(start_info)
        start_vertical.addWidget(start_button)
        self.setLayout(start_vertical)

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Тестирование")
        self.initUI()
        self.show()

    def initUI(self):
        
        test_vertical = QVBoxLayout()

        age_input = QLineEdit()
        fio_input = QLineEdit()

        test_vertical.addWidget(QLabel("Введите Фамилию Имя Отчество"))
        test_vertical.addWidget(fio_input)
        test_vertical.addWidget(QLabel("Введите возраст"))
        test_vertical.addWidget(age_input)

        test_vertical.addWidget(QLabel(TEXT_HELP1))

        first_test_btn = QPushButton("начать первый тест")
        test_vertical.addWidget(first_test_btn)

        timer = QLabel("00:00:15")
        test_vertical.addWidget(timer)

        first_puls_input = QLineEdit("0")
        test_vertical.addWidget(first_puls_input)

        test_vertical.addWidget(QLabel(TEXT_HELP2))

        squat_btn = QPushButton("начать приседания")
        test_vertical.addWidget(squat_btn)

        test_vertical.addWidget(QLabel(TEXT_HELP3))

        final_test_btn = QPushButton("начать финальный тест")
        test_vertical.addWidget(final_test_btn)

        second_puls_input = QLineEdit("0")
        test_vertical.addWidget(second_puls_input)

        third_puls_input = QLineEdit("0")
        test_vertical.addWidget(third_puls_input)

        result_btn = QPushButton("отправить результаты")
        test_vertical.addWidget(result_btn)
        self.setLayout(test_vertical)