import sqlite3

"""
for reference, see: https://docs.python.org/3/library/sqlite3.html
"""
if __name__ == "__main__":
    
    """
    create connection to database &
    cursor object to execute SQL commands
    """
    db_connection = sqlite3.connect("database.db")
    cursor = db_connection.cursor()

    # greet db use
    print("Enter your SQL commands to execute in sqlite3.")
    print("Enter a blank line to exit.")

    # accept new SQL commands until empty line is entered
    buffer = ""
    while True:

        # get new command line input
        line = input()
        if line == "":
            break

        # read and execute SQL command
        buffer += line
        if sqlite3.complete_statement(buffer):
            try:
                buffer = buffer.strip()
                cursor.execute(buffer)
                if buffer.lstrip().upper().startswith("SELECT"):
                    print(cur.fetchall())
            except sqlite3.Error as e:
                print("An error occurred:", e.args[0])
            buffer = ""

    # close to database connection to allow other processes to access db file
    db_connection.close()

