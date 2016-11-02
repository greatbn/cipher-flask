#coding: utf-8
from flask import Flask, render_template, redirect, url_for, request, jsonify, abort, make_response
from flask_bootstrap import Bootstrap
app = Flask(__name__)
Bootstrap(app)
methods = [
    {
        "id": 1,
        "name": "affine",
        "description": "Mat ma affine",
    },
    {
        "id": 2,
        "name": "inverse",
        "description": "Nghich dao cua mot so"
    },
    {
        "id": 3,
        "name": "caesar",
        "description": "Mat ma caesar shift"
    },
    {
        "id": 4,
        "name": "vigenere",
        "description": "Mat ma vigenere"
    }
]
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error':'Not Found'}))
@app.errorhandler(400)
def error_in_data(error):
    return make_response(jsonify({'error':'Your data not true'}))
@app.route("/v1.0/methods", methods=['GET'])
def get_methods():
    return jsonify({'methods': methods})

@app.route("/v1.0/methods/<int:method_id>", methods=['GET','POST'])
def get_method(method_id):
    method = [method for method in methods if method['id'] == method_id ]
    if len(method):
        return jsonify({'method':method})
    else:
        abort(404)
@app.route("/v1.0/encrypt/<int:method_id>", methods=['POST'])
def encrypt(method_id):
    method = [method for method in methods if method['id'] == method_id ]
    if len(method):
        if method_id == 1:
            if not 'a' in request.json or not 'b' in request.json or not 'plain_text' in request.json:
                abort(400)
            else:
                from ciphers import affine
                aff = affine.AffineCipher(a=request.json['a'],
                                          b=request.json['b'],
                                          text=request.json['plain_text'])
                result ={
                    'method': method[0]['name'],
                    'a': request.json['a'],
                    'b': request.json['b'],
                    'plain_text': request.json['plain_text'],
                    'cipher_text': aff._encrypt()
                }
                print result
                return jsonify({'result': result})
        elif method_id == 2:
            if not 'moduloNumber' in request.json or not 'inverseNumber' in request.json:
                abort(400)
            else:
                from ciphers import inverse
                inv = inverse.InverseCalculate(moduloNumber=request.json['moduloNumber'],
                                               inverseNumber=request.json['inverseNumber'])
                result = {
                    'method': method[0]['name'],
                    'moduloNumber': request.json['moduloNumber'],
                    'inverseNumber': request.json['inverseNumber'],
                    'result': inv._inverse()
                }
                return jsonify({'result': result})
        elif method_id == 3:
            if not 'key' in request.json or not 'plain_text' in request.json:
                abort(400)
            else:
                from ciphers import caesar
                ca = caesar.CaesarCipher(k=request.json['key'],
                                         text=request.json['plain_text'])

                result = {
                    'method': method[0]['name'],
                    'key': request.json['key'],
                    'plain_text': request.json['plain_text'],
                    'cipher_text': ca._encrypt()
                }
                return jsonify({'result': result})
        elif method_id == 4:
            if not 'key' in request.json or not 'plain_text' in request.json:
                abort(400)
            else:
                from ciphers import vigenere
                vi = vigenere.VigenereCipher(key=request.json['key'],
                                             text=request.json['plain_text'])
                result = {
                    'method': method[0]['name'],
                    'key': request.json['key'],
                    'plain_text': request.json['plain_text'],
                    'cipher_text': vi._encrypt()
                }
                return jsonify({'result': result})
@app.route("/v1.0/decrypt/<int:method_id>", methods=['POST'])
def decrypt(method_id):
    method = [method for method in methods if method['id'] == method_id ]
    if len(method):
        if method_id == 1:
            if not 'a' in request.json or not 'b' in request.json or not 'cipher_text' in request.json:
                abort(400)
            else:
                from ciphers import affine
                aff = affine.AffineCipher(a=request.json['a'],
                                          b=request.json['b'],
                                          text=request.json['cipher_text'])
                result ={
                    'method': method[0]['name'],
                    'a': request.json['a'],
                    'b': request.json['b'],
                    'cipher_text': request.json['cipher_text'],
                    'plain_text': aff._decrypt()
                }
                return jsonify({'result': result})
        elif method_id == 2:
            if not 'moduloNumber' in request.json or not 'inverseNumber' in request.json:
                abort(400)
            else:
                from ciphers import inverse
                inv = inverse.InverseCalculate(moduloNumber=request.json['moduloNumber'],
                                               inverseNumber=request.json['inverseNumber'])
                result_inv = inv._inverse()
                if result_inv is False:
                    result_inv = 'Nhập chưa đúng'
                result = {
                    'method': method[0]['name'],
                    'moduloNumber': request.json['moduloNumber'],
                    'inverseNumber': request.json['inverseNumber'],
                    'result': result_inv
                }
                return jsonify({'result': result})
        elif method_id == 3:
            if not 'key' in request.json or not 'cipher_text' in request.json:
                abort(400)
            else:
                from ciphers import caesar
                ca = caesar.CaesarCipher(k=request.json['key'],
                                         text=request.json['cipher_text'])

                result = {
                    'method': method[0]['name'],
                    'key': request.json['key'],
                    'cipher_text': request.json['cipher_text'],
                    'plain_text': ca._decrypt()
                }
                return jsonify({'result': result})
        elif method_id == 4:
            if not 'key' in request.json or not 'cipher_text' in request.json:
                abort(400)
            else:
                from ciphers import vigenere
                vi = vigenere.VigenereCipher(key=request.json['key'],
                                             text=request.json['cipher_text'])
                result = {
                    'method': method[0]['name'],
                    'key': request.json['key'],
                    'cipher_text': request.json['cipher_text'],
                    'plain_text': vi._encrypt()
                }
                return jsonify({'result': result})

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/affine", methods = ["GET", "POST"])
def affine():
    if request.method == "GET":
        return render_template("affine.html")
@app.route("/inverse")
def inverse():
    return render_template("inverse.html")
@app.route("/caesar")
def caesar():
    return render_template("caesar.html")
if __name__ == '__main__':
    app.run(debug=True)
