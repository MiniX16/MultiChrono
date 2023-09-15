import tkinter as tk
from tkinter import ttk

from chrono import Chrono
from chrono_threading import ChronoThread


root = tk.Tk()
header = tk.Canvas(width=280, height=100, bg='#3F2E3E', highlightthickness=0)

generators = []
GAP = 100


class ChronoGenerator():
    """Allow the app to generate new chronometers with all its fuctionalities.
    """
    def __init__(self, gap):
        self.body = tk.Canvas(
            width=250,
            height=80,
            bg='#3F2E3E',
            highlightthickness=0
        )
        self.rename_chron_button = tk.Button(
            bg='#3F2E3E',
            activebackground='#3F2E3E',
            activeforeground='#331D2C',
            border=0,
            text='Chronometer',
            foreground='#A78295',
            font=('Times New Roman', 13, 'bold'),
            command=self.open_rename_chron
        )
        self.restart_chron_button = tk.Button(
            bg='#A78295',
            activebackground='#EFE1D1',
            border=0,
            text='↺',
            font=('Times New Roman', 15, 'bold'),
            command=self.restart_button
        )
        self.start_chron_button = tk.Button(
            bg='#A78295',
            activebackground='#EFE1D1',
            border=0,
            text='▐▐ ',
            font=('Times New Roman', 12,),
            command=self.update_button
        )
        self.chrono = Chrono(self.body, 80, 48)
        self.chrono_thread = ChronoThread(self.chrono)
        self.body.place(x=25, y=150 + gap)
        self.start_chron_button.place(x=190, y=195 + gap)
        self.rename_chron_button.place(x=30, y=152 + gap)
        self.restart_chron_button.place(x=191, y=155 + gap)
        self.chrono_thread.start()

    def update_button(self):
        """Change the simbol of the start/pause button when pressed."""
        if self.start_chron_button.cget('text') == '►':
            self.start_chron_button.config(
                text='▐▐ ',
                font=('Times New Roman', 12,)
            )
            Chrono.stop_chrono(self.chrono)
        else:
            self.start_chron_button.config(
                text='►',
                font=('Times New Roman', 13, 'bold')
            )
            Chrono.start_chrono(self.chrono)

    def restart_button(self):
        """Call the restart fuction from the chronometer."""
        self.chrono.restart_chrono()

    def open_rename_chron(self):
        """Open a new window to allow the user rename the selected chornometer.
        """
        rename_window = tk.Toplevel()
        rename_window.title('Rename Chronometer')
        rename_window.config(bg='#331D2C')
        rename_window.geometry('250x100')
        rename_window.resizable(False, False)

        new_name = ttk.Entry(rename_window)

        confirm_name_button = tk.Button(
            rename_window,
            bg='#3F2E3E',
            activebackground='#2D1D2D',
            border=0,
            text='✎',
            foreground='white',
            font=('Times New Roman', 15, 'bold'),
            command=lambda: self.close_rename_chron(new_name, rename_window)
        )

        confirm_name_button.place(x=180, y=30)
        new_name.place(x=50, y=40)

    def close_rename_chron(self, name, window):
        """Close and confirm the writen name and updates the button's name into
        the new one.
        """
        self.rename_chron_button.config(text=name.get())
        window.destroy()


def generate_chrono():
    """Create and chronometer generator that places the chronometer and all
    its features.
    """
    add_chron_button.place(x=120, y=250 + len(generators) * GAP)
    generators.append(ChronoGenerator(len(generators) * GAP))


root.title('MultiCrono')
root.config(bg='#331D2C')
root.geometry('300x600')
root.resizable(False, True)

add_chron_button = tk.Button(
    width=3,
    height=1,
    bg='#3F2E3E',
    activebackground='#2D1D2D',
    border=0,
    text='+',
    font=('Times New Roman', 25, 'bold'),
    command=generate_chrono
)

texto = header.create_text(
    140,
    50,
    text='MultiChrono',
    font=('Times New Roman', 30),
    fill='#A78295'
)

header.place(x=10, y=25)
add_chron_button.place(x=120, y=250)


if __name__ == '__main__':

    root.mainloop()
