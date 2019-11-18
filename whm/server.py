import eventlet
import socketio
from requests import post


sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})


@sio.on('enter_room', namespace="/whm")
def enter_room(sid, room_name):
    print("ENTER ROOM")
    sio.enter_room(sid, room_name)
    print('connectINGGGGG', room_name)
    print("Enter Room")


@sio.on('connect', namespace="/whm")
def connect(sid, environ):
    print('connect', sid)


@sio.on('message_db', namespace="/whm")
def message_db(sid, data):
    print("DB DATA DB")
    print(data)
    post('http://localhost:5000' + '/api/resultsmetrics/', json=data)


@sio.on('message', namespace="/whm")
def message(sid, data):
    print("DB DATA ONLINE")
    print(data[0])

    if isinstance(data[0], dict):
        heart_fr = str(data[0].get('heart'))
        heart_ox = str(data[0].get('oximetry'))
        temp = "%.2f" % round(data[0].get('temperature'), 2)
        heart_bpm = 0
        try:
            if len(str(data[0].get('heart'))) > 4:
                fr_str = "{}.{}".format(heart_fr[0], heart_fr[1:3])
                print("FR>4: " + fr_str)
                heart_bpm = float(fr_str) * 60
            elif len(str(data[0].get('heart'))) > 2:
                fr_str = "0.{}".format(heart_fr[:2])
                heart_bpm = float(fr_str) * 60
                print("FR<4: " + fr_str)
            else:
                print("Sem medidor")

            if len(heart_ox) > 4:
                data[0].update({'oximetry': 100})
            elif len(heart_ox) > 3:
                data[0].update({'oximetry': heart_ox[:2]})
            else:
                data[0].update({'oximetry': 0})

            data[0].update({'heart': round(heart_bpm)})
            data[0].update({'temperature': temp})

        except Exception as e:
            print("Error Sensors not measure: " + e)

    sio.emit('response_front', data)


@sio.on('disconnect', namespace="/whm")
def disconnect(sid):
    print('disconnect ', sid)


if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5050)), app)
