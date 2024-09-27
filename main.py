# from crypt import methods

import flask
from flask import Flask, render_template, request
from pandas.core.interchange.dataframe_protocol import DataFrame

# from flask.globals import app_ctx

# Khởi tạo đối tượng app
app: Flask=Flask(__name__,static_url_path='/static')

# Định tuyến hàm gọi ở trang gốc
@app.route("/")
def index():
    return render_template("search.html", search_text="")
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
    html_data=df.to_html(classes='data', escape=False)
    return render_template("page_03_Table.html",table=html_data)
def load_data():
    import pandas as pd
    df=pd.read_csv("gradedata.csv")
    #chỉ hiện 5 bản ghi
    html_table=df.iloc[:5].to_html(classes='data',escape=False)
    return html_table
def load_data(search_text:str):
    import pandas as pd
    df=pd.read_csv('gradedata.csv')
    dfX=df
    if search_text !="":
        dfX=df[(df["fname"]==search_text) |
             (df["lname"]==search_text)]
        print(dfX)
    html_table=dfX.to_html(classes='data',escape=False)
    return html_table

# @app.route("/loadPage04")
# def loadPage04():
#     html_table=load_data()
#     print(html_table)
#     print(type(html_table))
#     return render_template('page_04_Table.html',
#                            tables=html_table,
#                            titles=html_table.columns.values)
@app.route("/search",methods=['POST'])
def search():
    search_text=request.form['searchInput']
    html_table=load_data(search_text)
    return render_template("search.html",
                           search_text=search_text,table=html_table)
# chạy web
if __name__== '__main__':
    print(__name__)
    app.run(host='0.0.0.0', port=5000)