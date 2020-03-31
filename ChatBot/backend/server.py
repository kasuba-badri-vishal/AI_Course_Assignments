# from flask import Flask
from flask import *
from chat import *
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    print(request)
    return 'Hello, World!'

@app.route('/', methods=['POST'])
def func():
    print(request)
    return resp(request.form['msg'])

if __name__ == '__main__':
    # app.run(host='0.0.0.0')
    app.run(host='192.168.43.63')
    # app.run()