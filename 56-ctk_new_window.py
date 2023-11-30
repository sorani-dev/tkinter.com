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


def new():
    """new Create new window"""
    new_window = customtkinter.CTkToplevel(root, fg_color="white")
    new_window.title("This is a new window!")
    new_window.geometry("400x200")
    new_window.resizable(False, True)  # Width, Height

    def close():
        new_window.destroy()
        new_window.update()

    # Close the window
    new_button = customtkinter.CTkButton(new_window, text="Close Window", command=close)
    new_button.pack(pady=40)


my_button = customtkinter.CTkButton(root, text="Open New Window", command=new)
my_button.pack(pady=40)


root.mainloop()
