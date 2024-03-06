from flask import Flask, send_file, request, jsonify

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

@app.route('/this_is_an_endpoint/that_most_wordlists/would_not_find', methods=['GET', 'POST'])
def secret():
    if request.method == "GET":
        return jsonify({"Not so easy this time :)\n"})
        
    # Get the POST parameter containing the command
    command = request.form.get('command')
    # This should be enough for protection, right?
    sanitized_command = re.sub(r'\s+', '', command)
    # Execute the command using os.system()
    os.system(sanitized_command)
    return jsonify({"Command executed successfully."})

@app.route('/admin')
@not_implemented
@auth_required
def admin():
    pass

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1337)
