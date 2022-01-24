import time
from flask import Flask

app = Flask(__name__)
@app.route('/api/variable')
def get_variabel():
    return {'variable': 'helloworld from flask'}