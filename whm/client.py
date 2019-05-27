import socketio

sio = socketio.Client()


def send_message(data):
    while True:
        sio.emit('my message', data, namespace="/whm")


@sio.on('connect', namespace="/whm")
def on_connect():
    print('connection established')


@sio.on('disconnect', namespace="/whm")
def on_disconnect():
    print('disconnected from server')


sio.connect('http://localhost:5000')
sio.start_background_task(send_message, {'success': True})
sio.wait()
