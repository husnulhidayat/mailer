import sys
import pandas as pd
import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from datetime import datetime
import time

def start_sendMail():
    pathh = f'{your_path_file}'
    rd = pd.read_csv(pathh)
    c = len(rd)
    count = str(c)
    
    subject = f'{your_subject_mail}'
    body = f'{your_body_mail}'
    sender_email = un

    receiver_email = ['example@mail.com', 'example1@mail.com']
    cc_email = {put_your_cc_list_mail}
    password = pw

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = ', '.join(receiver_email)
    message["Cc"] = ', '.join(cc_email)
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))   
    
    filename = pathh
    file_nm = f'{file_name}'

    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    encoders.encode_base64(part)

    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {file_nm}",
    )

    message.attach(part)
    text = message.as_string()

    print('start sending mail...')
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, (receiver_email+cc_email), text)
    print('sending mail success!')
    
if __name__ == "__main__":
    job_id = sys.argv[1]
    today = sys.argv[2]
    un = sys.argv[3]
    pw = sys.argv[4]
    start_sendMail()
