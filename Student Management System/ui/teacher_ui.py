from tabulate import tabulate
from models.person import Teacher

def add_teacher(db):
    print('\033[1;35m┌──────────────────────────┐')
    print('│     Add New Teacher      │')
    print('└──────────────────────────┘\033[0m')

    name    = input('  📛 Name       : ')

    ValidAge = False
    while not ValidAge:
        try:
            age = int(input('  🎂 Age        : '))
            if age < 18 or age > 65:
                print('  ❌ Age must be between 18 and 65!')
            else:
                ValidAge = True
        except ValueError:
            print('  ❌ Invalid Age!')

    address = input('  🏠 Address    : ')
    phone   = input('  📞 Phone      : ')
    subject = input('  📖 Subject    : ')

    ValidSalary = False
    while not ValidSalary:
        try:
            salary = int(input('  💰 Salary/yr  : ₹'))
            if salary < 1:
                print('  ❌ Salary must be greater than 0!')
            else:
                ValidSalary = True
        except ValueError:
            print('  ❌ Invalid Salary!')

    curr_teacher = Teacher(name, age, address, phone, subject, salary)
    person_id = db.add_person(curr_teacher)
    curr_teacher.person_id = person_id

    if person_id:
        teacher_id = db.add_teacher(curr_teacher)
        print()
        print('  ✅ Teacher Added Successfully!')
        print(f'  📋 Person  Id : {person_id}')
        print(f'  📋 Teacher Id : {teacher_id}')
    else:
        print('  ❌ Phone Number already registered!')


def list_teachers(db):
    teacher_data = db.list_teachers()

    print('\033[1;35m┌──────────────────────────┐')
    print('│     Teacher Records      │')
    print('└──────────────────────────┘\033[0m')

    if not teacher_data:
        print('  💠 No teachers found.')
        return

    print(tabulate(
        teacher_data,
        headers=['Person Id', 'Teacher Id', 'Name', 'Age', 'Address', 'Phone', 'Subject', 'Salary (₹)'],
        tablefmt='rounded_outline',
        numalign='center',
        stralign='left'
    ))
    print(f'\n  📋 Total Teachers : {len(teacher_data)}')