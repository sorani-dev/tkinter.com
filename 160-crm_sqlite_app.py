from pathlib import Path
from tkinter import (
    CENTER,
    END,
    NO,
    RIGHT,
    W,
    Button,
    Entry,
    Frame,
    Label,
    LabelFrame,
    Tk,
    ttk,
    Y,
)
import faker

root = Tk()
root.title("TreeBase")
root.iconbitmap(Path(__file__).parent.joinpath("images", "codemy.ico"))
root.geometry("1000x500")

# Add some Style
style = ttk.Style()

# Pick a Theme
style.theme_use("default")

# Configure the Treeview Colors
style.configure(
    "Treeview",
    background="#d3d3d3",
    foreground="black",
    rowheight=25,
    fieldbackground="#d3d3d3",
)


# Change the Selected Color
style.map("Treeview", background=[("selected", "#347083")])


# Create a Treeview Frame
tree_frame = Frame(root)
tree_frame.pack(pady=10)


# Create a Treeview Scrollbar
tree_scroll = ttk.Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)


# Create the Treeview
my_tree = ttk.Treeview(
    tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended"
)
my_tree.pack()

# Configure the Scrollbar
tree_scroll.config(command=my_tree.yview)

# Define the Columns
my_tree["columns"] = (
    "First Name",
    "Last Name",
    "ID",
    "Address",
    "Zipcode",
    "City",
    "Country",
)

# Format the Columns
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("First Name", anchor=W, width=140)
my_tree.column("Last Name", anchor=W, width=140)
my_tree.column("ID", anchor=CENTER, width=140)
my_tree.column("Address", anchor=CENTER, width=140)
my_tree.column("Zipcode", anchor=CENTER, width=140)
my_tree.column("City", anchor=CENTER, width=140)
my_tree.column("Country", anchor=CENTER, width=140)

# Create Headings
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("First Name", text="First Name", anchor=W)
my_tree.heading("Last Name", text="Last Name", anchor=W)
my_tree.heading("ID", text="ID", anchor=CENTER)
my_tree.heading("Address", text="Address", anchor=CENTER)
my_tree.heading("Zipcode", text="Zipcode", anchor=CENTER)
my_tree.heading("City", text="City", anchor=CENTER)
my_tree.heading("Country", text="Country", anchor=CENTER)

# Add Fake Data
fake = faker.Faker()
contacts = []
for i in range(1, 500):
    contacts.append(
        [
            fake.first_name(),
            fake.last_name(),
            i,
            fake.street_address(),
            fake.postcode(),
            fake.city(),
            fake.country().upper(),
        ]
    )
print(contacts)

# Create Stripe Row Tags
my_tree.tag_configure("oddrow", background="white")
my_tree.tag_configure("evenrow", background="lightblue")

# Add the data to the screen

for i, record in enumerate(contacts):
    # if i % 2 == 0:
    #     my_tree.insert(parent='', index='end', iid=i, text='', values=(
    #         record[0],
    #         record[1],
    #         record[2],
    #         record[3],
    #         record[4],
    #         record[5],
    #         record[6],
    #     ), tags=('evenrow', ))
    # else:
    print(i)
    my_tree.insert(
        parent="",
        index="end",
        iid=i,
        text="",
        values=(
            record[0],
            record[1],
            record[2],
            record[3],
            record[4],
            record[5],
            record[6],
        ),
        tags=("evenrow" if i % 2 == 0 else "oddrow",),
    )

# Add record Entry boxes
data_frame = LabelFrame(root, text="Record")
data_frame.pack(fill="x", expand=True, padx=20)

fn_label = Label(data_frame, text="First Name")
fn_label.grid(column=0, row=0, padx=10, pady=10)
fn_entry = Entry(data_frame)
fn_entry.grid(column=1, row=0, padx=10, pady=10)

ln_label = Label(data_frame, text="Last Name")
ln_label.grid(column=2, row=0, padx=10, pady=10)
ln_entry = Entry(data_frame)
ln_entry.grid(column=3, row=0, padx=10, pady=10)


id_label = Label(data_frame, text="ID")
id_label.grid(column=4, row=0, padx=10, pady=10)
id_entry = Entry(data_frame)
id_entry.grid(column=5, row=0, padx=10, pady=10)


