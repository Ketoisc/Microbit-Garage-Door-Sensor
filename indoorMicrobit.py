# updated microbit with 3 garage doors
from microbit import *
import radio
import utime
radio.config(group=1)
radio.on()
present = utime.ticks_ms()


while True:
    defaultLED = Image("60606:60606:60606:60606:60606:")    # all garages are open
    door1LED = Image("00006:00006:00006:00006:00006:")      # far right door
    door2LED = Image("00600:00600:00600:00600:00600:")      # middle door
    door3LED = Image("60000:60000:60000:60000:60000:")      # emily's door, far left
    door12LED = Image("00606:00606:00606:00606:00606:")     # mum and dad
    door13LED = Image("60006:60006:60006:60006:60006:")     # emily and dad
    door23LED = Image("60600:60600:60600:60600:60600:")     # emily and mum
    X = Image("60006:06060:00600:06060:60006:")

    if button_a.is_pressed():
        radio.send('Door1')
        sleep(200)

    if button_b.is_pressed():
        radio.send('Door2')
        sleep(200)

    response = radio.receive()
    if response == 'CLOSE,CLOSE,CLOSE':
        display.clear()
    elif response == 'OPEN,CLOSE,CLOSE':
        display.show(door1LED)
    elif response == 'CLOSE,OPEN,CLOSE':
        display.show(door2LED)
    elif response == 'CLOSE,CLOSE,OPEN':
        display.show(door3LED)
    elif response == 'OPEN,OPEN,CLOSE':
        display.show(door12LED)
    elif response == 'OPEN,CLOSE,OPEN':
        display.show(door13LED)
    elif response == 'CLOSE,OPEN,OPEN':
        display.show(door23LED)
    elif response == 'PING':
        present = utime.ticks_ms()

    if utime.ticks_diff(utime.ticks_ms(), present) > 300000:
        display.show(X)
