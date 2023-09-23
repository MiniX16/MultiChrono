"""Open the window where all the program will be run. Generates all the
chronometers and all its buttoms. Furthermore, it configures the window.
"""
import tkinter as tk
from tkinter import filedialog, ttk

from chrono import Chrono
from chrono_threading import ChronoThread

root = tk.Tk()
header = tk.Canvas(width=280, height=100, bg='#3F2E3E', highlightthickness=0)

generators = []
GAP = 100


class ChronoGenerator():
    """Allow the app to generate new chronometers with all its fuctionalities.
    """
    def __init__(self, gap) -> None:
        self.body = tk.Canvas(
            width=250,
            height=80,
            bg='#3F2E3E',
            highlightthickness=0,
        )
        self.rename_chron_button = tk.Button(
            bg='#3F2E3E',
            activebackground='#3F2E3E',
            activeforeground='#331D2C',
            border=0,
            text='Chronometer',
            foreground='#A78295',
            font=('Times New Roman', 13, 'bold'),
            command=self.open_rename_chron,
        )
        self.restart_chron_button = tk.Button(
            bg='#A78295',
            activebackground='#EFE1D1',
            border=0,
            text='↺',
            font=('Times New Roman', 15, 'bold'),
            command=self.restart_button,
        )
        self.start_chron_button = tk.Button(
            bg='#A78295',
            activebackground='#EFE1D1',
            border=0,
            text='▐▐ ',
            font=('Times New Roman', 12,),
            command=self.update_button,
        )
        self.delete_chron_button = tk.Button(
            width=2,
            height=3,
            bg='#A78295',
            activebackground='#EFE1D1',
            border=0,
            text='❌',
            font=('Times New Roman', 11, 'bold'),
            command=lambda: [self.relocate_chronos(), self.remove_chron()]
        )

        self.chrono = Chrono(self.body, 80, 48)
        self.chrono_thread = ChronoThread(self.chrono)
        self.body.place(x=25, y=160 + gap)
        self.start_chron_button.place(x=190, y=205 + gap)
        self.rename_chron_button.place(x=30, y=162 + gap)
        self.restart_chron_button.place(x=191, y=165 + gap)
        self.delete_chron_button.place(x=240, y=168 + gap)
        self.chrono_thread.start()

    def update_button(self) -> None:
        """Change the simbol of the start/pause button when pressed."""
        if self.start_chron_button.cget('text') == '►':
            self.start_chron_button.config(
                text='▐▐ ',
                font=('Times New Roman', 12,),
            )
            Chrono.stop_chrono(self.chrono)
        else:
            self.start_chron_button.config(
                text='►',
                font=('Times New Roman', 13, 'bold'),
            )
            Chrono.start_chrono(self.chrono)

    def restart_button(self) -> None:
        """Call the restart fuction from the chronometer."""
        self.chrono.restart_chrono()

    def open_rename_chron(self) -> None:
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
            command=lambda: self.close_rename_chron(new_name, rename_window),
        )

        confirm_name_button.place(x=180, y=30)
        new_name.place(x=50, y=40)

    def close_rename_chron(self, name, window) -> None:
        """Close and confirm the writen name and updates the button's name into
        the new one.
        """
        self.rename_chron_button.config(text=name.get())
        window.destroy()

    def relocate_chronos(self) -> None:
        """Relocate all indicated chronometers just one site higher."""
        behind_self = False

        for chrono in generators:
            if behind_self:

                to_relocate = [
                    chrono.body,
                    chrono.rename_chron_button,
                    chrono.start_chron_button,
                    chrono.restart_chron_button,
                    chrono.delete_chron_button,
                ]
                for item in to_relocate:
                    item.place(x=item.winfo_x(), y=item.winfo_y() - GAP)

            if chrono.body.winfo_y() == self.body.winfo_y():
                index = generators.index(chrono)
                behind_self = True

        add_chron_button.place(
            x=add_chron_button.winfo_x(),
            y=add_chron_button.winfo_y() - GAP,
        )
        del generators[index]  # Deletes himself from the generators list

    def remove_chron(self) -> None:
        """Remove all the chronometer and chronometer's elemnts from the
        window and returns the list of chronometer to move.
        """
        to_destroy = [
            self.body,
            self.rename_chron_button,
            self.start_chron_button,
            self.restart_chron_button,
            self.delete_chron_button,
        ]

        for item in to_destroy:
            item.destroy()


def generate_chrono() -> None:
    """Create and chronometer generator that places the chronometer and all
    its features.
    """
    add_chron_button.place(x=120, y=260 + len(generators) * GAP)
    generators.append(ChronoGenerator(len(generators) * GAP))


def import_chronos(loaded) -> None:
    """Take the variable generated by the loading file and generates the
    correct chronometers.
    """
    for chrono in loaded:
        generate_chrono()
        generators[-1].rename_chron_button.config(
            text=chrono[0],
            font=('Times New Roman', 13, 'bold'),
        )
        generators[-1].chrono.my_time = float(chrono[1])
        generators[-1].chrono.canvas.itemconfig(
            generators[-1].chrono.view,
            text=Chrono.format_time(float(chrono[1])),
        )


def save_chronos() -> None:
    """Allow the user to save in a txt file the values and configuration of
    all chronometers.
    """
    saved_file = filedialog.asksaveasfilename(
        defaultextension='.txt',
        filetypes=[
            ("Archivos de texto", "*.txt"),
            ("Todos los archivos", "*.*"),
        ]
    )
    if saved_file:
        with open(saved_file, 'w', encoding='utf-8') as file:
            to_save = ''
            for generator in generators:
                generator.chrono.stop_chrono()
                to_save += (
                    generator.rename_chron_button.cget('text')
                    + '\n'
                    + str(generator.chrono.actual_time)
                    + '\n'
                )
            file.write(to_save)


def load_chronos() -> None:
    """Allow the user to load a txt file with all chronos."""
    loaded_chronos = []
    loaded_file = filedialog.askopenfilename(
        filetypes=[
            ("Archivos de texto", "*.txt"),
            ("Todos los archivos", "*.*"),
        ]
    )
    if loaded_file:
        with open(loaded_file, "r", encoding='utf-8') as file:
            for line, text in enumerate(file):
                if int(line) % 2 == 0:
                    name = text
                else:
                    loaded_chronos.append([name[:-1], text[:-1]])
    import_chronos(loaded_chronos)


if __name__ == '__main__':
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
        command=generate_chrono,
    )

    save_button = tk.Button(
        width=3,
        height=1,
        bg='#3F2E3E',
        activebackground='#2D1D2D',
        border=0,
        text='⬇',
        font=('Times New Roman', 11, 'bold'),
        command=save_chronos,
    )

    load_button = tk.Button(
        width=3,
        height=1,
        bg='#3F2E3E',
        activebackground='#2D1D2D',
        border=0,
        text='⬆',
        font=('Times New Roman', 11, 'bold'),
        command=load_chronos,
    )

    texto = header.create_text(
        140,
        50,
        text='MultiChrono',
        font=('Times New Roman', 30),
        fill='#A78295',
    )

    header.place(x=10, y=35)
    add_chron_button.place(x=120, y=160)
    save_button.place(x=5, y=5)
    load_button.place(x=45, y=5)

    root.mainloop()
