import pandas as pd
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


df = pd.read_csv('input.csv') #change this to us responses.cv file

def send_certificate(name, email, certificate_dir, remaining_emails):

    EMAIL = "" #your email address
    PASSWORD = "" #this is not my actual password, this is app password. Refer to the readme file for more info
    SUBJECT = "Certificate of Participation" #subject of the email
    BODY = f"""Dear {name},

    Thank you for participating in our event. Please find attached, your certificate of participation.

    Best regards,
    Organizing team.
    """

    SMTP_PORT = 587
    SMTP_SERVER = "smtp.gmail.com"



    message = MIMEMultipart()
    message['From'] = EMAIL  
    message['To'] = email
    message['Subject'] = SUBJECT


    # body = BODY.format(namePlaceholder=name)
    message.attach(MIMEText(BODY, 'plain'))

    certificate_path = os.path.join(certificate_dir, f"{name}.png")
    with open(certificate_path, 'rb') as f:
        attach = MIMEApplication(f.read(),_subtype = "png")
        attach.add_header('Content-Disposition', 'attachment', filename=str(name)+".png")
        message.attach(attach)

    smtp_server = SMTP_SERVER  
    smtp_port = SMTP_PORT  
    username = EMAIL  
    password = PASSWORD  
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(username, password)
        server.sendmail(username, email, message.as_string())

    # print status update
    remaining_emails -= 1
    print(f"Certificate sent to {name} at {email}  - {remaining_emails} left ")

    return remaining_emails

remaining_emails = len(df)
for _, row in df.iterrows():
    global name
    name = row['Name']
    email = row['Email']
    certificate_dir = "Generated Certificates"
    remaining_emails = send_certificate(name, email, certificate_dir, remaining_emails)
