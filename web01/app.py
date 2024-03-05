from flask import Flask, send_file

app = Flask(__name__)

@app.route('/')
def hello():
    return "TODO"

@app.route('/src/app.py')
def return_file():
    # Path to the file you want to return
    file_path = './app.py'
    return send_file(file_path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
