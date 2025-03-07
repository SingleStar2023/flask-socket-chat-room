from flask import Flask , render_template
from flask_socketio import SocketIO , emit

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
    
@socket.on("message")
def message(data):
    emit("message",data)

if __name__ == "__main__":
    socket.run(app)