from pathlib import Path
from tkinter import Tk

import ttkbootstrap as tb
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledFrame

# Variables
# Global Constants
BASE_PATH: Path = Path(__file__).parent.resolve()
TITLE: str = "Scrolled Frame!"
DIMENSIONS = "700x350"

# Make app
root: Tk = tb.Window(themename="superhero")
root.title(f"TTk Bootstrap - {TITLE}")
root.iconbitmap(Path(BASE_PATH, "images", "codemy.ico").resolve())
root.geometry(DIMENSIONS)

# µLet's craete a Scrolled Frame
my_frame = ScrolledFrame(root, autohide=False, bootstyle="light")
my_frame.pack(padx=15, pady=15, fill=BOTH, expand=YES)


# Creat some buttons
for x in range(21):
    tb.Button(my_frame, bootstyle=INFO, text=f"Click Me! {x}").pack(pady=10)

root.mainloop()
