from flask import Flask
import seconds2dd as sec
import sys

app = Flask(__name__)

@app.route('/')
def index():
    return "Please give me some seconds!"

@app.route('/<int:seconds>')
def seconds(seconds):
    response = sec.ddhhmmss(seconds)
    return response

@app.route('/version')
def version():
    return "0.0.1"

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')