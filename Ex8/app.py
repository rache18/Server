from flask import Flask, render_template, url_for , request , redirect , session ,blueprints ,jsonify
import  mysql, mysql.connector

app = Flask(__name__)
app.secret_key = '1234'

users = {"user1": {"First Name": "Racheli","Last Name": "Eliyahu", "Email": "rachelosh184@gmail.com", "User Name": "Rache"},
         "user2": {"First Name": "Doda", "Last Name": "Simi", "Email": "DodaSimi2010@gmai.com" , "User Name": "coolDoda"},
         "user3": {"First Name": "Kim", "Last Name": "Kardeshian", "Email": "kimik@gmai.com", "User Name": "kimi"},
         "user4": {"First Name": "billie", "Last Name": "Eilish", "Email": "billiesh@gmai.com","User Name": "billiesh"},
         "user5": {"First Name": "Leo", "Last Name": "Messi", "Email": "leo@gmai.com","User Name": "messiTheKing"}
         }


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


@app.route('/assignment9' , methods = ['GET','POST'])
def assignment9():
    current_method = request.method
    if current_method == 'GET':
        if 'email' in request.args:
            email = request.args['email']
            if email is '':
                return render_template('assignment9.html', search=True, users=users, haveUser=True)
            user_dic = {}
            num = 1
            for user in users.values():
                if user['Email'] == email:
                    user_dic[num] = user
                num += 1
            if len(user_dic) != 0:
                return render_template('assignment9.html', search=True, haveUser=True, users=user_dic)
            else:
                return render_template('assignment9.html', haveUser=False, search=True)
        return render_template('assignment9.html')
    elif current_method == 'POST':
        users[request.form['firstName']] = {'First Name': request.form['firstName'],
                                            'Last Name': request.form['lastName'],
                                            'Email': request.form['email'],
                                            'User Name': request.form['userName']}
        session['login'] = True
        session['userName'] = request.form['userName']
        return render_template('assignment9.html')

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session['login'] = False
    return render_template('assignment9.html')



if __name__ == '__main__':
    app.run()