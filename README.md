
This Arduino sketch allows you to control four relays via UDP commands.

Hardware requirements
Arduino board
4 relays
Ethernet shield

Software requirements
Arduino IDE

Getting Started
Connect your relays to your Arduino board.
Connect your Ethernet shield to the Arduino board
Open the sketch in the Arduino IDE
Update the MAC address and IP address in the sketch to match your Ethernet shield's MAC and IP address
Upload the sketch to your Arduino board

Send UDP commands to control the relays in the format "ON/OFF relay_number"
The sketch will send back a response indicating the status of the command and also the state of the relay.

Notes
The sketch uses the Ethernet library and EthernetUDP library, make sure they are included in your Arduino IDE
The sketch assumes that the device sending the UDP commands is on the same network as the Arduino board
The default UDP port used in the sketch is 1331, you can change it to any other port you desire
The sketch assumes that the relays are normally closed and turns them on when a "on" command is sent
You can modify the sketch as per your requirement, for example to include more relays or change the pin numbers
You can also modify the sketch to monitor the state of relays via other means, such as over HTTP or MQTT
Conclusion
This sketch is a simple example of how to control relays via UDP commands using an Arduino board and Ethernet shield. 
It can be easily modified to suit your specific needs or expanded to include more features.



Additional is a Python script with gui that can control the relay over ethernet tkinter library in Python is required, make sure that you have the same ip-adress on both places and that they are connected to the same network.
