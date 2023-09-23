from pathlib import Path
from tkinter import Tk

import ttkbootstrap as tb
from ttkbootstrap.constants import *

# Variables
# Global Constants
BASE_PATH: Path = Path(__file__).parent.resolve()
TITLE: str = "Spinbox"
DIMENSIONS = "500x350"

# Make app
root: Tk = tb.Window(themename="superhero")
root.title(f"TTk Bootstrap - {TITLE}")
root.iconbitmap(Path(BASE_PATH, "images", "codemy.ico").resolve())
root.geometry(DIMENSIONS)


def spinny():
    """spinny Get the spinner value and set it into the label"""
    my_label.config(text=my_spinbox.get())


# Spinbox List
stuff = ["Lisbeth", "John", "Ana", "April", "Sam", "Bob", "Simon"]


# Spinbox!!
my_spinbox = tb.Spinbox(
    root,
    bootstyle=SUCCESS,
    font=("Helvetica", 18),
    from_=0,  # Start value
    to=10,  # End value
    values=stuff,  # Overrides the from_ and to
    state="readonly",  # Selectable state of the widget
    command=spinny,  # use the selected box each time it is changed
)
my_spinbox.pack(pady=20)

# Set Spinbox default
my_spinbox.set("Lisbeth")

# Button
my_button = tb.Button(root, text="Click Me!", bootstyle=SUCCESS, command=spinny)
my_button.pack(pady=20)

# Label
my_label = tb.Label(root, text="", font=("Helvetica", 18))
my_label.pack(pady=20)

root.mainloop()
