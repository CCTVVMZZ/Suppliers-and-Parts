import sqlite3

suppliers = [
    (1, "Smith", 20, "London"),
    (2, "Jones", 30, "Paris"),
    (3, "Blake", 30, "Paris"),
    (4, "Clark", 20, "London"),
    (5, "Adams", 30, "Athens"),
    ]

parts = [
    (1, "Nut", "Red", 12.0, "London"),
    (2, "Bolt", "Green", 17.0, "Paris"),
    (3, "Screw", "Blue", 17.0, "Oslo"),
    (4, "Screw", "Red", 14.0, "London"),
    (5, "Cam", "Blue", 12.0, "Paris"),
    (6, "Cog", "Red", 19.0, "London"),
    ]

shipments = [
    (1, 1, 300),
    (1, 2, 200),
    (1, 3, 400),
    (1, 4, 200),
    (1, 5, 100),
    (1, 6, 100),
    (2, 1, 300),
    (2, 2, 400),
    (3, 2, 200),
    (4, 2, 200),
    (4, 4, 300),
    (4, 5, 400),
    ]

def create_suppliers_and_parts(con):
    cur = con.cursor()

    # create the tables
    
    cur.execute("""
    CREATE TABLE S (
    SNO     integer primary key,
    SNAME   text    NOT NULL,
    STATUS  integer NOT NULL,
    CITY    text    NOT NULL
    )
    """)

    cur.execute("""
    CREATE TABLE P (
    PNO     integer primary key,
    PNAME   text    NOT NULL,
    COLOR   text    NOT NULL,
    WEIGHT  real    NOT NULL,
    CITY    text    NOT NULL
    )""")

    cur.execute("""
    CREATE TABLE SP (
    SNO     integer          NOT NULL, 
    PNO     integer          NOT NULL,
    QTY     integer          NOT NULL,
    PRIMARY KEY (SNO, PNO),
    FOREIGN KEY(SNO) REFERENCES S(SNO),
    FOREIGN KEY(PNO) REFERENCES P(PNO)
    )""")

    cur.executemany("INSERT INTO S VALUES (?, ?, ?, ?)", suppliers)

    cur.executemany("INSERT INTO P VALUES (?, ?, ?, ?, ?)", parts)

    cur.executemany("INSERT INTO SP VALUES (?, ?, ?)", shipments)

if __name__ == "__main__":
    import sys
    import os
    if len(sys.argv) == 2 and not os.path.exists(sys.argv[1]):        
        con = sqlite3.connect(sys.argv[1])
        create_suppliers_and_parts(con)
        con.commit()
        con.close()
