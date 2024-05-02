import sqlite3
from faker import Faker

# Create a Faker instance
fake = Faker()

# Create a connection to the SQLite database
conn = sqlite3.connect('pocdb.db')

# Create a cursor object
cur = conn.cursor()


# Create the Employee table if it doesn't exist
cur.execute("""
    CREATE TABLE IF NOT EXISTS Employee (
        name TEXT,
        dob TEXT,
        city TEXT,
        deptno INTEGER,
        role TEXT
    )
""")

# Generate and insert fake data into the Employee table
for _ in range(100):  # Generate 100 records
    cur.execute("""
        INSERT INTO Employee (name, dob, city, deptno, role) 
        VALUES (?, ?, ?, ?, ?)
    """, (fake.name(), fake.date_of_birth(minimum_age=30, maximum_age=50).isoformat(), fake.city(), fake.random_int(min=100, max=999), fake.job()))

# Commit the transaction
conn.commit()

# Close the connection
conn.close()
