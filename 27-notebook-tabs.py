from pathlib import Path
from tkinter import Text, Tk

import ttkbootstrap as tb
from ttkbootstrap.constants import *

# Variables
# Global Constants
BASE_PATH: Path = Path(__file__).parent.resolve()
TITLE: str = "Notebook Tabs!"
DIMENSIONS = "500x475"

# Make app
root: Tk = tb.Window(themename="superhero")
root.title(f"TTk Bootstrap - {TITLE}")
root.iconbitmap(Path(BASE_PATH, "images", "codemy.ico").resolve())
root.geometry(DIMENSIONS)


my_notebook = tb.Notebook(root, bootstyle=DARK)
my_notebook.pack(pady=20)

# Frames for tabs
tab_1 = tb.Frame(my_notebook)
tab_2 = tb.Frame(my_notebook)

# First Frame
# Label
my_label1 = tb.Label(tab_1, text="My Awesome Label!", font=("Helvetica", 18))
my_label1.pack(pady=20)

# Text box
my_text = Text(tab_1, width=70, height=10)
my_text.pack(pady=10, padx=10)


# Button
my_button = tb.Button(tab_1, text="Click Me!", bootstyle="danger outline")
my_button.pack(pady=20)

# Second Frame
# Label
my_label2 = tb.Label(tab_2, text="This Is Tab Two!", font=("Helvetica", 18))
my_label2.pack(pady=20)

# Add the Frames to the notebook
my_notebook.add(tab_1, text="Tab One")
my_notebook.add(child=tab_2, text="Tab Two")

root.mainloop()
