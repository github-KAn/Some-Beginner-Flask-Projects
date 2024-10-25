from flask import Flask, request, jsonify, render_template,request,redirect,flash
import requests

#Create a flask app
app=Flask(__name__)
app.secret_key="FelixPham"
#set the base url
base_url="http://127.0.0.1:5000/users"
#define a route
@app.route("/")
def index():
    response=requests.get(base_url)
    #check if the response is successful
    if response.status_code==200:
        #Parse the response as a json object
        users=response.json()
        #return render template
        return render_template("user.html",users=users)
    else:
        flash("something went wrong please try again later")
    return render_template("user.html")
@app.route("/", methods=["GET","POST"])
def add():
    if request.method=="POST":
        user_name=request.form.get("name")
        user_email=request.form.get("email")
        user_password= request.form.get("password")
        if user_name and user_email and user_password;
            response=request.post(base_url)


# app.route("/user",methods=["POST"])
# def get_users():
#run the app
if __name__=="__main__":
    app.run(debug=True,port=5001)