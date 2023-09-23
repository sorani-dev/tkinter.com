from pathlib import Path
from tkinter import Tk

import ttkbootstrap as tb
from ttkbootstrap.constants import *

# Variables
# Global Constants
BASE_PATH: Path = Path(__file__).parent.resolve()
TITLE: str = "Slider/Scale"
DIMENSIONS = "500x350"

# Make app
root: Tk = tb.Window(themename="superhero")
root.title(f"TTk Bootstrap - {TITLE}")
root.iconbitmap(Path(BASE_PATH, "images", "codemy.ico").resolve())
root.geometry(DIMENSIONS)


def scaler(e):
    """scaler Change the label on scale value change

    :param e: Event
    :type e:
    """
    my_label.config(text=f"{int(my_scale.get())}%")


# Create a Scale/Slider
my_scale = tb.Scale(
    root,
    bootstyle=WARNING,
    length=400,  # Physical length
    orient="horizontal",  # 'horizontal' or 'vertical'
    from_=0,  # Starting value
    to=100,  # End value
    state="normal",  # disabled:  not selectable, normal: selectable (default)
    command=scaler,
)
my_scale.pack(pady=50)


# Create a Label
my_label = tb.Label(root, text="", font=("Helvetica", 18))
my_label.pack()

root.mainloop()
