# alarm2.py
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDateTime
# import pymongo
import makeInform
import databaseConnection


class Alarm2(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lbl1 = QLabel('1. 날짜 & 시간 설정')

        self.datetimeedit = QDateTimeEdit(self)
        self.datetimeedit.setDateTime(QDateTime.currentDateTime())
        self.datetimeedit.setDateTimeRange(QDateTime(1900, 1, 1, 00, 00, 00), QDateTime(2100, 1, 1, 00, 00, 00))
        self.datetimeedit.setDisplayFormat('yyyy.MM.dd hh:mm:ss')


        lbl2 = QLabel('2. alarm 내용', self)
        # self.lbl1.move(60, 40)

        self.te = QTextEdit()
        self.te.setAcceptRichText(False)
        # self.te.move(60, 70)

        btn = QPushButton(self)
        btn.setText('3. 확인')

        btn.clicked.connect(self.save_alarm)
        # btn.clicked.connect(self.load_alarm)

        vbox = QVBoxLayout()
        vbox.addWidget(lbl1)
        vbox.addWidget(self.datetimeedit)
        vbox.addWidget(lbl2)
        vbox.addWidget(self.te)
        vbox.addWidget(btn)
        vbox.addStretch()

        self.setLayout(vbox)

        self.setWindowTitle('Alarm 설정')
        self.setGeometry(300, 300, 300, 200)
        self.show()


    def save_alarm(self):
        # print("save_alarm_test 1")
        widgetLst = [self.datetimeedit, self.te]
        # print("save_alarm_test 2")
        make_inform = makeInform.MakeInform()
        query = make_inform.makeQuery(widgetLst,1)
        # print("save_alarm_test 3")
        dbConnection = databaseConnection.DatabaseConnection()
        dbConnection.dbSave(query,1)
        # print("save query 완료")

    def load_alarm(self):
        dbConnection = databaseConnection.DatabaseConnection()
        dbConnection.loadDB(1)
        # print("loadDB 완료")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Alarm2()
    sys.exit(app.exec_())