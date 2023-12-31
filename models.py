from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import PickleType

db = SQLAlchemy()

class Administrator(db.Model):
    adminUsername = db.Column(db.String(255), primary_key=True)
    password = db.Column(db.String(255), nullable=False)

class Product(db.Model):
    productId = db.Column(db.Integer, primary_key=True)
    productType = db.Column(db.String(255))
    productDescription = db.Column(db.Text)
    productSize = db.Column(PickleType)  # List of sizes
    productColor = db.Column(PickleType)  # List of colors

class Customer(db.Model):
    customerId = db.Column(db.Integer, primary_key=True)
    def __repr__(self):
        return f'<Customer {self.customerName} - Email: {self.email}>'

class Orders(db.Model):
    orderId = db.Column(db.Integer, primary_key=True)
    customerId = db.Column(db.Integer, db.ForeignKey('customer.customerId'))
    customerName = db.Column(db.String(255), nullable=False)
    address = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    creditCardInfo = db.Column(db.String(255))
    shippingInfo = db.Column(db.Text)
    orderDate = db.Column(db.Date)
    status = db.Column(db.String(50))
    total = db.Column(db.Float)

class ShoppingCart(db.Model):
    cartID = db.Column(db.Integer, primary_key=True)
    total = db.Column(db.Float)
    customerId = db.Column(db.Integer, db.ForeignKey('customer.customerId'))
    itemID = db.Column(db.Integer, db.ForeignKey('shopping_cart_item.itemID'))

class ShoppingCartItem(db.Model):
    itemID = db.Column(db.Integer, primary_key=True)
    refProductID = db.Column(db.Integer, db.ForeignKey('product.productId'))
    cartID = db.Column(db.Integer, db.ForeignKey('shopping_cart.cartID'))
    quantity = db.Column(db.Integer, nullable=False)
    customSize = db.Column(db.String(50))
    customColor = db.Column(db.String(50))
    customDesign = db.Column(db.Text)

def init_app(app):
    db.init_app(app)