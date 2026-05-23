#Chapter 16 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter16.html

#note: this program doesn't enforce unique ingredients or meal names

import sqlite3
#create the database using the parameters given by the assignment
def create_database(db):
    db.execute('CREATE TABLE IF NOT EXISTS meals (name TEXT) STRICT')
    db.execute('CREATE TABLE IF NOT EXISTS ingredients (name TEXT, meal_id INTEGER, FOREIGN KEY(meal_id) REFERENCES meals (rowid)) STRICT')

def query_database(db):
    print(f'Connecting to {database_name} ...')
    while True:
        print(f'\nInput a query:')
        user_input = input().strip()

        if user_input.lower() == 'quit':
            break
        
        #if the prompt has a colon then we treat it as an insert query
        if ":" in user_input:
            colon_count = user_input.count(":")
            if colon_count > 1:
                print(f'\nPlease enter a valid format. Queries should be in these formats:')
                print(f'    One colon: onigiri:rice,nori,salt,sesame seeds')
                print(f'    No colon: chicken')
                continue
            split_query = user_input.split(':')
            meal = split_query[0].strip()
            ingredients = split_query[1].split(',')

            #insert into the meals table first to generate a rowid number
            insert_meal = db.execute('INSERT INTO meals VALUES (?)', (meal,))
            insert_meal_id = insert_meal.lastrowid
            
            #add each ingredient into the ingredients table using the rowid number for the meal
            for ingredient in ingredients:
                db.execute('INSERT INTO ingredients VALUES (?, ?)', (ingredient.strip(), insert_meal_id,))
            print(f'Meal added: {meal}')
        else:
            #get the meal rowid so that we can join tables later
            meal_id = db.execute('SELECT rowid FROM meals WHERE name = ?', (user_input,)).fetchall()
            if meal_id: 
                #meal_id is initially returned in the [(2,)] format so we use [0] to access the tuple then [0] again to access the rowid
                meal_id = meal_id[0][0]
                print(f"\nIngredients of {user_input}:")
                meal_ingredients = db.execute("""
                                              SELECT name
                                              FROM ingredients
                                              WHERE meal_id = ?
                                              """, (meal_id,))
                for thing in meal_ingredients:
                    print(f'    {thing[0]}')
            else:
                #select all the meals that have this ingredient
                meal_names = db.execute("""
                                        SELECT m.name
                                        FROM ingredients AS i
                                        INNER JOIN meals AS m
                                        ON i.meal_id = m.rowid
                                        WHERE i.name = ?
                                        """, (user_input,)).fetchall()
                if meal_names:
                    print(f"\nMeals that use {user_input}:")
                    #meal_names returns something like ('onigiri',) so we need to access the first item in the tuple by using [0]
                    for thing in meal_names:
                        print(f'    {thing[0]}')
                else:
                    print(f'\nIngredient or meal not found.')
                
    print(db.execute('SELECT * FROM meals').fetchall())
    print(db.execute('SELECT * FROM ingredients').fetchall())



database_name = 'meal.db'

conn = sqlite3.connect(database_name)
conn.execute('BEGIN')
create_database(conn)
query_database(conn)
#conn.rollback()
conn.commit()

"""
asdf = conn.execute('SELECT name FROM sqlite_schema WHERE type="table"').fetchall()
print(asdf)
    #[('meals',), ('ingredients',)]
aaa = conn.execute('PRAGMA TABLE_INFO(meals)').fetchall()
print(aaa)
    #[(0, 'name', 'TEXT', 0, None, 0)]
aaa = conn.execute('PRAGMA TABLE_INFO(ingredients)').fetchall()
print(aaa)
    #[(0, 'name', 'TEXT', 0, None, 0), (1, 'meal_id', 'INTEGER', 0, None, 0)]
"""

conn.close()