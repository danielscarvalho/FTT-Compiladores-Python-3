from flask import Flask, url_for
from markupsafe import escape

# https://flask.palletsprojects.com/en/1.1.x/quickstart/

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(escape(username))

@app.route('/add/<a>/<b>')
def add(a, b):
    return 'soma: {}'.format(escape(int(a)+int(b)))

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
    print(url_for('add', a='0', b='0'))