from flask import Flask, render_template, request

app: Flask=Flask(__name__,static_url_path='/static')

# Định tuyến hàm gọi ở trang gốc
@app.route("/")
def index():
if __name__== '__main__':
    print(__name__)
    app.run(host='0.0.0.0', port=5000)