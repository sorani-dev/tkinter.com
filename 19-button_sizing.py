from pathlib import Path
from tkinter import Tk
from ttkbootstrap.constants import *
import ttkbootstrap as tb

# Variables 
# Global Constants
BASE_PATH: Path = Path(__file__).parent.resolve()
TITLE:str = "Resize Buttons" 
DIMENSIONS = "500x350"

# Make app
root:Tk = tb.Window(themename="superhero")
root.title(f"{TITLE}")
root.iconbitmap(Path(BASE_PATH, "images", "codemy.ico").resolve())
root.geometry(DIMENSIONS)


# Style (for the Button)
my_style: tb.Style = tb.Style()
# style name: which bootstype you want to use 
# plus the name of the Widget separated by dots
my_style.configure('success.Outline.TButton', font=("Helvetica", 18))


my_button = tb.Button(text="Hello World!", width=20, bootstyle="success", 
style="success.Outline.TButton")
my_button.pack(pady=40)

root.mainloop()
