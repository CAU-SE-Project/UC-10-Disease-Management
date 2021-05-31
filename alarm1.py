# alarm1.py
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


class Alarm1(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn1 = QPushButton(self)
        btn1.setText('alarm 설정')

        btn2 = QPushButton(self)
        btn2.setText('alarm 목록')

        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)

        self.setLayout(vbox)
        self.setWindowTitle('Alarm')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Alarm1()
    sys.exit(app.exec_())