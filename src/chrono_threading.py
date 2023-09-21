"""Allow the chronometer work at the same time other chronos and the window is
working.
"""
import time
from threading import Thread


class ChronoThread(Thread):
    """A multithreading class so every chronometer can work at the same time.
    """
    def __init__(self, chrono) -> None:
        super().__init__()
        self.chrono = chrono
        self.update_gap = 0.01  # In seconds.

    def run(self) -> None:
        while True:
            time.sleep(self.update_gap)
            while self.chrono.state:
                self.chrono.canvas.itemconfig(
                    self.chrono.view,
                    text=self.chrono.update_chrono(),
                )
                time.sleep(self.update_gap)
