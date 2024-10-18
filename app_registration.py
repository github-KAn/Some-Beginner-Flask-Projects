# from crypt import methods

from flask import Flask,render_template, request,redirect, url_for
import sqlite3

app=Flask(__name__)
app.secret_key="my key"
sqldbname="db/website.db"


@app.route("/")
def index():
    return render_template("registration_db.html",username_error="",
                           email_error="",
                           password_error="",
                           registration_success="")
def generateID():
    max_id=0
    # khai bao bien de tra lai db
    conn=sqlite3.connect(sqldbname)
    cursor=conn.cursor()

    sqlcommand= "Select Max(id) from user"
    cursor.execute(sqlcommand)
    max_id= cursor.fetchone()[0]
    return max_id
def saveToDB(name,email,password):
    # get Max from database
    id_max=generateID()
    if id_max>0:
        id_max=id_max+1
    else: id_max=1
    print(id_max)
    conn=sqlite3.connect(sqldbname)
    #Create a cursor object
    cursor=conn.cursor()
    #Insert the user into users table using parameterized query
    sqlcommand="Insert into user" "(id,name, email,password) VALUES (?,?,?,?)"
    cursor.execute(sqlcommand,(id_max,name,email,password))

    #commit the changes
    conn.commit()
    #close the connection
    conn.close()
    #return a success message
    return id_max
@app.route("/register", methods=['POST'])
def register():
    username=request.form["username"]
    password = request.form["password"]
    email = request.form["email"]
    username_error = "";    email_error = "";    password_error = "";    registration_success = ""
    # Server side validation
    if not username: username_error="Username is required"
    if not password: password_error = "password is required"
    if username_error or password_error:
        return render_template("registration_db.html", username_error=username_error,
                               email_error=email_error,
                               password_error=password_error,
                               registration_success="")
    # perform registration logic here
    newID=saveToDB(username,email,password)
    stroutput=f'Registered: Username:{username} - Password:{password}'
    registration_success="Registstration Successful! with id="+ str(newID)
    print(registration_success+stroutput)
    return render_template("registration_db.html", username_error=username_error,
                               email_error=email_error,
                               password_error=password_error,
                               registration_success=registration_success+stroutput)

if __name__== '__main__':
    print(__name__)
    app.run(host='0.0.0.0', port=5002,debug=True)