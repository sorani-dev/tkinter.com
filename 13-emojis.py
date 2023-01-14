from pathlib import Path
from tkinter import Label, Tk

import emoji

# Variables 
# Global Constants
BASE_PATH: Path = Path(__file__).parent.resolve()
TITLE:str = "Emoji's" 
DIMENSIONS = "500x350"

# Make app
root:Tk = Tk()
root.title(f"{TITLE}")
root.iconbitmap(Path(BASE_PATH, "images", "codemy.ico").resolve())
root.geometry(DIMENSIONS)

print(emoji.LANGUAGES, emoji.EMOJI_DATA)

# Create a Label
my_label = Label(master=root, text=f"{emoji.emojize(':astonished_face:')} {emoji.emojize(':face_screaming_in_fear:')} ", font=("Helvetica", 32))
my_label.pack(pady=50)  

root.mainloop()
