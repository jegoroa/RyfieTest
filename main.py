from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout

from windows import FirstWin, TestWin, FinalWin

app = QApplication([])


final_win = FinalWin()
test_win = TestWin(final_win)
start_win = FirstWin(test_win)

app.exec()