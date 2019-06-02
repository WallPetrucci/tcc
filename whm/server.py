import eventlet
import socketio

sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})


@sio.on('connect', namespace="/whm")
def connect(sid, environ):
    print('connect', sid)
    pass


@sio.on('message', namespace="/whm")
def message(sid, data):
    print('Servidor Diz: ', data)
    sio.emit('response_front', data)


@sio.on('disconnect', namespace="/whm")
def disconnect(sid):
    print('disconnect ', sid)


if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)
