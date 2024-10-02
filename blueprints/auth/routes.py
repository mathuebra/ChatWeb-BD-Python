from flask import render_template, redirect, url_for, flash, session, request
from . import auth_bp
from .forms import LoginForm, RegisterForm
from database import Database

db = Database('/home/mathuebra/VS/DatabasePython/ChatWeb/chatweb')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = db.verify_login(email, password)
        
        if user:
            session['user_id'] = user
            flash('Login realizado!', 'Sucesso!')
            return redirect(url_for('main.home'))
        else:
            flash('Login falhou!', 'Falha!') 
        
    return render_template('auth/login.html', form=form)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        name = form.name.data
        birthdate = form.birthdate.data

        if db.register(email, password, birthdate, name):
            flash('Conta criada, você já pode fazer login!', 'Sucesso!')
            return redirect(url_for('auth.login'))
        else:
            flash('Erro ao criar conta', 'Falha!')

    return render_template('auth/register.html', form=form)
