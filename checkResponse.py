from pageMaker import Display
import sys

class CheckResponse():
    def __init__(self):
        self.req = 0

    def dis_page(self, num):
        if num == 1:
            self.req = num
            dis = Display()
            dis.dis_page(self.req)

        elif num == 3:
            self.req = num
            dis = Display()
            dis.dis_page(self.req)

        elif num == 5:
            self.req = num
            dis = Display()
            dis.dis_page(self.req)

        else:
            sys.exit()