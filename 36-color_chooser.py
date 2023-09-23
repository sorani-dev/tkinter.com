from pathlib import Path
from tkinter import Tk

import ttkbootstrap as tb
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs.colorchooser import ColorChooserDialog

# Variables
# Global Constants
BASE_PATH: Path = Path(__file__).parent.resolve()
TITLE: str = "Color Chooser"
DIMENSIONS = "700x350"

# Make app
root: Tk = tb.Window(themename="superhero")
root.title(f"TTk Bootstrap - {TITLE}")
root.iconbitmap(Path(BASE_PATH, "images", "codemy.ico").resolve())
root.geometry(DIMENSIONS)


def change_bg_color():
    # Create Color Chooser
    my_color = ColorChooserDialog()
    # Show Color Chooser
    my_color.show()
    # Return Color Chooser Info
    # forma of the return value: {RGB} {HSL} HEX
    colors = my_color.result
    # Output colors result to the label (.hex, .hsl, .rgb)
    my_label.config(text=colors.hex)
    # Change the background color of the app to chosen color
    # root.configure(background=my_color.result.hex)
    root.configure(background=colors.hex)


my_button = tb.Button(
    root, text="Change Background Color!", bootstyle=DANGER, command=change_bg_color
)
my_button.pack(pady=40)

my_label = tb.Label(root, text="", font=("Hevetica", 18))
my_label.pack(pady=10)


root.mainloop()
