from socketio.exceptions import ConnectionError as WHMConnectionError
from temp import MLX90614
from socketio import Client
from time import sleep
from datetime import datetime
from uuid import getnode as get_mac
import constants as const
import random


# Objects and Variables for using in Main

sio = Client()
data_client = []
sensor_temperatura = MLX90614()
status_message = False
conn_status = False
mac = get_mac()


# Callbacks SocketIO

@sio.on('connect', namespace="/whm")
def on_connect():
    global status_message, conn_status
    print('CONNECT ON')
    status_message = True
    conn_status = True


@sio.on('disconnect', namespace="/whm")
def on_disconnect():
    global status_message
    print("CONNECT OFF")
    status_message = False


# Functions call socket.IO

def connect_socket(host=const.HOST_LOCAL, port=const.PORT_LOCAL):
    sio.connect('http://{}:{}'.format(host, port))


def send_message(sensor_data):
    try:
        print('Send Message for Server')
        data_client.append(sensor_data)
        sio.emit('message', data_client, namespace="/whm")
        data_client.clear()
    except WHMConnectionError as e:
        print("Disconnect Error: ", e)


# WHM - Application

if __name__ == '__main__':
    while True:
        sleep(2)
        current_date = datetime.now()
        if conn_status is not True:
            connect_socket()
        if status_message is True:
            sio.start_background_task(send_message({'whm_id': mac,
                                                    'fc': random.randrange(60, 120),
                                                    'ox': random.randrange(96, 100),
                                                    'temp': sensor_temperatura.get_obj_temp(),
                                                    'date': current_date.strftime('%d/%m/%Y %H:%M')}))
        else:
            print("Save in Database Local: ", {'whm_id': mac,
                                               'fc': random.randrange(60, 120),
                                               'ox': random.randrange(96, 100),
                                               'temp': sensor_temperatura.get_obj_temp(),
                                               'date': current_date.strftime('%d/%m/%Y %H:%M')})

