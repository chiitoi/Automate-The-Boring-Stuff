import sqlite3

conn = sqlite3.connect('monitorFreeSpace.db')
space_data = conn.execute('SELECT * FROM freespace').fetchall()
for sd in space_data:
    free_space = sd[0]
    date = sd[1]
    print(f'Free space: {free_space} bytes, date: {date}')