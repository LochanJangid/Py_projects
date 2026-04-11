from tabulate import tabulate
from models.person import Student

AVAILABLE_GRADES = ['pp.3', 'pp.4', 'pp.5', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII']

def add_student(db):
    print('\033[1;36m┌──────────────────────────┐')
    print('│     Add New Student      │')
    print('└──────────────────────────┘\033[0m')

    name = input('  📛 Name      : ')

    ValidAge = False
    while not ValidAge:
        try:
            age = int(input('  🎂 Age       : '))
            if age < 3 or age > 25:
                print('  ❌ Age must be between 3 and 25!')
            else:
                ValidAge = True
        except ValueError:
            print('  ❌ Invalid Age!')

    address = input('  🏠 Address   : ')
    phone   = input('  📞 Phone     : ')

    ValidGrade = False
    while not ValidGrade:
        print(f'  📚 Available Grades: {", ".join(AVAILABLE_GRADES)}')
        grade = input('  📚 Grade     : ')
        if grade in AVAILABLE_GRADES:
            ValidGrade = True
        else:
            print('  ❌ Invalid Grade!')

    curr_student = Student(name, age, address, phone, grade)
    person_id = db.add_person(curr_student)
    curr_student.person_id = person_id

    if person_id:
        student_id = db.add_student(curr_student)
        print()
        print('  ✅ Student Added Successfully!')
        print(f'  📋 Person  Id : {person_id}')
        print(f'  📋 Student Id : {student_id}')
    else:
        print('  ❌ Phone Number already registered!')


def list_students(db):
    students_data = db.list_students()

    print('\033[1;36m┌──────────────────────────┐')
    print('│      Student Records     │')
    print('└──────────────────────────┘\033[0m')

    if not students_data:
        print('  💠 No students found.')
        return

    print(tabulate(
        students_data,
        headers=['Person Id', 'Student Id', 'Name', 'Age', 'Address', 'Phone', 'Grade'],
        tablefmt='rounded_outline',    # cleaner than grid
        numalign='center',
        stralign='left'
    ))
    print(f'\n  📋 Total Students: {len(students_data)}')