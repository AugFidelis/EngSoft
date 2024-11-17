from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

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
    if(request.method == 'POST'):
        email = request.form.get('email')
        primeiro_nome = request.form.get('primeiro_nome')
        senha1 = request.form.get('senha1')
        senha2 = request.form.get('senha2')

        if(len(email) < 4):
            flash('Email deve ter mais que 4 caracteres!', category='erro')
        elif(len(primeiro_nome) < 2):
            flash('Primeiro nome deve ter mais que 2 caracteres!', category='erro')
        elif(senha1 != senha2):
            flash('As senhas não são iguais!', category='erro')
        elif(len(senha1) < 7):
            flash('Senha deve ter mais que 7 caracteres!', category='erro')
        else:
            # adicionar usuario pro banco de dados
            flash('Usuário registrado com sucesso!', category='sucesso')

    return render_template('signup.html')