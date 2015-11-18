#program exam 1
from flask import Flask, url_for #the name of the application package

app = Flask(__name__)

@app.route('/')
def hello_world():
#    return 'Hello World!'
    with app.test_request_context():
        return redirect(url_for('login'))

@app.route('/login/')
def login():
    return 'log_in'

if __name__ == '__main__':
    app.run()

app.debug = True #소스 변경과 디버거 제공
app.run(host = '172.16.39.21', port = 5000)
