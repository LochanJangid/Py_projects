import sqlite3
import re
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    conn = sqlite3.connect('phonebook.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM phonebook')
    contacts = cursor.fetchall()
    conn.close()
    return render_template('index.html', contacts=contacts)

@app.route('/add_contact', methods=["POST", "GET"])
def add_contact():
    if request.method == 'POST':
        # valid every input if neccassay 
        name = request.form.get('name')
        number = request.form.get('number')
        errors = []

        if not name:
            errors.append('Name is required.')
        if not re.search(r'^\d{10}$', number):
            errors.append('Enter a valid phone number.')
        
        if errors:
            return render_template('add_contact.html', errors=errors)  
                

        email = request.form.get('email')
        relation = request.form.get('relation')
        company = request.form.get('company')     


        # insert new contact in phonebook
        conn = sqlite3.connect('phonebook.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO phonebook (name, number, email, relation, company) VALUES(?, ?, ?, ?, ?)', (name, number, email, relation, company))
        conn.commit()
        conn.close()
        return redirect('/')

    return render_template('add_contact.html')

@app.route('/contact_detail', methods=["POST"])
def contact_detail():
    id = request.form.get("id")
    conn = sqlite3.connect('phonebook.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM phonebook WHERE id = ?', id)
    details = cursor.fetchone()
    conn.close()

    return render_template('contact_detail.html', details=details)

@app.route('/delete_contact', methods=["POST"])
def delete_contact():
    id = request.form.get("id")
    conn = sqlite3.connect('phonebook.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM phonebook WHERE id = ?', id)
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/show_contacts')
def show_contacts():
    q=''
    if request.args.get("q"):    
        q = request.args.get("q")
        
    conn = sqlite3.connect('phonebook.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM phonebook WHERE name LIKE ?', ('%'+q+'%',))
    contacts = cursor.fetchall()
    conn.close()

    return render_template('show_contacts.html', contacts=contacts)

@app.route('/search')
def search():
    return render_template('search.html')