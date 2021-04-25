#!/usr/bin/python3
import os  # used to all external commands
import sys  # used to exit the script
import dbus
import dbus.service
import dbus.mainloop.glib
import time
# import thread
import keymap


class BtkStringClient():
    # constants
    KEY_DOWN_TIME = 0.000001
    KEY_DELAY = 0.000001

    def __init__(self):
        # the structure for a bt keyboard input report (size is 10 bytes)
        self.state = [
            0xA1,  # this is an input report
            0x01,  # Usage report = Keyboard
            # Bit array for Modifier keys
            [0,  # Right GUI - Windows Key
                 0,  # Right ALT
                 0,  # Right Shift
                 0,  # Right Control
                 0,  # Left GUI
                 0,  # Left ALT
                 0,  # Left Shift
                 0],  # Left Control
            0x00,  # Vendor reserved
            0x00,  # rest is space for 6 keys
            0x00,
            0x00,
            0x00,
            0x00,
            0x00]
        self.scancodes = {" ": "KEY_SPACE"}
        # connect with the Bluetooth keyboard server
        print("setting up DBus Client")
        self.bus = dbus.SystemBus()
        self.btkservice = self.bus.get_object(
            'org.thanhle.btkbservice', '/org/thanhle/btkbservice')
        self.iface = dbus.Interface(self.btkservice, 'org.thanhle.btkbservice')

    def send_key_state(self):
        """sends a single frame of the current key state to the emulator server"""
        bin_str = ""
        element = self.state[2]
        for bit in element:
            bin_str += str(bit)
        self.iface.send_keys(int(bin_str, 2), self.state[4:10])

    def send_key_down(self, scancode):
        """sends a key down event to the server"""
        self.state[4] = scancode
        self.send_key_state()

    def send_key_up(self):
        """sends a key up event to the server"""
        self.state[4] = 0
        self.send_key_state()

    def send_string(self, string_to_send):
        altArray = [0] * len(string_to_send)
        numKeyArray = [0] * len(string_to_send)
        for i in range(len(string_to_send)):
            
            if (string_to_send[i] in "πΠ"):
                altArray[i]=1
                altArray.insert(i+1,1)
                altArray.insert(i+2,1)
                numKeyArray[i] = 1
                numKeyArray.insert(i+1,1)
                numKeyArray.insert(i+2,1)
                string_to_send = string_to_send[:i] + "227" + string_to_send[i+1:]
        altArrayIndex = 0
        for c in string_to_send:
            self.state[2][1] = altArray[altArrayIndex]
            altArrayIndex = altArrayIndex+1
            if (c.isalpha() and c == c.upper()):
                self.state[2][2] =1
            else:
                self.state[2][2] =0
            if (c in "!@#$%^&*:\"?+_\~"):
                self.state[2][2] =1
            #if (altArray[altArrayIndex] == 1):
             #   self.state[2][1] = 1
            #else:
             #   self.state[2][1] = 0
            #altArrayIndex = altArrayIndex+1
            cu = c.upper()
            if(cu in self.scancodes):
                scantablekey = self.scancodes[cu]
            else:
                scantablekey = "KEY_"+c.upper()
                print("KEY_"+c+" "+str(altArray[altArrayIndex-1]))

            if (numKeyArray[i] == 1 and scantablekey in ["KEY_1","KEY_2","KEY_3","KEY_4","KEY_5","KEY_6","KEY_7","KEY_8","KEY_9","KEY_0"]):
                scantablekey = scantablekey[:4]+"KP"+scantablekey[4:]
            
            scancode = keymap.keytable[scantablekey]
            self.send_key_down(scancode)
            #time.sleep(BtkStringClient.KEY_DOWN_TIME)
            self.send_key_up()
            #time.sleep(BtkStringClient.KEY_DELAY)


if __name__ == "__main__":
    if(len(sys.argv) < 2):
        print("Usage: send_string <string to send ")
        exit()
    dc = BtkStringClient()
    string_to_send = sys.argv[1]
    print("Sending " + string_to_send)
    dc.send_string(string_to_send)
    print("Done.")
