import csv

filepath = 'phonebook.csv'
def search_number(name):
    """Search for a contact in phonebook."""
    # Read phonebook.csv
    with open(filepath, "r") as f:
        reader = csv.DictReader(f)
        contacts = 0
        for contact in reader:
            if name in contact['name']:
                print(f'| {contact['name']} : {contact['number']}')
                contacts += 1
    return contacts

def show_contacts():
    """Show a full list of contacts"""
    with open(filepath, "r") as f:
        reader = csv.DictReader(f)
        contacts = 0
        for contact in reader:
            print(f'| {contact['name']} : {contact['number']}')
            contacts += 1
    return contacts

def write_number(name, number):
    """Append numbers in phonebook."""
    with open(filepath, 'a', newline='\n') as f:
        writer = csv.DictWriter(f, ['name', 'number'])
        writer.writerow({'name': name, 'number': number})