address_label = Label(data_frame, text="Address")
address_label.grid(column=0, row=1, padx=10, pady=10)
address_entry = Entry(data_frame)
address_entry.grid(column=1, row=1, padx=10, pady=10)


zip_label = Label(data_frame, text="Postal Code")
zip_label.grid(column=2, row=1, padx=10, pady=10)
zip_entry = Entry(data_frame)
zip_entry.grid(column=3, row=1, padx=10, pady=10)


city_label = Label(data_frame, text="City")
city_label.grid(column=4, row=1, padx=10, pady=10)
city_entry = Entry(data_frame)
city_entry.grid(column=5, row=1, padx=10, pady=10)


country_label = Label(data_frame, text="Country")
country_label.grid(column=7, row=1, padx=10, pady=10)
country_entry = Entry(data_frame)
country_entry.grid(column=8, row=1, padx=10, pady=10)


def move_up() -> None:
    """
    Move row up
    """
    rows = my_tree.selection()
    for row in rows:
        my_tree.move(row, my_tree.parent(row), my_tree.index(row) - 1)


def move_down() -> None:
    """
    Move row down
    """
    rows = my_tree.selection()
    for row in reversed(rows):
        my_tree.move(row, my_tree.parent(row), my_tree.index(row) + 1)


def remove_one() -> None:
    """Remove one record"""
    selected = my_tree.selection()[0]
    my_tree.delete(selected)


def remove_many() -> None:
    """Remove many records"""
    select = my_tree.selection()
    for record in select:
        my_tree.delete(record)


def remove_all() -> None:
    """
    Remove all records
    """
    for record in my_tree.get_children():
        my_tree.delete(record)


def clear_entries():
    """
    Clear all Entry boxes
    """
    fn_entry.delete(0, END)
    ln_entry.delete(0, END)
    id_entry.delete(0, END)
    address_entry.delete(0, END)
    zip_entry.delete(0, END)
    city_entry.delete(0, END)
    country_entry.delete(0, END)

def update_record():
    """
    Update a record from entry boxes input data populated by the selected record
    """
    # Grab the record number
    selected = my_tree.focus()
    
    # Update record
    my_tree.item(selected, text='', values=(
        fn_entry.get(),
        ln_entry.get(),
        id_entry.get(),
        address_entry.get(),
        zip_entry.get(),
        city_entry.get(),
        country_entry.get(),
    ))
    

def select_record(event) -> None:
    """
    Select a Record
    event: Event. Event generated from selection binding by mouse
    """
    # Clear entry boxes
    clear_entries()

    # Grab Record number
    selected = my_tree.focus()
    try:
        # Grab record value
        values = my_tree.item(selected, "values")

        # Output to entry boxes
        fn_entry.insert(0, values[0])
        ln_entry.insert(0, values[1])
        id_entry.insert(0, values[2])
        address_entry.insert(0, values[3])
        zip_entry.insert(0, values[4])
        city_entry.insert(0, values[5])
        country_entry.insert(0, values[6])
    except IndexError:
        print("no record selected")


# Add Buttons
button_frame = LabelFrame(root, text="Commands")
button_frame.pack(fill="x", expand=True, padx=20)

update_button = Button(button_frame, text="Update Record", command=update_record)
update_button.grid(row=0, column=0, padx=10, pady=10)


add_button = Button(button_frame, text="Add Record")
add_button.grid(row=0, column=1, padx=10, pady=10)


remove_all_button = Button(button_frame, text="Remove All Records", command=remove_all)
remove_all_button.grid(row=0, column=2, padx=10, pady=10)


remove_one_button = Button(button_frame, text="Remove One Record", command=remove_one)
remove_one_button.grid(row=0, column=3, padx=10, pady=10)

remove_many_selected_button = Button(
    button_frame, text="Remove Many Selected Records", command=remove_many
)
remove_many_selected_button.grid(row=0, column=4, padx=10, pady=10)

moveup_button = Button(button_frame, text="Move Up", command=move_up)
moveup_button.grid(row=0, column=5, padx=10, pady=10)

movedown_button = Button(button_frame, text="Move Down", command=move_down)
movedown_button.grid(row=0, column=6, padx=10, pady=10)

select_button = Button(button_frame, text="Clear Entry Boxes", command=clear_entries)
select_button.grid(row=0, column=7, padx=10, pady=10)


# Bind the Treeview
my_tree.bind("<ButtonRelease-1>", select_record)

root.mainloop()
