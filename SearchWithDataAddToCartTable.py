# from crypt import methods


import flask
from flask import Flask, render_template, request, session, redirect, url_for
import sqlite3
from pandas.core.interchange.dataframe_protocol import DataFrame


# from flask.globals import app_ctx

# Khởi tạo đối tượng app
app: Flask=Flask(__name__,static_url_path='/static')
app.secret_key="2323nana7272"
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
    return render_template("searchWithCssDataDBAddToCartTable.html", search_text="")
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
    products=load_data(search_text)
    return render_template("search.html",
                           search_text=search_text,products=products)
@app.route("/searchData",methods=['POST'])
def searchData():
    search_text=request.form["searchInput"]
    products=load_data_from_db(search_text)
    print(search_text)
    return render_template("searchWithCssDataDBAddToCartTable.html",
                           search_text=search_text,products=products)

@app.route("/cart/add",methods=['POST'])
def add_to_cart():
    # declare database to get price
    sqldbname= "db/website.db"
    # 2. Get the product and quantity from the form
    product_id=request.form["product_id"]
    quantity=int(request.form["quantity"])

    # 3 Get the product name and price from the database
    # or change the structure of shopping cart
    conn=sqlite3.connect(sqldbname)
    curs=conn.cursor()
    curs.execute(" SELECT model,price "
                 "FROM storages WHERE id= ?", (product_id,))
    # 3.1 Get one product
    product=curs.fetchone()
    conn.close()
    # 4. Create a dictionary for the product
    product_dict={
        "id":product_id,
        "name":product[0],
        "price":product[1],
        "quantity":quantity
    }
    # 5 get the cart from the session or create an empty list
    cart = session.get("cart", [])

    # 6 check if the product is already in the cart
    found =False
    for item in cart:
        if item["id"]==product_id:
            # 6.1 update the quantity of the existing product
            item["quantity"] += quantity
            found = True
            break
    if not found:
        # 6.2 add the new product to the cart
        cart.append(product_dict)
    #7. save the cart back to the session
    session["cart"]= cart
    #8 Print ot
    rows= len(cart)
    outputmessage=(f'"Product added to cart successfully"'
                   f"</br>Current: "+str(rows) + " products"
                   f'</br>Continue Search! <a href="/">Search Page</a>'
                   f'</br>View Shopping Cart! <a href="/view_cart">ViewCart</a>')
    #reutrn a success message
    return outputmessage
@app.route("/viewcart", methods=["POST"])
def viewcart():
    # get the cart from the session or create an empty list
    # render the cart.html template and pass the cart
    current_cart= []
    if "cart" in session:
        current_cart=session.get("cart",[])
        return render_template("cart.html",carts=current_cart)
@app.route("/view_cart")
def view_cart():
    # get the cart from the session or create an empty list
    # render the cart.html template and pass the cart
    current_cart= []
    if "cart" in session:
        current_cart=session.get("cart",[])
        return render_template("cart_update.html",carts=current_cart)
@app.route("/update_cart", methods=["POST"])
def update_cart():
    cart=session.get('cart',[])
    new_cart=[]
    for product in cart:
        product_id=str(product['id'])

        if f'quantity --product_id' in request.form:
            quantity= int(request.form[f'quantity--{product_id}'])
            #if the quantity is 0 or this is a delete field skip this product
            if quantity== 0 or f'delete--{product_id}' in request.form:
                continue
            #Otherwise, upate the quantity of the prodcut
            product['quantity']=quantity
        new_cart.append(product)

    session['cart']=new_cart
    return redirect(url_for('view_cart'))
# chạy web
if __name__== '__main__':
    print(__name__)
    app.run(host='0.0.0.0', port=5000,debug=True)