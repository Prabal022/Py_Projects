from flask import Flask,render_template, url_for
import joblib


app = Flask(__name__)

#Routes
@app.route('/')
def index():
    return render_template('index.html')

#Templates
@app.route('/about/')
def about():
    return render_template('about.html')



if __name__ == '__main__':
    app.run(debug=True)
