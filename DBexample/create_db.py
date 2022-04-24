import sqlite3 as s

def run_script(filename):

    # connect to database.db
    connection = s.connect("database.db")

    # run sql script at filename
    with open(filename, "r") as sql_file:
        connection.executescript(sql_file.read())

    # close db connection
    connection.close()

if __name__ == "__main__":
    run_script("demo.sql")

