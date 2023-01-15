from pathlib import Path
from tkinter import Tk
from ttkbootstrap.constants import *
import ttkbootstrap as tb

# Variables 
# Global Constants
BASE_PATH: Path = Path(__file__).parent.resolve()
TITLE:str = "" 
DIMENSIONS = "500x350"

# Make app
root:Tk = tb.Window(themename="superhero")
root.title(f"TTk Bootstrap - {TITLE}")
root.iconbitmap(Path(BASE_PATH, "images", "codemy.ico").resolve())
root.geometry(DIMENSIONS)

root.mainloop()
