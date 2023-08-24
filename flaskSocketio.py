from flask import Flask, render_template,request
from flask_socketio import SocketIO, emit,send

app = Flask(__name__)
socketio = SocketIO(app)
#when we need debug
#socketio = SocketIO(logger=True, engineio_logger=True)

@app.route('/')
def index():
    return render_template('index.html')

# @socketio.on('user_message')
# def handle_my_custom_event(arg1, arg2, arg3):
#     print('received args: ' + arg1 + arg2 + arg3)
#     socketio.send(arg1)


@socketio.on('message')
def handle_message(data):
    print('received message: ' + data)
    send(data)

@socketio.on('json')
def handle_json(json):
    print('received json: ' + str(json))
    send(json, json=True)

@socketio.on('connect')
def test_connect():
    emit('user_message',  {'data':'Lets dance'})

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')

@socketio.on_error()        # Handles the default namespace
def error_handler(e):
    print(str(e))

@socketio.on_error('/chat') # handles the '/chat' namespace
def error_handler_chat(e):
    pass

@socketio.on_error_default  # handles all namespaces without an explicit error handler
def default_error_handler(e):
    print(request.event["message"]) # "my error event"
    print(request.event["args"])    # (data,)

if __name__ == '__main__':
    socketio.run(app)
    #socketio.run(app, host="0.0.0.0", debug=True, ssl_context=('cert.pem', 'key.pem'))