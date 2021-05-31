# symptom2.py
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import makeInform
import databaseConnection

class Sym_2(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        # self.setLayout(grid)

        self.lbl0 = QLabel('1. 날짜 & 시간')

        self.datetimeedit = QDateTimeEdit(self)
        self.datetimeedit.setDateTime(QDateTime.currentDateTime())
        self.datetimeedit.setDateTimeRange(QDateTime(1900, 1, 1, 00, 00, 00), QDateTime(2100, 1, 1, 00, 00, 00))
        self.datetimeedit.setDisplayFormat('yyyy.MM.dd hh:mm:ss')

        self.lbl1 = QLabel('2. 증상', self)
        # self.lbl1.move(60, 40)

        self.te = QTextEdit()
        self.te.setAcceptRichText(False)
        # self.te.move(60, 70)

        self.lbl2 = QLabel('3. 강도', self)
        # self.lbl2.move(60, 100)

        self.lbl3 = QLabel('약', self)
        # self.lbl3.move(60, 130)

        self.rbtn1 = QRadioButton(self)
        # rbtn1.move(90, 130)
        # rbtn1.setChecked(True)

        self.rbtn2 = QRadioButton(self)
        # rbtn2.move(120, 130)

        self.rbtn3 = QRadioButton(self)
        # rbtn3.move(150, 130)

        self.rbtn4 = QRadioButton(self)
        # rbtn4.move(180, 130)

        self.rbtn5 = QRadioButton(self)
        # rbtn5.move(210, 130)

        self.lbl4 = QLabel('강', self)
        # self.lbl4.move(240, 130)

        btn = QPushButton(self)
        btn.setText('확인')

        btn.clicked.connect(self.save_symptom)
        # btn.move(110, 160)

        grid.addWidget(self.lbl0, 0, 0, 1, 7)
        grid.addWidget(self.datetimeedit, 1, 0, 1, 7)
        grid.addWidget(self.lbl1,2,0,1,7)
        grid.addWidget(self.te,3,0,1,7)
        grid.addWidget(self.lbl2,4,0,1,7)
        grid.addWidget(self.lbl3,5,0)
        grid.addWidget(self.rbtn1,5,1)
        grid.addWidget(self.rbtn2,5,2)
        grid.addWidget(self.rbtn3,5,3)
        grid.addWidget(self.rbtn4,5,4)
        grid.addWidget(self.rbtn5,5,5)
        grid.addWidget(self.lbl4,5,6)
        grid.addWidget(btn,6,0,1,7)

        self.setLayout(grid)

        self.setWindowTitle('Symptom 입력')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def save_symptom(self):
        # print("save_symptom_test 1")
        widgetLst = [self.te, self.rbtn1, self.rbtn2, self.rbtn3, self.rbtn4, self.rbtn5, self.datetimeedit ]
        # print("save_symptom_test 2")
        make_inform = makeInform.MakeInform()
        query = make_inform.makeQuery(widgetLst,2)
        # print("save_symptom_test 3")

        dbConnection = databaseConnection.DatabaseConnection()
        dbConnection.dbSave(query,2)

        # print("save query 완료")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Sym_2()
    sys.exit(app.exec_())