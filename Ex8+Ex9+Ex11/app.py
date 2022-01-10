from flask import Flask, render_template, url_for , request , redirect , session ,blueprints ,jsonify
import  mysql, mysql.connector
import os, sys
from flask import jsonify
import requests
import random

app = Flask(__name__)
app.secret_key = '1234'
def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         password='root',
                                         database='web')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)

    if query_type == 'commit':
        connection.commit()
        return_value = True
    if query_type == 'fetch':
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value


from assignment10.assignment10 import assignment10
app.register_blueprint(assignment10)

users = {"user1": {"First Name": "Racheli","Last Name": "Eliyahu", "Email": "rachelosh184@gmail.com", "User Name": "Rache"},
         "user2": {"First Name": "Doda", "Last Name": "Simi", "Email": "DodaSimi2010@gmail.com" , "User Name": "coolDoda"},
         "user3": {"First Name": "Kim", "Last Name": "Kardeshian", "Email": "kimik@gmail.com", "User Name": "kimi"},
         "user4": {"First Name": "billie", "Last Name": "Eilish", "Email": "billiesh@gmail.com","User Name": "billiesh"},
         "user5": {"First Name": "Leo", "Last Name": "Messi", "Email": "leo@gmail.com","User Name": "messiTheKing"}
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

#  assignment 11

def get_users():
    usersTable = interact_db(query="select * from web.users", query_type='fetch')
    return_dict = {}
    for user in usersTable:
        return_dict[f'user_{user.UserName}'] = {
            'First Name': user.FirstName,
            'User Name': user.UserName,
            'Last Name': user.LastName,
            'Email': user.Email,
        }
    return jsonify(return_dict)

@app.route('/assignment11/users' , methods = ['GET','DELETE','POST','PUY'])
def users():
    usersJson = get_users()
    return usersJson



def get_user(num):
    res = requests.get(f'https://reqres.in/api/users/{num}')
    res = res.json()
    return res


@app.route('/assignment11/outer_source', methods=['GET','DELETE','POST','PUY'])
def req_backend_func():
    num = 1
    if "number" in request.args:
        num = int(request.args['number'])
        user = get_user(num)
        return render_template('Assignment11Forms.html', user=user)
    else:
        return render_template('Assignment11Forms.html')


@app.route('/assignment12/restapi_users', defaults={'user_id': -1})
@app.route('/assignment12/restapi_users/<int:user_id>')
def get_user_func(user_id):
    if user_id == -1:
       user_id = 1
    return_dict = {}
    print(user_id)
    query = "select * from users WHERE id='%s';" % user_id
    user = interact_db(query=query, query_type='fetch')
    if len(user) == 0:
        return_dict = {
            'status': 'failed',
            'message': 'user not found'
        }
    else:
        return_dict[f'user_{user[0].id}'] = {
            'First Name': user[0].FirstName,
            'User Name': user[0].UserName,
            'Last Name': user[0].LastName,
            'Email': user[0].Email,
        }
    return jsonify(return_dict)

if __name__ == '__main__':
    app.run(debug=True)


