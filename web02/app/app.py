from functools import wraps
from flask import Flask, request, send_file, jsonify
import os
import re


# ctf{1-h0w_d1d_y0u_f1nd_th1s}

app = Flask(__name__)

def not_implemented(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        return jsonify({"message": "This endpoint is not implemented yet :/"}), 501
    return decorated_function

@app.route('/')
def index():
    return jsonify({"message": "TODO: This application is still under construction. NB! DO NOT USE IN PRODUCTION!"})

@app.route('/uploads')
@not_implemented
def uploads():
    pass

@app.route('/files', methods=['GET', 'POST'])
def files():
    if request.method == "GET":
        return jsonify({"message": "Please use POST requests with 'filename=<file>' in the request body, GET is not implemented yet!"})
    
    file_path = request.form.get('filename')
    return send_file(file_path)

@app.route('/admin')
@not_implemented
def admin():
    pass

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
