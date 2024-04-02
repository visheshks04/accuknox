import csv
import sqlite3

csv_file = 'User_Data.csv'
db_file = 'sqlite.db'

conn = sqlite3.connect(db_file)
cursor = conn.cursor()


create_table_query = '''
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    gender TEXT,
    age INTEGER,
    estimated_salary INTEGER,
    purchased INTEGER
)
'''

cursor.execute(create_table_query)
conn.commit()

with open(csv_file, 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        user_id = row['User ID']
        gender = row['Gender']
        age = row['Age']
        estimated_salary = row['EstimatedSalary']
        purchased = row['Purchased']

        # Insert the data in database
        insert_query = '''
        INSERT INTO users (user_id, gender, age, estimated_salary, purchased)
        VALUES (?, ?, ?, ?, ?)
        '''
        cursor.execute(insert_query, (user_id, gender, age, estimated_salary, purchased))

# Commit changes and close database connection
conn.commit()
conn.close()
