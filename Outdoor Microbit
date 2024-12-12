from microbit import *
import radio
import utime
radio.config(group=1)
radio.on()
display.enable(False)
openn = 0
closed = 1
# open now = 1 or != 0
# closed now = 0

# this program sends the state of the garage doors to the indoor unit
# to indicate if they're open or closed.
# the format of the data it sends is;
# "[door1 state],[door2 state],[door3 state]"
#
# OPEN = door is open
# CLOSE = door is closed
# eg.
# "CLOSE,CLOSE,CLOSE" - all doors are closed
# "CLOSE,CLOSE,OPEN" - door1 is closed, door2 is closed, door3 is open
# "CLOSE,OPEN,OPEN" - door1 is closed, door2 is open, door3 is open

# checks if the doors open or closed and only send a signal when something changes.
# this is so it doesn't 'talk' constantly.


while True:
    heartbeat = 3000
    startTime = utime.ticks_ms()
    currentTime = utime.ticks_ms()
    pState = pin2.read_digital()   # previous state of door1
    pState2 = pin8.read_digital()   # previous state of door2
    pState3 = pin16.read_digital()  # previous state of door3

    if pState == 0:
        door1 = 'CLOSE,'
    else:
        door1 = 'OPEN,'

    if pState2 == 0:
        door2 = 'CLOSE,'
    else:
        door2 = 'OPEN,'

    if pState3 == 0:
        door3 = 'CLOSE'
    else:
        door3 = 'OPEN'

    doorstate = door1 + door2 + door3
    radio.send(doorstate)

    while utime.ticks_diff(currentTime, startTime) < heartbeat:
        cState = pin2.read_digital()    # get current state of door1
        cState2 = pin8.read_digital()   # get current state of door2
        cState3 = pin16.read_digital()  # get current state of door3
        # testing door conditions
        # 1 = open, 0 = closed

        if cState != pState or cState2 != pState2 or cState3 != pState3:
            if cState == 0:
                door1 = 'CLOSE,'
            else:
                door1 = 'OPEN,'

            if cState2 == 0:
                door2 = 'CLOSE,'
            else:
                door2 = 'OPEN,'

            if cState3 == 0:
                door3 = 'CLOSE,'
            else:
                door3 = 'OPEN,'

            doorstate = door1 + door2 + door3
            radio.send(doorstate)

        startTime = utime.ticks_ms()

        # send heartbeat ping every 3 seconds
        if utime.ticks_diff(currentTime, startTime) >= heartbeat:
            radio.send('PING')
            startTime = utime.ticks_ms()


        # relay switch, opens garage doors w indoor microbit
        message = radio.receive()
        if message == 'Door1':
            pin0.write_digital(1)
            sleep(300)
            pin0.write_digital(0)

        if message == 'Door2':
            pin1.write_digital(1)
            sleep(300)
            pin1.write_digital(0)


        currentTime = utime.ticks_ms()


