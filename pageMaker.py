# pageMaker

import action1
import symptom1
import symptom2
import main_page
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5 import QtWidgets
import sys
from symptom1 import *
from symptom2 import Sym_2
from action1 import Action1
from action2 import Action2
from alarm1 import Alarm1
from alarm2 import Alarm2

class Display():
    def __init__(self):
        super().__init__()

    def dis_page(self, page_num):

        if page_num == 1:
            app1 = QApplication(sys.argv)
            ex1 = symptom1.Sym_1()
            ex1.show()

        elif page_num == 2:
            ex = Sym_2()

        elif page_num == 3:
            ex = Action1()

        elif page_num == 4:
            ex = Action2()

        elif page_num == 5:
            ex = Alarm1()

        elif page_num == 6:
            ex = Alarm2()

        else:
            sys.exit()
