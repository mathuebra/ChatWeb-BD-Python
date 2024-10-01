from flask import render_template, redirect, url_for, flash, session
from . import auth_bp
from .forms import LoginForm
from database import Database

db = Database('/home/mathuebra/VS/DatabasePython/ChatWeb/chatweb')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user_id = db.verify_login(username, password)
        
        if user is not None:
            session['USER_ID'] = user_id
            flash('Login realizado!', 'Sucesso!')
            return redirect(url_for('main.home'))
        else:
            flash('Login falhou!', 'Falha!') 
        
    return render_template('auth/login.html', form=form)

@auth_bp.route('/register')
def register():
    return render_template('auth/register.html')
