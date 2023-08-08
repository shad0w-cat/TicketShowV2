from flask import Flask, render_template, request
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

EMAIL_ADDRESS = "iamstuarttheminion@gmail.com"
EMAIL_PASSWORD = "aplnoeailycvpgwg"
SMTP_SERVER = 'localhost'
SMTP_PORT = 1025 

def send_email(to_email, subject, message):
    print("in send")

    msg = EmailMessage()
    print("after email message")
    msg.set_content(message)
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to_email
    try:
        print("in try")
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
            print("here")
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            print("logged in")
            smtp.send_message(msg)
        return 'Email sent successfully!'
    except Exception as e:
        print(e.msg())


if __name__ == '__main__':
    send_email()