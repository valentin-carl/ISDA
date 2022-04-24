import sqlite3

"""
for reference, see: https://docs.python.org/3/library/sqlite3.html
"""
if __name__ == "__main__":

    # establish database connection
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    # greet user
    print("Please enter your SQL commands")

    # start reading console input and try executing it
    buffer = ""
    while True:
    
        # read user input
        line = input()
        if line == "":
            break
        buffer += line

        # if user entered valid sql command, try to execute it
        if sqlite3.complete_statement(buffer):
            try:
                cursor.execute(buffer)
                if buffer.startswith("SELECT") or buffer.startswith("select"):
                    print(cursor.fetchall())
            except sqlite3.Error as e:
                print("An error occurred:", e.args[0])
            buffer = ""

    # close the database connection
    connection.close()

