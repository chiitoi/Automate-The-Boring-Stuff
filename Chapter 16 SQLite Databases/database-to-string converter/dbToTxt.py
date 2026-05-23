#Chapter 16 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter16.html

import sqlite3

def db_to_txt(db_filename):
    conn = sqlite3.connect(db_filename)
    try:
        #returns ('cats',) so we need to access the first entry using [0] at the end
        table_name = conn.execute('SELECT name FROM sqlite_schema WHERE type="table"').fetchone()[0]
        table_columns =  conn.execute(f'PRAGMA TABLE_INFO({table_name})').fetchall()
        
        #header row
        column_names = ['rowid']
        for column in table_columns:
            column_names.append(column[1])

        #print(",".join(column_names))
        rows = conn.execute(f'SELECT rowid, * FROM {table_name}')
        
        #(cid, name, type, notnull, dflt_value, pk)
        #column id, column name, column type, whether notnull is enforced (1 = yes), default value, whether column is part of the primary key
        #print(table_columns)

        with open(f'{db_filename}.txt', 'w', encoding='utf-8') as file_obj:
            file_obj.write(",".join(column_names) + '\n')

            #data rows
            for row in rows:
                row_string = ",".join(str(value) for value in row)
                #print(row_string)
                file_obj.write(row_string + '\n')
    finally:
        conn.close()
    
db_name = 'sweigartcats.db'
db_to_txt(db_name)
