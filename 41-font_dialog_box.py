from pathlib import Path
from tkinter import Tk

import ttkbootstrap as tb
from ttkbootstrap.dialogs import FontDialog

# Variables
# Global Constants
BASE_PATH: Path = Path(__file__).parent.resolve()
TITLE: str = "Font Dialog!"
DIMENSIONS = "300x200"

# Make app
root: Tk = tb.Window(themename="superhero")
root.title(f"TTk Bootstrap - {TITLE}")
root.iconbitmap(Path(BASE_PATH, "images", "codemy.ico").resolve())
root.geometry(DIMENSIONS)


def open_font_dialog():
    """open_font_dialog Open a FontDialog box"""
    # Define Font Dialog
    fd = FontDialog()
    #  Show the box
    fd.show()

    # Capture the Result fd.result and update label
    my_label.config(font=fd.result)


# Create a Label and a Button
my_button = tb.Button(root, text="Open Font Dialog", command=open_font_dialog)
my_button.pack(pady=40)

my_label = tb.Label(root, text="Hello World!")
my_label.pack(pady=10)


root.mainloop()
