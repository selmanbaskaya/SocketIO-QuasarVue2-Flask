from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO, emit

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")


@app.route('/', methods=["GET"])
@app.route('/index', methods=["GET"])
def index():
    return "Welcome to TwinAPI by SIMULARGE INC"


@socketio.on('my-url')
def myUrl(url):
    print("URL IS HERE: ", url)
    emit('response', {'msg': "socketio operations is successfully!"})
