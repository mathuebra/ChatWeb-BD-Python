from flask import render_template
from . import main_bp

@main_bp.route('/home')
def home():
    return render_template('main/home.html')
