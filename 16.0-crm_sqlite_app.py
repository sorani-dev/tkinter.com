import configparser
import sqlite3
from configparser import ConfigParser
from pathlib import Path
from tkinter import (CENTER, END, NO, RIGHT, Button, Entry, Frame, Label,
                     LabelFrame, Menu, Tk, Toplevel, W, Y, colorchooser,
                     messagebox, ttk)

import faker

root = Tk()
root.title("TreeBase")
root.iconbitmap(Path(__file__).parent.joinpath("images", "codemy.ico"))
root.geometry("1000x500")


# Default values as constants
DEFAULT_PRIMARY_COLOR = "white"
DEFAULT_SECONDARY_COLOR = "lightblue"
DEFAULT_HIGHLIGHT_COLOR = "#347083"
# Section name
INI_SECTION_NAME = "COLORS"
# ini file path and name
INI_FILE_PATH = "./treebase.ini"

# Read the config file, read then import the colors
parser = ConfigParser()
# Read the file
file = parser.read("treebase.ini")
try:
    saved_primary_color = parser.get(INI_SECTION_NAME, "primary_color")
    saved_secondary_color = parser.get(INI_SECTION_NAME, "secondary_color")
    saved_highlight_color = parser.get(INI_SECTION_NAME, "highlight_color")

except configparser.NoSectionError as e:
    print(e)
    saved_primary_color = DEFAULT_PRIMARY_COLOR
    saved_secondary_color = DEFAULT_SECONDARY_COLOR
    saved_highlight_color = DEFAULT_HIGHLIGHT_COLOR

    # Save config
    parser = ConfigParser()
    with open(INI_FILE_PATH, "w", encoding="UTF-8") as config:
        # Add the colors section
        parser.add_section("COLORS")
        # Set the color change
        parser.set(INI_SECTION_NAME, "primary_color", saved_primary_color)
        parser.set(INI_SECTION_NAME, "secondary_color", saved_secondary_color)
        parser.set(INI_SECTION_NAME, "highlight_color", saved_highlight_color)
        parser.write(config)


def query_database_customers(search_term: str = "") -> None:
    """Retrieve the table results and inject them in the treeview

    Keyword Arguments:
        search_term --  Last name if parameter is not empty (default: {''})
    """
    # Empty Treeview table of all data
    my_tree.delete(*my_tree.get_children())

    # Create a database or connect to one that exists
    conn = sqlite3.connect("tree_crm.db")

    # Create a cursor instance
    cursor = conn.cursor()

    if search_term:
        cursor.execute(
            "SELECT rowid, * FROM customers WHERE last_name LIKE ?",
            (f"%{search_term}%",),
        )
    else:
        cursor.execute("SELECT rowid, * FROM customers")
    records = cursor.fetchall()
    # pprint.pprint(records)

    # Add the data to the screen
    for i, record in enumerate(records):
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
        # print(i)
        my_tree.insert(
            parent="",
            index="end",
            iid=i,
            text="",
            values=(
                record[1],
                record[2],
                record[0],
                record[4],
                record[5],
                record[6],
                record[7],
            ),
            tags=("evenrow" if i % 2 == 0 else "oddrow",),
        )
    # Commit changes
    conn.commit()

    # Close the connection
    conn.close()


def lookup_records():
    """
    Search database for customers based on a search criteria
    """

    def search_records():
        """earch a customer by last name"""
        lookup_record = search_entry.get().strip()

        # Close the search box
        search.destroy()

        # Clear the Treeview Table
        my_tree.delete(*my_tree.get_children())

        query_database_customers(lookup_record)

    search = Toplevel(root)
    search.title("Lookup Records")
    search.geometry("400x200")
    search.iconbitmap(Path(__file__).parent.joinpath("images", "codemy.ico"))

    # Create a label frame
    search_frame = LabelFrame(search, text="Last Name")
    search_frame.pack(padx=10, pady=10)

    # Add an Entry box
    search_entry = Entry(search_frame, font=("Helvetica", 18))
    search_entry.pack(padx=20, pady=20)

    # Add button
    search_button = Button(search, text="Search records", command=search_records)
    search_button.pack(padx=20, pady=20)


