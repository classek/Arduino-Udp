import socket
from tkinter import *

class App:
    def __init__(self, master):
        self.master = master
        master.title("Relay Control")

        self.relay_label = Label(master, text="Relay Number:")
        self.relay_label.grid(row=0, column=0)
        self.relay_entry = Entry(master)
        self.relay_entry.grid(row=0, column=1)

        self.on_button = Button(master, text="On", command=self.on)
        self.on_button.grid(row=1, column=0)
        self.off_button = Button(master, text="Off", command=self.off)
        self.off_button.grid(row=1, column=1)

        self.response_label = Label(master, text="Response:")
        self.response_label.grid(row=2, column=0)
        self.response_var = StringVar()
        self.response_var.set("none")
        self.response_display = Label(master, textvariable=self.response_var)
        self.response_display.grid(row=2, column=1)

    def on(self):
        relay = self.relay_entry.get()
        response = self.send_udp_command(relay, "ON")
        self.response_var.set(response)

    def off(self):
        relay = self.relay_entry.get()
        response = self.send_udp_command(relay, "OFF")
        self.response_var.set(response)

    def send_udp_command(self, relay, state):
        UDP_IP = "192.168.1.11"
        UDP_PORT = 1331
        MESSAGE = state + " " + relay

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(MESSAGE.encode(), (UDP_IP, UDP_PORT))

        # Sätt tidsgräns för att vänta på svaret
        sock.settimeout(2)
        try:
            data, addr = sock.recvfrom(1024)
            response = data.decode()
        except socket.timeout:
            response = "No response from device"

        print("Command sent:", MESSAGE)
        print("Response:", response)
        return response

root = Tk()
app = App(root)
root.mainloop()
