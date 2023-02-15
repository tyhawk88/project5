from flask import Flask, jsonify, request
from markupsafe import escape
import hashlib, math

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'

@app.route('/md5/<string>')
def md5(string):

    result = hashlib.md5()
    result.update(string.encode('utf-8'))
    calculation = result.hexdigest()
    
    data = {
            "input" : string,
            "output" : calculation,
        }

    return jsonify(data)
    
"""  
@app.route('/factorial/<int>')
def factorial(int):

    number = int(integer)
    return math.factorial(number)
    
@app.route('/is-prime/<int>')
def prime(int):
"""

if __name__ == '__main__':
    app.run()