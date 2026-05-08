#Chapter 12 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter12.html

import pymsgbox, time
sleep_time = ""
while True:
    sleep_time = pymsgbox.prompt('This is a simple timer program.\n'
                                 'Please input how many seconds this program is pause:'
    )
    
    #pymsgbox.prompt returns None if the user selects Cancel
    if sleep_time is None:
        break

    #exit the loop if the user enters a digit
    if sleep_time.isdigit():
        sleep_time = int(sleep_time)
        break
    
    pymsgbox.alert("Please enter a valid number")

#check if the user input wasn't none
if isinstance(sleep_time, int):
    time.sleep(sleep_time)
    pymsgbox.alert("Time's up!")
else:
    pymsgbox.alert("No time detected, aborting program.")