from socketio.exceptions import ConnectionError as WHMConnectionError
# from temp import MLX90614
# from max30100 import MAX30100, MODE_SPO2
from socketio import Client
from time import sleep
from datetime import datetime
from uuid import getnode as get_mac
import constants as const
import sqlite3
import json
from random import randrange


# Objects and Variables for using in Main
sio = Client()

# sensor_temperatura = MLX90614()
# sensor_fc_ox = MAX30100()
# sensor_fc_ox


status_message = False
conn_status = False


mac = get_mac()
conn_local = sqlite3.connect(const.DB_LOCAL)
c = conn_local.cursor()

# Create table
conn_local.execute('''CREATE TABLE IF NOT EXISTS `whm_local`
             (data_whm text)''')


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
    try:
        sio.connect('http://{}:{}'.format(host, port))
    except WHMConnectionError:
        pass

def send_message_local(sensor_data):
    try:
        sio.emit('message_local', sensor_data, namespace="/whm")
    except WHMConnectionError as e:
        print("Disconnect Error: ", e)


def send_message_db(sensor_data):
    try:
        sio.emit('message_db', sensor_data, namespace="/whm")
    except WHMConnectionError as e:
        print("Disconnect Error: ", e)


# WHM - Application
if __name__ == '__main__':
    while True:
        # sleep(2)
        current_date = datetime.now()

        # Controll Buffer Sensor
        # for i in range(1, 1000):
        #     sensor_fc_ox.read_sensor()

        if conn_status is not True:
            connect_socket(const.HOST_LOCAL, const.PORT_LOCAL)

        if status_message is True:

            c.execute('SELECT * FROM whm_local')
            data_db_local = c.fetchall()

            if len(data_db_local):
                print("Send Database Local for Server")
                sio.start_background_task(send_message_db(data_db_local))
                c.execute("DELETE FROM whm_local")

            else:
                print("Send Data Online DB and Real Time")
                sio.start_background_task(send_message_db([{'whm_id': mac,
                                                            'heart': randrange(50, 160),
                                                            'oximetry': randrange(80, 100),
                                                            'temperature': randrange(35, 40),
                                                            'date_results': current_date.strftime("%Y-%m-%d %H:%M:%S")}]))

                sio.start_background_task(send_message_local([{'whm_id': mac,
                                                               'heart': randrange(50, 160),
                                                               'oximetry': randrange(80, 100),
                                                               'temperature': randrange(35, 40),
                                                               'date_results': current_date.strftime("%Y-%m-%d %H:%M:%S")}]))
        else:

            print("Save in Database Local")
            conn_local.execute(''' INSERT INTO whm_local VALUES(?)''', (json.dumps({'whm_id': mac,
                                                                                    'heart': randrange(50, 160),
                                                                                    'oximetry': randrange(80, 100),
                                                                                    'temperature': randrange(35, 40),
                                                                                    'date_results': current_date.strftime("%Y-%m-%d %H:%M:%S")}),))
            conn_local.commit()
