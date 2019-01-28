from flask import render_template, request, flash
from flask_login import current_user, login_user, logout_user
from werkzeug.utils import redirect

from voteitapp import db, app
from voteitapp.forms import LoginForm, SignUpForm
from voteitapp.models import User


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('/index')
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password_hash(password=form.password.data):
            return redirect('/login')
        login_user(user)
        print 'logged in'
        return redirect('/posts')
    return render_template('/user/login.html', title='Sign In', form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if request.method == 'POST':
        user = User(username=form.data['username'], email=form.data['email'])
        db.session.add(user)
        user.set_password_hash(password=form.data['password'])
        db.session.commit()
        login_user(user)
        return redirect('/posts')
    else:
        return render_template('/user/signup.html', title='Sign Up', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect('/login')


@app.route('/profile')
def profile():
    user = db.session.query(User).outerjoin(User.posts).filter(User.id == current_user.id).one()
    if not user:
        render_template('/')
    else:
        return render_template('/user/detail.html', user=user)


@app.route('/users/user/<id>/')
def user(id):
    user = db.session.query(User).outerjoin(User.posts).filter(User.id == id).one()
    if not user:
        render_template('/')
    else:
        return render_template('/user/detail.html', user=user)
