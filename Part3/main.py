"""
Student: Muhammad J. Jarad
Class: CIS-2532-NET01
Instructor: DR.Sam
Assignment#: 12 part 2 CH17.2

"""

import sqlite3
import pandas as pd


def main():
    connection = sqlite3.connect("books.db")

    authorLast = pd.read_sql("""SELECT last FROM authors
                                ORDER BY last DESC""", connection)
    print(authorLast)
    print()

    bookTitle = pd.read_sql("""SELECT title FROM titles
                                ORDER BY title ASC""", connection)
    print(bookTitle)
    print()

    authorISBN = pd.read_sql("""SELECT first, last, title, copyright, titles.isbn
                                    FROM authors, titles
                                    INNER JOIN author_ISBN
                                    ON authors.id = author_ISBN.id 
                                    WHERE Last Like "Wald"
                                    ORDER BY title ASC
                                    """, connection)
    print(authorISBN)
    print()

    cursor = connection.cursor()

    cursor.execute("""INSERT INTO authors (first, last)
                   Values("Jhon", "Doe")""")
    Authors = pd.read_sql("""SELECT * FROM authors""", connection)

    print(Authors)
    print()

    cursor.execute("""INSERT INTO titles (isbn, title, edition, copyright)
                       Values("0101010101", "Jhon Does' Book", 1, 2022)""")
    cursor.execute("""INSERT INTO author_ISBN (id, isbn)
                       Values(6, "0101010101")""")

    Titles = pd.read_sql("""SELECT * FROM titles""", connection)
    AuthorISBN = pd.read_sql("""SELECT * FROM author_ISBN""", connection)

    print(Titles)
    print()
    print(AuthorISBN)


main()