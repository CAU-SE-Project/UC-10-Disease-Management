# action1.py
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


class Action1(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn1 = QPushButton(self)
        btn1.setText('action 입력')

        btn2 = QPushButton(self)
        btn2.setText('action 조회')

        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)

        self.setLayout(vbox)
        self.setWindowTitle('Action')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Action1()
    sys.exit(app.exec_())