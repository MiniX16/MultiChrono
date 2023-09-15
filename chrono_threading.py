import time
from threading import Thread


class ChronoThread(Thread):
    """A multithreading class so every chronometer can work at the same time.
    """
    def __init__(self, chrono):
        super().__init__()
        self.chrono = chrono

    def run(self):
        while True:
            time.sleep(1)
            while self.chrono.state:
                time.sleep(1)
                self.chrono.canvas.itemconfig(
                    self.chrono.view,
                    text=self.chrono.update_chrono()
                )
