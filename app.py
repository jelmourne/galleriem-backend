import json
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/Product", methods=["GET"])
def getProducts():
    return "dsadsa"


@app.route("/Product/<id>", methods=["GET"])
def getProduct(id):
    return id


if __name__ == "__main__":
    app.run()
