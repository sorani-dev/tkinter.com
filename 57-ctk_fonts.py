from pathlib import Path
from tkinter import Tk
import customtkinter

# Variables
# Global Constants
BASE_PATH: Path = Path(__file__).parent.resolve()
TITLE: str = "Fonts"
DIMENSIONS = "400x200"


# Make app
root: Tk = customtkinter.CTk()

root.title(f"Custom Tkinter - {TITLE}")
root.iconbitmap(Path(BASE_PATH, "images", "codemy.ico").resolve())
root.geometry(DIMENSIONS)


def change():
    """change Change the text font"""
    my_font.configure(
        underline=False, overstrike=False, size=22, slant="roman", family="Helvetica"
    )


my_font = customtkinter.CTkFont(family="Helvetica")
my_font = customtkinter.CTkFont(
    family="Times",
    size=44,
    weight="bold",  # "normal" , "bold" (default: None)
    slant="italic",  # "italic", "roman" (default: "roman")
    underline=True,  # boolean (default: False)
    overstrike=True,  # boolean (default: False)
)

my_label = customtkinter.CTkLabel(root, text="This is text", font=my_font)
my_label.pack(pady=40)

my_button = customtkinter.CTkButton(root, text="Change Text Font", command=change)
my_button.pack()

root.mainloop()