def primary_color():
    """Choose and modify the primary color of the Treeview  table"""
    primary_color_ = colorchooser.askcolor()[1]

    # Update Treeview striped color for even rows
    if primary_color_:
        # Create Stripe Row Tags
        my_tree.tag_configure("evenrow", background=primary_color_)

        # Save config
        parser = ConfigParser()
        # Read the file
        parser.read(INI_FILE_PATH)
        with open(INI_FILE_PATH, "w", encoding="UTF-8") as config:
            # Set the color change
            parser.set(INI_SECTION_NAME, "primary_color", primary_color_)
            parser.write(config)


def secondary_color():
    """Choose and modify the secondary color of the Treeview  table"""
    secondary_color_ = colorchooser.askcolor()[1]

    # Update Treeview striped color for odd rows
    if secondary_color_:
        # Create Stripe Row Tags
        my_tree.tag_configure("oddrow", background=secondary_color_)

        # Save config
        parser = ConfigParser()
        # Read the file
        parser.read(INI_FILE_PATH)
        with open(INI_FILE_PATH, "w", encoding="UTF-8") as config:
            # Set the color change
            parser.set(INI_SECTION_NAME, "secondary_color", secondary_color_)
            parser.write(config)


def highlight_color():
    """Choose and modify the highlight color of the Treeview  table"""
    highlight_color_ = colorchooser.askcolor()[1]

    # Update Treeview hightlight color when selection of row occurs
    if highlight_color_:
        # Change the Selected Color
        style.map("Treeview", background=[("selected", highlight_color_)])

        # Save config
        parser = ConfigParser()
        # Read the file
        parser.read(INI_FILE_PATH)
        # Save the config file with changes
        with open(INI_FILE_PATH, "w", encoding="UTF-8") as config:
            # Set the color change
            parser.set(INI_SECTION_NAME, "highlight_color", highlight_color_)
            parser.write(config)


def reset_colors():
    """
    Reset colors to their default values znd save it to the config file
    """
    # Create Stripe Row Tags
    my_tree.tag_configure("evenrow", background=DEFAULT_PRIMARY_COLOR)
    my_tree.tag_configure("oddrow", background=DEFAULT_SECONDARY_COLOR)

    # Change the Selected Color
    style.map("Treeview", background=[("selected", DEFAULT_HIGHLIGHT_COLOR)])

    # Save config
    parser = ConfigParser()
    # Read the file
    parser.read(INI_FILE_PATH)
    # Save the config file with changes
    with open(INI_FILE_PATH, "w", encoding="UTF-8") as config:
        # Set the color change
        parser.set(INI_SECTION_NAME, "primary_color", DEFAULT_PRIMARY_COLOR)
        parser.set(INI_SECTION_NAME, "secondary_color", DEFAULT_SECONDARY_COLOR)
        parser.set(INI_SECTION_NAME, "highlight_color", DEFAULT_HIGHLIGHT_COLOR)
        parser.write(config)


# Add Menu
my_menu = Menu(root)
root.config(menu=my_menu)


# Configure the options menu
options_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Options", menu=options_menu)

# Dropdown menu
options_menu.add_command(label="Change Primary Color", command=primary_color)
options_menu.add_command(label="Change Secondary Color", command=secondary_color)
options_menu.add_command(label="Highlight Color", command=highlight_color)
options_menu.add_command(label="Reset Colors", command=reset_colors)
options_menu.add_separator()
options_menu.add_command(label="Exit", command=root.quit)


# Configure the search menu
search_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Search", menu=search_menu)

# earch menu
search_menu.add_command(label="Search", command=lookup_records)
search_menu.add_separator()
search_menu.add_command(label="Reset view", command=query_database_customers)


