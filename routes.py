from flask import Flask, render_template, url_for, flash, redirect
from flask_mail import Message
from final_year import app, db, bcrypt
from final_year.forms import RegistrationForm, LoginForm, AppointmentForm  
from final_year.models import User, Appointment
from flask_login import login_user, current_user, logout_user, login_required

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/sign_up", methods=['GET', 'POST'])
def sign_up():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(fullname=form.fullname.data, 
                    username=form.username.data, 
                    email=form.email.data, 
                    password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created', 'success')
        return redirect(url_for('login'))
    return render_template('sign_up.html', title='Sign Up', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash('Login successful', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login not successful. Please check email and password', 'danger')
    return render_template('log.html', title='Login', form=form)


@app.route("/appointment", methods=['GET', 'POST'])
def appoint():
    form = AppointmentForm()
    if form.validate_on_submit():
        appoint = Appointment(
        fullname=form.fullname.data,
        phone_number=form.phone_number.data,
        email=form.email.data,
        reason=form.reason.data           
        )
        db.session.add(appoint)
        db.session.commit()
        flash('Your appointment has been set', 'success')
        return redirect(url_for('appointment'))
    return render_template('appointment.html', title='Appointment', form=form)

@app.route("/services")
def services():
    return render_template('services.html')

@app.route("/staff")
def staff():
    return render_template('staff.html')

@app.route("/test")
def test():
    return render_template('test.html')

@app.route("/test_mail")
def test_mail():
    # Assuming this route is for testing email functionality
    flash('This is a test email function.', 'info')
    return redirect(url_for('home'))

@app.route("/view", methods=['GET', 'POST'])
@login_required
def view():
    appointments = Appointment.query.all()  # Fetch all appointments from the database
    return render_template('view.html', appointments=appointments)

@app.route("/schedule")
def schedule():
    form = AppointmentForm()
    if form.validate_on_submit():
        appoint = Appointment(
        fullname=form.fullname.data,
        phone_number=form.phone_number.data,
        email=form.email.data,
        reason=form.reason.data           
        )
        db.session.add(Appointment)
        db.session.commit()
        flash('Your appointment has been set', 'success')
        return redirect(url_for('home'))
    return render_template('index.html', title='Appointment', form=form)

    return render_template('test.html')
        