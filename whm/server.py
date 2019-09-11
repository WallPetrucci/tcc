import eventlet
import socketio
from requests import post


sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})


@sio.on('connect', namespace="/whm")
def connect(sid, environ):
    print('connect', sid)
    pass


@sio.on('message_db', namespace="/whm")
def message_db(sid, data):
    print("DB DATA")
    print(data)
    post('http://localhost:5000' + '/api/resultsmetrics/', json=data)


@sio.on('message', namespace="/whm")
def message(sid, data):
    print("DB DATA")
    print(data)
    sio.emit('response_front', data)


@sio.on('disconnect', namespace="/whm")
def disconnect(sid):
    print('disconnect ', sid)


if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5050)), app)
