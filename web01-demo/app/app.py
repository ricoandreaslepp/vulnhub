from flask import Flask, send_file, request

# ctf{1-s3cr3t_rout3}

app = Flask(__name__)

@app.route('/')
def index():
    return "TODO: This application is still under construction. NB! DO NOT USE IN PRODUCTION!\n"

@app.route('/src/app.py')
def return_file():
    # Path to the file you want to return
    file_path = request.args.get('file') or './app.py'
    print(file_path)
    return send_file(file_path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
