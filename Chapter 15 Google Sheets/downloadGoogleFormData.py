#Chapter 15 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter15.html

import ezsheets

link = ''
ss = ezsheets.Spreadsheet(link)

sheet = ss.sheets[0]
emails = sheet.getColumn(3)
for email in emails:
    if email.strip():
        print(email)