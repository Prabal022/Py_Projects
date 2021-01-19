from email.message import EmailMessage
from email.mime.text import MIMEText
from email.policy import SMTP
import smtplib

def send_email(email, height, average_height, count):
    from_email = ""  #Enter source Email Address
    from_password = "" #Enter Source Email password ------- set less secure app access to yes in source email (i.e google - account - less secure access app)
    to_email = email

    subject = "Height Data"
    message = "Hey There, your height is <strong>%s</strong>.Average height of all is <strong>%s</strong> and that is calculated out of <strong>%s</strong> entries." % (height, average_height, count)

    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email

    gmail = smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email,from_password)
    gmail.send_message(msg)






