import sqlite3

class Database:
    """A Model for update and insert data into Database."""
    def __init__(self, db_file):
        self.db_file = db_file
    
    def add_person(self, p):
        with sqlite3.connect(self.db_file) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            try:
                cursor.execute('''
                    INSERT INTO persons (name, age, address, phone)
                    VALUES (?, ?, ?, ?)
                    ''', (p.name, p.age, p.address, p.phone))
            except sqlite3.IntegrityError: 
                return 0
            else:
                conn.commit()
            cursor.execute('''
                SELECT id FROM persons
                WHERE name = ? AND age = ?
                AND address = ? AND phone = ?''', (p.name, p.age, p.address, p.phone))
            assigned_id = cursor.fetchone()['id']
            return assigned_id
    
    def add_student(self, st):
        with sqlite3.connect(self.db_file) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO students (person_id, grade)
                VALUES (?, ?)
                ''', (st.person_id, st.grade))
            conn.commit()
            cursor.execute('''
                SELECT id FROM students
                WHERE person_id = ?
                ''', (st.person_id, ))
            assigned_id = cursor.fetchone()['id']
            return assigned_id
    
    def add_teacher(self, teacher):
        with sqlite3.connect(self.db_file) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO teachers (person_id, subject, salary)
                VALUES (?, ?, ?)
                ''', (teacher.person_id, teacher.subject, teacher.salary))
            conn.commit()
            cursor.execute('''
                SELECT id FROM teachers
                WHERE person_id = ?
                ''', (teacher.person_id, ))
            assigned_id = cursor.fetchone()['id']
            return assigned_id
    
    def deposite_fee(self, st_id, fee_amount):
        with sqlite3.connect(self.db_file) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            # Check that st_id is valid or not
            cursor.execute('SELECT * FROM students WHERE person_id = ?', st_id) 
            st_row = cursor.fetchone()
            if not st_row:
                return '❌ Student id Not Exists.'
            
            cursor.execute('''
                SELECT SUM(fee_amount) as paid_fee
                FROM fee_payments
                WHERE st_id = ?
            ''', st_id)
            paid_fee = cursor.fetchone()['paid_fee']

            cursor.execute('''
                SELECT fee FROM fee_structure
                WHERE grade = ?
            ''', (st_row.grade, ))
            total_fee = cursor.fetchone()['fee']

            due_fee = total_fee - paid_fee

            if due_fee == 0:
                return f'No Due Fee. Enjoy!'
            
            if fee_amount > due_fee:
                donate_fee = fee_amount - due_fee # For Now Just Donate to Thin Air
                fee_amount = due_fee

            cursor.execute('''
                INSERT INTO fee_payments (st_id, fee_amount)
                VALUES (?, ?)
            ''', st_id, fee_amount)
            conn.commit()
            return f'✅ Fee Deposited Successfully!'

    def give_salary(self, teacher_id, salary_amount):
        with sqlite3.connect(self.db_file) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            # Check that teacher_id is valid or not
            cursor.execute('SELECT * FROM teachers WHERE person_id = ?', teacher_id) 
            teacher_row = cursor.fetchone()
            if not teacher_row:
                return '❌ Teacher id Not Exists.'
            
            cursor.execute('''
                SELECT SUM(salary_amount) as given_salary
                FROM salary_payments
                WHERE teacher_id = ?
            ''', teacher_id)
            given_salary = cursor.fetchone()['given_salary']

            cursor.execute('''
                SELECT salary FROM teachers
                WHERE grade = ?
            ''', st_row.grade)
            salary = cursor.fetchone()['salary']

            due_salary = salary - given_salary

            if due_salary == 0:
                return f'You Gived full salary!'
            
            if fee_amount > due_salary:
                donate_salary = fee_amount - due_salary # For Now Just Donate to Thin Air
                fee_amount = due_salary

            cursor.execute('''
                INSERT INTO fee_payments (st_id, fee_amount)
                VALUES (?, ?)
            ''', st_id, fee_amount)
            conn.commit()
            return f'✅ Salary Given Successfully!'
        
    def list_all_students(self):
        with sqlite3.connect(self.db_file) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()

            cursor.execute('''
                SELECT students.id , name, age, address, phone, students.grade FROM persons
                JOIN students ON persons.id = students.person_id
            ''')

            st_data = cursor.fetchall()
            return st_data
    
    def list_all_teachers(self):
        with sqlite3.connect(self.db_file) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()

            cursor.execute('''
                SELECT teachers.id , name, age, address, phone, teachers.subject, teachers.salary FROM persons
                JOIN teachers ON persons.id = teachers.person_id
            ''')

            teacher_data = cursor.fetchall()
            return teacher_data

    def fee_structure(self, fee_dict):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            for grade, fee in fee_dict.items():
                cursor.execute('''
                    INSERT INTO fee_structure (grade, fee)
                    VALUES (?, ?)
                    ''', (grade, fee))
            conn.commit()

def update_fee_structure():
    db = Database('SchoolData.db')

    fee_structure_dict = {
        'pp.3' : 3999,
        'pp.4' : 3999,
        'pp.5' : 3999,
        'I'    : 5999,
        'II'   : 6999,
        'III'  : 7999,
        'IV'   : 8999,
        'V'    : 9999,
        'VI'   : 10999,
        'VII'  : 11999,
        'VIII' : 12999,
        'IX'   : 13999,
        'X'    : 14999,
        'XI'   : 15999,
        'XII'  : 16999

    }
    try:
        db.fee_structure(fee_structure_dict)
    except Exception as e:
        print(f'❌ Error: {e}')
    else:
        print('✅ Fee Structure Updated!')

if __name__ == '__main__':
    pass
    # update_fee_structure()