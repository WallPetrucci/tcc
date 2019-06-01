from socketio import Client
from socketio.exceptions import ConnectionError as WHMConnectionError
import constants as const

sio = Client()
data_client = list()


@sio.on('connect', namespace="/whm")
def on_connect():
    print("Connect ON")


@sio.on('disconnect', namespace="/whm")
def on_disconnect():
    print("Connect OFF")


class SocketWhm():
    def __new__(self):
        sio.connect('http://{}:{}'.format(const.HOST, const.PORT))
        sio.start_background_task(self.send_message(self))
        sio.wait()

    def send_message(self):
        try:
            while True:
                sio.emit('my message', 'Salve', namespace="/whm")
        except WHMConnectionError as e:
            print("Disconnect Error: ", e)


SocketWhm()
