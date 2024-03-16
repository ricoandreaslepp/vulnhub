from flask import Flask, request, send_file

# ctf{1-s3cr3t_rout3}

app = Flask(__name__)

@app.route('/')
def index():
    return "TODO: This application is still under construction. NB! DO NOT USE IN PRODUCTION!\n"

@app.route('/app')
def return_file():
    # Path to the file you want to return
    file_path = request.args.get('file') or './app.py'
    return send_file(file_path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
