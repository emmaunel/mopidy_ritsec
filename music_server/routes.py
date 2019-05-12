from flask import render_template
from music_server import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Test'}
    return render_template('index.html', title='Home', user=user)