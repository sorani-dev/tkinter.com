from pathlib import Path
from tkinter import END, Label

import customtkinter
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Initialize master widget root
root = customtkinter.CTk()

root.title("Simon Cateau Tkinter - BMI Calculator")
root.iconbitmap(
    Path(__file__).parent.resolve().joinpath("images", "codemy.ico").resolve()
)
root.geometry("500x650")


# Define the image
meter = ImageTk.PhotoImage(
    Image.open(
        Path(__file__).parent.resolve().joinpath("images", "meter2.png").resolve()
    )
)
meter_image = Label(root, image=meter, bd=0)
meter_image.pack(pady=20)


def get_bmi() -> None:
    """
    Calculate and display BMI score
    """
    # Calculate BMI (weight/height^2) If pounds and inches multiply result by 703
    try:
        our_height_old = (int(h_entry.get()) / 100) * (int(h_entry.get()) / 100)
        our_height = (int(h_entry.get()) / 100) ** 2
    except ValueError:
        our_height_old = float(h_entry.get()) * float(h_entry.get())
        our_height = float(h_entry.get()) ** 2

    our_weight = int(w_entry.get())

    bmi = our_weight / our_height * 703
    bmi_rounded = round(bmi, 1)

    results.configure(text=f"{bmi_rounded}")

    # Logic
    if bmi_rounded < 18.5:
        results.configure(text=f"{bmi_rounded}\nUnderweight", text_color="#54D1E1")
    elif bmi_rounded >= 18.5 and bmi_rounded < 24.9:
        results.configure(text=f"{bmi_rounded}\nNormal", text_color="#b3d686")
    elif bmi_rounded >= 25.0 and bmi_rounded < 29.9:
        results.configure(text=f"{bmi_rounded}\nOverweight", text_color="#fed429")
    elif bmi_rounded >= 30.0 and bmi_rounded < 34.9:
        results.configure(text=f"{bmi_rounded}\nObese", text_color="#fbaf42")
    elif bmi_rounded >= 35.0:
        results.configure(text=f"{bmi_rounded}\nExtreme Obese", text_color="#f25356")


def clear_screen() -> None:
    """
    Delete all entry boxes
    """
    h_entry.delete(0, END)
    w_entry.delete(0, END)
    results.config(text="")


# Define Entry Boxes
# Height entry
h_entry = customtkinter.CTkEntry(
    master=root,
    placeholder_text="Height in inches",
    width=200,
    height=30,
    border_width=1,
    corner_radius=10,
)
h_entry.pack(pady=20)

# Width Entry
w_entry = customtkinter.CTkEntry(
    master=root,
    placeholder_text="Weight in pounds",
    width=200,
    height=30,
    border_width=1,
    corner_radius=10,
)
w_entry.pack(pady=20)

# Buttons
button_bmi = customtkinter.CTkButton(
    master=root,
    text="Calculate BMI",
    width=100,
    height=40,
    compound="top",
    command=get_bmi,
)
button_bmi.pack(pady=20)

button_clear_screen = customtkinter.CTkButton(
    master=root,
    text="Clear Screen",
    width=100,
    height=40,
    fg_color="#D35B58",
    hover_color="#C77C78",
    command=clear_screen,
)
button_clear_screen.pack(pady=20)

# Result
results = customtkinter.CTkLabel(master=root, text="", font=("Helvetica", 28))
results.pack(pady=50)


# Run program
root.mainloop()
