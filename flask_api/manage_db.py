import sqlite3

def insert_data():
    # Connect to the database
    conn = sqlite3.connect('todos.db')
    cur = conn.cursor()

    # Insert new data
    cur.execute("INSERT INTO todo (title, description) VALUES (?, ?)", ('New Todo', 'Description of the new todo'))
    cur.execute("INSERT INTO contact (name, phone_number) VALUES (?, ?)", ('Jane Doe', '987-654-3210'))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    insert_data()
