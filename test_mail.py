from flask import render_template, redirect, url_for, flash
from final_year import app, mail
from flask_mail import Message

@app.route('/send_test_email')
def send_test_email():
    try:
        msg = Message(
            subject="Test Email from Flask",
            recipients=["sheundaalex@gmail.com"],  # Replace with your email address
            body="This is a test email sent from your Flask application."
        )
        mail.send(msg)
        flash('Test email sent successfully!', 'success')
    except Exception as e:
        flash(f'Failed to send email: {str(e)}', 'danger')
    
    return redirect(url_for('test'))  # Redirect to the home page or any other page