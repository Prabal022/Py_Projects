import re
from flask import Flask,render_template, url_for
import joblib
from pandas_datareader import data
import datetime
from bokeh.plotting import figure, show, output_file
from bokeh.embed import components
from bokeh.resources import CDN

app = Flask(__name__)

#Routes
@app.route('/')
def index():
    return render_template('index.html')

#Templates
@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/plot/')
def plot():
    start = datetime.datetime(2020,1,1)
    end = datetime.datetime(2020,10,31)

    df=data.DataReader(name="GOOG",data_source="yahoo",start=start, end=end)

    def inc_dec(c, o):
        if c > o:
            value = "Increase"
        elif c < o:
            value = "Decrease"
        else:
            value = "Equal"
        return value

    df["status"] =[inc_dec(c, o) for c, o in zip(df.Close,df.Open)]
    df["Middle"] = (df.Open + df.Close)/2
    df["Height"] = abs(df.Close-df.Open)

    p = figure(x_axis_type = 'datetime', width=1000, height=300, sizing_mode="scale_width")
    p.title.text = "Candelstick Chart"
    p.grid.grid_line_alpha=0.3

    hours_12 = 12*60*60*1000

    p.segment(df.index, df.High, df.index, df.Low, color="black")

    p.rect(df.index[df.status =="Increase"],df.Middle[df.status=="Increase"],
        hours_12, df.Height[df.status =="Increase"],fill_color="green",line_color="black")

    p.rect(df.index[df.status =="Decrease"],df.Middle[df.status=="Decrease"],
        hours_12, df.Height[df.status =="Decrease"],fill_color="red",line_color="black")


    script1, div1 = components(p)

    cdn_js = CDN.js_files[0]
    
    return render_template('plot.html', script1=script1, div1=div1, cdn_js=cdn_js)
    


if __name__ == '__main__':
    app.run(debug=True)
