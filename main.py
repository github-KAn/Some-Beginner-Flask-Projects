import flask
from flask import Flask, render_template, request

# from flask.globals import app_ctx

# Khởi tạo đối tượng app
app=Flask(__name__)

# Định tuyến hàm gọi ở trang gốc
@app.route("/")
def index():
    return render_template("welcome.html")
@app.route("/html")
def html_page():
    html_=("<h1>hello</h1>"
           "<h2>abcd</h2>")
    return html_
@app.route("/loadAccount")
def loadAccount():
    account="Felix"
    return render_template("account.html", acc=account)
# chạy web
if __name__== '__main__':
    print(__name__)
    app.run(host='0.0.0.0', port=5000, debug=True)