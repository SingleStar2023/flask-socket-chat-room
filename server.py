import eventlet
eventlet.monkey_patch()

from flask import Flask , render_template
from flask_socketio import SocketIO , emit , join_room , leave_room

app = Flask("application",template_folder="",static_folder="")
socket = SocketIO(app,async_mode="eventlet")

@app.route("/")
def home():
    return render_template("index.html")

@socket.on("connect")
def cl_con():
    print("A new client connected !!")

@socket.on("disconnect")
def cl_dis():
    print("A client disconnected !!")

@socket.on("join")
def join_to(data):
    join_room(data["room"])

@socket.on("leave")
def leave_to(data):
    leave_room(data["room"])
    
@socket.on("message")
def message(data):
    emit("message",data["message"],to=data["room"])

if __name__ == "__main__":
    socket.run(app)