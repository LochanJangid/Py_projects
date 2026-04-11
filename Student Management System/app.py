from database.database import Database
from ui.student_ui import add_student, list_students
from ui.teacher_ui import add_teacher, list_teachers
from ui.utils_ui import show_intro, show_all_commands, exit_program, update_person_details
from ui.finance_ui import deposit_fee, pay_salary, list_payments

def main():
    db = Database('SchoolData.db')
    funcs = {
        1: add_student,
        2: add_teacher,
        3: deposit_fee,
        4: pay_salary,
        5: list_payments,
        6: update_person_details,
        7: list_students,
        8: list_teachers,
        9: show_all_commands,
        0: exit_program 
    }
    # Main Display
    show_intro()
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