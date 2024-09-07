from datetime import datetime, timedelta
from flask import current_app
from flask_mail import Message
from final_year import mail, db
from final_year.models import Appointment

def send_reminders():
    with current_app.app_context():
        now = datetime.now()
        reminder_time = now + timedelta(hours=24)  # Remind 24 hours in advance

        # Combine date and time to get a single datetime object for comparison
        appointments = Appointment.query.filter(
            db.func.datetime(Appointment.date, Appointment.time) <= reminder_time,
            db.func.datetime(Appointment.date, Appointment.time) > now
        ).all()

        for appointment in appointments:
            try:
                msg = Message(
                    "Appointment Reminder",
                    recipients=[appointment.email],
                    body=f"Hello {appointment.fullname},\n\n"
                         f"This is a reminder for your appointment on {appointment.date} at {appointment.time}.\n"
                         f"Reason: {appointment.reason}\n\n"
                         f"Thank you!"
                )
                mail.send(msg)
            except Exception as e:
                print(f"Failed to send reminder for {appointment.fullname}: {e}")
