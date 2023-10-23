import os
from flask import Flask, jsonify, request
from models import db
from models import *
os.environ["FLASK_ENV"] = "development"
app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route("/", methods=["GET"])
def welcome():
    new_customer = Customer(
    customerName="test Doe",
    address="Toronto Street",
    email="test@test.com",
    creditCardInfo="1111-1111-1111-3456",
    shippingInfo="456 111 Street"
)
    # Add the new customer to the session and commit the transaction
    db.session.add(new_customer)
    db.session.commit()

    return f"Created Customer: {new_customer.customerName}"

@app.route("/Product", methods=["GET"])
def getProducts():
    return "dsadsa"

@app.route("/Product/<id>", methods=["GET"])
def getProduct(id):
    return id

if __name__ == "__main__":
    with app.app_context():  
        db.create_all()  
    app.run(debug=True)
