from socketIO_client import SocketIO
import logging
from gpiozero import PWMLED

#logs schrijven
logging.basicConfig(level=logging.DEBUG)
#connectie maken via socketIO
socketIO = SocketIO('http://boiling-peak-90026.herokuapp.com', port=None)

#dictionary met alle leds
leds = [{'id' : 0, 'led' : PWMLED(17)}, {'id' : 1, 'led' : PWMLED(27)}, {'id' : 2, 'led' : PWMLED(22)}, {'id' : 3, 'led' : PWMLED(18)}, {'id' : 4, 'led' : PWMLED(23)}, {'id' : 5, 'led' : PWMLED(24)}]

#functie om een bepaalde led op een bepaalde value te zetten (value: 0-1)
def on_led_value(*args):
    data = args[0]
    value = float(data['value'])
    led = int(data['led'])
    
    for i in leds:                          #for loop om alle leds af te lopen
        if i['id'] == led:                  #bij de goede led:
            i['led'].value = value          #value toewijzen aan de led
    socketIO.emit('led_value', data)        #reactie naar de server sturen

socketIO.on('led_value', on_led_value)      #zodra het pakketje ontvangen is vanaf de server voer de functie on_led_value uit
socketIO.wait()                             #wachten op signaal
