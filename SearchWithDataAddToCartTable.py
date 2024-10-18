# from crypt import methods
from itertools import product

import flask
from flask import Flask, render_template, request
import sqlite3
from pandas.core.interchange.dataframe_protocol import DataFrame

# from flask.globals import app_ctx

# Khởi tạo đối tượng app
app: Flask=Flask(__name__,static_url_path='/static')
sqldbname="db/website.db"
# Định tuyến hàm gọi ở trang gốc
@app.route("/")
def index():
    conn=sqlite3.connect(sqldbname)
    cursor=conn.cursor()
    sqlcommand="SELECT * from STORAGES"
    cursor.execute(sqlcommand)
    data=cursor.fetchall()
    conn.close()
    # return render_template("index.html",table=data)
    return render_template("searchWithCssDataDB.html", search_text="")
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
def load_data_from_db(search_text:str):
    sqldbname="db/website.db"
    if search_text !="":
        conn=sqlite3.connect(sqldbname)
        cursor=conn.cursor()
        sqlcommand="SELECT * FROM STORAGES WHERE model like '%"+search_text+"%'"
        sqlcommand=sqlcommand+ "or brand like '%"+search_text+"%'"
        sqlcommand=sqlcommand+ "or details like '%" +search_text+"%'"
        cursor.execute(sqlcommand)
        data=cursor.fetchall()
        conn.close()
        return data

@app.route("/search",methods=['POST'])
def search():
    search_text=request.form["searchInput"]
    html_table=load_data(search_text)
    return render_template("search.html",
                           search_text=search_text,table=html_table)
@app.route("/searchData",methods=['POST'])
def searchData():
    search_text=request.form["searchInput"]
    html_table=load_data_from_db(search_text)
    print(search_text)
    print(html_table)
    return render_template("searchWithCssDataDB.html",
                           search_text=search_text,table=html_table)
@app.route("/cart/add",methods=['POST'])
def add_to_cart():
    # declare database to get price
    sqldbname= "db/website.db"
    # 2. Get the product and quantity from the form
    product_id=request.form["product_id"]
    # chạy web
if __name__== '__main__':
    print(__name__)
    app.run(host='0.0.0.0', port=5000,debug=True)