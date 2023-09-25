from pathlib import Path

import customtkinter

# Set the theme and color options

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme(
    "dark-blue"
)  # Themes: blue (default), dark-blue, green

# Make app
root = customtkinter.CTk()

root.title("Tkinter.com - Checkbox!")
root.iconbitmap(Path(__file__).parent.joinpath("images", "codemy.ico").resolve())
root.geometry("750x500")


def game():
    """game Play the game when checkbox is checked"""
    if check_var.get() == "on":
        my_label.configure(text="You clicked the thing")
    else:
        my_label.configure(text="You didn't click the thing")
    text_var.set("Anwesome!!")
    print(text_var.get())


def clear_me():
    """clear_me Clear the checkbox"""
    my_check.deselect()
    text_var.set("Would You Like To Play A Game?")


# Checkbox state
check_var = customtkinter.StringVar(value="off")
# Checkbox text
text_var = customtkinter.StringVar(value="Would You Like To Play A Game?")

my_check = customtkinter.CTkCheckBox(
    root,
    # text="Would You Like To Play A Game?",
    variable=check_var,
    onvalue="on",
    offvalue="off",
    checkbox_height=50,  # in pixels
    checkbox_width=50,  # in pixels
    font=("Helvetica", 18),
    corner_radius=50,  # checkbox corners more round with higher value
    fg_color="blue",
    hover_color="green",
    text_color="blue",
    hover=False,
    textvariable=text_var,
)
my_check.pack(pady=40)


my_label = customtkinter.CTkLabel(root, text="")
my_label.pack(pady=20)


my_button = customtkinter.CTkButton(root, text="Submit", command=game)
my_button.pack(pady=20)


clear_button = customtkinter.CTkButton(root, text="Clear", command=clear_me)
clear_button.pack(pady=20)


toggle_button = customtkinter.CTkButton(root, text="Toggle", command=my_check.toggle)
toggle_button.pack(pady=20)


select_button = customtkinter.CTkButton(root, text="Select", command=my_check.select)
select_button.pack(pady=20)


root.mainloop()
