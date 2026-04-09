import sqlite3

conn = sqlite3.connect('SchoolData.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS persons (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        address TEXT,
        phone TEXT UNIQUE)
    ''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        person_id INTEGER,
        grade TEXT,
        FOREIGN KEY (person_id) REFERENCES persons(id))
    ''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS teachers (
        id INTEGER PRIMARY KEY,
        person_id INTEGER,
        subject TEXT,
        salary INTEGER,
        FOREIGN KEY (person_id) REFERENCES persons(id))
    ''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS fee_structure (
        grade TEXT UNIQUE NOT NULL,
        fee INTEGER NOT NULL)
    ''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS fee_payments (
        id INTEGER PRIMARY KEY,
        st_id INTEGER,
        fee_amount INTEGER NOT NULL,
        payment_date DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (st_id) REFERENCES students (id))
    ''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS salary_payments (
        id INTEGER PRIMARY KEY,
        teacher_id INTEGER NOT NULL,
        salary_amount INTEGER NOT NULL,
        payment_date DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (teacher_id) REFERENCES teachers(id))
    ''')

conn.commit()
conn.close()