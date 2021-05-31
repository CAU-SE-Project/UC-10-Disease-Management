# symptom1.py
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from main_page import *
from controller import *
from pageMaker import *


class Sym_1(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        con = Controller()
        btn1 = QPushButton(self)
        btn1.setText('symptom 입력')

        btn2 = QPushButton(self)
        btn2.setText('symptom 조회')

        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)

        self.setLayout(vbox)
        self.setWindowTitle('QPushButton')
        self.setGeometry(300, 300, 300, 200)
        # self.show()

if __name__ == "__main__":
    app1 = QApplication(sys.argv)
    ex1 = Sym_1()
    ex1.show()
    app1.exec_()
