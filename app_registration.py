from flask import Flask,render_template, request,redirect, url_for
import sqlite3

app=Flask(__name__)
app.secret_key="my key"
sqldbname="db/website.db"

def SaveToDB(uname,email,pass):
    # get Max from database
    id_max=
    conn=sqlite3.connect(sqldbname)
    cursor=conn.cursor()
    sqlcommand="Insert into user (id,name, email,password)"
def generateID():
    max_id=0
    # khai bao bien de tra lai db
@app.route("/")
def index():
    return render_template("registration_db.html",username_error="",
                           email_error="",
                           password_error="",
                           registration_success="")
@app.route("/register")
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
    newID=SaveToDB(username,email,password)
    stroutput=f'Registered: Username:{username} - Password:{password}'
    registration_success="Registstration Successful! with id="+ str(newID)

if __name__== '__main__':
    print(__name__)
    app.run(host='0.0.0.0', port=5002,debug=True)