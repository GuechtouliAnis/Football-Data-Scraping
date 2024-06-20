import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect('leagues-stats-2023-2024.db')

# Get a cursor object
cursor = conn.cursor()

# Get a list of all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# Loop through the tables and export each one to a CSV file
for table in tables:
    table_name = table[0]
    df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
    df.to_csv(f"Data/{table_name}.csv", index=False)

# Close the connection
conn.close()