# Add Fake Data
fake = faker.Faker()
customers = []
for i in range(1, 500):
    customers.append(
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
# print(customers)

# Database Stuff


def create_table_customer() -> None:
    """Create the customer Table"""
    # Create a database or connect to one that exists
    conn = sqlite3.connect("tree_crm.db")

    # Create a cursor instance
    cursor = conn.cursor()

    # Create table
    cursor.execute(
        """
                CREATE TABLE IF NOT EXISTS customers (
                    first_name TEXT,
                    last_name TEXT,
                    id INTEGER  PRIMARY KEY,
                    address TEXT,
                    zipcode TEXT,
                    city TEXT,
                    country TEXT
                )
                """
    )
    # Check if the table customers is empty
    count = cursor.execute("""SELECT COUNT(*) FROM customers""").fetchone()
    # Table is empty of records, thus insert new customers
    if count[0] == 0:
        # Add dummy data to table
        for record in customers:
            cursor.execute(
                """
                        INSERT INTO customers (first_name, last_name, id, address, zipcode, city, country)
                        VALUES (:first_name, :last_name, :id, :address, :zipcode, :city, :country)""",
                {
                    "first_name": record[0],
                    "last_name": record[1],
                    "id": record[2],
                    "address": record[3],
                    "zipcode": record[4],
                    "city": record[5],
                    "country": record[6],
                },
            )

    # Commit changes
    conn.commit()

    # Close the connection
    conn.close()


create_table_customer()

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
style.map("Treeview", background=[("selected", saved_highlight_color)])


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


# Create Stripe Row Tags
my_tree.tag_configure("oddrow", background=saved_primary_color)
my_tree.tag_configure("evenrow", background=saved_secondary_color)

# Add data from database to the Treeview
query_database_customers()

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
id_entry = Entry(data_frame, state="readonly")
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
    try:
        selected = my_tree.selection()[0]

        my_tree.delete(selected)

        # Create a database or connect to one that exists
        conn = sqlite3.connect("tree_crm.db")

        # Create a cursor instance
        cursor = conn.cursor()

        # Create table
        cursor.execute(
            """DELETE FROM customers
                    WHERE oid=:id""",
            {"id": id_entry.get()},
        )

        # Clear Entry boxes
        clear_entries()

        # Clear the Treeview Table
        my_tree.delete(*my_tree.get_children())

        # Commit changes
        conn.commit()

        # Close the connection
        conn.close()

        # Refresh the Treeview
        query_database_customers()

        # Add a little message box
        messagebox.showinfo("Deleted!", "Your Record has been successfully deleted!")
    except IndexError as e:
        print(e)


def remove_many() -> None:
    """Remove many records"""
    # print(my_tree.selection())
    # Confirm the deletion of all customers
    if messagebox.askyesno(
        "Confirm deletion",
        "This will delete EVERYTHING from the 'customers' table.\nAre you sure?",
    ):
        # Tuple of all row numbers
        select = my_tree.selection()

        # List of all ids correspondig to the selection
        ids = [(my_tree.item(record, "values")[2],) for record in select]

        # Delete from output table
        for record in select:
            my_tree.delete(record)

        # Create a database or connect to one that exists
        conn = sqlite3.connect("tree_crm.db")

        # Create a cursor instance
        cursor = conn.cursor()

        # Delete selected customers from customers table
        cursor.executemany("""DELETE FROM customers WHERE oid = ?""", ids)
        # Commit changes
        conn.commit()

        # Close the connection
        conn.close()

        # Update table otput
        query_database_customers()


def remove_all() -> None:
    """
    Remove all records
    """
    # Confirm the deletion of all customers
    if messagebox.askyesno(
        "Confirm deletion",
        "This will delete EVERYTHING from the 'customers' table.\nAre you sure?",
    ):
        for record in my_tree.get_children():
            my_tree.delete(record)

            # Create a database or connect to one that exists
        conn = sqlite3.connect("tree_crm.db")

        # Create a cursor instance
        cursor = conn.cursor()

        # Delete all customers from customers TABLE
        cursor.execute("DELETE FROM customers")

        # Clear Entry boxes
        clear_entries()

        # Clear the Treeview Table
        my_tree.delete(*my_tree.get_children())

        # Refresh the Treeview
        # query_database_customers()

        # Commit changes
        conn.commit()

        # Close the connection
        conn.close()

        # Add a little message box
        messagebox.showinfo("Deleted!", "All Records have been successfully deleted!")


def clear_entries():
    """
    Clear all Entry boxes
    """
    id_entry.config(state="normal")
    fn_entry.delete(0, END)
    ln_entry.delete(0, END)
    id_entry.delete(0, END)
    address_entry.delete(0, END)
    zip_entry.delete(0, END)
    city_entry.delete(0, END)
    country_entry.delete(0, END)
    id_entry.config(state="readonly")


def update_record():
    """
    Update a record from entry boxes input data populated by the selected record
    """
    # Grab the record number
    selected = my_tree.focus()

    # Update record
    my_tree.item(
        selected,
        text="",
        values=(
            fn_entry.get(),
            ln_entry.get(),
            id_entry.get(),
            address_entry.get(),
            zip_entry.get(),
            city_entry.get(),
            country_entry.get(),
        ),
    )
    # Update the customer table of the database
    # Create a database or connect to one that exists
    conn = sqlite3.connect("tree_crm.db")

    # Create a cursor instance
    cursor = conn.cursor()

    # Create table
    cursor.execute(
        """
                   UPDATE customers SET
                   first_name = :first_name,
                   last_name = :last_name,
                   address = :address,
                   zipcode = :zipcode,
                   city = :city,
                   country = :country
                   WHERE oid=:oid
                   """,
        {
            "first_name": fn_entry.get(),
            "last_name": ln_entry.get(),
            "address": address_entry.get(),
            "zipcode": zip_entry.get(),
            "city": city_entry.get(),
            "country": country_entry.get(),
            "oid": id_entry.get(),
        },
    )
    # Commit changes
    conn.commit()

    # Close the connection
    conn.close()

    # Clear Entry boxes
    clear_entries()


def add_record():
    """Add a record to the customers table"""

    # Create a database or connect to one that exists
    conn = sqlite3.connect("tree_crm.db")

    # Create a cursor instance
    cursor = conn.cursor()

    # Get the next id for the new record
    max_id = cursor.execute("SELECT MAX(id) FROM customers").fetchone()[0]
    # print("max_id", max_id)
    if max_id:
        new_id = max_id + 1
    else:
        new_id = 1
    # Add new customer
    cursor.execute(
        """
                   INSERT INTO customers (first_name, last_name, id, address, zipcode, city, country)
                    VALUES (:first_name, :last_name, :id, :address, :zipcode, :city, :country)
        """,
        {
            "first_name": fn_entry.get(),
            "last_name": ln_entry.get(),
            "address": address_entry.get(),
            "zipcode": zip_entry.get(),
            "city": city_entry.get(),
            "country": country_entry.get(),
            "id": new_id,
        },
    )

    # Commit changes
    conn.commit()

    # Close the connection
    conn.close()

    # Claer Entry boxes
    clear_entries()

    # Clear the Treeview Table
    my_tree.delete(*my_tree.get_children())

    # Run to pull data from the custumers table in the database from the start
    query_database_customers()


def select_record(event) -> None:
    """
    Select a Record
    event: Event. Event generated from selection binding by mouse
    """
    # Clear entry boxes
    clear_entries()

    id_entry.config(state="normal")

    # Grab Record number
    selected = my_tree.focus()
    try:
        # Grab record value
        values = my_tree.item(selected, "values")

        # Output to entry boxes
        fn_entry.insert(0, values[1])
        ln_entry.insert(0, values[2])
        id_entry.insert(0, values[0])
        address_entry.insert(0, values[4])
        zip_entry.insert(0, values[5])
        city_entry.insert(0, values[6])
        country_entry.insert(0, values[7])

        id_entry.config(state="readonly")
    except IndexError:
        print("no record selected")


# Add Buttons
button_frame = LabelFrame(root, text="Commands")
button_frame.pack(fill="x", expand=True, padx=20)

update_button = Button(button_frame, text="Update Record", command=update_record)
update_button.grid(row=0, column=0, padx=10, pady=10)


add_button = Button(button_frame, text="Add Record", command=add_record)
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
