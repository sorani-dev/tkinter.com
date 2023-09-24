from pathlib import Path
from tkinter import Tk

import ttkbootstrap as tb
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledText

# Variables
# Global Constants
BASE_PATH: Path = Path(__file__).parent.resolve()
TITLE: str = "Scrolled Text Widget?!"
DIMENSIONS = "700x350"

# Make app
root: Tk = tb.Window(themename="superhero")
root.title(f"TTk Bootstrap - {TITLE}")
root.iconbitmap(Path(BASE_PATH, "images", "codemy.ico").resolve())
root.geometry(DIMENSIONS)

# Text Widget
my_text = ScrolledText(
    root, height=20, width=110, wrap=WORD, autohide=False, bootstyle=DANGER, hbar=True
)
my_text.pack(pady=15)


root.mainloop()
