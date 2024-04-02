import requests
import sqlite3

conn = sqlite3.connect('books.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        author TEXT,
        publication_year INTEGER
    )
''')

# Google Books API key
api_key = 'AIzaSyCMn5b57mQD01u93rSMFx6qT9vx-ywQdtg'


query = 'Harry Potter'  

# Fetch data from the Google Books API
api_url = 'https://www.googleapis.com/books/v1/volumes'
params = {
    'q': query,
    'key': api_key,
}
response = requests.get(api_url, params=params)

if response.status_code == 200:
    books_data = response.json().get('items', [])
else:
    print('Failed to fetch data from the Google Books API')
    books_data = []

# Store data 
for book in books_data:
    volume_info = book.get('volumeInfo', {})
    title = volume_info.get('title', '')
    authors = volume_info.get('authors', [])
    author = ', '.join(authors) if authors else ''
    publication_year = volume_info.get('publishedDate', '').split('-')[0]

    # Insert the book into the database
    cursor.execute('''
        INSERT INTO books (title, author, publication_year)
        VALUES (?, ?, ?)
    ''', (title, author, publication_year))

conn.commit()
conn.close()

conn = sqlite3.connect('books.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM books')
books = cursor.fetchall()

for book in books:
    print(f'Title: {book[1]}, Author: {book[2]}, Publication Year: {book[3]}')

conn.close()
