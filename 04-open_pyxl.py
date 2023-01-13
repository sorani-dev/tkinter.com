from pathlib import Path
from tkinter import END, filedialog, messagebox
from tkinter import ttk
from tkinter.ttk import Treeview
from zipfile import BadZipFile

import customtkinter
import pandas as pd

BASE_PATH = Path(__file__).parent.resolve()

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Initialize master widget root
root = customtkinter.CTk()

root.title("Simon Cateau Tkinter - Excel Treeview")
root.iconbitmap(
    Path(__file__).parent.resolve().joinpath("images", "codemy.ico").resolve()
)
root.geometry("900x400")


def open_excel() -> None:
    """
    Open an Excel file
    """
    # Open a file
    my_file = filedialog.askopenfilename(
        title="Open File",
        filetypes=(
            ("Excel Files", "*.xls, *.xlsx"),
            ("Open Document SpreadSheet Files", "*.odf, *.odt"),
            ("All Files", "*.*"),
        ),
        defaultextension="*.xlsx",
        initialdir=BASE_PATH,
    )

    # Grab the file
    # if my_file == "":
    #     messagebox.showerror("Woah!", f"Please enter a filename")
    # return

    try:
        df: pd.DataFrame = pd.read_excel(my_file, engine="openpyxl")
    except BadZipFile as e:
        messagebox.showerror("Woah!", f"There was a problem! {e}")
        return
    except Exception as e:
        messagebox.showerror("Woah!", f"There was a problem! {e}")
        return

    # Clear the treeview
    my_tree.delete(*my_tree.get_children())

    # Get the headers
    my_tree["column"] = list(df.columns)
    my_tree["show"] = "headings"

    # Show the headers
    for col in my_tree["column"]:
        my_tree.heading(col, text=col)

    # Show Data
    df_rows: list = df.to_numpy().tolist()
    for row in df_rows:
        my_tree.insert("", END, values=row)


# Treeview
my_tree = Treeview(master=root)
my_tree.pack(pady=20)

# Hack the column height
my_tree.heading("#0", text="\n")

# Set tree style
style = ttk.Style()
style.theme_use("default")

# Change style colors
style.configure(
    "Treeview",
    backgroud="#707070",
    foreground="black",
    rowheight=25,
    fieldbackground="#707070",
)

# Change colors of headers
style.configure("Treeview.Heading", background="#535353", foreground="black")

# Change color of selected rows
style.map("Treeview", background=[("selected", "#535353")])

# Button
my_button = customtkinter.CTkButton(
    master=root, text="Open Excel File", command=open_excel
)
my_button.pack(pady=20)

root.mainloop()
