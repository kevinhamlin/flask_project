from flask import render_template, url_for, flash, redirect
from main.forms import RegistrationForm, LoginForm
from main.imports.posts import posts
from main import app, db, bcrypt
from main.models.models import User


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        #hash the password they gave us
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        #create a new instance of a user
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created. You are now able to login.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'hhhhhhhhhh':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login failed. Please check email and password.', 'danger')
    return render_template('login.html', title="Login", form=form)