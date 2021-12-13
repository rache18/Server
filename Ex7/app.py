from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def main():
    return 'Hey Arseni, this ex7 is uploaded in 12.13.2021,' \
           ' but - we spoke on email, I deleted original Ex7 and upload Ex8 on it by mistake ' \
           'hope you understand, thank you! '

@app.route('/about')
def about1():
    return 'learn about me!'

@app.route('/hi')
def hi():
 return redirect('/about')

@app.route('/menu')
def errorpage():
 return redirect(url_for('main'))

if __name__ == '__main__':
    app.run()


