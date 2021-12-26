from flask import Flask, render_template, url_for, session, request, redirect, Blueprint , flash
import mysql
import mysql.connector

app = Flask(__name__)
app.secret_key = "123"

assignment10 = Blueprint(
    'assignment10',
    __name__,
    static_folder='static',
    static_url_path='/assignment10',
    template_folder='templates'
)

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


@assignment10.route('/assignment10')
def users():
    usersTable = interact_db(query="select * from web.users", query_type='fetch')
    if session.get('messages'):
        x = session['messages']
        session.pop('messages')
        return render_template('assignment10.html', users=usersTable, messages = x)
    else:
        return render_template('assignment10.html', users=usersTable)


@assignment10.route('/insert', methods=['GET','POST'])
def insert():
    if request.method == 'POST':
        UserName = request.form['UserName']
        FirstName = request.form['FirstName']
        LastName = request.form['LastName']
        Email = request.form['Email']
        check_Email = "SELECT Email FROM web.users WHERE Email='%s';" % Email
        answer = interact_db(query=check_Email, query_type='fetch')
        if len(answer) == 0:
            interact_db(query="insert into web.users(UserName, FirstName ,LastName, Email)\
                                 value ('%s', '%s', '%s','%s');" % (UserName,FirstName ,LastName, Email), query_type='commit')
            session['messages'] ='User added!'
            return redirect('/assignment10')
        else:
            session['messages'] ='The Email you entered already exists, please try another one'
            return redirect('/assignment10')
    return render_template('assignment10.html', req_method=request.method)


@assignment10.route('/update', methods=['GET','POST'])
def update():
        user = request.form['UserName']
        FN = request.form['FirstName']
        LN = request.form['LastName']
        E = request.form['Email']
        interact_db(query=" UPDATE web.users SET UserName='%s',FirstName='%s' ,LastName='%s' WHERE Email='%s';"%\
                             (user, FN, LN, E), query_type='commit')
        session['messages'] = 'User Updated !'
        return redirect('/assignment10')


@assignment10.route('/delete', methods=['POST'])
def deleteUsers():
    userEmail = request.form['Email']
    check = "SELECT userName FROM web.users WHERE Email='%s';" % userEmail
    answer = interact_db(query=check, query_type='fetch')
    if len(answer) > 0:
        query = "delete from web.users where Email='%s';" % userEmail
        interact_db(query=query, query_type='commit')
        session['messages'] = 'User deleted from DB'
        return redirect('/assignment10')
    else:
        session['messages'] = 'Email dose not exists in DB'
        return redirect('/assignment10')
