from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm 

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
  
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
