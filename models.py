import sqlite3

con = sqlite3.connect('instance/availability.db', check_same_thread=False)
cursor = con.cursor()
dates = cursor.execute("SELECT * FROM Date").fetchall()
activities = cursor.execute('SELECT * FROM Activity').fetchall()
print(dates, activities)

def create_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Date (
        id INTEGER PRIMARY KEY,
        date TEXT UNIQUE NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Activity (
        id INTEGER PRIMARY KEY,
        name TEXT UNIQUE NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Booking (
        id INTEGER PRIMARY KEY,
        activity_name TEXT NOT NULL,
        booked_date TEXT NOT NULL,
        num_people INTEGER NOT NULL,
        customer_name TEXT NOT NULL,
        FOREIGN KEY (activity_name) REFERENCES Activity (name),
        FOREIGN KEY (booked_date) REFERENCES Date (date),
        UNIQUE (activity_name, booked_date)
    )
    ''')
    con.commit()
    con.close()

def setBooking(activity_name, booked_date, num_people, customer_name):
    cursor.execute("INSERT INTO Booking(activity_name, booked_date, num_people, customer_name) VALUES (?,?,?,?)", (activity_name, booked_date, num_people, customer_name))
    con.commit()

def setDate(date):
    cursor.execute("INSERT INTO Date (date) VALUES (?)", (date,))
    con.commit()

def setActivity(name):
    cursor.execute("INSERT INTO Activity (name) VALUES (?)", (name,))
    con.commit()
