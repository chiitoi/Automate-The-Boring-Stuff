#Chapter 21 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter21.html

import pyperclipimg, time, datetime

print('Recording clipboard... (Ctrl-C to stop)')
previous_content = None

try:
    while True:
        #if the user copies text then this will crash out so we use try to ignore the exception
        try:
            content = pyperclipimg.paste() # Get clipboard contents.
            if content != previous_content:
                # If it's different from the previous, print it:
                filename = f'clipboard-{str(datetime.datetime.now()).replace(":", "_")}.png'
                content.save(filename)
                print(f'Saved {filename}')
                previous_content = content
        except Exception:
            pass

        time.sleep(0.01)  # Pause to avoid hogging the CPU.
except KeyboardInterrupt:
    pass