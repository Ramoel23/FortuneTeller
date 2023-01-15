from flask import Flask, request
from flask import request
app = Flask(__name__)

@app.route('/')
def index():
   return  'Hello'

@app.route('/about')
def about():
    return 'About this app'

@app.route('/about/<username>')
def user_info(username):
    return f'Hello{username}'

    return '<h1>Hello World</h1>'

@app.route('/login',methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "Handle form POST"
    else:
        return "Handle GET request"

if __name__ == '__main__':
   app.run(debug=True)