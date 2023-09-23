from pathlib import Path
from tkinter import Text, Tk

import ttkbootstrap as tb
from ttkbootstrap.constants import *

# Variables
# Global Constants
BASE_PATH: Path = Path(__file__).parent.resolve()
TITLE: str = "Scrollbar"
DIMENSIONS = "500x350"

# Make app
root: Tk = tb.Window(themename="superhero")
root.title(f"TTk Bootstrap - {TITLE}")
root.iconbitmap(Path(BASE_PATH, "images", "codemy.ico").resolve())
root.geometry(DIMENSIONS)

# Frame
my_frame = tb.Frame(root)
my_frame.pack(pady=20)

# Create a Scrollbar
my_scroll = tb.Scrollbar(
    my_frame,
    orient="horizontal",
    bootstyle="dark round",  # different bootstyles to add to scrollbar:
    # - round
    # no add -> square scrollbar at its ends
)
my_scroll.pack(side="bottom", fill="x")

# Create a Text Widget
my_text = Text(
    my_frame,
    width=30,
    height=25,
    xscrollcommand=my_scroll.set,
    wrap="none",
    font=("Helvatica", 18),
)
my_text.pack()

# Configure the scrollbar
my_scroll.config(command=my_text.xview)

root.mainloop()
