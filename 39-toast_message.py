from pathlib import Path
from tkinter import Tk

import ttkbootstrap as tb
from ttkbootstrap.constants import *
from ttkbootstrap.toast import ToastNotification

# Variables
# Global Constants
BASE_PATH: Path = Path(__file__).parent.resolve()
TITLE: str = "Toast Message!"
DIMENSIONS = "300x200"

# Make app
root: Tk = tb.Window(themename="superhero")
root.title(f"TTk Bootstrap - {TITLE}")
root.iconbitmap(Path(BASE_PATH, "images", "codemy.ico").resolve())
root.geometry(DIMENSIONS)


def clicker():
    """clicker Show the ToastNotification"""
    toast.show_toast()


toast = ToastNotification(
    title="My Toast Title",
    message="This is a Toast Message",
    duration=3000,  # duration in milliseconds. Default: None
    alert=True,  # Ring the display bell (True) or not (False). Default: False
    position=(-20, 30, "sw"),  # tuple(int, int, str). Defaut position is bottom right
)

my_button = tb.Button(root, text="Click Me!", command=clicker)
my_button.pack(pady=40)


root.mainloop()
