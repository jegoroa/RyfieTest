from PyQt5.QtCore import Qt, QTimer, QTime
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

        self.timer1 = QTimer()
        self.timer1.timeout.connect(self.first_timer_change)
        self.first_test_btn.clicked.connect(self.start_first_timer)

        self.timer2 = QTimer()
        self.timer2.timeout.connect(self.second_timer_change)
        self.squat_btn.clicked.connect(self.start_second_timer)

        self.timer3 = QTimer()
        self.timer3.timeout.connect(self.third_timer_change)
        self.final_test_btn.clicked.connect(self.start_third_timer)

        self.show()

    def start_first_timer(self):
        self.time = QTime(0,0,15)
        self.timer1.start(1000)

    def first_timer_change(self):
        self.time = self.time.addSecs(-1)
        self.timer_label.setText(self.time.toString("hh:mm:ss"))
        if self.time.second() == 0:
            self.timer1.stop()

    def start_second_timer(self):
        self.time = QTime(0,0,45)
        self.timer2.start(1000)

    def second_timer_change(self):
        self.time = self.time.addSecs(-1)
        self.timer_label.setText(self.time.toString("hh:mm:ss"))
        if self.time.second() == 0:
            self.timer2.stop()

    def start_third_timer(self):
        self.timer_label.setStyleSheet('color:green;font-size:72px')
        self.time = QTime(0,0,45)
        self.timer3.start(1000)

    def third_timer_change(self):
        self.time = self.time.addSecs(-1)
        self.timer_label.setText(self.time.toString("hh:mm:ss"))
        
        if self.time.second() == 30:
            self.timer_label.setStyleSheet('color:black;font-size:72px')

        if self.time.second() == 15:
            self.timer_label.setStyleSheet('color:green;font-size:72px')

        if self.time.second() == 0:
            self.timer_label.setStyleSheet('color:black;font-size:72px')
            self.timer3.stop()

    def initUI(self):
        
        test_vertical = QVBoxLayout()

        age_input = QLineEdit()
        fio_input = QLineEdit()

        test_vertical.addWidget(QLabel("Введите Фамилию Имя Отчество"))
        test_vertical.addWidget(fio_input)
        test_vertical.addWidget(QLabel("Введите возраст"))
        test_vertical.addWidget(age_input)

        test_vertical.addWidget(QLabel(TEXT_HELP1))

        self.first_test_btn = QPushButton("начать первый тест")
        test_vertical.addWidget(self.first_test_btn)

        self.timer_label = QLabel("00:00:15")
        self.timer_label.setStyleSheet("font-size:72px")
        test_vertical.addWidget(self.timer_label)

        test_vertical.addWidget(QLabel("Впишите пульс сюда"))

        first_puls_input = QLineEdit("0")
        test_vertical.addWidget(first_puls_input)

        test_vertical.addWidget(QLabel(TEXT_HELP2))

        self.squat_btn = QPushButton("начать приседания")
        test_vertical.addWidget(self.squat_btn)

        test_vertical.addWidget(QLabel(TEXT_HELP3))

        self.final_test_btn = QPushButton("начать финальный тест")
        test_vertical.addWidget(self.final_test_btn)

        test_vertical.addWidget(QLabel("Впишите пульс за первые 15 сек. сюда"))
        second_puls_input = QLineEdit("0")
        test_vertical.addWidget(second_puls_input)

        test_vertical.addWidget(QLabel("Впишите пульс за последние 15 сек. сюда"))
        third_puls_input = QLineEdit("0")
        test_vertical.addWidget(third_puls_input)

        result_btn = QPushButton("отправить результаты")
        test_vertical.addWidget(result_btn)
        self.setLayout(test_vertical)