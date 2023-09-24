from pathlib import Path
from tkinter import PhotoImage, Tk

import ttkbootstrap as tb
from ttkbootstrap.icons import Icon

# Variables
# Global Constants
BASE_PATH: Path = Path(__file__).parent.resolve()
TITLE: str = "Icons!"
DIMENSIONS = "500x350"

# Make app
root: Tk = tb.Window(themename="superhero")
root.title(f"TTk Bootstrap - {TITLE}")
root.iconbitmap(Path(BASE_PATH, "images", "codemy.ico").resolve())
root.geometry(DIMENSIONS)


# Icons : warning, icon, error, info, question
img = PhotoImage(data=Icon.warning)
img = PhotoImage(data=Icon.icon)
img = PhotoImage(data=Icon.error)
img = PhotoImage(data=Icon.info)
img = PhotoImage(data=Icon.question)

# Label
my_label = tb.Label(image=img)
my_label.pack(pady=40)


root.mainloop()
