from pathlib import Path
from tkinter import Tk
from ttkbootstrap.constants import *
import ttkbootstrap as tb

# Variables
# Global Constants
BASE_PATH: Path = Path(__file__).parent.resolve()
TITLE: str = "Entry box widget"
DIMENSIONS = "500x350"

# Make app
root: Tk = tb.Window(themename="superhero")
root.title(f"TTk Bootstrap - {TITLE}")
root.iconbitmap(Path(BASE_PATH, "images", "codemy.ico").resolve())
root.geometry(DIMENSIONS)

# Create Entry Function
def speak() -> None:
    my_label.config(text=f"You Typed: {my_entry.get()}")


# Create Entry Widget
# Colors: primary, secondary, success, info, warning, danger, light, dark
my_entry = tb.Entry(
    root,
    bootstyle=SUCCESS,
    font=("Helvetica", 18),
    foreground="#003660",
    width=15,
    show="*",
)
my_entry.pack(pady=50)

# Create Button
my_button = tb.Button(
    root, bootstyle="dangeer, outline", text="Click Me", command=speak
)
my_button.pack(pady=20)

# Create Label
my_label = tb.Label(root, text="")
my_label.pack(pady=20)

root.mainloop()
