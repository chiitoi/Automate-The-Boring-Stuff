#Chapter 16 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter16.html

import sqlite3, pprint

database_name = 'sweigartcats.db'

conn = sqlite3.connect(database_name, isolation_level=None)
tables = conn.execute('SELECT name FROM sqlite_schema WHERE type="table"').fetchall()
print(f'The tables available in "{database_name}" are:')
for table in tables:
    print(f'    {table[0]}')
print()

v_info = conn.execute('PRAGMA TABLE_INFO(vaccinations)').fetchall()
print(f'The "vaccination" table has the following columns:')
pprint.pprint(v_info)
print()

#lists the info as id, seq, table, from, to, on_update, on_delete, match
#[(0, 0, 'cats', 'cat_id', 'rowid', 'NO ACTION', 'NO ACTION', 'NONE')]
print(conn.execute('PRAGMA foreign_key_list(vaccinations)').fetchall())
print()

c_info = conn.execute('PRAGMA TABLE_INFO(cats)').fetchall()
print(f'The "cats" table has the following columns:')
pprint.pprint(c_info)
print()

cats = conn.execute('SELECT c.name FROM cats AS c LEFT JOIN vaccinations AS v ON c.id = v.cat_id AND v.vaccine IN ("rabies", "FeLV", "FVRCP") GROUP BY c.id HAVING COUNT(DISTINCT v.vaccine) < 3')
print(f'Here are all the cats that do not have the "rabies", "FeLV", and "FVRCP" vaccines:')
for cat in cats:
    print(f'    {cat[0]}')
print()

vaccines = conn.execute('SELECT c.name, c.birthdate, v.vaccine, v.date_administered FROM cats AS c INNER JOIN vaccinations AS v ON c.id = v.cat_id WHERE v.date_administered < c.birthdate')
print(f'The following cats had their vaccinations administered before their birthdates:')
for result in vaccines:
    print(f'\tName: {result[0]}\n\tBirthday: {result[1]}\n\tVaccine: {result[2]}\n\tDate administered: {result[3]}\n')