from math import inf
from pathlib import Path
from tkinter import END, Button, Entry, IntVar, Label, Text, Tk, filedialog, messagebox
from tkinter.ttk import LabelFrame
import pypdf

# Variables
# Global Constants
BASE_PATH: Path = Path(__file__).parent.resolve()
TITLE: str = "PDF Text Extractor"
DIMENSIONS = "500x700"

# Utilities Functions
def show_error_message(message: str, title: str = "Woah!")->None:
    messagebox.showerror(title, f"There was a problem! {message}")


# Make app
root: Tk = Tk()
root.title(f"Simon Cateau Tkinter - {TITLE}")
root.iconbitmap(Path(BASE_PATH, "images", "codemy.ico").resolve())
root.geometry(DIMENSIONS)

# Open PDF File Function
def open_pdf() -> None:
    """
    Open and parse a PDF File
    """
    my_file = filedialog.askopenfilename(
        title="Open File",
        filetypes=(("PDF Files", "*.pdf"), ("All Files", "*.*")),
        initialdir=BASE_PATH,
    )
    try:
        # Open File
        pdf_file = pypdf.PdfReader(my_file)
        # Get the number of pages
        # print(len(pdf_file.pages))
        
        number_of_pages = len(pdf_file.pages)
        # print(number_of_pages, len(pdf_file.pages), pdf_file.metadata)

        # Get current page number entered
        try:
            # Remove 1 to entry for pages is a list (index start at 0 not 1)
            current_page_number = int(my_entry.get().strip()) - 1
        except ValueError:
            current_page_number  = 1
        # Make current page number between 0 (1st page) and max pages (last page)
        if current_page_number < 0:
            raise Exception("Page number is negative")
        elif current_page_number >= number_of_pages:
            raise Exception("Page number is too high")
        
        # Update Pages Label
        page_plural = "s" if number_of_pages > 1 else ""
        pages_label.config(
            text=f"Showing {current_page_number + 1} of {number_of_pages} page{page_plural}..."
        )
        val = ""
        my_entry.setvar(val, str(current_page_number))

        # print(pages_label["text"], current_page_number)

        # Select page to read
        current_page:pypdf.PageObject = pdf_file.pages[current_page_number]

        # Get the text content
        content = current_page.extract_text()

        # Clear the text box
        my_text.delete(1.0, END)

        # Output PDF text contents to text
        my_text.insert(1.0, content)   
    except Exception as e:
        print(e)
        show_error_message(message=str(e))


# Text Box
my_text = Text(root, width=60, height=25)
my_text.pack(pady=20)

# LabelFrame and Entry Box
my_labelframe = LabelFrame(root, text="Select Page to Open")
my_labelframe.pack(pady=10)


my_label = Label(my_labelframe, text="Page Number: ")
my_label.grid(row=0, column=0, pady=10, padx=10)

my_entry = Entry(my_labelframe)
my_entry.grid(row=1, column=0, pady=10, padx=10)


# Open Button
my_button = Button(master=root, text="Open PDF", command=open_pdf)
my_button.pack(pady=20)

# Page Number Label
pages_label = Label(master=root, text="")
pages_label.pack(pady=20)

root.mainloop()
