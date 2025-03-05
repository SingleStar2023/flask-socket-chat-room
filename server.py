from flask import Flask
from flask_socketio import SocketIO , emit

app = Flask("application")
socket = SocketIO(app)

@app.route("/")
def home():
    return "This is the server side !!"

@socket.on("connect")
def cl_con():
    print("A new client connected !!")

@socket.on("disconnect")
def cl_dis():
    print("A client disconnected !!")
    
@socket.on("message")
def message(data):
    emit("message",data)

if __name__ == "__main__":
    socket.run(app)