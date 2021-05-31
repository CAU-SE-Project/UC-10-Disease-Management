# action3.py
import sys
from PyQt5.QtWidgets import *
import databaseConnection

class Alarm3(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.tableWidget = QTableWidget()
        query_list = self.load_alarm()
        rowNum = len(query_list)
        self.tableWidget.setRowCount(rowNum)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(
            ['시간', '행동 기록']
        )
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        for i in range(rowNum):
            dateTimeVar = query_list[i][0]
            self.tableWidget.setItem(i, 0, QTableWidgetItem(dateTimeVar))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(query_list[i][1]))

        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)
        self.setLayout(layout)

        self.setWindowTitle('Action 조회')
        self.setGeometry(300, 100, 600, 400)
        self.show()

    def load_alarm(self):

        dbConnection = databaseConnection.DatabaseConnection()
        query_list = dbConnection.loadDB(3)
        # print("load query 완료")
        return query_list

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Alarm3()
    sys.exit(app.exec_())