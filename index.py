from flask import Flask
import seconds2dd as sec
import sys

app = Flask(__name__)

@app.route('/')
def index():
    return "Please give me some seconds, and/or the hours per day your work day is, in /seconds/hours_per_day format"

@app.route('/<int:seconds>')
@app.route('/<int:seconds>/<hours>')
def seconds(seconds, hours=7.5):
    response = sec.ddhhmmss(seconds, hours)
    return response

@app.route('/version')
def version():
    return "0.0.2"

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')