#Chapter 12 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter12.html

import subprocess
subprocess.run(['python', '-m', 'PyInstaller', '--onefile', 'msgBoxGuess.py'])
subprocess.run(['python', '-m', 'PyInstaller', '--onefile', 'msgBoxTimer.py'])