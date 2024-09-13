import flask
from flask import Flask, render_template

# from flask.globals import app_ctx

# Khởi tạo đối tượng app
app=Flask(__name__)

# Định tuyến hàm gọi ở trang gốc
@app.route("/")
def index():
    return "web site 2"
@app.route("/html")
def html_page():
    html_=("<h1>hello2</h1>"
           "<h2>abcd2</h2>")
    return html_
# @app.route("/about")
# def about_page():
#     return render_template()
# chạy web
if __name__== '__main__':
    print(__name__)
    app.run(host='0.0.0.0', port=5001)