from flask import Flask, jsonify, request
import seconds2dd as sec
import sys

appVersion = "0.0.3"

app = Flask(__name__)

@app.route('/')
def index():
    return "Please give me some seconds, and/or the hours per day your work day is, in /seconds/hours_per_day format"

@app.route('/<int:seconds>')
@app.route('/<int:seconds>/<hours>')
def seconds(seconds, hours=7.5):
    returnRaw = request.args.get('raw')
    response = sec.ddhhmmss(seconds, hours)
    if returnRaw:
        return response
    else:
        return jsonify(
            response=dict(
                raw=response,
                human=sec.parseValue(response)
            ),
            appVersion=appVersion
        )

@app.route('/version')
def version():
    return appVersion

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')