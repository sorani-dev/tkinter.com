from pathlib import Path
from ttkthemes import ThemedTk

# Variables 
# Global Constants
BASE_PATH: Path = Path(__file__).parent.resolve()
TITLE:str = "Default Title" 
DIMENSIONS = "500x350"

# Make app
root:ThemedTk = ThemedTk()
root.title(f"Simon Cateau Tkinter - {TITLE}")
root.iconbitmap(Path(BASE_PATH, "images", "codemy.ico").resolve())
root.geometry(DIMENSIONS)

root.mainloop()
