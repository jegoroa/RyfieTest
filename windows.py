from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from settings import *

#ctrl + k
#ctrl + 0

class FirstWin(QWidget):
    def __init__(self,second_win):
        super().__init__()
        self.second_win = second_win
        self.setWindowTitle("Начало теста")
        self.initUI()
        self.show()
    
    def show_next(self):
        self.second_win.show()
        self.hide()

    def initUI(self):
        start_vertical = QVBoxLayout()
        start_title = QLabel(HELLO_TEXT)
        start_info = QLabel(FIRST_TEXT)
        start_button = QPushButton("НАЧАТЬ")
        start_button.clicked.connect(self.show_next)

        start_vertical.addWidget(start_title)
        start_vertical.addWidget(start_info)
        start_vertical.addWidget(start_button)
        self.setLayout(start_vertical)

class TestWin(QWidget):

    def __init__(self, final_win):
        super().__init__()
        self.final_win = final_win

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

    def show_next(self):
        self.final_win.show()
        self.hide()

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

    def calc_ryfue_kef(self):
        p1 = int(self.first_puls_input.text())
        p2 = int(self.second_puls_input.text())
        p3 = int(self.third_puls_input.text())
        
        kef = (4 * (p1+p2+p3) - 200)/10

        age = int(self.age_input.text())

        if age in [7,8]:
            if kef <= 6.4: result = "высокий"
            elif kef < 17: result = "средний"
            else: result = "низкий"

        elif age in [9,10]:
            if kef <= 4.9: result = "высокий"
            elif kef < 15.5: result = "средний"
            else: result = "низкий"

        #и так далее...
        else:
            if kef <= 0.4: result = "высокий"
            elif kef < 11: result = "средний"
            else: result = "низкий"

        self.final_win.set_result(kef,result)
        self.show_next()
        return {'kef':kef, 'result':result}

    def initUI(self):

        test_vertical = QVBoxLayout()

        self.age_input = QLineEdit()
        fio_input = QLineEdit()

        test_vertical.addWidget(QLabel("Введите Фамилию Имя Отчество"))
        test_vertical.addWidget(fio_input)
        test_vertical.addWidget(QLabel("Введите возраст"))
        test_vertical.addWidget(self.age_input)

        test_vertical.addWidget(QLabel(TEXT_HELP1))

        self.first_test_btn = QPushButton("начать первый тест")
        test_vertical.addWidget(self.first_test_btn)

        self.timer_label = QLabel("00:00:15")
        self.timer_label.setStyleSheet("font-size:72px")
        test_vertical.addWidget(self.timer_label)

        test_vertical.addWidget(QLabel("Впишите пульс сюда"))

        self.first_puls_input = QLineEdit("0")
        test_vertical.addWidget(self.first_puls_input)

        test_vertical.addWidget(QLabel(TEXT_HELP2))

        self.squat_btn = QPushButton("начать приседания")
        test_vertical.addWidget(self.squat_btn)

        test_vertical.addWidget(QLabel(TEXT_HELP3))

        self.final_test_btn = QPushButton("начать финальный тест")
        test_vertical.addWidget(self.final_test_btn)

        test_vertical.addWidget(QLabel("Впишите пульс за первые 15 сек. сюда"))
        self.second_puls_input = QLineEdit("0")
        test_vertical.addWidget(self.second_puls_input)

        test_vertical.addWidget(QLabel("Впишите пульс за последние 15 сек. сюда"))
        self.third_puls_input = QLineEdit("0")
        test_vertical.addWidget(self.third_puls_input)

        result_btn = QPushButton("отправить результаты")
        result_btn.clicked.connect(self.calc_ryfue_kef)

        test_vertical.addWidget(result_btn)
        self.setLayout(test_vertical)

class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Резульат теста")
        self.initUI()

    def set_result(self,kef,result):
        self.result_label.setText("Ваш индекс Руфье " + str(kef) + " здоровье " + result)

    def initUI(self):
        start_vertical = QVBoxLayout()
        final_title = QLabel("ваш результат")
        self.result_label = QLabel("тут будет результат")

        start_vertical.addWidget(final_title)
        start_vertical.addWidget(self.result_label)

        self.setLayout(start_vertical)