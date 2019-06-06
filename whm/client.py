from socketio.exceptions import ConnectionError as WHMConnectionError
# from temp import MLX90614
from socketio import Client
from time import sleep
from json import dump, load
from datetime import datetime

import constants as const
import random


conn_status = False
status_message = False

sio = Client()
data_client = list()
# sensor_temperatura = MLX90614()


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


socketobj = SocketWhm(const.HOST_LOCAL, const.PORT_LOCAL)

try:
    while True:
        current_date = datetime.now()
        if status_message is True:
            sio.start_background_task(socketobj.send_message({'whm_id': "09123901823902",
                                                              'fc': random.randrange(60, 120),
                                                              'ox': random.randrange(96, 100),
                                                              'temp': random.randrange(35, 40),
                                                              'date': current_date.strftime('%d/%m/%Y %H:%M')}))
        else:
            escrever_json({'whm_id': "09123901823902", 'fc': 80, 'ox': 98, 'temp': 37,
                           'date': current_date.strftime('%d/%m/%Y %H:%M')})
        sleep(2)
except:
    print("Deu ruim")
