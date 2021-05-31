#Controller

import main_page
from checkResponse import CheckResponse

class Controller():
    def __init__(self):
        super().__init__()
        self.req = 0

    def checkreq(self, num):
        self.req = num
        Chk = CheckResponse()
        Chk.dis_page(self.req)