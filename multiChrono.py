import tkinter as tk
from tkinter import ttk

from chrono import Chrono
from chrono_threading import ChronoThread


root = tk.Tk()
header = tk.Canvas(width=280, height=100, bg='#3F2E3E', highlightthickness=0)


body = tk.Canvas(width=250, height=80, bg='#3F2E3E', highlightthickness=0)
chronometers = [Chrono(body, 80, 48)]
threads = [ChronoThread(chronometers[0])]


threads[0].start()


def create_chrono(canvas, coord_x, coord_y):
    """Create a chronometer at the correct coords generating a new canvas with
    its buttons.
    """
    chronometers.append(Chrono(canvas, coord_x, coord_y))
    threads.append(ChronoThread(chronometers[0]))


def update_button(button):
    """Change the simbol of the start/pause button when pressed."""
    if button.cget('text') == '►':
        button.config(text='▐▐ ', font=('Times New Roman', 12,))
        Chrono.stop_chrono(chronometers[0])
    else:
        button.config(text='►', font=('Times New Roman', 13, 'bold'))
        Chrono.start_chrono(chronometers[0])


def restart_button(chrono):
    """Call the restart fuction from the chronometer."""
    chrono.restart_chrono()


def open_rename_chron(button):
    """Open a new window to allow the user rename the selected chornometer."""
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
        command=lambda: close_rename_chron(button, new_name, rename_window)
    )

    confirm_name_button.place(x=180, y=30)
    new_name.place(x=50, y=40)


def close_rename_chron(button, name, window):
    """Close and confirm the writen name and updates the button's name into
    the new one.
    """
    button.config(text=name.get())
    window.destroy()


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
    command=lambda: create_chrono(body, 115, 55)
)

start_chron_button = tk.Button(
    bg='#A78295',
    activebackground='#EFE1D1',
    border=0,
    text='▐▐ ',
    font=('Times New Roman', 12,),
    command=lambda: update_button(start_chron_button)
)

restart_chron_button = tk.Button(
    bg='#A78295',
    activebackground='#EFE1D1',
    border=0,
    text='↺',
    font=('Times New Roman', 15, 'bold'),
    command=lambda: restart_button(chronometers[0])
)

rename_chron_button = tk.Button(
    bg='#3F2E3E',
    activebackground='#3F2E3E',
    activeforeground='#331D2C',
    border=0,
    text='Chronometer',
    foreground='#A78295',
    font=('Times New Roman', 13, 'bold'),
    command=lambda: open_rename_chron(rename_chron_button)
)

texto = header.create_text(
    140,
    50,
    text='MultiChrono',
    font=('Times New Roman', 30),
    fill='#A78295'
)

header.place(x=10, y=25)
body.place(x=25, y=150)
add_chron_button.place(x=120, y=250)
start_chron_button.place(x=190, y=195)
rename_chron_button.place(x=30, y=152)
restart_chron_button.place(x=191, y=155)


root.mainloop()
