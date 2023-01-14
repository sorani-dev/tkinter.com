from pathlib import Path
from tkinter import END, Button, Entry, Text, Tk
from tkinter.ttk import LabelFrame
import whois

# Variables 
# Global Constants
BASE_PATH: Path = Path(__file__).parent.resolve()
TITLE:str = "Domain Name Lookup" 
DIMENSIONS = "500x550"

# Make app
root:Tk = Tk()
root.title(f"Simon Cateau Tkinter - {TITLE}")
root.iconbitmap(Path(BASE_PATH, "images", "codemy.ico").resolve())
root.geometry(DIMENSIONS)

# Lookup function
def lookup() -> None:
    """
    Lookup WHOIS from DSN
    """
    # Delete Text in box
    my_text.delete(1.0, END)

    # Get Domain Info
    domain = my_entry.get().strip()
    domain_info:whois.parser.WhoisEntry = whois.whois(domain)

    # my_text.insert(1.0, str(domain_info))

    # Loop over the domain info
    for key, value in domain_info.items(): 
        # Output to text box
        my_text.insert(1.0, f"{key}: {value}" + "\n\n")


# GUI
my_frame = LabelFrame(root, text="Lookup Domain Name")
my_frame.pack(pady=20)

my_entry = Entry(my_frame, font=("Helvetica", 18))
my_entry.grid(row=0, column=0, pady=10, padx=10)

my_button = Button(master=my_frame, text="Lookup Domain", command=lookup)
my_button.grid(row=0, column=1, padx=10)

my_text = Text(master=root, width=50)
my_text.pack()


root.mainloop()
