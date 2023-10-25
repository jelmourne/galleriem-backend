import os
from flask import Flask, jsonify, request
from models import db
from models import *

os.environ["FLASK_ENV"] = "development"
app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    basedir, "database.db"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


@app.route("/admin/add", methods=["GET"])
def add_admin():
    new_admin = Administrator(adminUsername="adminUser", password="securePassword123")
    db.session.add(new_admin)
    db.session.commit()
    return jsonify(message="New admin added"), 201


@app.route("/admin/login", methods=["POST"])
@app.route("/add/product", methods=["GET"])
def add_product():
    new_product = Product(
        productType="Shirt",
        productDescription="A cool shirt for summer.",
        productSize=["S", "M", "L", "XL"],
        productColor=["Red", "Blue", "Green"],
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify(message="New product added"), 201


@app.route("/add/customer", methods=["GET"])
def add_customer():
    new_customer = Customer()
    db.session.add(new_customer)
    db.session.commit()
    return jsonify(message="New customer added"), 201


@app.route("/add/order", methods=["GET"])
def add_order():
    import datetime

    new_order = Order(
        customerId=1,
        customerName="John Doe",
        address="123 Elm St, Springfield",
        email="john.doe@example.com",
        creditCardInfo="1111-2222-3333-4444",
        shippingInfo="123 Elm St, Springfield",
        orderDate=datetime.date.today(),
        status="Processing",
        total=99.99,
    )
    db.session.add(new_order)
    db.session.commit()
    return jsonify(message="New order added"), 201


@app.route("/add/cart", methods=["GET"])
def add_cart():
    new_cart = ShoppingCart(total=49.99, customerId=1, itemID=1)
    db.session.add(new_cart)
    db.session.commit()
    return jsonify(message="New cart added"), 201


@app.route("/add/cart-item", methods=["GET"])
def add_cart_item():
    new_cart_item = ShoppingCartItem(
        refProductID=1,
        cartID=1,
        quantity=2,
        customSize="L",
        customColor="Blue",
        customDesign="Design123",
    )
    db.session.add(new_cart_item)
    db.session.commit()
    return jsonify(message="New cart item added"), 201


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
