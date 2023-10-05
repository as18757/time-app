from flask import Flask
from datetime import datetime
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'
@app.route('/time')
def latest_time():
    now=datetime.now()
    curr_time=now.strftime("%H:%M:%S")
    return curr_time


app.run(host='0.0.0.0',
        port=8080,
        debug=True)
