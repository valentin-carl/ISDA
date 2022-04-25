import sqlite3 as s

def delete_tables(cursor, tables: list[str]) -> None:
    for table in tables:
        cursor.execute(f"DROP TABLE IF EXISTS {table};")

def create_tables(cursor) -> None:
    
    # PROF
    cursor.execute("""CREATE TABLE PROF (
            ProfID INT NOT NULL,
            Name VARCHAR(50)
            );""")

    # FACHGEBIET
    cursor.execute("""CREATE TABLE FACHGEBIET (
            FachgebietID INT NOT NULL,
            Name VARCHAR(50)
            );""")

    # MODUL
    cursor.execute("""CREATE TABLE MODUL (
            ModulID INT NOT NULL,
            Name VARCHAR(50)
            );""")

    # BETREUT
    cursor.execute("""CREATE TABLE BETREUT (
            ProfID INT NOT NULL,
            ModulID INT NOT NULL
            );""")

    # LEITET
    cursor.execute("""CREATE TABLE LEITET (
            ProfID INT NOT NULL,
            FachgebietID INT NOT NULL
            );""")

def load_data(cursor) -> None:
    
    # Professoren
    profs = ["Niedermeier", "Markl", "Tschorsch", "Brill", "Kreutzer", "Müller", "Nestmann", "Sprekeler", "Obermayer", "Blankertz", "Möller", "Seifert", "Nordholz", "Glesner", "Haufe"]

    # Fachgebiete
    fachgebiete = ["AKT", "DIMA", "DSI", "ALGO", "LaS", "IDA", "MTV", "MKP", "NI", "NT", "QU", "SECT", "SVNSA", "SESE", "UNIML"]

    # Module
    module = ["Informationssysteme und Datenanalyse", "Machine Learning 1", "Brain-Computer Interfacing", "Computational Social Choice", "Softwaretechnik und Programmierparadigmen"]

    for i in range(len(profs)):
        cursor.execute(f"INSERT INTO PROF VALUES ({i}, \"{profs[i]}\");")

    for i in range(len(fachgebiete)):
        cursor.execute(f"INSERT INTO FACHGEBIET VALUES ({i}, \"{fachgebiete[i]}\");")

    for i in range(len(module)):
        cursor.execute(f"INSERT INTO MODUL VALUES ({i}, \"{module[i]}\");")

    for i in range(len(profs)):
        cursor.execute(f"INSERT INTO LEITET VALUES ({i}, {i});")

    cursor.execute("INSERT INTO BETREUT VALUES (1, 0);")
    cursor.execute("INSERT INTO BETREUT VALUES (5, 1);")
    cursor.execute("INSERT INTO BETREUT VALUES (9, 2);")
    cursor.execute("INSERT INTO BETREUT VALUES (3, 3);")
    cursor.execute("INSERT INTO BETREUT VALUES (13, 4);")

if __name__ == "__main__":
    connection = s.connect("database.db")
    cursor = connection.cursor()

    tables = ["PROFESSOR", "FACHGEBIET", "MODUL", "BETREUT", "LEITET"]

    # reset DB
    delete_tables(cursor, tables)
    create_tables(cursor)

    # load data
    load_data(cursor)
    connection.commit()

    # close DB connection
    connection.close()
