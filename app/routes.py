from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Mahi'}
    posts = [
        {
            'author':{'username':'vikas'},
            'body': 'I will have a govt job',
            'time': '02/03/2018',
            'views': 266,
            'last_seen': '5 hrs ago'
        },
        {
            'author': {'username':'Manish'},
            'body': 'I\'ll repair cycles',
            'time': '03/03/2018',
            'views': 1000,
            'last_seen': '2 hrs ago'
        }
    ]
    return render_template('index.html', user=user, title='BlogHome', posts=posts)
