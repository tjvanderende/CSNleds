from socketIO_client import SocketIO
import logging
logging.basicConfig(level=logging.DEBUG)

def on_bbb_response(*args):
    print('on_bbb_response', args)

def on_aaa_response(*args):
    print('on_aaa_response', args)

with SocketIO('http://boiling-peak-90026.herokuapp.com', port=None) as socketIO:
    socketIO.emit('lighton', 'new-tx')
    socketIO.on('led', on_aaa_response)
    socketIO.wait()