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
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM titles")

    head = []
    for i in cursor.description:
        head.append(i[0])

    df = pd.DataFrame(cursor.fetchall(), columns=head)
    print(df)

main()