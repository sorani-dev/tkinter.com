from pathlib import Path
from tkinter import Tk

import ttkbootstrap as tb
from ttkbootstrap.constants import *

# Variables
# Global Constants
BASE_PATH: Path = Path(__file__).parent.resolve()
TITLE: str = "Separator and Sizegrip"
DIMENSIONS = "500x350"

# Make app
root: Tk = tb.Window(themename="superhero")
root.title(f"TTk Bootstrap - {TITLE}")
root.iconbitmap(Path(BASE_PATH, "images", "codemy.ico").resolve())
root.geometry(DIMENSIONS)


label1 = tb.Label(root, text="Label 1", bootstyle=LIGHT)
label1.pack(pady=40)

# Separator
my_sep = tb.Separator(root, bootstyle=INFO, orient="horizontal")
my_sep.pack(fill=X, padx=(100, 100))


label2 = tb.Label(root, text="Label 2", bootstyle=LIGHT)
label2.pack(pady=40)

# Sizegrip
my_sizegrip = tb.Sizegrip(root, bootstyle="info")
my_sizegrip.pack(anchor=SE, fill="both", expand=True)


root.mainloop()
