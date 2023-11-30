from pathlib import Path
from tkinter import Tk
import customtkinter

# Variables
# Global Constants
BASE_PATH: Path = Path(__file__).parent.resolve()
TITLE: str = "Input Window"
DIMENSIONS = "400x200"


# Make app
root: Tk = customtkinter.CTk()

root.title(f"Custom Tkinter - {TITLE}")
root.iconbitmap(Path(BASE_PATH, "images", "codemy.ico").resolve())
root.geometry(DIMENSIONS)


def input_():
    """input_"""
    dialog = customtkinter.CTkInputDialog(
        text="What is your Name?",
        title="Hello There!",
        fg_color="white",
        button_fg_color="red",
        button_hover_color="pink",
        button_text_color="black",
        entry_fg_color="green",
        entry_border_color="red",
        entry_text_color="#aaaaaa",
    )
    input_text = dialog.get_input()
    if input_text:
        my_label.configure(text=f"Hello {input_text}")
    else:
        my_label.configure(text="You forget to type anything!")


# Create a Button
my_button = customtkinter.CTkButton(root, text="Click Me!", command=input_)
my_button.pack(pady=40)

# Create a Label
my_label = customtkinter.CTkLabel(root, text="")
my_label.pack(pady=10)


root.mainloop()
