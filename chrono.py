"""Contains the class that defines the behabiour of each chronometer."""
import time


class Chrono:
    """Class that allows the chronometer to start, stop and be destroyed."""
    def __init__(self, canvas, coord_x, coord_y):
        self.state = False  # Chonometer starts when True
        self.origin = time.time()
        self.canvas = canvas
        self.my_time = 0
        self.view = canvas.create_text(
            coord_x,
            coord_y,
            text='00:00:00',
            font=('Times New Roman', 20),
            fill='#A78295'
        )

    def elapsed_time(self):
        """Output the time elapsed alowing to continue since the last time
        saved.
        """
        return (time.time() - self.origin) + self.my_time

    @staticmethod
    def format_time(elapsed_time):
        """Format the seconds given by time.time()"""
        minutes, seconds = divmod(int(elapsed_time), 60)
        hours, minutes = divmod(minutes, 60)
        return f"{hours:02}:{minutes:02}:{seconds:02}"

    def start_chrono(self):
        """Start the chronometer after redefining the state variable."""
        self.state = True
        self.origin = time.time()

    def stop_chrono(self):
        """Stop the chronometer after redefining the state variable."""
        self.state = False
        self.my_time = self.elapsed_time()

    def update_chrono(self):
        """Get the time that has passed since the begining formated."""
        return self.format_time(self.elapsed_time())

    def restart_chrono(self):
        """The timer sets to zero and starts again."""
        self.origin = time.time()
        self.my_time = 0
        self.canvas.itemconfig(
            self.view,
            text='00:00:00'
        )

    def destroy_chrono(self):
        """Destroy the chonometer."""
