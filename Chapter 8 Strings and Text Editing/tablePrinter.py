tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(string_table):
    rows = len(string_table)
    cols = len(string_table[0])
    new_table = []
    col_widths = []

    #Find the max width of each column so that we can use .rjust() for each item later
    for row in string_table:
        max_length = max(len(item) for item in row)
        col_widths.append(max_length)
    
    #We're rotating the matrix so we first need to access the table by column first (apples, Alice, dogs) then go through each row for the individual items
    #This is appended into a new table so that looks like the following
    """
      apples Alice  dogs
     oranges   Bob  cats
    cherries Carol moose
      banana David goose
    """
    for k in range(cols):
        new_row = []
        for i in range(rows):
            subject = string_table[i][k]
            new_row.append(subject.rjust(col_widths[i]))
        new_table.append(new_row)

    string = ""
    #Joining each row into a single string then combining all the rows with a new line
    for row in new_table:
        string += " ".join(row) + "\n"
    return string

print(printTable(tableData))