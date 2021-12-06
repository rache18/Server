from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def main():
    return 'This is Web Course!'

@app.route('/about')
def about1():
    return 'My name is Racheli, I am 26 years old'

@app.route('/info')
def info():
 return redirect('/about')

@app.route('/payment')
def errorpage():
 return redirect(url_for('main'))

if __name__ == '__main__':
    app.run()