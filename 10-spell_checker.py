from pathlib import Path
from tkinter import END, Button, Text, Tk
from textblob import TextBlob

# Variables 
# Global Constants
BASE_PATH: Path = Path(__file__).parent.resolve()
TITLE:str = "Spell Checker" 
DIMENSIONS = "500x500"

# Make app
root:Tk = Tk()
root.title(f"Simon Cateau Tkinter - {TITLE}")
root.iconbitmap(Path(BASE_PATH, "images", "codemy.ico").resolve())
root.geometry(DIMENSIONS)

def spellerize() ->None:
    """
    Spell check the text in the Text box
    """
    # Grab text from box
    text_content:str = my_text.get(1.0, END)
    # Delete text box contents
    my_text.delete(1.0, END)

    # Convert text to blob
    blobby = TextBlob(text=text_content)
    # Fix spelling errors
    my_text.insert(1.0, str(blobby.correct()))


# Build GUI
my_text =Text(master=root, width=50)
my_text.pack(pady=20)

my_button = Button(master=root, text="Fix Spelling Errors", command=spellerize)
my_button.pack(pady=20)

root.mainloop()
