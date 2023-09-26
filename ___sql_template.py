    # Create a database or connect to one that exists
    conn = sqlite3.connect("tree_crm.db")

    # Create a cursor instance
    cursor = conn.cursor()

    # Create table
    cursor.execute(
    )
   # Commit changes
    conn.commit()

    # Close the connection
    conn.close()
