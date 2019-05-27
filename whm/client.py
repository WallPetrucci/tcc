import socketio

sio = socketio.Client()


@sio.on('connect')
def on_connect():
    print('connection established')


@sio.on('my message')
def on_message(data):
    print('message received with ', data)
    sio.emit('my response', {'response': 'my response'})


@sio.on('disconnect')
def on_disconnect():
    print('disconnected from server')


sio.connect('http://34.232.109.146:5000')

while 1:
    sio.emit('my message', {"message": "Connection TOPPER"}, namespace='/whm')
    sio.await()
