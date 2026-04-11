def show_intro():
    print('\033[1;36m')
    print('╔══════════════════════════════════════╗')
    print('║     SMS — School Management System   ║')
    print('║             Version  1.0             ║')
    print('╠══════════════════════════════════════╣')
    print('║  Designed by  : Lochan Jangid        ║')
    print('║  Database     : SchoolData.db        ║')
    print('║  Type 0 to exit • Type 9 for help    ║')
    print('╚══════════════════════════════════════╝')
    print('\033[0m')


def exit_program(_):                      # _ is cleaner than blabla
    print()
    print('  💐 Thank you for using SMS!')
    print('\033[1;32m  Designed & Created by Lochan Jangid\033[0m')
    print()
    exit(0)


def show_all_commands(funcs):
    print('\033[1;33m')
    print('  ┌─────┬──────────────────────────────┐')
    print('  │ CMD │ ACTION                       │')
    print('  ├─────┼──────────────────────────────┤')
    for command, func in funcs.items():
        if command == 0:
            print('  ├─────┼──────────────────────────────┤')
        name = func.__name__.replace('_', ' ').title()
        print(f'  │ {command:<3} │ {name:<28} │')
    print('  └─────┴──────────────────────────────┘')
    print('\033[0m')


def update_person_details(db):
    print('\033[1;34m┌──────────────────────────┐')
    print('│   Update Person Details  │')
    print('└──────────────────────────┘\033[0m')

    ValidId = False
    while not ValidId:
        try:
            person_id = int(input('  🔍 Person Id : '))
        except ValueError:
            print('  ❌ Invalid Person Id!')
        else:
            person_detail = db.get_person_detail(person_id)
            if not person_detail:
                print(f'  ❌ No Person Found with Id: {person_id}')
                print('  💡 Check the student or teacher list for valid Ids.')
            else:
                ValidId = True

    print()
    print('  💡 Press Enter to keep the current value.')
    print()

    raw_name    = input(f'  📛 Name    [{person_detail["name"]}] : ')
    raw_address = input(f'  🏠 Address [{person_detail["address"]}] : ')
    raw_phone   = input(f'  📞 Phone   [{person_detail["phone"]}] : ')

    # age needs separate validation
    raw_age = None
    while True:
        age_input = input(f'  🎂 Age     [{person_detail["age"]}] : ')
        if age_input == '':                        # keep current
            raw_age = person_detail['age']
            break
        try:
            raw_age = int(age_input)
            if raw_age < 3 or raw_age > 65:
                print('  ❌ Age must be between 3 and 65!')
            else:
                break
        except ValueError:
            print('  ❌ Invalid Age!')

    # fallback to existing value if user pressed Enter
    name    = raw_name    or person_detail['name']
    address = raw_address or person_detail['address']
    phone   = raw_phone   or person_detail['phone']

    db.update_person(person_id, name, raw_age, address, phone)
    print()
    print('  ✅ Person Details Updated Successfully!')