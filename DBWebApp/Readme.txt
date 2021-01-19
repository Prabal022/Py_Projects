to be able to work with this project, 

1. create postgre sql database in local machine by launching python session after enablinng virtual environment
    python 
    from app import db
    db.create_all

2. updating source email ID and password for gmail from which details will be sent to recipents
    from_email 
    from_password 

3. for google mails, update "less Secure app access to SMTP" ON this will help email.py file to access your mailbox.
    google->account->less secure app access (OFF by default)