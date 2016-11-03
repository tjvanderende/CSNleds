from socketIO_client import SocketIO
import logging
logging.basicConfig(level=logging.DEBUG)
socketIO = SocketIO('http://boiling-peak-90026.herokuapp.com', port=None)

def on_led_value(*args):
    '''
    Wordt aangeroepen op basis van led_switch
    :param args: Data object { led: id van ledje, status: 1 = aan, 0 = uit;
    :return: None
    '''
    data = args[0]
    value = float(data['value'])
    socketIO.emit('led_value', data)


socketIO.on('led_value', on_led_value)
socketIO.wait()