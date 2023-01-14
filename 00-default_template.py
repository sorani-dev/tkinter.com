from pathlib import Path
from tkinter import Tk

# Variables 
# Global Constants
BASE_PATH: Path = Path(__file__).parent.resolve()
TITLE:str = "Default Title" 
DIMENSIONS = "500x350"

# Make app
root:Tk = Tk()
root.title(f"Simon Cateau Tkinter - {TITLE}")
root.iconbitmap(Path(BASE_PATH, "images", "codemy.ico").resolve())
root.geometry(DIMENSIONS)

root.mainloop()
