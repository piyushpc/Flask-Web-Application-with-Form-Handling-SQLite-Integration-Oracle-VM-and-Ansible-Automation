import sqlite3

# Connect to the database
conn = sqlite3.connect('todos.db')

# Create a cursor object
cur = conn.cursor()

# Fetch all todos
cur.execute("SELECT * FROM todo")
todos = cur.fetchall()
print("Todos:")
for todo in todos:
    print(todo)

# Fetch all contacts
cur.execute("SELECT * FROM contact")
contacts = cur.fetchall()
print("\nContacts:")
for contact in contacts:
    print(contact)

# Close the connection
conn.close()

