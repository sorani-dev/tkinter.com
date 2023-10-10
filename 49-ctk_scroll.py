from pathlib import Path
from tkinter import Tk
import customtkinter

# Variables
# Global Constants
BASE_PATH: Path = Path(__file__).parent.resolve()
TITLE: str = "Scrollable Frame!"
DIMENSIONS = "700x300"


# Make app
root: Tk = customtkinter.CTk()

root.title(f"Custom Tkinter - {TITLE}")
root.iconbitmap(Path(BASE_PATH, "images", "codemy.ico").resolve())
root.geometry(DIMENSIONS)


# Create a Scrollable Frame
my_frame = customtkinter.CTkScrollableFrame(
    root,
    orientation="vertical",  # 'horizontal' or 'vertical' (default: 'vertical')
    width=300,
    height=200,
    label_text="Hello world!",
    label_fg_color="blue",
    label_text_color="orange",
    label_font=("Helevetica", 18),
    label_anchor="center",  # n, ne, e, se, s, sw, w, nw, center, (default: 'center')
    border_width=3,
    border_color="limegreen",
    fg_color="crimson",
    scrollbar_fg_color="yellow",
    scrollbar_button_color="magenta",
    scrollbar_button_hover_color="#b61d8c",
    corner_radius=15,
)
my_frame.pack(pady=40)

# For loop for Buttons
for _ in range(20):
    customtkinter.CTkButton(my_frame, text="This is a button!").pack(pady=10)


root.mainloop()
