from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app = Flask(__name__)

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:531998@localhost/audio-2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init db
db = SQLAlchemy(app)

# Init ma
ma = Marshmallow(app)

# Product Class/Model


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200))
    price = db.Column(db.Integer)
    qty = db.Column(db.Integer)

    def __init__(self, name, description, price, qty):
        self.name = name
        self.description = description
        self.price = price
        self.qty = qty


# Product Schema
class ProductSchema(ma.Schema):
    class Meta:  # To Show which field
        fields = ('id', 'name', 'description', 'price', 'qty')


# Init Schema
product_schema = ProductSchema()  # one Product
products_schema = ProductSchema(many=True)  # Many Products

# Add a product


@app.route('/product', methods=['POST'])
def add_product():
    name = request.json['name']
    description = request.json['description']
    qty = request.json['qty']
    price = request.json['price']

    new_procduct = Product(name, description, qty, price)
    db.session.add(new_procduct)
    db.session.commit()

    return product_schema.jsonify(new_procduct)  # single product

# Get All Products


@app.route('/product', methods=['GET'])
def get_products():
    all_products = Product.query.all()
    result = products_schema.dump(all_products)  # many product
    # A dictionary/object have a property called data which iclude list of products
    return jsonify(result)

# Get Single product


@app.route('/product/<id>', methods=['GET'])
def get_product(id):
    product = Product.query.get(id)
    # A dictionary/object have a property called data which iclude list of products
    return product_schema.jsonify(product)

# Update a Product


@app.route('/product/<id>', methods=['PUT'])
def update_product(id):

    product = Product.query.get(id)

    name = request.json['name']
    description = request.json['description']
    qty = request.json['qty']
    price = request.json['price']

    product.name = name
    product.description = description
    product.price = price
    product.qty = qty

    new_procduct = Product(name, description, qty, price)
    db.session.commit()

    return product_schema.jsonify(new_procduct)  # single product

    # Example
    # @app.route('/', methods=['GET'])
    # def get():
    #     return jsonify({'msg': 'Hello world'})

# Delete


# @app.route('/product/<id>', methods=['DELETE'])
# def delete_product(id):
#     product = Product.query.get(id)
#     db.session.delete(product)
#     db.session.commit()
#     # A dictionary/object have a property called data which iclude list of products
#     return product_schema.jsonify(product)


if __name__ == '__main__':
    app.run(debug=True)
