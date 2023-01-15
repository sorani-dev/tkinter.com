import os
from pathlib import Path
from tkinter import Button, Label, Tk, filedialog

# Variables 
# Global Constants
BASE_PATH: Path = Path(__file__).parent.resolve()
TITLE:str = "Check number of files..." 
DIMENSIONS = "500x350"

# Make app
root:Tk = Tk()
root.title(f"{TITLE}")
root.iconbitmap(Path(BASE_PATH, "images", "codemy.ico").resolve())
root.geometry(DIMENSIONS)

def checker() -> None:
    """
    Check and display the number of files in a particular directory
    """
    # Counters
    number_of_files:int =0
    number_of_directories:int =0

    # Choose Directory
    input_path = filedialog.askdirectory()
    
    if input_path:
        # Loop through directory and count files
        for root, dirs, files in os.walk(input_path):
            # Count files
            for _ in files:
                number_of_files +=1
            # print(number_of_files)
            # number_of_files = sum(bool(f) for f in files) 
            # print(number_of_files)
            for _ in dirs:
                number_of_directories +=1
            # Update the File count label
            my_label.config(text=f"Check Number of Files: {number_of_files}\nNumber of directories: {number_of_directories}")

# GUI
my_label = Label(master=root, text="Number of Files: ", font=("Helvetica", 28))
my_label.pack(pady=50)

my_button= Button(master=root, text="Check Number Of Files", command=checker)
my_button.pack()

root.mainloop()
