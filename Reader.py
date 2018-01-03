import threading,globcfg
import time,random
from Gui import Gui

class Reader(threading.Thread):
    def __init__(self, book, lock, number, g):
        threading.Thread.__init__(self)
        self.book = book
        self.name = 'Reader'
        self.lock=lock
        self.id = number
        self.on=False
        self.gui = g

    def run(self):
        self.on=True
        print("[log]thread[{number}] {name} start...".format(number=self.id, name=self.name))
        print("The reader " + str(self.id) + " comes to the reading room")
        self.gui.change_state("R", self.id, self.gui.scheduling, self.gui.r_waiting)
        self.book.want_to_read()
        print("The reader " + str(self.id) + " begins reading")
        self.gui.change_state("R", self.id, self.gui.r_waiting, self.gui.filing)
        time.sleep(random.expovariate(1/globcfg.lamRW)/10)
        print("The reader " + str(self.id) + " ends reading")
        self.gui.change_state("R", self.id, self.gui.filing, self.gui.nowhere)
        self.book.end_reading()
        print("The reader " + str(self.id) + " leaves the reading room")
