@app.route('/delete/<friend_id>'
def delete(friend_id):
    query = "DELETE FROM friends WHERE id = :id"
    data = {'id': friend_id}
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/friends/<id>/delete_confirm', methods=['POST'])
def delete_confirm(id):
    friendquery = "select * from friends WHERE id = :id"
    frienddata = {'id': int(id)}
    friend = mysql.query_db(friendquery, frienddata)
    flash("{} {} was removed.".format(friend[0]['first_name'],friend[0]['last_name']), "success")
    query = "DELETE FROM friends WHERE id = '{}'".format(id)
    mysql.query_db(query)
    return redirect('/')
    
