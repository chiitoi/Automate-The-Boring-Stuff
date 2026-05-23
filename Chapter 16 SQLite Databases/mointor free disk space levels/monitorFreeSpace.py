#Chapter 16 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter16.html

import psutil, datetime, sqlite3, time

#print(psutil.disk_usage('C:\\').free)  # Windows
#print(psutil.disk_usage('/').free)  # macOS and Linux

conn = sqlite3.connect('monitorFreeSpace.db', isolation_level=None)
conn.execute('CREATE TABLE IF NOT EXISTS freespace (free INT, timestamp TEXT) STRICT')
print('Monitoring disk free space. Press Ctrl-C to quit.')
try:
    while True:
        free_space = psutil.disk_usage('C:\\').free
        current_time = str(datetime.datetime.now())
        conn.execute('INSERT INTO freespace VALUES (?, ?)', (free_space, current_time))
        print(free_space, current_time)
        time.sleep(1)
except:
    pass
