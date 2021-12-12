from flask import Flask, redirect, url_for ,render_template

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('CVgrid.html')

@app.route('/Ex2')
def about1():
    return render_template('exercise2.html')

@app.route('/Form')
def info():
    return render_template('forms.html')

@app.route('/assignment8')
def assignment8():
    bakeryProducts =("cooKies", "bread", "english cake")
    return render_template('assignment8.html',bakeryProducts = bakeryProducts)



# @app.route('/payment')
# def errorpage():
#  return redirect(url_for('main'))

if __name__ == '__main__':
    app.run()