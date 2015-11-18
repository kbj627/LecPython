#program exam 1
from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def hello(name=None):
    data = [dict(href='http://www.naver.com', caption='네이버'),
            dict(href='http://www.google.com', caption='구글'),
            dict(href='http://www.daum.net', caption='다음')]
    data2 = {'title' : 'Hello',
             'name' : 'greenjoa'}
#    return render_template('hello.html', name=name, items = data)
#    return render_template('hello.html', **data2)
    return render_template('main.html', name=name)

if __name__ == '__main__':
    #app.debug = True
    app.run()