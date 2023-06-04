from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '쓸다리없는거 다 지움ㅋ'

@app.route('/user')
def user():
    return '내가 바로 유저다.'

if __name__ == '__main__':
    app.run(host="0.0.0.0")
