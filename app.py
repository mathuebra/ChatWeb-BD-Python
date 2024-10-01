from flask import Flask, redirect, url_for
from database import Database
from blueprints.auth import auth_bp
from blueprints.main import main_bp

app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.secret_key='super secret key'

db = Database('/home/mathuebra/VS/DatabasePython/ChatWeb/chatweb')

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(main_bp)

@app.route('/')
def index():
    return redirect(url_for('auth.login'))

if __name__ == '__main__':
    app.run(debug=True)