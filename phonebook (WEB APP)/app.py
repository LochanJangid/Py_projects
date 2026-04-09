import sqlite3
import re
from flask import Flask, render_template, session, request, redirect, jsonify
from datetime import timedelta
from database import Database
from flask_bcrypt import Bcrypt
from jinja2.exceptions import TemplateNotFound
app = Flask(__name__)
bcrypt = Bcrypt(app)

app.secret_key = 'hhhhhhhhh'
app.permanent_session_lifetime = timedelta(days=30)
# session.permanent = True

db = Database('phonebook.db')

@app.errorhandler(TemplateNotFound)
def handle_template_not_found(e):
    return render_template('template_not_found.html')

@app.route('/')
def index():
    contacts = db.query('SELECT * FROM phonebook', "fetchall")
    if not session.get("username"):
        return render_template('home.html')
    return render_template('index.html', contacts=contacts, username=session["username"])

@app.route('/register', methods=["GET", "POST"])
def register():
    if session.get("username"):
        return render_template('/')
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        errors = []
        if not username and not password and not confirm_password:
            errors.append('PLEASE FILL ALL DETAILS!')

        registerd_username = db.query('SELECT * FROM users WHERE username = ?', username, operation="fetchall")
        if registerd_username:
            errors.append('USERNAME IS ALREADY EXIST!')

        # if email given valid it
        if email:
            if not re.search(r'^[\w]+@([\w]+\.)*[\w]+\.[\w]+$', email):
                errors.append('INVALID EMAIL')
        # Strong password
        if not re.search(r'[\w]+', password) or not re.search(r'[\d]+', password) or not re.search(r'[\W]+', password):
            errors.append('CHOOSE  STRONG PASSWORD')

        if confirm_password != password:
            errors.append('PASSWORD NOT MATCHED!')
        
        if errors:
            return jsonify({'errors': errors})

        hash = bcrypt.generate_password_hash(password).decode('utf-8')
        db.query('INSERT INTO users (username, email, password) VALUES (?, ?, ?)', username, email, hash)
        session["username"] = username

        return redirect('/')

    return render_template('user_registration.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    if session.get("username"):
        return render_template('/')
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        errors = []
        if not username or not password:
            errors.append('PLEASE FILL USERNAME AND PASSWORD')

        user_id = db.query('SELECT * FROM users WHERE username = ?', username, operation="fetchone")

        if user_id is None:
            errors.append('USERNAME DOES NOT EXIST!')
            return jsonify({"errors": errors})
        if bcrypt.check_password_hash(user_id["password"], password):
            errors.append('USERNAME AND PASSWORD DON\'T MATCH!')

        if errors:
            return jsonify({"errors": errors})

        session["username"] = username

        return redirect('/')

    return render_template('user_login.html')

@app.route('/logout')
def logout():
    # clear session
    session.clear()
    return redirect('/')

@app.route('/add_contact', methods=["POST", "GET"])
def add_contact():
    if not session.get("username"):
        return render_template('/')
    if request.method == 'POST':
        # valid every input if neccassay 
        name = request.form.get('name')
        number = request.form.get('number')
        email = request.form.get('email')
        relation = request.form.get('relation')
        company = request.form.get('company')     

        errors = []

        if not name:
            errors.append('Name is required.')
        if not re.search(r'^\d{10}$', number):
            errors.append('Enter a valid phone number.')
        if email:
            if not re.search(r'^\w+@\w+\.com$', email):
                errors.append('Enter a valid email.')
        
        if errors:
            return render_template('add_contact.html', errors=errors)  

        # insert new contact in phonebook
        user_id = db.query('SELECT * FROM users WHERE username = ?', session["username"], operation="fetchone")
        if user_id is None:
            return 'INVALID USER'
        db.query('INSERT INTO phonebook (name, number, email, relation, company, user_id) VALUES(?, ?, ?, ?, ?, ?)', name, number, email, relation, company, user_id["id"])
        return redirect('/')

    return render_template('add_contact.html')

@app.route('/contact_detail', methods=["POST"])
def contact_detail():
    if not session.get("username"):
        return render_template('/')
    id = request.form.get("id")
    details = db.query('SELECT * FROM phonebook WHERE id = ?', id, operation="fetchone")
    return render_template('contact_detail.html', details=details)

@app.route('/delete_contact', methods=["POST"])
def delete_contact():
    if not session.get("username"):
        return render_template('/')    
    id = request.form.get("id")
    db.query('DELETE FROM phonebook WHERE id = ?', id)
    return redirect('/')

@app.route('/show_contacts')
def show_contacts():
    if not session.get("username"):
        return render_template('/')
    q=''
    if request.args.get("q"):    
        q = request.args.get("q")
    
    contacts = db.query('SELECT * FROM phonebook WHERE name LIKE ? AND user_id = (SELECT id FROM users WHERE username = ?)', '%'+q+'%', session["username"], operation="fetchall")

    return render_template('show_contacts.html', contacts=contacts)

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/modify_contact', methods=['POST', 'GET'])
def modify_contact():
    if not session.get("username"):
        return render_template('/')

    if request.method == 'POST':
        # valid every input if neccassay 
        id = request.form.get('id')
        name = request.form.get('name')
        number = request.form.get('number')
        email = request.form.get('email')
        relation = request.form.get('relation')
        company = request.form.get('company')    

        errors = []

        if not name:
            errors.append('Name is required.')
        if not re.search(r'^\d{10}$', number):
            errors.append('Enter a valid phone number.')
        if email:
            if not re.search(r'^\w+@\w+\.com$', email):
                errors.append('Enter a valid email.')
        
        if errors:
            return render_template('modify_contact.html', errors=errors)  
        # insert new contact in phonebook
        db.query('UPDATE phonebook SET name = ?, number =?,  email = ?,  relation = ?, company = ? WHERE id = ?', (name, number, email, relation, company, id))
        return redirect('/')
    
    details = db.query('SELECT * FROM phonebook WHERE id = ?', request.args.get("id"), operation="fetchone")
    return render_template('modify_contact.html', details=details)  