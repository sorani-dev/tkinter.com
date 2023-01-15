from itertools import count
from pathlib import Path
from tkinter import Tk
from ttkbootstrap.constants import *
import ttkbootstrap.constants as bc
import ttkbootstrap as tb

# Variables
# Global Constants
BASE_PATH: Path = Path(__file__).parent.resolve()
TITLE: str = "Introduction"
DIMENSIONS = "500x350"

# Make app
root: Tk = tb.Window(themename="superhero")
root.title(f"TTk Bootstrap - {TITLE}")
root.iconbitmap(Path(BASE_PATH, "images", "codemy.ico").resolve())
root.geometry(DIMENSIONS)

counter: int = 0


def changer() -> None:
    """
    Change the text in the label on button click
    """
    global counter
    counter += 1

    if counter % 2 == 0:
        my_label.config(text="Hello World!")
    else:
        my_label.config(text="Goodbye World!")


# Colors:
# default, primary, success, info, danger, light, dark

# Create a Label
my_label = tb.Label(
    master=root,
    text="Hello World!",
    font=("Helvetica", 28),
    bootstyle=(SUCCESS, INVERSE),
)
my_label = tb.Label(
    master=root,
    text="Hello World!",
    font=("Helvetica", 28),
    bootstyle="success, inverse",
)
my_label.pack(pady=50)

# Create a Button
my_button = tb.Button(
    master=root, text="Click Me!", bootstyle=(PRIMARY), command=changer
)
my_button = tb.Button(
    master=root, text="Click Me!", bootstyle=(SUCCESS, OUTLINE), command=changer
)
# my_button = tb.Button(master=root, t      ext="Click Me!", bootstyle=(SUCCESS, LINK), command=changer)
my_button.pack(pady=20)

root.mainloop()
