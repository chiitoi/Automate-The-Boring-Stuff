#Chapter 14 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter14.html

import sys, openpyxl

if len(sys.argv) != 4:
    print('This script requires 3 arguments, please double check your input.')
    sys.exit()
    
if not sys.argv[1].isdigit() or not sys.argv[2].isdigit():
    print('The first and second argument must be a digit.')
    sys.exit()

starting_row = int(sys.argv[1])
blank_rows = int(sys.argv[2])
excel_file_name = sys.argv[3]

wb = openpyxl.load_workbook(excel_file_name)
sheet = wb.active

new_wb = openpyxl.Workbook()
new_sheet = new_wb.active

for row_value in range(1, sheet.max_row + 1):
    for column_value in range(1, sheet.max_column + 1):
        old_cell = sheet.cell(row=row_value, column=column_value)

        #all rows before the starting row are preserved and everything else is shifted by the blank number of rows
        if row_value >= starting_row:
            new_cell = new_sheet.cell(row=row_value+blank_rows, column=column_value)
        else:
            new_cell = new_sheet.cell(row=row_value, column=column_value)
            
        new_cell.value = old_cell.value

new_wb.save('updatedSheet.xlsx')

#not intended but the easiest method
#sheet.insert_rows(starting_row, blank_rows)
#wb.save('updatedSheet.xlsx')

