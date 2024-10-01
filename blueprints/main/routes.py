from flask import render_template
from . import main_bp

@main_bp.route('/')
def index():
    return render_template('main/index.html')

@main_bp.route('/profile')
def profile():
    return render_template('main/profile.html')
