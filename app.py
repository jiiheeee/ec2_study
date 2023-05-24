from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/user')
def hello_world():
    return '나는그루트다'

@app.route('/user_info')
def hello_world():
    return '나는 그루트아님'
if __name__ == '__main__':
    app.run()
