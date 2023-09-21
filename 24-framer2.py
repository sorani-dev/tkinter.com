from pathlib import Path
from tkinter import Frame, Tk
from ttkbootstrap.constants import *
import ttkbootstrap as tb

# Variables
# Global Constants
BASE_PATH: Path = Path(__file__).parent.resolve()
TITLE: str = "Frames and Labels!"
DIMENSIONS = "500x350"

# Make app
root: Tk = tb.Window(themename="superhero")
root.title(f"TTk Bootstrap - {TITLE}")
root.iconbitmap(Path(BASE_PATH, "images", "codemy.ico").resolve())
root.geometry(DIMENSIONS)

def thing():
    pass

my_frame = Frame(root) # tb.Frame(root, bootstyle=DARK)
my_frame.pack(pady=30)

# Entry box
my_entry = tb.Entry(my_frame,  font=("Helvetica", 18))
my_entry.pack(pady=20, padx=20)

# Button
my_button = tb.Button(root, text="CLICK ME!", bootstyle=DARK, command=thing)
my_button.pack(pady=20, padx=20)

# Label
my_label = tb.Label(root, text="Hello There!", font=("Helvetica", 18), bootstyle="inverse light")
my_label.pack(pady=20)

root.mainloop()
