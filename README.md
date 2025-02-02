This project utilises two Microbits to detect garage door movement and display the LED lights that correspond to the appropriately opened doors. The outdoor Microbit is wired to three magnetic reed switches to detect each garage door's position, and is also connected to two relay switches to trigger garage door movement. The indoor microbit is able to open and close two garage doors by sending radio signals to the outdoor Microbit. It also displays the current states of each door through its built-in LED display. A heartbeat system is implemented to minimise radio noise and ensure a constant connection is maintained and can be monitored between the Microbits.

NOTE: Microbits only have two built-in buttons, so the indoor Microbit is only able to open two doors but can still detect and display the third. The wiring of the two relay switches determines which doors can be opened.

## Hardware Requirements
- **2x Microbits (BBC Micro:bit)**
- **3x Magnetic reed switches**
- **2x Relay switches**
- **Power sources for indoor and outdoor Microbits**

## Installation and Setup
1. Clone this repository
2. Open the code using a Python editor such as Mu Editor
3. Upload/flash the code to each Microbit (one for indoor, one for outdoor)
4. Connect relay switches and reed switches on appropriate pins (pins 0 and 1 for relay switches, pins 2, 8 and 16 for reed switches)
5. Connect both Microbits to appropriate power source
