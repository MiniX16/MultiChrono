from threading import Thread


class ChronoThread(Thread):
    """A multithreading class so every chronometer can work at the same time.
    """
    def __init__(self, chrono):
        super().__init__()
        self.chrono = chrono

    def run(self):
        while True:
            while self.chrono.state:
                self.chrono.canvas.itemconfig(
                    self.chrono.view,
                    text=self.chrono.update_chrono()
                )
