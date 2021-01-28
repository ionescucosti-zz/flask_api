import sqlite3

conn = sqlite3.connect('database.db')
print("Opened database successfully");

conn.execute('CREATE TABLE requests (endpoint_name TEXT, call_params TEXT, result TEXT, timestamp TEXT)')
print("Table created successfully");
conn.close()