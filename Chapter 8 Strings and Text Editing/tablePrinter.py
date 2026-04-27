tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(string_table):
    rows = len(string_table)
    cols = len(string_table[0])
    new_table = []
    col_widths = []

    for row in string_table:
        max_length = max(len(item) for item in row)
        col_widths.append(max_length)
    
    for k in range(cols):
        new_row = []
        for i in range(rows):
            subject = string_table[i][k]
            new_row.append(subject.rjust(col_widths[i]))
        new_table.append(new_row)

    string = ""
    for row in new_table:
        string += " ".join(row) + "\n"
    return string

print(printTable(tableData))