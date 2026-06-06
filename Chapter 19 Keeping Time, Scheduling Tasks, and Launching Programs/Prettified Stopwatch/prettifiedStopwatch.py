#Chapter 19 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter19.html

# A simple stopwatch program
import time, pyperclip 

# Display the program's instructions.
print('Press ENTER to begin and to mark laps. Ctrl-C quits.')
input()  # Press Enter to begin.
print('Started.')
start_time = time.time()  # Get the first lap's start time.
last_time = start_time
lap_number = 1

laps = []

# Start tracking the lap times.
try:
  while True:
    input()
    lap_time = round(time.time() - last_time, 2)
    total_time = round(time.time() - start_time, 2)
    time_printed = f'Lap # {str(lap_number).rjust(2)}: {str(total_time).rjust(7)} ({str(lap_time).rjust(7)})'
    print(time_printed, end='')
    laps.append(time_printed)
    lap_number += 1
    last_time = time.time() # Reset the last lap time.
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    print('\nDone.')
    clipboard_string = "\n".join(laps)
    pyperclip.copy(clipboard_string)
    print('Lap times have been copied to the clipboard.')