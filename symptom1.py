# symptom1.py
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


class Sym_1(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn1 = QPushButton(self)
        btn1.setText('symptom 입력')

        btn2 = QPushButton(self)
        btn2.setText('symptom 조회')

        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)

        self.setLayout(vbox)
        self.setWindowTitle('Symptom')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Sym_1()
    sys.exit(app.exec_())