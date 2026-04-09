from tabulate import tabulate
from database.database import Database
from models.person import Student, Teacher

def add_student(db):
    name = input('Student Name: ')
    ValidAge = False
    while not ValidAge:
        try:
            age = int(input('Student Age: '))
        except ValueError:
            print('❌ Invalid Age!')
        else:
            ValidAge = True
    address = input('Student Address: ')
    phone = input('Student Phone Number: ')
    
    available_grades = {'pp.3', 'pp.4', 'pp.5', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VII', 'IX', 'X', 'XI', 'XII'}
    ValidGrade = False
    while not ValidGrade:
        grade = input('Student Grade: ')
        if grade in available_grades:
            ValidGrade = True
        else:
            print(f'❌ Grade Not Available {available_grades}')

    curr_student = Student(name, age, address, phone, grade)
    person_id = db.add_person(curr_student)
    curr_student.person_id = person_id # add a attribute person_id
    if person_id:
        student_id = db.add_student(curr_student)
        print('-> Student Added Successfully!')
        print(f'-> Student Id: {student_id}.')
    else:
        print('-> A Student Already Exists with this Phone Number.')

def add_teacher(db):
    name = input('Teacher Name: ')
    ValidAge = False
    while not ValidAge:
        try:
            age = int(input('Teacher Age: '))
        except ValueError:
            print('❌ Invalid Age!')
        else:
            ValidAge = True
    address = input('Teacher Address: ')
    phone = input('Teacher Phone Number: ')
    subject = input('Teaching Subject: ')
    ValidSalary = False
    while not ValidSalary:
        try:
            salary = int(input('Teacher Salary Per Annum: '))
        except ValueError:
            print('❌ Invalid Salary!')
        else:
            ValidSalary = True

    curr_teacher = Teacher(name, age, address, phone, subject, salary)
    person_id = db.add_person(curr_teacher)
    curr_teacher.person_id = person_id # add a attribute person_id
    if person_id:
        teacher_id = db.add_teacher(curr_teacher)
        print('-> Teacher Added Successfully!')
        print(f'->Teacher Id: {teacher_id}')
    else:
        print('-> A Teacher Already Exists with this Phone Number.')

def list_all_students(db):
    students_data = db.list_all_students()
    if not students_data:
        print('💠 0 Students 💠')
        return

    print(tabulate(students_data, headers=['Id', 'Name', 'Age', 'Address', 'Phone Number', 'Grade'],  tablefmt='grid'))    
def list_all_teachers(db):
    teacher_data = db.list_all_teachers()
    if not teacher_data:
        print('💠 0 Teachers 💠')
        return

    print(tabulate(teacher_data, headers=['Id', 'Name', 'Age', 'Address', 'Phone Number', 'Subject', 'Salary'],  tablefmt='grid'))    

def exit_programm(blabla):
    print('💐 Thank you for Trusting and Using Our SMS - Student Management System.')
    print('\033[1;30m.> Designed & Created by \033[32m\033[1mLochan Jangid\033[0m\033[0m')
    exit(0)

def show_all_commands(funcs):
    print('SMS Commands 🚦')
    for command, func in funcs.items():
        print(f'| {command}. {func.__name__.replace('_', ' ').title()}')

def main():
    db = Database('SchoolData.db')
    funcs = {
        1: add_student,
        2: add_teacher,
        7: list_all_students,
        8: list_all_teachers,
        9: show_all_commands,
        0: exit_programm
    }
    # Main Display
    show_all_commands(funcs)
    while True:
        try:
            command = int(input('Command: '))
        except ValueError:
            print('❌ Wrong Command.')
            print('To see all commands use command-9')
            continue

        if command not in funcs.keys():
            print('❌ Wrong Command.')
            print('To see all commands use command-9')
            continue
        command = int(command)
        if command == 9:
            funcs[command](funcs) # for display commands 
        else:
            funcs[command](db)

if __name__ == '__main__':
    main()