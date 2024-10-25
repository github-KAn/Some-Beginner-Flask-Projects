from flask import Flask, request, jsonify, render_template,request,redirect
import sqlite3

#Create a flask app
app=Flask(__name__)
app.secret_key="FelixPham"
#set the base url
base_url="http://127.0.0.1:5000/users"
#define a route
@app.route("/")
def index():
    response=requests.get(base_url)
    #check if the response
# app.route("/user",methods=["POST"])
# def get_users():
#run the app
if __name__=="__main__":
    app.run(debug=True,port=5000)