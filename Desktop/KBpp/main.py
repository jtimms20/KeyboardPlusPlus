
# main.py
# import the kivy module
import kivy
import os
import threading
import time
  
# It’s required that the base Class 
# of your App inherits from the App class.
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

os.environ['KIVY_WINDOW'] = 'egl_rpi'

from kivy.core.window import Window
Window.size=(800,480)
Window.fullscreen = True

def wait1ms():
    time.sleep(0.001)
def runTr1c1():
    os.system("python3 /home/pi/BL_keyboard_RPI/keyboard/send_string.py \'" + open("/home/pi/Desktop/KBpp/keybindings/r1c1.txt",'r').read()+"\'")
def runTr1c2():
    os.system("python3 /home/pi/BL_keyboard_RPI/keyboard/send_string.py \'" + open("/home/pi/Desktop/KBpp/keybindings/r1c2.txt",'r').read()+"\'")
def runTr1c3():
    os.system("python3 /home/pi/BL_keyboard_RPI/keyboard/send_string.py \'" + open("/home/pi/Desktop/KBpp/keybindings/r1c3.txt",'r').read()+"\'")
def runTr1c4():
    os.system("python3 /home/pi/BL_keyboard_RPI/keyboard/send_string.py \'" + open("/home/pi/Desktop/KBpp/keybindings/r1c4.txt",'r').read()+"\'")

def runTr2c1():
    os.system("python3 /home/pi/BL_keyboard_RPI/keyboard/send_string.py \'" + open("/home/pi/Desktop/KBpp/keybindings/r2c1.txt",'r').read()+"\'")
def runTr2c2():
    os.system("python3 /home/pi/BL_keyboard_RPI/keyboard/send_string.py \'" + open("/home/pi/Desktop/KBpp/keybindings/r2c2.txt",'r').read()+"\'")
def runTr2c3():
    os.system("python3 /home/pi/BL_keyboard_RPI/keyboard/send_string.py \'" + open("/home/pi/Desktop/KBpp/keybindings/r2c3.txt",'r').read()+"\'")
def runTr2c4():
    os.system("python3 /home/pi/BL_keyboard_RPI/keyboard/send_string.py \'" + open("/home/pi/Desktop/KBpp/keybindings/r2c4.txt",'r').read()+"\'")

def runTr3c1():
    os.system("python3 /home/pi/BL_keyboard_RPI/keyboard/send_string.py \'" + open("/home/pi/Desktop/KBpp/keybindings/r3c1.txt",'r').read()+"\'")
def runTr3c2():
    os.system("python3 /home/pi/BL_keyboard_RPI/keyboard/send_string.py \'" + open("/home/pi/Desktop/KBpp/keybindings/r3c2.txt",'r').read()+"\'")
def runTr3c3():
    os.system("python3 /home/pi/BL_keyboard_RPI/keyboard/send_string.py \'" + open("/home/pi/Desktop/KBpp/keybindings/r3c3.txt",'r').read()+"\'")
def runTr3c4():
    os.system("python3 /home/pi/BL_keyboard_RPI/keyboard/send_string.py \'" + open("/home/pi/Desktop/KBpp/keybindings/r3c4.txt",'r').read()+"\'")

#def waitForAllT()

# This class stores the info of .kv file
# when it is called goes to my.kv file
class KeypadWidget(GridLayout): 
    pass
    def keyboard_send_r1c1(self):
        btnTh = threading.Thread(target=runTr1c1)
        btnTh.start()
    def keyboard_send_r1c2(self):
        btnTh = threading.Thread(target=runTr1c2)
        btnTh.start()
    def keyboard_send_r1c3(self):
        btnTh = threading.Thread(target=runTr1c3)
        btnTh.start()
    def keyboard_send_r1c4(self):
        btnTh = threading.Thread(target=runTr1c4)
        btnTh.start()

    def keyboard_send_r2c1(self):
        btnTh = threading.Thread(target=runTr2c1)
        btnTh.start()
    def keyboard_send_r2c2(self):
        btnTh = threading.Thread(target=runTr2c2)
        btnTh.start()
    def keyboard_send_r2c3(self):
        btnTh = threading.Thread(target=runTr2c3)
        btnTh.start()
    def keyboard_send_r2c4(self):
        btnTh = threading.Thread(target=runTr2c4)
        btnTh.start()

    def keyboard_send_r3c1(self):
        btnTh = threading.Thread(target=runTr3c1)
        btnTh.start()
    def keyboard_send_r3c2(self):
        btnTh = threading.Thread(target=runTr3c2)
        btnTh.start()
    def keyboard_send_r3c3(self):
        btnTh = threading.Thread(target=runTr3c3)
        btnTh.start()
    def keyboard_send_r3c4(self):
        btnTh = threading.Thread(target=runTr3c4)
        btnTh.start()

class MainWidget(BoxLayout):
    pass
    def program_exit(self):
            exit()

class MenuWidget(BoxLayout):
    pass
    def program_exit(self):
        exit()
  
# we are defining the Base Class of our Kivy App
class GUI_KBppApp(App):
    def build(self):
        self.title = "KB++ GUI v0.2"
        # return a MainWidget() as a root widget
        return MainWidget()
    
  
if __name__ == '__main__':
      
    # Here the class MyApp is initialized
    # and its run() method called.
    GUI_KBppApp().run()

