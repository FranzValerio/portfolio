from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, join_room, leave_room

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# Dictionary to keep track of students' statuses
students_status = {}

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('join')
def on_join(data):
    username = data['username']
    students_status[username] = 'red'
    emit('update_status', students_status, broadcast=True)

@socketio.on('status_change')
def status_change(data):
    username = data['username']
    status = data['status']
    students_status[username] = status
    emit('update_status', students_status, broadcast=True)

@socketio.on('reset')
def reset():
    global students_status
    students_status = {key: 'red' for key in students_status.keys()}
    emit('update_status', students_status, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
