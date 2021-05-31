# main_page.py
import sys
from symptom1 import *
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5 import QtWidgets
from controller import *
from symptom2 import Sym_2
from action1 import Action1
from action2 import Action2
from alarm1 import Alarm1
from alarm2 import Alarm2

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn1 = QPushButton(self)
        btn1.setText('symptom 기록')
        btn1.clicked.connect(lambda: self.setreq(1))

        btn2 = QPushButton(self)
        btn2.setText('action 기록')
        btn2.clicked.connect(lambda: self.setreq(3))

        btn3 = QPushButton(self)
        btn3.setText('alarm 등록')
        btn3.clicked.connect(lambda: self.setreq(5))

        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)

        self.setLayout(vbox)
        self.setWindowTitle('QPushButton')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def setreq(self, num):
        Con = Controller()
        Con.checkreq(num)
        sys.exit(app.exec_())


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = Main()

    sys.exit(app.exec_())
