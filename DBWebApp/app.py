from types import MethodType
from flask import Flask, app, render_template, url_for , request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func

app = Flask(__name__)


#Database 
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:3542@Noe@localhost/height_collect'
db=SQLAlchemy(app)

class Data(db.Model):
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key=True)
    email_ = db.Column(db.String(120), unique=True)
    height_ = db.Column(db.Integer)
    

    def __init__(self, email_, height_):
        self.email_ = email_
        self.height_ = height_

#Routes
@app.route('/')
def index():
    return render_template('index.html')

#Templates
@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        email = request.form["email-name"]
        height = request.form["height-name"]
        
        if db.session.query(Data).filter(Data.email_==email).count() == 0:
            data = Data(email, height)
            db.session.add(data)
            db.session.commit()

            average_height = db.session.query(func.avg(Data.height_)).scalar()
            average_height = round(average_height,2)
            count = db.session.query(Data.height_).count()
            send_email(email, height, average_height, count)

            return render_template('success.html')
        return render_template('index.html',
        text = "you have already submitted a query from this tempalte")


if __name__ == '__main__':
    app.run(debug=True)





