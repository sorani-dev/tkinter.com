from pathlib import Path
from telnetlib import OUTMRK
from tkinter import Frame, IntVar, Label, Menu, Tk, ttk

BASE_PATH = Path(__file__).parent.resolve()

root = Tk()
root.title("Simon Cateau Tkinter - Styles and Themes")
root.iconbitmap(Path(BASE_PATH, "images", "codemy.ico").resolve())
root.geometry("500x350")

# First method to Style Widgets interface
style = ttk.Style(master=root)
style.theme_use("default")

# See included styles
print(ttk.Style().theme_names())
theme_list: tuple[str] = ttk.Style().theme_names()

def theme_change(theme:str) -> None:
    """
    Change the UI current theme style

    Args:
        theme (str): Theme name
    """
    print(theme)
    # Change style
    style.theme_use(themename=theme)
    # Display current theme name
    my_label.config(text=f"Login - {theme}")
    pass

# Create a Menu to display and toggle on or off available ttk themes
my_menu = Menu(master=root)
root.config(menu=my_menu)

theme_menu = Menu(master=my_menu, tearoff=0)
my_menu.add_cascade(label="Themes", menu=theme_menu)

# Sub menu
for theme in theme_list:
    theme_menu.add_command(label=theme.title(), command=lambda theme=theme: theme_change(theme=theme))

# Create the Widgets
# Header Label
my_label = Label(master=root, text="Login", font=("Helvetica", 18))
my_label.pack(pady=20)

# Login Frame
login_frame = ttk.Frame(root)
login_frame.pack(pady=20)

# Username and Password Entry Boxes and Labels
un_label = ttk.Label(login_frame, text="User Name: ")
un_label.grid(row=0, column=0, padx=10, pady=(20, 5))

un_entry = ttk.Entry(login_frame)
un_entry.grid(row=0, column=1, padx=10, pady=(20, 5))

pwd_label = ttk.Label(login_frame, text="Password: ")
pwd_label.grid(row=1, column=0, padx=10, pady=(20, 5))

pwd_entry = ttk.Entry(login_frame, show="*")
pwd_entry.grid(row=1, column=1, padx=10, pady=(20, 5))


# Login Button
my_button = ttk.Button(master=root, text="Login")
my_button.pack(pady=0)

# Radio Frame
radio_frame = Frame(root)
radio_frame.pack(pady=0)

var = IntVar()

my_radio1 = ttk.Radiobutton(radio_frame, text="Remenber Me", variable=var, )
my_radio1.grid(row=0, column=0, padx=20)

my_radio1 = ttk.Radiobutton(radio_frame, text="Don't Remenber Me", variable=var, )
my_radio1.grid(row=0, column=1)



root.mainloop()
