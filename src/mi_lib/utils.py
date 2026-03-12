import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from datetime import timedelta, date
import os

def send_email(to, subject, file_names, body, email_address, email_app_password):

    # create email
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = email_address
    msg['To'] = ", ".join(to)
    body = MIMEText(body)
    msg.attach(body)

    # Adjuntar múltiples archivos
    for file_name in file_names:
        try:
            with open(file_name, 'rb') as file:
                msg.attach(MIMEApplication(
                    file.read(),
                    Name=os.path.basename(file_name)
                ))
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo {file_name}")
            continue

    smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_obj.starttls()
    smtp_obj.login(email_address, email_app_password)

    smtp_obj.sendmail(msg['From'],to, msg.as_string())
    smtp_obj.quit()
