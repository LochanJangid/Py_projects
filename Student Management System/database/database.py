import sqlite3

class Database:
    """Handles all read/write operations for SchoolData.db."""

    def __init__(self, db_file):
        self.db_file = db_file
    
    def _connect(self):
        conn = sqlite3.connect(self.db_file)
        conn.row_factory = sqlite3.Row
        return conn

    def get_person_name(self, id, who):
        with self._connect() as conn:
            cursor = conn.cursor()
            if who == 'student':
                cursor.execute('''
                    SELECT name FROM persons
                    WHERE id = (
                        SELECT person_id FROM students
                        WHERE id = ?)
                    ''', (id, ))
            else:
                cursor.execute('''
                    SELECT name FROM persons
                    WHERE id = (
                        SELECT person_id FROM teachers
                        WHERE id = ?)
                    ''', (id, ))
            person_name = cursor.fetchone()

            return person_name['name'] if person_name else None
    
    def get_person_detail(self, id):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT * FROM persons
                WHERE id = ?
            ''', (id, ))
            person_detail = cursor.fetchone()

            return person_detail if person_detail else 0
            

    def add_person(self, p):
        with self._connect() as conn:
            cursor = conn.cursor()
            try:
                cursor.execute('''
                    INSERT INTO persons (name, age, address, phone)
                    VALUES (?, ?, ?, ?)
                    ''', (p.name, p.age, p.address, p.phone))
                conn.commit()
                return cursor.lastrawid
            except sqlite3.IntegrityError: 
                return None
    
    def add_student(self, st):
        with self._connect() as conn:
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
        with self._connect() as conn:
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
    
    def update_person(self, person_id,  name, age, address, phone):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE persons
                SET name = ?, age = ?, address = ?, phone = ?
                WHERE id = ?
                ''', (name, age, address, phone, person_id))
            conn.commit()

    def due_fee(self, st_id):
         with self._connect() as conn:
            cursor = conn.cursor()
            # Check that st_id is valid or not
            cursor.execute('SELECT * FROM students WHERE id = ?', (st_id, )) 
            st_row = cursor.fetchone()
            if not st_row:
                return None
            
            cursor.execute('''
                SELECT SUM(fee_amount) as paid_fee
                FROM fee_payments
                WHERE st_id = ?
            ''', (st_id, ))
            paid_fee = cursor.fetchone()['paid_fee']
            if paid_fee == None:
                paid_fee = 0

            cursor.execute('''
                SELECT fee FROM fee_structure
                WHERE grade = ?
            ''', (st_row['grade'], ))
            total_fee = cursor.fetchone()['fee']
            due_fee = total_fee - paid_fee

            return due_fee
         
    def pending_salary(self, teacher_id):
         with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM teachers WHERE id = ?', (teacher_id, )) 
            teacher_row = cursor.fetchone()
            if not teacher_row:
                return None
            
            cursor.execute('''
                SELECT SUM(salary_amount) as given_salary
                FROM salary_payments
                WHERE teacher_id = ?
            ''', (teacher_id, ))
            given_salary = cursor.fetchone()['given_salary']
            if given_salary == None:
                given_salary = 0

            pending_fee = teacher_row['salary'] - given_salary
            return pending_fee
 
 
    def deposit_fee(self, st_id, fee_amount, due_fee):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO fee_payments (st_id, fee_amount)
                VALUES (?, ?)
            ''', (st_id, fee_amount))
            conn.commit()

    
    def pay_salary(self, teacher_id, salary_amount):
        with self._connect() as conn:
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO salary_payments (teacher_id, salary_amount)
                VALUES (?, ?)
            ''', (teacher_id, salary_amount))
            conn.commit()

    def list_students(self):
        with self._connect() as conn:
            cursor = conn.cursor()

            cursor.execute('''
                SELECT persons.id, students.id , name, age, address, phone, students.grade FROM persons
                JOIN students ON persons.id = students.person_id
            ''')

            st_data = cursor.fetchall()
            return st_data
    
    def list_teachers(self):
        with self._connect() as conn:
            cursor = conn.cursor()

            cursor.execute('''
                SELECT persons.id, teachers.id , name, age, address, phone, teachers.subject, teachers.salary FROM persons
                JOIN teachers ON persons.id = teachers.person_id
            ''')

            teacher_data = cursor.fetchall()
            return teacher_data
    
    def list_fee_payments(self):
        with self._connect() as conn:
            cursor = conn.cursor()

            cursor.execute('''
                SELECT fee_payments.id, st_id, fee_amount, payment_date 
                FROM fee_payments
                JOIN students ON fee_payments.st_id = students.id
            ''')

            payment_data = cursor.fetchall()
            return payment_data
    
    def list_salary_payments(self):
        with self._connect() as conn:
            cursor = conn.cursor()

            cursor.execute('''
                SELECT salary_payments.id, teacher_id, salary_amount, payment_date 
                FROM salary_payments
                JOIN teachers ON salary_payments.teacher_id = teachers.id
            ''')

            payment_data = cursor.fetchall()
            return payment_data

    def fee_structure(self, fee_dict):
        with sqlite3.connect() as conn:
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
    # update_fee_structure()
    pass