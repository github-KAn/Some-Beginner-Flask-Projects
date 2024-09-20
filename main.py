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
@app.route("/welcome/<pname>")
def welcome(pname):
    return render_template("welcome2.html",acc=pname)
@app.route("/loadPage01")
def loadPage01():
    lst=[0,1,2,3]
    return render_template("page_01_for.html",seq=lst)
@app.route("/loadPage03")
def loadPage03():
    import pandas as pd
    data={
        "Name":["John","Anna","Peter","Linda"],
        "Age": [28,24,35,32],
        "City":["New York","Paris","Berlin","London"]
    }
    df=pd.DataFrame(data)
    html_data=df.to_html(classes='data', escape=False);
    return render_template("page_03_Table.html",table=html_data)
@app.route("/loadPage04")
def loadPage04():
    html_table=load_data()
    return render_template()
# chạy web
if __name__== '__main__':
    print(__name__)
    app.run(host='0.0.0.0', port=5000, debug=True)