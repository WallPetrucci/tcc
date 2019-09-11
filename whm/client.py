from socketio.exceptions import ConnectionError as WHMConnectionError
# from temp import MLX90614
from socketio import Client
from time import sleep
from datetime import datetime
from uuid import getnode as get_mac
import constants as const
import random
import sqlite3


# Objects and Variables for using in Main

sio = Client()
# sensor_temperatura = MLX90614()
status_message = False
conn_status = False
mac = get_mac()
conn_local = sqlite3.connect(const.DB_LOCAL)

# Create table
conn_local.execute('''CREATE TABLE IF NOT EXISTS `whm_local`
             (date text, trans text, symbol text, qty real, price real)''')


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
        data_client = []
        data_client.append(sensor_data)
        sio.emit('message', data_client, namespace="/whm")
        data_client.clear()
    except WHMConnectionError as e:
        print("Disconnect Error: ", e)


def send_message_db(sensor_data):
    try:
        data_client = []
        data_client.append(sensor_data)
        sio.emit('message_db', data_client, namespace="/whm")
        data_client.clear()
    except WHMConnectionError as e:
        print("Disconnect Error: ", e)

# WHM - Application


if __name__ == '__main__':
    while True:
        sleep(2)
        current_date = datetime.now()

        if conn_status is not True:
            connect_socket(const.HOST_LOCAL, const.PORT_LOCAL)

        if status_message is True:

            sio.start_background_task(send_message({'User_idUser': 1,
                                                    'heart': random.randrange(60, 120),
                                                    'oximetry': random.randrange(96, 100),
                                                    'temperature': random.randrange(35, 40),
                                                    'date_results': current_date.strftime("%Y-%m-%d %H:%M:%S")}))
            sio.start_background_task(send_message_db({'User_idUser': 1,
                                                       'heart': random.randrange(60, 120),
                                                       'oximetry': random.randrange(96, 100),
                                                       'temperature': random.randrange(35, 40),
                                                       'date_results': current_date.strftime("%Y-%m-%d %H:%M:%S")}))
        else:

            print("Save in Database Local: ", {'whm_id': mac,
                                               'fc': random.randrange(60, 120),
                                               'ox': random.randrange(96, 100),
                                               'temp': random.randrange(35, 40),
                                               'date': current_date.strftime('%Y-%m-%d %H:%M')})
