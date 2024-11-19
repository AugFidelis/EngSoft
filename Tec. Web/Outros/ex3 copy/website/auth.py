from flask import Blueprint, render_template, request, flash
import mysql.connector

auth = Blueprint('auth', __name__)

# Add database connection configuration
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="teste"
)
cursor = db.cursor()

# Create users table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        email VARCHAR(150) UNIQUE,
        primeiro_nome VARCHAR(150),
        senha VARCHAR(150)
    )
""")
db.commit()

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return '<p>logout</p>'

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        primeiro_nome = request.form.get('primeiro_nome')
        senha1 = request.form.get('senha1')
        senha2 = request.form.get('senha2')

        # Check if email already exists
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()
        
        if user:
            flash('Email já está registrado.', category='erro')
        elif len(email) < 4:
            flash('Email deve ter mais que 4 caracteres!', category='erro')
        elif len(primeiro_nome) < 2:
            flash('Primeiro nome deve ter mais que 2 caracteres!', category='erro')
        elif senha1 != senha2:
            flash('As senhas não são iguais!', category='erro')
        elif len(senha1) < 7:
            flash('Senha deve ter mais que 7 caracteres!', category='erro')
        else:
            # Store password as plain text (not recommended for production!)
            cursor.execute("INSERT INTO usuarios (email, primeiro_nome, senha) VALUES (%s, %s, %s)",
                         (email, primeiro_nome, senha1))
            db.commit()
            data = request.form
            print(data)
            flash('Usuário registrado com sucesso!', category='sucesso')

    return render_template('signup.html')