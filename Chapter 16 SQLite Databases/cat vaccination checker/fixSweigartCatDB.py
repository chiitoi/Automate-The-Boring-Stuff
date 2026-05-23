import sqlite3

"""
The database included within the online materials zip has an incomplete database. When examining the file it outputs the following:
conn = sqlite3.connect('sweigartcats.db', isolation_level=None)
asdf = conn.execute('SELECT name FROM sqlite_schema WHERE type="table"').fetchall()
print(asdf)
    [('cats',), ('vaccinations',)]

aaa = conn.execute('PRAGMA TABLE_INFO(vaccinations)').fetchall()
print(aaa)
    [(0, 'vaccine', 'TEXT', 0, None, 0), (1, 'date_administered', 'TEXT', 0, None, 0), (2, 'administered_by', 'TEXT', 0, None, 0), (3, 'cat_id', 'INTEGER', 0, None, 0)]

aaa = conn.execute('PRAGMA TABLE_INFO(cats)').fetchall()
print(aaa)
    [(0, 'name', 'TEXT', 1, None, 0), (1, 'birthdate', 'TEXT', 0, None, 0), (2, 'description', 'TEXT', 0, None, 0), (3, 'weight_kg', 'REAL', 0, None, 0)]

according to https://www.sqlite.org/pragma.html#pragma_table_info the table_info method returns:
    "name" (its name);
    "type" (data type if given, else '');
    "notnull" (whether or not the column can be NULL);
    "dflt_value" (the default value for the column);
    "pk" (either zero for columns that are not part of the primary key, or the 1-based index of the column within the primary key).

so the cat table doesn't have an open primary key that the vaccination table can use as a foreign key to link them (there is rowid that sqlite adds for each table but IMO it's better to have an explicit primary key).
This file is an attempt to try and fix it by creating a new table with an INTERGER column and copying over the data
"""

def fix_sweigart_cat_db(database_name):
    conn = sqlite3.connect("sweigartcats.db")

    #create a new table
    conn.execute("""
    CREATE TABLE cats_new (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        birthdate TEXT,
        description TEXT,
        weight_kg REAL
    )
    """)

    #copy old rows into new table
    conn.execute("""
    INSERT INTO cats_new (name, birthdate, description, weight_kg)
    SELECT name, birthdate, description, weight_kg
    FROM cats
    """)

    #delete old table
    conn.execute("DROP TABLE cats")

    #rename new table
    conn.execute("ALTER TABLE cats_new RENAME TO cats")

    conn.commit()
    conn.close()

db_name = 'sweigartcats.db'

fix_sweigart_cat_db(db_name)