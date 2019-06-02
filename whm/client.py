from socketio import Client
from socketio.exceptions import ConnectionError as WHMConnectionError
from time import sleep
from os import remove
from threading import Thread
from json import dump, load
from datetime import datetime
import constants as const


conn_status = False
status_message = False

sio = Client()
data_client = list()


class ThreadWhm(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self, conn):
        if conn:
            print("Run True")
            remove('sensor.json')
        while conn is not True:
            data_client.append


whmcontrol = ThreadWhm()


# Methods for Controller sensor when connect off #
def escrever_json(res):
    with open('sensor.json', 'a') as f:
        dump(res, f, separators=(', ', ': '))


def ler_json():
    with open('sensor.json') as f:
        data = load(f)
    return data


# Callbacks SocketIO
@sio.on('connect', namespace="/whm")
def on_connect():
    print('CONNECT ON')
    global conn_status, status_message
    conn_status = True
    status_message = True


@sio.on('disconnect', namespace="/whm")
def on_disconnect():
    print("CONNECT OFF")
    global conn_status, status_message
    conn_status = False
    status_message = False


class SocketWhm():
    def __init__(self, host, port):
        sio.connect('http://{}:{}'.format(host, port))

    def send_message(self, sensor_data):
        try:
            print('Chega aqui')
            data_client.append(sensor_data)
            sio.emit('message', data_client, namespace="/whm")
            data_client.clear()
        except WHMConnectionError as e:
            print("Disconnect Error: ", e)


socketobj = SocketWhm(const.HOST_LOCAL, const.PORT)

try:
    while True:
        current_date = datetime.now()
        if status_message is True:
            sio.start_background_task(socketobj.send_message({'whm_id': "09123901823902",
                                                              'fc': 75, 'ox': 100, 'temp': 36.6,
                                                              'date': current_date.strftime('%d/%m/%Y %H:%M')}))
        else:
            escrever_json({'whm_id': "09123901823902", 'fc': 80, 'ox': 98, 'temp': 37,
                           'date': current_date.strftime('%d/%m/%Y %H:%M')})
        sleep(2)
except:
    print("Deu ruim")
