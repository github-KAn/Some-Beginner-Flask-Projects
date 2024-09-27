from flask import (Flask, render_template, request,
                    redirect,url_for,session)

app: Flask=Flask(__name__,static_url_path='/static')
app.secret_key="2323nana7272"
# Định tuyến hàm gọi ở trang gốc
@app.route("/")
def index():
    if 'username' in session:
        username=session['username']
        print(session)
        return (f"Hello, {username}! "
                f"<a href='/logout'>Logout</a>")
    return "Welcome! <a href='/login'>Login</a>"

@app.route("/logout")
def logout():
    session.pop('username',None)
    #remove username from the session
    return redirect(url_for("index"))

@app.route("/login", methods=['GET', 'POST'])
def login():
    # Khi nhận dữ liệu từ hành vi post, sau khi nhận dữ liệu # từ session sẽ gọi định tuyến sang trang index
    if request.method == 'POST':
        username = request.form['username']
        # Store 'username' in the session
        session['username'] = username
        return redirect(url_for('index'))
    # Trường hợp mặc định là vào trang login
    return render_template('login.html')
if __name__== '__main__':
    print(__name__)
    app.run(host='0.0.0.0', port=5000,debug=True)