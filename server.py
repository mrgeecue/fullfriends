from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')

@app.route('/')
def index():
    query = "SELECT * FROM friends"
    friends = mysql.query_db(query)
    print friends
    return render_template('index.html', all_friends=friends)

@app.route('/friends')
def edit(id):
    query = "INSERT INTO friends (first_name, last_name, occupation) VALUES (:first_name, :last_name, :occupation)"
    data = {
             'first_name': request.form['first_name'],
             'last_name':  request.form['last_name'],
             'occupation': request.form['occupation'],
             'id': friend_id
           }
    mysql.query_db(query, data)
    return redirect('/')

def delete():
    if request.form["delete"] == 2:
        print "DELETE DELETE DELETE"


app.run(debug=True)

#
# @app.route('/friends', methods=['POST'])
# def create():
#     errors = 0
#     #Check first name
#     if request.form['first_name'] == '':
#         flash('First name cannot be blank', 'firstNameError')
#         errors += 1
#     elif not regex_name.match(request.form['first_name']):
# #     elif any(char.isdigit() for char in request.form['first_name']) == True:
#         flash('First name cannot have numbers','firstNameError')
#         errors += 1
#     else:
#         flash('Success! First name is valid.', 'success')
#       #Check last name
#     if request.form['last_name'] == '':
#         flash('Last name cannot be blank', 'lastNameError')
#         errors += 1
#     elif not regex_name.match(request.form['last_name']):
# #     elif any(char.isdigit() for char in request.form['last_name']) == True:
#         flash('Last name cannot have numbers', 'lastNameError')
#         errors += 1
#     else:
#         flash('Success! Last name is valid.', 'success')
#
# @app.route('/friends/<id>', methods=['POST'])
# def editInfo(id):
#     query = "select * from friends WHERE id = :id"
#     data = {
#              'id': id
#            }
#     oneFriend = mysql.query_db(query, data)
#     #Check first name
#     if request.form['first_name'] == '':
#         #if user leaves first_name field blank, leave it alone in db
#         temp_first = oneFriend[0]['first_name']
#     elif not regex_name.match(request.form['first_name']):
#         #if user inputs invalid first_name, leave it alone in db
#         temp_first = oneFriend[0]['first_name']
#         flash('First name cannot have numbers','firstNameError')
#     else:
#         temp_first = request.form['first_name']
#         flash('Success! First name changed.', 'success')
#     #Check last name
#     if request.form['last_name'] == '':
#         #if user leaves last_name field blank, leave it alone in db
#         temp_last = oneFriend[0]['last_name']
#     elif not regex_name.match(request.form['last_name']):
#         #if user inputs invalid last_name, leave it alone in db
#         temp_last = oneFriend[0]['last_name']
#         flash('Last name cannot have numbers', 'lastNameError')
#     else:
#         temp_last = request.form['last_name']
#         flash('Success! Last name changed.', 'success')
#     #Check occupation
#     if request.form['occupation'] == '':
#         #if user leaves occupation field blank, leave it alone in db
#         temp_occ = oneFriend[0]['occupation']
#     else:
#         temp_occ = request.form['occupation']
#         flash('Success! Occupation changed.', 'success')
#     query = "UPDATE friends set first_name= :first_name, last_name= :last_name, occupation= :occupation, updated_at = NOW() WHERE id = :id"
#     data = {
#              'first_name': temp_first,
#              'last_name': temp_last,
#              'occupation': temp_occ,
#              'id': id
#            }
#     mysql.query_db(query, data)
#     return redirect('/')
# @app.route('/friends/<id>/edit')
# def viewEdit(id):
#     query = "select * from friends WHERE id = :id"
#     data = {'id': id}
#     friend = mysql.query_db(query, data)
#     print friend
#     return render_template('edit.html', friend=friend[0])
