from flask import Flask, request,jsonify
import sqlite3

#Create a flask app
app=Flask(__name__)
#Connect to the database
sqldbname="db/website.db"
@app.route("/users",methods=["GET"])
def get_users():
    conn= sqlite3.connect(sqldbname)
    cur=conn.cursor()
    #querry
    cur.execute("SELECT * FROM user ")
    users=cur.fetchall()
    #Convert the result to a list of dictionaries
    users_list=[]
    for user in users:
            users_list.append({"_id":user[0],"name":user[1],
                                "email":user[2],"password":user[3]})
    # if user:
    return jsonify(users_list)
@app.route("/users/<int:_id>",methods=["GET"])
def get_user(_id):
    conn= sqlite3.connect(sqldbname)
    cur=conn.cursor()
    #querry
    cur.execute("SELECT * FROM user WHERE id =?",(_id,))
    user=cur.fetchone()
    #Convert the result to a list of dictionaries
    if user:
        user_dict={"id":user[0], "name":user[1],
                   "email":user[2],"pasword":user[3]}
    # if user:
        return jsonify(user_dict)
    else:
        return "User not found",404
app.route("/users",methods=["POST"])
def add_user():
    conn = sqlite3.connect(sqldbname)
    cur = conn.cursor()
    #get the user name, email and password from the request body
    user_name=request.json.get("name")
    user_email=request.json.get("email")
    user_password=request.json.get("password")
    #check if the user name, email and password are val_id
    if user_name and user_email and user_password:
        #Insert the user into the database
        cur.execute("INSERT INTO user (name,email,password)"
                    " VALUES (?,?,?)", (user_name,user_email,user_password))
        conn.commit()
        #Get the _id of the inserted user
        user_id= cur.lastrowid
        #Return the _id as a JSON response
        return jsonify({"_id":user_id})
    else:
        return "User name, email and password are required",400

@app.route("/users/<int:_id>",methods=["PUT"])
def update_users(_id):
    conn= sqlite3.connect(sqldbname)
    cur=conn.cursor()
    # get the user name, email and password from the request body
    user_name = request.json.get("name")
    user_email = request.json.get("email")
    user_password = request.json.get("password")
    if user_name and user_email and user_password:
        #Insert the user into the database
        cur.execute("UPDATE user SET name=?, email=?,"
                    " password=? WHERE id=?",(user_name,user_email,user_password,_id))
        conn.commit()
        if cur.rowcount>0:
            return jsonify({"message":"User updated successfully"})
        else:
            return "User not found", 404
    else:
        return "User name, email and password are required",400
@app.route("/users/<int:_id>",methods=["DELETE"])
def delete_user(_id):
    conn=sqlite3.connect(sqldbname)
    cur=conn.cursor()
    #Delete the user from data base
    print(_id)
    cur.execute("DELETE FROM user WHERE id= ?",(_id,))
    conn.commit()
    if cur.rowcount>0:
        return jsonify({"message":"User deleted successfully"})
    else:
        return "User not found",404



#run the app
if __name__=="__main__":
    app.run(debug=True,port=5000)