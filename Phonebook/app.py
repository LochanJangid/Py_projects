import csv
import sys

# condition check for sys
if len(sys.argv) != 3:
    print('TypeError: [python ./phonebook.py name number]')


# Read phonebook.csv
with open("phonebook.csv", "r") as file:
    reader = csv.DictReader(file)
    for fieldname in reader.fieldnames:
        print(fieldname, end='\t')
    print()
    for contact in reader:
        print(contact['name'], end="\t")
        print(contact['number'])

# Write phonebook.csv

fieldnames = ['name','number']
name = sys.argv[1]
number = sys.argv[2] 

with open("phonebook.csv", "a", newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writerow({fieldnames[0]: name, fieldnames[1]: number})
