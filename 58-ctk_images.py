from pathlib import Path
from tkinter import Tk
import customtkinter

from PIL import Image


# Variables
# Global Constants
BASE_PATH: Path = Path(__file__).parent.resolve()
TITLE: str = "Images"
DIMENSIONS = "400x550"

# Set the theme and color options

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme(
    "dark-blue"
)  # Themes: blue (default), dark-blue, green


# Make app
root: Tk = customtkinter.CTk()

root.title(f"Custom Tkinter - {TITLE}")
root.iconbitmap(Path(BASE_PATH, "images", "codemy.ico").resolve())
root.geometry(DIMENSIONS)


my_image = customtkinter.CTkImage(
    light_image=Image.open("images/aspen1.png"),
    dark_image=Image.open("images/aspen1.png"),
    size=(180, 250),  # Width x Height
)

my_label = customtkinter.CTkLabel(root, text="", image=my_image)
my_label.pack(pady=10)


root.mainloop()
