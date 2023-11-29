from pathlib import Path
from tkinter import Tk
import customtkinter

# Variables
# Global Constants
BASE_PATH: Path = Path(__file__).parent.resolve()
TITLE: str = "TextBox"
DIMENSIONS = "700x300"


# Make app
root: Tk = customtkinter.CTk()

root.title(f"Custom Tkinter - {TITLE}")
root.iconbitmap(Path(BASE_PATH, "images", "codemy.ico").resolve())
root.geometry(DIMENSIONS)

thing = ""


def delete():
    """delete Delete all text from text box"""
    my_text.delete(0.0, "end")


def copy():
    """copy Copy all text from text box"""
    global thing
    thing = my_text.get(0.0, "end")


def paste():
    """paste Paste text into text box"""
    if thing:
        my_text.insert("end", thing)
    else:
        my_text.insert("end", "There is nothing to paste!!")


my_text = customtkinter.CTkTextbox(
    root,
    width=600,
    height=200,
    corner_radius=20,
    border_width=10,
    border_color="#003660",
    border_spacing=10,
    fg_color="silver",
    text_color="black",
    font=("Helvetica", 18),
    wrap="word",  # "char", "word", "none" (default: "char")
    activate_scrollbars=True,  # Boolean (default: True)
    scrollbar_button_color="blue",
    scrollbar_button_hover_color="red",
)
my_text.pack(pady=20)

my_frame = customtkinter.CTkFrame(root)
my_frame.pack(pady=10)


delete_button = customtkinter.CTkButton(my_frame, text="Delete", command=delete)
copy_button = customtkinter.CTkButton(my_frame, text="Copy", command=copy)
paste_button = customtkinter.CTkButton(my_frame, text="Paste", command=paste)

delete_button.grid(row=0, column=0)
copy_button.grid(row=0, column=1, padx=10)
paste_button.grid(row=0, column=2)

root.mainloop()
