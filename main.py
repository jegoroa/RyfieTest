from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout

from windows import FirstWin, TestWin

app = QApplication([])

start_win = FirstWin()

test_win = TestWin()

app.exec()