#Chapter 15 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter15.html

import ezsheets
ss = ezsheets.Spreadsheet('1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg')
sheet = ss.sheets[0]
rows = sheet.getRows()


for row_number, row in enumerate(rows, start = 1):
    #skip the headers
    if row_number == 1:
        continue

    beans_per_jar, jars, total_beans, *rest = row

    #skip blank rows
    if not (beans_per_jar and jars and total_beans):
        continue
    
    #protect in case there are characters instead of digits in the sheet
    try:
        beans_per_jar = int(beans_per_jar)
        jars = int(jars)
        total_beans = int(total_beans)
    except ValueError:
        print(f'Row {row_number} has invalid data.')
        continue

    #print(beans_per_jar, jars, total_beans)

    if beans_per_jar * jars != total_beans:
        print(f'Row {row_number} has errors.')
        print(f'{beans_per_jar} * {jars} evaluates to {beans_per_jar*jars}, not {total_beans}')