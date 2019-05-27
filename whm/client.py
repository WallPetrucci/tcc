import socketio

sio = socketio.Client()


def send_message(data):
    while True:
        sio.emit('my response', data, namespace="/whm")


@sio.on('connect')
def on_connect():
    print('connection established')


@sio.on('disconnect')
def on_disconnect():
    print('disconnected from server')


sio.connect('http://34.232.109.146:5000')
sio.start_background_task(send_message, {'success': True})
sio.wait()
