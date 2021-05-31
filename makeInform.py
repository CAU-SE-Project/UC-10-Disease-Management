# makeInform.py
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MakeInform():
    def __init__(self):
        query = {}

    def makeQuery(self, widgetLst, req):
        # print("들어옴")
        self.query = {}
        if req==1: # alarm
            time = widgetLst[0].dateTime()
            self.query["time"] = time.toString(Qt.DefaultLocaleShortDate)
            inform = widgetLst[1].toPlainText()
            self.query["inform"] = inform
            # print(self.query)

        elif req==2: # symptom
            time = widgetLst[6].dateTime()
            self.query["time"] = time.toString(Qt.DefaultLocaleShortDate)
            symptom = widgetLst[0].toPlainText()
            self.query["symptom"] = symptom
            level = 0
            if widgetLst[1].isChecked():
                level = 1
            elif widgetLst[2].isChecked():
                level = 2
            elif widgetLst[3].isChecked():
                level = 3
            elif widgetLst[4].isChecked():
                level = 4
            elif widgetLst[5].isChecked():
                level = 5
            self.query["level"] = level

        if req==3: # action
            time = widgetLst[0].dateTime()
            self.query["time"] = time.toString(Qt.DefaultLocaleShortDate)
            action = widgetLst[1].toPlainText()
            self.query["action"] = action

        # print("makeQuery끝")
        return self.query
