from flask import render_template
from app import app
from models.order_list import order_list

@app.route("/orders")
def index():
    return render_template("index.html", title = "Home", orders = order_list)

@app.route("/orders/<index>")
def index2(index):
    single_order = order_list[int(index)]
    return render_template("order.html", order = single_order)
