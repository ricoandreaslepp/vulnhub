from functools import wraps
from flask import Flask, request, jsonify

# ctf{1-h0w_d1d_y0u_f1nd_th1s}

app = Flask(__name__)

def not_implemented(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        return jsonify({"message": "This endpoint is not implemented yet :/"}), 501
    return decorated_function

def auth_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        isadmin = request.cookies.get('isadmin')
        if not isadmin:
            return jsonify({"message": "Not authenticated!"}), 401
    return decorated_function

@app.route('/')
def index():
    return jsonify({"message": "TODO: This application is still under construction. NB! DO NOT USE IN PRODUCTION!"})

@app.route('/uploads')
@not_implemented
def uploads():
    pass

@app.route('/files')
@not_implemented
def rolled():
    pass

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=443)
