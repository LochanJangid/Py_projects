from tabulate import tabulate

def deposit_fee(db):
    print('\033[1;36m┌──────────────────────────┐')
    print('│       Deposit Fee        │')
    print('└──────────────────────────┘\033[0m')

    ValidId = False
    while not ValidId:
        try:
            st_id = int(input('  🔍 Student Id : '))
        except ValueError:
            print('  ❌ Invalid Student Id!')
        else:
            st_name = db.get_person_name(st_id, 'student')
            if not st_name:
                print(f'  ❌ No Student Found with Id: {st_id}')
            else:
                ValidId = True

    due_fee = db.due_fee(st_id)
    print()
    print(f'  📋 Student  : {st_name}')
    print(f'  💰 Due Fee  : ₹{due_fee:,.2f}')

    if due_fee == 0:
        print('  ✅ Fee Already Paid in Full!')
        return

    donation = 0                          # ← always initialize before the loop
    ValidAmount = False
    while not ValidAmount:
        try:
            amount = int(input('  💳 Amount   : ₹'))
        except ValueError:
            print('  ❌ Invalid Amount!')
            continue

        if amount <= 0:
            print('  ❌ Amount Must Be Greater Than Zero!')
        elif amount > due_fee:
            excess = amount - due_fee
            print(f'  ❌ Amount exceeds due fee by ₹{excess:,.2f}')
            donate = input(f'  💐 Donate excess ₹{excess:,.2f} to poor children? [Y/n]: ')
            if donate.lower() in ['y', 'yes', 'ok', 'fine']:
                amount = due_fee          # clamp to exact due
                donation = excess         # track separately
                ValidAmount = True
                print(f'  🙏 ₹{donation:,.2f} will be donated. Thank you!')
            # if user says no, loop continues — ask for amount again
        else:
            ValidAmount = True

    db.deposit_fee(st_id, amount, due_fee)
    if donation:
        db.record_donation(donation)

    remaining = due_fee - amount
    print()
    print(f'  ✅ Payment of ₹{amount:,.2f} Recorded!')
    if remaining > 0:
        print(f'  💰 Remaining Fee : ₹{remaining:,.2f}')
    else:
        print(f'  🎉 Fee Fully Cleared!')


def pay_salary(db):
    print('\033[1;35m┌──────────────────────────┐')
    print('│       Pay Salary         │')
    print('└──────────────────────────┘\033[0m')

    ValidId = False
    while not ValidId:
        try:
            teacher_id = int(input('  🔍 Teacher Id : '))
        except ValueError:
            print('  ❌ Invalid Teacher Id!')
        else:
            teacher_name = db.get_person_name(teacher_id, 'teacher')
            if not teacher_name:
                print(f'  ❌ No Teacher Found with Id: {teacher_id}')
            else:
                ValidId = True

    pending_salary = db.pending_salary(teacher_id)
    print()
    print(f'  📋 Teacher         : {teacher_name}')
    print(f'  💰 Pending Salary  : ₹{pending_salary:,.2f}')

    if pending_salary == 0:
        print('  ✅ Full Salary Already Paid!')
        return

    ValidAmount = False
    while not ValidAmount:
        try:
            amount = int(input('  💳 Amount      : ₹'))
        except ValueError:
            print('  ❌ Invalid Amount!')
            continue

        if amount <= 0:
            print('  ❌ Amount Must Be Greater Than Zero!')
        elif amount > pending_salary:
            print(f'  ❌ Exceeds Pending Salary of ₹{pending_salary:,.2f}!')
        else:
            ValidAmount = True

    db.pay_salary(teacher_id, amount)
    remaining = pending_salary - amount
    print()
    print(f'  ✅ Salary of ₹{amount:,.2f} Paid!')
    if remaining > 0:
        print(f'  💰 Remaining Salary : ₹{remaining:,.2f}')
    else:
        print(f'  🎉 Full Salary Cleared!')


def list_payments(db):
    print('\033[1;33m┌──────────────────────────┐')
    print('│      Payment Records     │')
    print('└──────────────────────────┘\033[0m')
    print('  1. Fee Payments')
    print('  2. Salary Payments')

    list_choice = input('  Choice : ').strip().lower()

    if 'fee' in list_choice or list_choice == '1':
        headers  = ['Payment Id', 'Student Id', 'Amount (₹)', 'Date & Time']
        payments = db.list_fee_payments()
        title    = 'Fee Payments'
    elif 'salary' in list_choice or list_choice == '2':
        headers  = ['Payment Id', 'Teacher Id', 'Amount (₹)', 'Date & Time']
        payments = db.list_salary_payments()
        title    = 'Salary Payments'
    else:
        print('  ❌ Invalid Choice!')
        return

    print()
    if not payments:
        print(f'  💠 No {title} found.')
        return                            # ← was missing, printed empty table before

    print(tabulate(
        payments,
        headers=headers,
        tablefmt='rounded_outline',
        numalign='center',
        stralign='left'
    ))
    print(f'\n  📋 Total Transactions : {len(payments)}')