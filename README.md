<p align="center">
  <img src=https://github.com/MiniX16/MultiChrono/blob/main/assets/Icon.png alt="Proyect's Title">
</p>
<p align="center">
  <a href="https://github.com/MiniX16/MultiChrono/actions/workflows/pylint.yml">
    <img src="https://github.com/MiniX16/MultiChrono/actions/workflows/pylint.yml/badge.svg" alt="pylint">
  </a>
  <a>
    <img src="https://img.shields.io/badge/STATUS-FINISHED-%232db84d" alt="Build Status">
  </a>
  <a>
    <img src="https://img.shields.io/badge/tkinter-0.1.0-purple" alt="Based-on library">
  </a>
</p>

---

This is a simple GUI made with Python, based on [_tkinter_](https://docs.python.org/es/3/library/tkinter.html), a useful microframework for creating user interfaces. This program is quite straightforward; I've created it as an introduction to GUI development.

The program allows you to  __create multiple chronometers__ within a tiny GUI. These chronometers have basic functionalities, such as  __starting__, __stoping__, __changing their names__ (by clicking on the chronometer's name), and __removing__ them.You can also __save__ the current chronometers, including their names and respective time values. With a saved file, you can later __load__ these chronometers to continue where you left off."

# Usage

Usage is very simple. To get started, run the following command to install the requirements, which in this case is only the tkinter library:

`pip install -r requirements.txt`

Next, execute this command to launch the program when you are in the _src_ folder:

`python multi_chrono`

The interface is very straightforward; I believe each button clearly indicates its function.

---

Here you have some images of how the program looks like:

<p align="center">
  <img src=https://github.com/MiniX16/MultiChrono/blob/main/assets/Empty_img.png alt="No chronometers">
  <img src=https://github.com/MiniX16/MultiChrono/blob/main/assets/Chronometers_img.png alt="chronometers">
</p>


> [!NOTE]  
> Keep in mind that you can modify the saved _txt file_ to load the timers you want with the values you prefer. The syntax is simple; on an odd-numbered line (starting with the first), you put the name, and on the next line (even-numbered), you put the desired value in seconds, ending with _'.0'_ just like in the image:
<p align="center">
  <img src=https://github.com/MiniX16/MultiChrono/blob/main/assets/Load_file_img.png alt="save">
</p>
